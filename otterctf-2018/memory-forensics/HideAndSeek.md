# Hide and Seek
Points: 100

```
The reason that we took rick's PC memory dump is because there was a malware infection. Please find the malware process name (including the extension)

BEAWARE! There are only 3 attempts to get the right flag!

format: CTF{flag}
```

# Solution:

Now, it boils down to finding the process and that too within 3 attempts. `pslist` would list down the process

```
python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 pslist
Volatility Foundation Volatility Framework 2.6
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa8018d44740 System                    4      0     95      411 ------      0 2018-08-04 19:26:03 UTC+0000                                 
0xfffffa801947e4d0 smss.exe                260      4      2       30 ------      0 2018-08-04 19:26:03 UTC+0000                                 
0xfffffa801a0c8380 csrss.exe               348    336      9      563      0      0 2018-08-04 19:26:10 UTC+0000                                 
0xfffffa80198d3b30 csrss.exe               388    380     11      460      1      0 2018-08-04 19:26:11 UTC+0000                                 
0xfffffa801a2ed060 wininit.exe             396    336      3       78      0      0 2018-08-04 19:26:11 UTC+0000                                 
0xfffffa801aaf4060 winlogon.exe            432    380      3      113      1      0 2018-08-04 19:26:11 UTC+0000                                 
0xfffffa801ab377c0 services.exe            492    396     11      242      0      0 2018-08-04 19:26:12 UTC+0000                                 
0xfffffa801ab3f060 lsass.exe               500    396      7      610      0      0 2018-08-04 19:26:12 UTC+0000                                 
0xfffffa801ab461a0 lsm.exe                 508    396     10      148      0      0 2018-08-04 19:26:12 UTC+0000                                 
0xfffffa8018e3c890 svchost.exe             604    492     11      376      0      0 2018-08-04 19:26:16 UTC+0000                                 
0xfffffa801abbdb30 vmacthlp.exe            668    492      3       56      0      0 2018-08-04 19:26:16 UTC+0000                                 
0xfffffa801abebb30 svchost.exe             712    492      8      301      0      0 2018-08-04 19:26:17 UTC+0000                                 
0xfffffa801ac2e9e0 svchost.exe             808    492     22      508      0      0 2018-08-04 19:26:18 UTC+0000                                 
0xfffffa801ac31b30 svchost.exe             844    492     17      396      0      0 2018-08-04 19:26:18 UTC+0000                                 
0xfffffa801ac4db30 svchost.exe             868    492     45     1114      0      0 2018-08-04 19:26:18 UTC+0000                                 
0xfffffa801ac753a0 audiodg.exe             960    808      7      151      0      0 2018-08-04 19:26:19 UTC+0000                                 
0xfffffa801ac97060 svchost.exe            1012    492     12      554      0      0 2018-08-04 19:26:20 UTC+0000                                 
0xfffffa801acd37e0 svchost.exe             620    492     19      415      0      0 2018-08-04 19:26:21 UTC+0000                                 
0xfffffa801ad5ab30 spoolsv.exe            1120    492     14      346      0      0 2018-08-04 19:26:22 UTC+0000                                 
0xfffffa801ad718a0 svchost.exe            1164    492     18      312      0      0 2018-08-04 19:26:23 UTC+0000                                 
0xfffffa801ae0f630 VGAuthService.         1356    492      3       85      0      0 2018-08-04 19:26:25 UTC+0000                                 
0xfffffa801ae92920 vmtoolsd.exe           1428    492      9      313      0      0 2018-08-04 19:26:27 UTC+0000                                 
0xfffffa8019124b30 WmiPrvSE.exe           1800    604      9      222      0      0 2018-08-04 19:26:39 UTC+0000                                 
0xfffffa801afe7800 svchost.exe            1948    492      6       96      0      0 2018-08-04 19:26:42 UTC+0000                                 
0xfffffa801ae7f630 dllhost.exe            1324    492     15      207      0      0 2018-08-04 19:26:42 UTC+0000                                 
0xfffffa801aff3b30 msdtc.exe              1436    492     14      155      0      0 2018-08-04 19:26:43 UTC+0000                                 
0xfffffa801b112060 WmiPrvSE.exe           2136    604     12      324      0      0 2018-08-04 19:26:51 UTC+0000                                 
0xfffffa801b1e9b30 taskhost.exe           2344    492      8      193      1      0 2018-08-04 19:26:57 UTC+0000                                 
0xfffffa801b232060 sppsvc.exe             2500    492      4      149      0      0 2018-08-04 19:26:58 UTC+0000                                 
0xfffffa801b1fab30 dwm.exe                2704    844      4       97      1      0 2018-08-04 19:27:04 UTC+0000                                 
0xfffffa801b27e060 explorer.exe           2728   2696     33      854      1      0 2018-08-04 19:27:04 UTC+0000                                 
0xfffffa801b1cdb30 vmtoolsd.exe           2804   2728      6      190      1      0 2018-08-04 19:27:06 UTC+0000                                 
0xfffffa801b290b30 BitTorrent.exe         2836   2728     24      471      1      1 2018-08-04 19:27:07 UTC+0000                                 
0xfffffa801b2f02e0 WebCompanion.e         2844   2728      0 --------      1      0 2018-08-04 19:27:07 UTC+0000   2018-08-04 19:33:33 UTC+0000  
0xfffffa801b3aab30 SearchIndexer.         3064    492     11      610      0      0 2018-08-04 19:27:14 UTC+0000                                 
0xfffffa801b4a7b30 bittorrentie.e         2308   2836     15      337      1      1 2018-08-04 19:27:19 UTC+0000                                 
0xfffffa801b4c9b30 bittorrentie.e         2624   2836     13      316      1      1 2018-08-04 19:27:21 UTC+0000                                 
0xfffffa801b5cb740 LunarMS.exe             708   2728     18      346      1      1 2018-08-04 19:27:39 UTC+0000                                 
0xfffffa801988c2d0 PresentationFo          724    492      6      148      0      0 2018-08-04 19:27:52 UTC+0000                                 
0xfffffa801b603610 mscorsvw.exe            412    492      7       86      0      1 2018-08-04 19:28:42 UTC+0000                                 
0xfffffa801a6af9f0 svchost.exe             164    492     12      147      0      0 2018-08-04 19:28:42 UTC+0000                                 
0xfffffa801a6c2700 mscorsvw.exe           3124    492      7       77      0      0 2018-08-04 19:28:43 UTC+0000                                 
0xfffffa801a6e4b30 svchost.exe            3196    492     14      352      0      0 2018-08-04 19:28:44 UTC+0000                                 
0xfffffa801a4e3870 chrome.exe             4076   2728     44     1160      1      0 2018-08-04 19:29:30 UTC+0000                                 
0xfffffa801a4eab30 chrome.exe             4084   4076      8       86      1      0 2018-08-04 19:29:30 UTC+0000                                 
0xfffffa801a502b30 chrome.exe              576   4076      2       58      1      0 2018-08-04 19:29:31 UTC+0000                                 
0xfffffa801a4f7b30 chrome.exe             1808   4076     13      229      1      0 2018-08-04 19:29:32 UTC+0000                                 
0xfffffa801aa00a90 chrome.exe             3924   4076     16      228      1      0 2018-08-04 19:29:51 UTC+0000                                 
0xfffffa801a7f98f0 chrome.exe             2748   4076     15      181      1      0 2018-08-04 19:31:15 UTC+0000                                 
0xfffffa801b486b30 Rick And Morty         3820   2728      4      185      1      1 2018-08-04 19:32:55 UTC+0000                                 
0xfffffa801a4c5b30 vmware-tray.ex         3720   3820      8      147      1      1 2018-08-04 19:33:02 UTC+0000                                 
0xfffffa801b18f060 WebCompanionIn         3880   1484     15      522      0      1 2018-08-04 19:33:07 UTC+0000                                 
0xfffffa801a635240 chrome.exe             3648   4076     16      207      1      0 2018-08-04 19:33:38 UTC+0000                                 
0xfffffa801a5ef1f0 chrome.exe             1796   4076     15      170      1      0 2018-08-04 19:33:41 UTC+0000                                 
0xfffffa801b08f060 sc.exe                 3208   3880      0 --------      0      0 2018-08-04 19:33:47 UTC+0000   2018-08-04 19:33:48 UTC+0000  
0xfffffa801aeb6890 sc.exe                  452   3880      0 --------      0      0 2018-08-04 19:33:48 UTC+0000   2018-08-04 19:33:48 UTC+0000  
0xfffffa801aa72b30 sc.exe                 3504   3880      0 --------      0      0 2018-08-04 19:33:48 UTC+0000   2018-08-04 19:33:48 UTC+0000  
0xfffffa801ac01060 sc.exe                 2028   3880      0 --------      0      0 2018-08-04 19:33:49 UTC+0000   2018-08-04 19:34:03 UTC+0000  
0xfffffa801aad1060 Lavasoft.WCAss         3496    492     14      473      0      0 2018-08-04 19:33:49 UTC+0000                                 
0xfffffa801a6268b0 WebCompanion.e         3856   3880     15      386      0      1 2018-08-04 19:34:05 UTC+0000                                 
0xfffffa801b1fd960 notepad.exe            3304   3132      2       79      1      0 2018-08-04 19:34:10 UTC+0000                                 
0xfffffa801a572b30 cmd.exe                3916   1428      0 --------      0      0 2018-08-04 19:34:22 UTC+0000   2018-08-04 19:34:22 UTC+0000  
0xfffffa801a6643d0 conhost.exe            2420    348      0       30      0      0 2018-08-04 19:34:22 UTC+0000   2018-08-04 19:34:22 UTC+0000  
```

