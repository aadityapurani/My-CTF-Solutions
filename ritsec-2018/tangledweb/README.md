# The Tangled Web (200 points)

Category: Web

_Writeup_

The [url](http://fun.ritsec.club:8007) was provided to us. Navigating to that, we can see hyperlinks on the website (a lot of). If we click one of those, it will point to few more. 
This same concept I have encountered in HackerRank's CTF (maybe in 2015-1016). I had the code ready actually.

The solver script : solver.py

Hence, the idea was to automate the process and list out all the links, The STDOUT was cluttered with

```
Extracting URL : http://fun.ritsec.club:8007/
Extracting URL : http://fun.ritsec.club:8007/Never.html
Extracting URL : http://fun.ritsec.club:8007/Gonna.html
Extracting URL : http://fun.ritsec.club:8007/Give.html
Extracting URL : http://fun.ritsec.club:8007/You.html
Extracting URL : http://fun.ritsec.club:8007/Up.html
Extracting URL : http://fun.ritsec.club:8007/Feel.html
Extracting URL : http://fun.ritsec.club:8007/The.html
Extracting URL : http://fun.ritsec.club:8007/Love.html
Extracting URL : http://fun.ritsec.club:8007/Tonight.html
Extracting URL : http://fun.ritsec.club:8007/World.html
Extracting URL : http://fun.ritsec.club:8007/Is.html
Extracting URL : http://fun.ritsec.club:8007/Would.html
Extracting URL : http://fun.ritsec.club:8007/Not.html
Extracting URL : http://fun.ritsec.club:8007/Believe.html
Extracting URL : http://fun.ritsec.club:8007/Your.html
Extracting URL : http://fun.ritsec.club:8007/Eyes.html
Extracting URL : http://fun.ritsec.club:8007/If.html
Extracting URL : http://fun.ritsec.club:8007/Ten.html
Extracting URL : http://fun.ritsec.club:8007/Million.html
Extracting URL : http://fun.ritsec.club:8007/Fireflies.html
Extracting URL : http://fun.ritsec.club:8007/Roll.html
Extracting URL : http://fun.ritsec.club:8007/Me.html
Extracting URL : http://fun.ritsec.club:8007/More.html
Extracting URL : http://fun.ritsec.club:8007/Away.html
Extracting URL : http://fun.ritsec.club:8007/From.html
Extracting URL : http://fun.ritsec.club:8007/Freedom.html
Extracting URL : http://fun.ritsec.club:8007/Just.html
Extracting URL : http://fun.ritsec.club:8007/Like.html
Extracting URL : http://fun.ritsec.club:8007/A.html
Extracting URL : http://fun.ritsec.club:8007/Lot.html
Extracting URL : http://fun.ritsec.club:8007/To.html
Extracting URL : http://fun.ritsec.club:8007/Take.html
Extracting URL : http://fun.ritsec.club:8007/Waving.html
Extracting URL : http://fun.ritsec.club:8007/Fl4gggg1337.html
Extracting URL : http://fun.ritsec.club:8007/Stars.html
Extracting URL : http://fun.ritsec.club:8007/Can.html
Extracting URL : http://fun.ritsec.club:8007/Somebody.html
Extracting URL : http://fun.ritsec.club:8007/Once.html
Extracting URL : http://fun.ritsec.club:8007/Told.html
Extracting URL : http://fun.ritsec.club:8007/Tell.html
Extracting URL : http://fun.ritsec.club:8007/When.html
Extracting URL : http://fun.ritsec.club:8007/I.html
Extracting URL : http://fun.ritsec.club:8007/Get.html
Extracting URL : http://fun.ritsec.club:8007/Older.html
Extracting URL : http://fun.ritsec.club:8007/Will.html
Extracting URL : http://fun.ritsec.club:8007/Be.html
Extracting URL : http://fun.ritsec.club:8007/Stronger.html
Extracting URL : http://fun.ritsec.club:8007/Theyll.html
Extracting URL : http://fun.ritsec.club:8007/Call.html
Extracting URL : http://fun.ritsec.club:8007/Its.html
Extracting URL : http://fun.ritsec.club:8007/Gucci.html
Extracting URL : http://fun.ritsec.club:8007/Gang.html
Extracting URL : http://fun.ritsec.club:8007/Ah.html
Extracting URL : http://fun.ritsec.club:8007/Ahhh.html
Extracting URL : http://fun.ritsec.club:8007/Ha.html
Extracting URL : http://fun.ritsec.club:8007/AH.html
Extracting URL : http://fun.ritsec.club:8007/AHHHA.html
Extracting URL : http://fun.ritsec.club:8007/AHHHHH.html
Extracting URL : http://fun.ritsec.club:8007/AHH.html
Extracting URL : http://fun.ritsec.club:8007/AHA.html
```

Nifty, we could figure out http://fun.ritsec.club:8007/Fl4gggg1337.html is something worth to look at. One more hyperlink 
http://fun.ritsec.club:8007/Stars.html (Even our script output that)

```
$ echo "UklUU0VDe0FSM19ZMFVfRjMzNzFOR18xVF9OMFdfTVJfS1I0QjU/IX0=" | base64 -d
RITSEC{AR3_Y0U_F3371NG_1T_N0W_MR_KR4B5?!}
```

Also, the comment on the page
```
<!-- REMOVE THIS NOTE LATER -->
<!-- Getting remote access is so much work. Just do fancy things on devsrule.php -->
```
gives rise to a sequel of this challenge (LazyDev) whose write-up you will see in a short-while on the repo.

##### Flag: RITSEC{AR3_Y0U_F3371NG_1T_N0W_MR_KR4B5?!}


