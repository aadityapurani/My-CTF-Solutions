# Recovery
Point: 300 points

```
Rick got to have his files recovered! What is the random password used to encrypt the files?

format: CTF{...}
```

# Solution:

This is a great challenge. Just like real world malware analysis. For the sake of completeness, I wish to recap

Process 3720 is the Malware

```
$ python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 dlllist -p 3720
Volatility Foundation Volatility Framework 2.6
************************************************************************
vmware-tray.ex pid:   3720
Command line : "C:\Users\Rick\AppData\Local\Temp\RarSFX0\vmware-tray.exe" 


Base                             Size          LoadCount LoadTime                       Path
------------------ ------------------ ------------------ ------------------------------ ----
0x0000000000ec0000            0x6e000             0xffff 1970-01-01 00:00:00 UTC+0000   C:\Users\Rick\AppData\Local\Temp\RarSFX0\vmware-tray.exe
0x00000000776f0000           0x1a9000             0xffff 1970-01-01 00:00:00 UTC+0000   C:\Windows\SYSTEM32\ntdll.dll
0x0000000075210000            0x3f000                0x3 2018-08-04 19:33:03 UTC+0000   C:\Windows\SYSTEM32\wow64.dll
0x00000000751b0000            0x5c000                0x1 2018-08-04 19:33:03 UTC+0000   C:\Windows\SYSTEM32\wow64win.dll
0x00000000751a0000             0x8000                0x1 2018-08-04 19:33:03 UTC+0000   C:\Windows\SYSTEM32\wow64cpu.dll
0x0000000000ec0000            0x6e000             0xffff 1970-01-01 00:00:00 UTC+0000   C:\Users\Rick\AppData\Local\Temp\RarSFX0\vmware-tray.exe
```

After that, we dump executable and next we dump process memory. A very beautiful thing in Memory forensics area.

```
$ python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 memdump -D dump/ -p 3720
```

As it is memory dump, the uncertainity with the data increases exponentially. We got to reverse the bin more

```C
public string CreatePassword(int length)
        {
            StringBuilder stringBuilder = new StringBuilder();
            Random random = new Random();
            while (0 < length--)
            {
                stringBuilder.Append("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*!=&?&/"[random.Next("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*!=&?&/".Length)]);
            }
            return stringBuilder.ToString();
        }
```
`Random()` is used, with no recovery for seed. So, good 'ol days are no more. We know the regex 
`abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*!=&?&/`

We reverse it bit more,
```
public void startAction()
 {
  string password = this.CreatePassword(15);
  string str = "\\Desktop\\";
  string location = this.userDir + this.userName + str;
  this.SendPassword(password);
  this.encryptDirectory(location, password);
  this.messageCreator();
 }
 ```
 The length of password is 15. So, we have regex with length. Now, I play it with my grepping skills. I was sure it won't let me [down](https://aadityapurani.com/2018/09/16/csaw-ctf-writeups-2018/#whyos)
 It all boils down to your critical thinking skills next.
 
 ```
 $ strings 3720.dmp > analyze.txt
 ```
 Now, we have proper textual (yeah garbage).
Intitially it was 20K lines even with exact 15 character strings. Using my grep skillz we went to 2.8K

```
$ grep -E '^.[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*!=&?&/]{14}$' analyze.txt | grep -vE 'Systems|Key|Java|Align|Driver|printer|MCLN|object|software|enough|Afd|enable|System|UUUU|Pos|SU|text|Body|Buffer|Length|match|Document|Un|On|tal|ing|ype|ign|Info|Instance|id32|p1|l1|File|Store|Selector|Available|Dll|Call|Make|maker|Init|Target|Put|Get|Requires|Column|0a1|0h1|0u1|0Z1|Params|resolve|0w1|0L1|0000000000000|Month|ByName|0000|000|2018|GUI|Command|long|status|Permission|IL|Il|Nil|web|NID|Runtime|es|Lower|Delayed|Transition|Bus|Flags|Image|Memory|Window|Loader|Manage|Class|Sink|Sys|Wow|MM|Create' | uniq | wc -l
2837
```

Now, I can read 2.8K lines
```
$ grep -E '^.[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*!=&?&/]{14}$' analyze.txt | grep -vE 'Systems|Key|Java|Align|Driver|printer|MCLN|object|software|enough|Afd|enable|System|UUUU|Pos|SU|text|Body|Buffer|Length|match|Document|Un|On|tal|ing|ype|ign|Info|Instance|id32|p1|l1|File|Store|Selector|Available|Dll|Call|Make|maker|Init|Target|Put|Get|Requires|Column|0a1|0h1|0u1|0Z1|Params|resolve|0w1|0L1|0000000000000|Month|ByName|0000|000|2018|GUI|Command|long|status|Permission|IL|Il|Nil|web|NID|Runtime|es|Lower|Delayed|Transition|Bus|Flags|Image|Memory|Window|Loader|Manage|Class|Sink|Sys|Wow|MM|Create' | uniq | less
```

Output:
```
444444440444444
66666FFFFFFFFFF
444444444444433
CLIPBRDWNDCLASS
utav4823DF041B0
aDOBofVYUNVnmp7
444444440444444
66666FFFFFFFFFF
444444444444433
ffnLffnLffnpffm
lemeneoepeqerep
y0N0O0P0Q0R0S0T
N0O0P0Q0R0S0T0z
nfelf&nlunfDnru
ffnLffnLffnpffm
LAeDRCeHNAexNAe
rAetrAeDsAe4sAe
53eX53eP33eD33e
...
```

We apply some more critical thinking skills, I reversed the binary and public key was in there `b03f5f7f11d50a3a` but what's the use of public key? A wise man said, we can know in memory area of the dump where it resides. I twisted my grep logic to 16 bytes and looked where my public key is in the memory.


```
$ grep -E '^.[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*!=&?&/]{15}$' analyze.txt | grep -vE 'Systems|Key|Java|Align|Driver|printer|MCLN|object|software|enough|Afd|enable|System|UUUU|Pos|SU|text|Body|Buffer|Length|match|Document|Un|On|tal|ing|ype|ign|Info|Instance|id32|p1|l1|File|Store|Selector|Available|Dll|Call|Make|maker|Init|Target|Put|Get|Requires|Column|0a1|0h1|0u1|0Z1|Params|resolve|0w1|0L1|0000000000000|Month|ByName|0000|000|2018|GUI|Command|long|status|Permission|IL|Il|Nil|web|ID|Runtime|es|Lower|Delayed|Transition|Bus|Flags|Image|Memory' | uniq | less
```
Output:
```
ssssssssssssssss
b03f5f7f11d50a3a
CryptoStreamMode
ContainerControl
ICryptoTransform
encryptDirectory
....
```

Sweet, it's right above. No need to apply energy to go traverse the rabbit hole. Now, we see the previous dump where we are supposed to search `key`
We are supposed to have the `key` right at the very top unless we are superunlucky and key matches one of our invert grep logic, then we will fail. But chances are super duper less.

Now, we have 2 candidates
```
utav4823DF041B0
aDOBofVYUNVnmp7
```
I tried each one as flag, and the second one worked.

##### Flag: CTF{aDOBofVYUNVnmp7}