A lot of processes. I narrowed done to unique process first.
```
notepad.exe
command.exe
conhost.exe
svchost.exe
LunarMS.exe
BitTorrent.exe
vmware-tray.exe
sc.exe
.....
```

Now, we have to reduce the possibilities. You will never have reduction strategy without identifying which process is important. I used `pstree` next.

```
$ python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 pstree
Volatility Foundation Volatility Framework 2.6
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xfffffa801b27e060:explorer.exe                     2728   2696     33    854 2018-08-04 19:27:04 UTC+0000
. 0xfffffa801b486b30:Rick And Morty                  3820   2728      4    185 2018-08-04 19:32:55 UTC+0000
.. 0xfffffa801a4c5b30:vmware-tray.ex                 3720   3820      8    147 2018-08-04 19:33:02 UTC+0000
. 0xfffffa801b2f02e0:WebCompanion.e                  2844   2728      0 ------ 2018-08-04 19:27:07 UTC+0000
. 0xfffffa801a4e3870:chrome.exe                      4076   2728     44   1160 2018-08-04 19:29:30 UTC+0000
.. 0xfffffa801a4eab30:chrome.exe                     4084   4076      8     86 2018-08-04 19:29:30 UTC+0000
.. 0xfffffa801a5ef1f0:chrome.exe                     1796   4076     15    170 2018-08-04 19:33:41 UTC+0000
.. 0xfffffa801aa00a90:chrome.exe                     3924   4076     16    228 2018-08-04 19:29:51 UTC+0000
.. 0xfffffa801a635240:chrome.exe                     3648   4076     16    207 2018-08-04 19:33:38 UTC+0000
.. 0xfffffa801a502b30:chrome.exe                      576   4076      2     58 2018-08-04 19:29:31 UTC+0000
.. 0xfffffa801a4f7b30:chrome.exe                     1808   4076     13    229 2018-08-04 19:29:32 UTC+0000
.. 0xfffffa801a7f98f0:chrome.exe                     2748   4076     15    181 2018-08-04 19:31:15 UTC+0000
. 0xfffffa801b5cb740:LunarMS.exe                      708   2728     18    346 2018-08-04 19:27:39 UTC+0000
. 0xfffffa801b1cdb30:vmtoolsd.exe                    2804   2728      6    190 2018-08-04 19:27:06 UTC+0000
. 0xfffffa801b290b30:BitTorrent.exe                  2836   2728     24    471 2018-08-04 19:27:07 UTC+0000
.. 0xfffffa801b4c9b30:bittorrentie.e                 2624   2836     13    316 2018-08-04 19:27:21 UTC+0000
.. 0xfffffa801b4a7b30:bittorrentie.e                 2308   2836     15    337 2018-08-04 19:27:19 UTC+0000
 0xfffffa8018d44740:System                              4      0     95    411 2018-08-04 19:26:03 UTC+0000
. 0xfffffa801947e4d0:smss.exe                         260      4      2     30 2018-08-04 19:26:03 UTC+0000
 0xfffffa801a2ed060:wininit.exe                       396    336      3     78 2018-08-04 19:26:11 UTC+0000
. 0xfffffa801ab377c0:services.exe                     492    396     11    242 2018-08-04 19:26:12 UTC+0000
.. 0xfffffa801afe7800:svchost.exe                    1948    492      6     96 2018-08-04 19:26:42 UTC+0000
.. 0xfffffa801ae92920:vmtoolsd.exe                   1428    492      9    313 2018-08-04 19:26:27 UTC+0000
... 0xfffffa801a572b30:cmd.exe                       3916   1428      0 ------ 2018-08-04 19:34:22 UTC+0000
.. 0xfffffa801ae0f630:VGAuthService.                 1356    492      3     85 2018-08-04 19:26:25 UTC+0000
.. 0xfffffa801abbdb30:vmacthlp.exe                    668    492      3     56 2018-08-04 19:26:16 UTC+0000
.. 0xfffffa801aad1060:Lavasoft.WCAss                 3496    492     14    473 2018-08-04 19:33:49 UTC+0000
.. 0xfffffa801a6af9f0:svchost.exe                     164    492     12    147 2018-08-04 19:28:42 UTC+0000
.. 0xfffffa801ac2e9e0:svchost.exe                     808    492     22    508 2018-08-04 19:26:18 UTC+0000
... 0xfffffa801ac753a0:audiodg.exe                    960    808      7    151 2018-08-04 19:26:19 UTC+0000
.. 0xfffffa801ae7f630:dllhost.exe                    1324    492     15    207 2018-08-04 19:26:42 UTC+0000
.. 0xfffffa801a6c2700:mscorsvw.exe                   3124    492      7     77 2018-08-04 19:28:43 UTC+0000
.. 0xfffffa801b232060:sppsvc.exe                     2500    492      4    149 2018-08-04 19:26:58 UTC+0000
.. 0xfffffa801abebb30:svchost.exe                     712    492      8    301 2018-08-04 19:26:17 UTC+0000
.. 0xfffffa801ad718a0:svchost.exe                    1164    492     18    312 2018-08-04 19:26:23 UTC+0000
.. 0xfffffa801ac31b30:svchost.exe                     844    492     17    396 2018-08-04 19:26:18 UTC+0000
... 0xfffffa801b1fab30:dwm.exe                       2704    844      4     97 2018-08-04 19:27:04 UTC+0000
.. 0xfffffa801988c2d0:PresentationFo                  724    492      6    148 2018-08-04 19:27:52 UTC+0000
.. 0xfffffa801b603610:mscorsvw.exe                    412    492      7     86 2018-08-04 19:28:42 UTC+0000
.. 0xfffffa8018e3c890:svchost.exe                     604    492     11    376 2018-08-04 19:26:16 UTC+0000
... 0xfffffa8019124b30:WmiPrvSE.exe                  1800    604      9    222 2018-08-04 19:26:39 UTC+0000
... 0xfffffa801b112060:WmiPrvSE.exe                  2136    604     12    324 2018-08-04 19:26:51 UTC+0000
.. 0xfffffa801ad5ab30:spoolsv.exe                    1120    492     14    346 2018-08-04 19:26:22 UTC+0000
.. 0xfffffa801ac4db30:svchost.exe                     868    492     45   1114 2018-08-04 19:26:18 UTC+0000
.. 0xfffffa801a6e4b30:svchost.exe                    3196    492     14    352 2018-08-04 19:28:44 UTC+0000
.. 0xfffffa801acd37e0:svchost.exe                     620    492     19    415 2018-08-04 19:26:21 UTC+0000
.. 0xfffffa801b1e9b30:taskhost.exe                   2344    492      8    193 2018-08-04 19:26:57 UTC+0000
.. 0xfffffa801ac97060:svchost.exe                    1012    492     12    554 2018-08-04 19:26:20 UTC+0000
.. 0xfffffa801b3aab30:SearchIndexer.                 3064    492     11    610 2018-08-04 19:27:14 UTC+0000
.. 0xfffffa801aff3b30:msdtc.exe                      1436    492     14    155 2018-08-04 19:26:43 UTC+0000
. 0xfffffa801ab3f060:lsass.exe                        500    396      7    610 2018-08-04 19:26:12 UTC+0000
. 0xfffffa801ab461a0:lsm.exe                          508    396     10    148 2018-08-04 19:26:12 UTC+0000
 0xfffffa801a0c8380:csrss.exe                         348    336      9    563 2018-08-04 19:26:10 UTC+0000
. 0xfffffa801a6643d0:conhost.exe                     2420    348      0     30 2018-08-04 19:34:22 UTC+0000
 0xfffffa80198d3b30:csrss.exe                         388    380     11    460 2018-08-04 19:26:11 UTC+0000
 0xfffffa801aaf4060:winlogon.exe                      432    380      3    113 2018-08-04 19:26:11 UTC+0000
 0xfffffa801b18f060:WebCompanionIn                   3880   1484     15    522 2018-08-04 19:33:07 UTC+0000
. 0xfffffa801aa72b30:sc.exe                          3504   3880      0 ------ 2018-08-04 19:33:48 UTC+0000
. 0xfffffa801aeb6890:sc.exe                           452   3880      0 ------ 2018-08-04 19:33:48 UTC+0000
. 0xfffffa801a6268b0:WebCompanion.e                  3856   3880     15    386 2018-08-04 19:34:05 UTC+0000
. 0xfffffa801b08f060:sc.exe                          3208   3880      0 ------ 2018-08-04 19:33:47 UTC+0000
. 0xfffffa801ac01060:sc.exe                          2028   3880      0 ------ 2018-08-04 19:33:49 UTC+0000
 0xfffffa801b1fd960:notepad.exe                      3304   3132      2     79 2018-08-04 19:34:10 UTC+0000
```

