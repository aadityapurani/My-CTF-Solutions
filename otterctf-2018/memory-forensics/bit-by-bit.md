# Bit by Bit
Point 100

```
Find Bitcoin address
```

# Description:

Now, we need to dump the `vmware-tray.exe` from the memory image. I do it with
```
$ python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 procdump -D dump/ -p 3720
```
If you want to see the dumped exec https://transfer.sh/Dss8z/hidd.exe
It is a real ransomware, so handle with care. and make sure you run it in VMWare / Virtual Box. Well, as you gotta patch the bin before you run it. But as it is a .NET executable, it is trivial to load it into Dnspy and retrieve the Bitcoin address

##### Flag: CTF{1MmpEmebJkqXG8nQv4cjJSmxZQFVmFo63M}
