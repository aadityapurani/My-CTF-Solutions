# PNGSVG 

Category: Web 

First, I checked whether there is a possibility for `ImageTragick` vulnerability. Next, I tried using `img` to fetch external image hosted on my server. Which gave me a hit with user-agent `CairoSVG`.


`CairoSVG 2.3.0` is the latest version and is only compatible in python. There were 2 (or 3 although not a framework) good candidates for framework - Flask and Djano. Third one being `SimpleHTTPServer` to serve files.

First, we need to get either RCE or XXE. I thought to first target for XXE. 

```xml
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<svg height="300" width="200">
  <text x="0" y="15" fill="red">test &xxe; test</text>
</svg>
```

It will generate a png with the content of passwd. But, the image is too small to fit everything. Hence, you can tweak the width parameter to make it wider. The max amount of it was 34,000 as after that the server used to timeout while conversion
So, keeping it 20,000 should do the job.

Hence, now we have to arbitrary file read. It's not well RCE so I cannot list out the file name. So, we can either guess the flag path or either file the directories.

First things First,

I checked `/etc/passwd` which had `/home/svgmagic` . Hence the following was tried next

```
/home/svgmagic/flag.txt
/home/flag.txt
/flag.txt
/var/flag.txt
/tmp/flag.txt
/var/www/html/flag.txt
/var/www/flag.txt
```

Still no success. Hence, we need to try harder. I suspected the flag being in the current working directory. To find current working directory. We have to first find process-id of the current process & then do
`/proc/<pid>/cwd/`.

I dumped `/proc/self/status` which gave me pid of the current running process. The process was `Gunicorn` which is used to serve flask files.

The process id was 28. Hence, I tried `/proc/28/cwd/flag.txt` , nope no luck. Apparently, we dumped all the proc files & docker files with no success.

Then suddenly, we crafted a payload

```xml
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:flag.txt> ]>
<svg height="300" width="3000">
  <text x="0" y="15" fill="red">test &xxe; test</text>
</svg>
```

After processing that to PNG, It gave us the flag. 

#TO-DO : Put the Flag
