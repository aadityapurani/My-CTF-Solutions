# Intigriti CTF Writeup 2019

The below report is in format sent to the Intigriti Team.

##### Proof of Concept

1.) Open the [Intigriti Tweet](https://twitter.com/intigriti/status/1082979668972748803), as we can see there is a url. The [image url](https://pbs.twimg.com/media/DweADlgXgAAehHh.jpg) can also be accessed by opening it in new tab

2.) Next, it seems that this image may have been shared from link via some other twitter a/c as twitter automatically expands it to preview mode. Hence, by that I found a different twitter account called [WhereIsTheFlag](https://twitter.com/WhereIsTheFlag) which does feel like an account related to the CTF challenge
This can be reproduceable by going to [Twitter Publish](https://publish.twitter.com) and in the url putting the initial Intigriti's Tweet.
The output
```
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">CHALLENGE: FIND THE FLAG🚩 &amp; WIN🏆! There&#39;s a secret flag hidden in this tweet. Can you find it? 🕵️ Check the rules in the replies! 👇<a href="https://twitter.com/hashtag/HackWithIntigriti?src=hash&amp;ref_src=twsrc%5Etfw">#HackWithIntigriti</a> <a href="https://twitter.com/hashtag/BugBounty?src=hash&amp;ref_src=twsrc%5Etfw">#BugBounty</a> <a href="https://twitter.com/hashtag/CTF?src=hash&amp;ref_src=twsrc%5Etfw">#CTF</a> <a href="https://t.co/0PFZNd692W">pic.twitter.com/0PFZNd692W</a></p>&mdash; intigriti (@intigriti) <a href="https://twitter.com/intigriti/status/1082979668972748803?ref_src=twsrc%5Etfw">January 9, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
```

As we can see `pic.twitter.com/0PFZNd692W` which leads to `https://twitter.com/WhereIsTheFlag/status/1082975045977362432/photo/1`

3.) We download the image using 
```
$ curl https://pbs.twimg.com/media/DweADlgXgAAehHh.jpg -o challenge.jpg
```

4.) Next, inspect the bytes inside the image using 
```
$ hexdump -C challenge.jpg | less
```
We can notice `PK` , `nottheflag.pdf` as strings inside it. The first one being a standard header format for ZIP files and other is the name of the file present inside that zip.

5.) We use 
```
$ mv challenge.jpg itsazip.zip
```
and extract it 
```
$ unzip itsazip.zip -d outputofzip/
```

6.) As expected, it contains `nottheflag.pdf` file, The content of the pdf file were
```
aHR0cHM6Ly9nby5pbnRpZ3JpdGkuY29tLzA3YjBmTDI0bGttdmE=
Source  for  this  cool  technique:  
https://twitter.com/David3141593/status/1058124224798380032
```

7.) It could be known that the first line is base64 chunk. We can decode it like
```
$ echo "aHR0cHM6Ly9nby5pbnRpZ3JpdGkuY29tLzA3YjBmTDI0bGttdmE=" | base64 -d
```
The output being
https://go.intigriti.com/07b0fL24lkmva

8.) One more link, so let's open it which enables us downloading data.zip file, but it is a password protected one. I tried `fcrackzip` a tool which enables zip password brute-forcing with custom wordlists, rockyou.txt etc. But it did not work

9.) Now we know that password is unguessable and non-bruteforceable, We look back at `step-2`, and open the profile. We inspect the profile image using `StegSolver.jar` but get nothing, next we can open the cover image which sort of looks like default twitter cover pic (Empty cover in other words), but it's not. The fine researchers of Intigriti tricked us, Hence we open the cover image, and can see `F1nDBuGz_` which is the password for `data.zip` file.

10.) Now, after extracting we could see 441 image files, either black or white color having 11x11 size. It is trivial that this points to QR-Code Type-1 format which has 21x21 data which equals to 441 images, confirming our assumption.

11.) Now, the goal is to combine those image and then get the output. For that, I use a tool called `montage` , it comes along with `imagemagick`. On a debian based system, it can be installed as
```
$ sudo apt installimagemagick
$ sudo apt install graphicsmagick-imagemagick-compat
```
Now, we can move files from `0_01.jpg` to `0_09.jpg` to `0_1.jpg` to `0_9.jpg` using `mv` linux command.

12.) Finally we run our `montage` command which looks like
```
$ montage $(for i in $(seq 1 441); do echo "1_$i.jpg";done) -mode Concatenate -tile 21x output.png
```
Essentially, it takes all the image and creates a table of 21 x 21 and concatenates it. There are other ways like manual retrieval or even using PIL Python. But, this one is short and crisp.
The final image looks like this

![Output](https://i.ibb.co/j4dW3CP/output.png)

13.) We can use our cell-phone QR code app or online web-app to upload the image and decode it

### FLAG:YOUWINTIGRITI