I analyzed a lot more process. But, for the sake of writeup, we will jump on what stands out.

```
 0xfffffa801b486b30:Rick And Morty                  3820   2728      4    185 2018-08-04 19:32:55 UTC+0000
.. 0xfffffa801a4c5b30:vmware-tray.ex                 3720   3820      8    147 2018-08-04 19:33:02 UTC+0000
```

This means, the process 3820 is spinning a child-process with pid 3720 whose parent process ppid is 3820. Strange, let's investigate

```
$ python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 dlllist -p 3820
Volatility Foundation Volatility Framework 2.6
************************************************************************
Rick And Morty pid:   3820
Command line : "C:\Torrents\Rick And Morty season 1 download.exe" 


Base                             Size          LoadCount LoadTime                       Path
------------------ ------------------ ------------------ ------------------------------ ----
0x0000000000400000            0x56000             0xffff 1970-01-01 00:00:00 UTC+0000   C:\Torrents\Rick And Morty season 1 download.exe
0x00000000776f0000           0x1a9000             0xffff 1970-01-01 00:00:00 UTC+0000   C:\Windows\SYSTEM32\ntdll.dll
0x0000000075210000            0x3f000                0x3 2018-08-04 19:32:55 UTC+0000   C:\Windows\SYSTEM32\wow64.dll
0x00000000751b0000            0x5c000                0x1 2018-08-04 19:32:55 UTC+0000   C:\Windows\SYSTEM32\wow64win.dll
0x00000000751a0000             0x8000                0x1 2018-08-04 19:32:55 UTC+0000   C:\Windows\SYSTEM32\wow64cpu.dll
0x0000000000400000            0x56000             0xffff 1970-01-01 00:00:00 UTC+0000   C:\Torrents\Rick And Morty season 1 download.exe
... omitted for brevity ...
```

Dawg, I told ya not to download exe's from Torrent. We can analyze vm-tray.exe now.

```
python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 dlllist -p 3720
Volatility Foundation Volatility Framework 2.6
************************************************************************
vmware-tray.ex pid:   3720
Command line : "C:\Users\Rick\AppData\Local\Temp\RarSFX0\vmware-tray.exe" 


Base                             Size          LoadCount LoadTime                       Path
------------------ ------------------ ------------------ ------------------------------ ----
0x0000000000ec0000            0x6e000             0xffff 1970-01-01 00:00:00 UTC+0000   C:\Users\Rick\AppData\Local\Temp\RarSFX0\vmware-tray.exe
... omitted for brevity ...
```
Interesting part is it is executing from a Temp folder, nice so the parent process executable acts as a dropper to the `vmware-tray.exe` which suspciously uses `dlls` which it should not use.
I dumped the process executable and figured out it is indeed a ransomware. (Hidden Tear - spoilers)

Hence,
##### Flag: CTF{vmware-tray.exe}
