# What's the Password
Points: 100

Description:
```
you got a sample of rick's PC's memory. can you get his user password? format: CTF{...}
https://mega.nz/#!sh8wmCIL!b4tpech4wzc3QQ6YgQ2uZnOmctRZ2duQxDqxbkWYipQ
```

If you like to wget: https://transfer.sh/AesNq/OtterCTF.7z

# Solution:
We are provided a memory sample, to analyze it we use an Open Source Memory Forensics software called [Volatility](https://www.volatilityfoundation.org). 
We need to first get a high level summary of what we are analyzing. For that, we can use the `imageinfo` command. There is a good [reference](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference)
It is highly recommended for viewers to go through the basics of memory forensics before attempting it. This challenge is sort of malware analysis style challenge. That's why this CTF is called Blue-Teaming event for a reason, so before starting thanks to Ultra Lutra for putting this awesome stuff together. 

You can download volatility from github source or if you think life is easy, you can just `apt-get install volatility`. 

First things first, check the image and get the profile
```
$ python vol.py -f OtterCTF.vmem imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/volatility-2.6.1/OtterCTF.vmem)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002c430a0L
          Number of Processors : 2
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002c44d00L
                KPCR for CPU 1 : 0xfffff880009ef000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2018-08-04 19:34:22 UTC+0000
     Image local date and time : 2018-08-04 22:34:22 +0300
```

We can use the profile `Win7SP1x64`. Next is to dump the credentials, for that we need `hivelist`.

```
$ python vol.py -f OtterCTF.vmem hivelist --profile=Win7SP1x64
Volatility Foundation Volatility Framework 2.6
Virtual            Physical           Name
------------------ ------------------ ----
0xfffff8a00377d2d0 0x00000000624162d0 \??\C:\System Volume Information\Syscache.hve
0xfffff8a00000f010 0x000000002d4c1010 [no name]
0xfffff8a000024010 0x000000002d50c010 \REGISTRY\MACHINE\SYSTEM
0xfffff8a000053320 0x000000002d5bb320 \REGISTRY\MACHINE\HARDWARE
0xfffff8a000109410 0x0000000029cb4410 \SystemRoot\System32\Config\SECURITY
0xfffff8a00033d410 0x000000002a958410 \Device\HarddiskVolume1\Boot\BCD
0xfffff8a0005d5010 0x000000002a983010 \SystemRoot\System32\Config\SOFTWARE
0xfffff8a001495010 0x0000000024912010 \SystemRoot\System32\Config\DEFAULT
0xfffff8a0016d4010 0x00000000214e1010 \SystemRoot\System32\Config\SAM
0xfffff8a00175b010 0x00000000211eb010 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0xfffff8a00176e410 0x00000000206db410 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0xfffff8a002090010 0x000000000b92b010 \??\C:\Users\Rick\ntuser.dat
0xfffff8a0020ad410 0x000000000db41410 \??\C:\Users\Rick\AppData\Local\Microsoft\Windows\UsrClass.dat
```

We are particularly interested in virtual offset of `SYSTEM` or `SAM` generally. In this case, we first dig through `SYSTEM`

```
$ python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 -s 0xfffff8a000024010 hashdump
Volatility Foundation Volatility Framework 2.6
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Rick:1000:aad3b435b51404eeaad3b435b51404ee:518172d012f97d3a8fcc089615283940:::
```

Look at the start of the writeup, your life was easy, now you see NTLM hashes, you go and google search the Administrator's hash it's empty and you see
`518172d012f97d3a8fcc089615283940` on some hash-cracking site with no success in cracking. Is it getting harder?
If it's a memory file, we can basically use mimikatz here, I downloaded the plugin from [here](https://github.com/volatilityfoundation/community/blob/master/FrancescoPicasso/mimikatz.py)

and then 
```
$  python vol.py --plugins=./plugin/ -f OtterCTF.vmem --profile=Win7SP1x64 mimikatz
Volatility Foundation Volatility Framework 2.6
Module   User             Domain           Password                                
-------- ---------------- ---------------- ----------------------------------------
wdigest  Rick             WIN-LO6FAF3DTFE  MortyIsReallyAnOtter                    
wdigest  WIN-LO6FAF3DTFE$ WORKGROUP       
```

##### Flag: MortyIsReallyAnOtter

