# General Info
Points: 100 point

```
Let's start easy,
PC Name:
IP:
```

# Solution:

IP address could be found it you run `netscan` on the memory dump under Local address.

```
$ python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 netscan
Volatility Foundation Volatility Framework 2.6
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x7d60f010         UDPv4    0.0.0.0:1900                   *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:17 UTC+0000
0x7d62b3f0         UDPv4    192.168.202.131:6771           *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:22 UTC+0000
0x7d62f4c0         UDPv4    127.0.0.1:62307                *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:17 UTC+0000
0x7d62f920         UDPv4    192.168.202.131:62306          *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:17 UTC+0000
0x7d6424c0         UDPv4    0.0.0.0:50762                  *:*                                   4076     chrome.exe     2018-08-04 19:33:37 UTC+0000
0x7d6b4250         UDPv6    ::1:1900                       *:*                                   164      svchost.exe    2018-08-04 19:28:42 UTC+0000
0x7d6e3230         UDPv4    127.0.0.1:6771                 *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:22 UTC+0000
0x7d6ed650         UDPv4    0.0.0.0:5355                   *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7d71c8a0         UDPv4    0.0.0.0:0                      *:*                                   868      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7d71c8a0         UDPv6    :::0                           *:*                                   868      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7d74a390         UDPv4    127.0.0.1:52847                *:*                                   2624     bittorrentie.e 2018-08-04 19:27:24 UTC+0000
0x7d7602c0         UDPv4    127.0.0.1:52846                *:*                                   2308     bittorrentie.e 2018-08-04 19:27:24 UTC+0000
0x7d787010         UDPv4    0.0.0.0:65452                  *:*                                   4076     chrome.exe     2018-08-04 19:33:42 UTC+0000
0x7d789b50         UDPv4    0.0.0.0:50523                  *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7d789b50         UDPv6    :::50523                       *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7d92a230         UDPv4    0.0.0.0:0                      *:*                                   868      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7d92a230         UDPv6    :::0                           *:*                                   868      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7d9e8b50         UDPv4    0.0.0.0:20830                  *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:15 UTC+0000
0x7d9f4560         UDPv4    0.0.0.0:0                      *:*                                   3856     WebCompanion.e 2018-08-04 19:34:22 UTC+0000
0x7d9f8cb0         UDPv4    0.0.0.0:20830                  *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:15 UTC+0000
0x7d9f8cb0         UDPv6    :::20830                       *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:15 UTC+0000
0x7d8bb390         TCPv4    0.0.0.0:9008                   0.0.0.0:0            LISTENING        4        System         
0x7d8bb390         TCPv6    :::9008                        :::0                 LISTENING        4        System         
0x7d9a9240         TCPv4    0.0.0.0:8733                   0.0.0.0:0            LISTENING        4        System         
0x7d9a9240         TCPv6    :::8733                        :::0                 LISTENING        4        System         
0x7d9e19e0         TCPv4    0.0.0.0:20830                  0.0.0.0:0            LISTENING        2836     BitTorrent.exe 
0x7d9e19e0         TCPv6    :::20830                       :::0                 LISTENING        2836     BitTorrent.exe 
0x7d9e1c90         TCPv4    0.0.0.0:20830                  0.0.0.0:0            LISTENING        2836     BitTorrent.exe 
0x7d42ba90         TCPv4    -:0                            56.219.196.26:0      CLOSED           2836     BitTorrent.exe 
0x7d6124d0         TCPv4    192.168.202.131:49530          77.102.199.102:7575  CLOSED           708      LunarMS.exe    
0x7d62d690         TCPv4    192.168.202.131:49229          169.1.143.215:8999   CLOSED           2836     BitTorrent.exe 
0x7d634350         TCPv6    -:0                            38db:c41a:80fa:ffff:38db:c41a:80fa:ffff:0 CLOSED           2836     BitTorrent.exe 
0x7d6f27f0         TCPv4    192.168.202.131:50381          71.198.155.180:34674 CLOSED           2836     BitTorrent.exe 
0x7d704010         TCPv4    192.168.202.131:50382          92.251.23.204:6881   CLOSED           2836     BitTorrent.exe 
0x7d708cf0         TCPv4    192.168.202.131:50364          91.140.89.116:31847  CLOSED           2836     BitTorrent.exe 
0x7d729620         TCPv4    -:50034                        142.129.37.27:24578  CLOSED           2836     BitTorrent.exe 
0x7d72cbe0         TCPv4    192.168.202.131:50340          23.37.43.27:80       CLOSED           3496     Lavasoft.WCAss 
0x7d7365a0         TCPv4    192.168.202.131:50358          23.37.43.27:80       CLOSED           3856     WebCompanion.e 
0x7d81c890         TCPv4    192.168.202.131:50335          185.154.111.20:60405 CLOSED           2836     BitTorrent.exe 
0x7d8fd530         TCPv4    192.168.202.131:50327          23.37.43.27:80       CLOSED           3496     Lavasoft.WCAss 
0x7d9cecf0         TCPv4    192.168.202.131:50373          173.239.232.46:2997  CLOSED           2836     BitTorrent.exe 
0x7d9d7cf0         TCPv4    192.168.202.131:50371          191.253.122.149:59163 CLOSED           2836     BitTorrent.exe 
0x7daefec0         UDPv4    0.0.0.0:0                      *:*                                   3856     WebCompanion.e 2018-08-04 19:34:22 UTC+0000
0x7daefec0         UDPv6    :::0                           *:*                                   3856     WebCompanion.e 2018-08-04 19:34:22 UTC+0000
0x7db83b90         UDPv4    0.0.0.0:0                      *:*                                   3880     WebCompanionIn 2018-08-04 19:33:30 UTC+0000
0x7db83b90         UDPv6    :::0                           *:*                                   3880     WebCompanionIn 2018-08-04 19:33:30 UTC+0000
0x7db9cdd0         UDPv4    0.0.0.0:0                      *:*                                   2844     WebCompanion.e 2018-08-04 19:30:05 UTC+0000
0x7db9cdd0         UDPv6    :::0                           *:*                                   2844     WebCompanion.e 2018-08-04 19:30:05 UTC+0000
0x7dc2dc30         UDPv4    0.0.0.0:50879                  *:*                                   4076     chrome.exe     2018-08-04 19:30:41 UTC+0000
0x7dc2dc30         UDPv6    :::50879                       *:*                                   4076     chrome.exe     2018-08-04 19:30:41 UTC+0000
0x7dc83810         UDPv4    0.0.0.0:5355                   *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7dc83810         UDPv6    :::5355                        *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7dd82c30         UDPv4    0.0.0.0:5355                   *:*                                   620      svchost.exe    2018-08-04 19:26:38 UTC+0000
0x7df00980         UDPv4    0.0.0.0:0                      *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7df00980         UDPv6    :::0                           *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7df04cc0         UDPv4    0.0.0.0:5355                   *:*                                   620      svchost.exe    2018-08-04 19:26:38 UTC+0000
0x7df04cc0         UDPv6    :::5355                        *:*                                   620      svchost.exe    2018-08-04 19:26:38 UTC+0000
0x7df5f010         UDPv4    0.0.0.0:55175                  *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7dfab010         UDPv4    0.0.0.0:58383                  *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7dfab010         UDPv6    :::58383                       *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7e12c1c0         UDPv4    0.0.0.0:0                      *:*                                   3880     WebCompanionIn 2018-08-04 19:33:27 UTC+0000
0x7e163a40         UDPv4    0.0.0.0:0                      *:*                                   3880     WebCompanionIn 2018-08-04 19:33:27 UTC+0000
0x7e163a40         UDPv6    :::0                           *:*                                   3880     WebCompanionIn 2018-08-04 19:33:27 UTC+0000
0x7e1cf010         UDPv4    192.168.202.131:137            *:*                                   4        System         2018-08-04 19:26:35 UTC+0000
0x7e1da010         UDPv4    192.168.202.131:138            *:*                                   4        System         2018-08-04 19:26:35 UTC+0000
0x7dc4ad30         TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        500      lsass.exe      
0x7dc4ad30         TCPv6    :::49155                       :::0                 LISTENING        500      lsass.exe      
0x7dc4b370         TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        500      lsass.exe      
0x7dd71010         TCPv4    0.0.0.0:445                    0.0.0.0:0            LISTENING        4        System         
0x7dd71010         TCPv6    :::445                         :::0                 LISTENING        4        System         
0x7ddca6b0         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        492      services.exe   
0x7ddcbc00         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        492      services.exe   
0x7ddcbc00         TCPv6    :::49156                       :::0                 LISTENING        492      services.exe   
0x7de09c30         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        396      wininit.exe    
0x7de09c30         TCPv6    :::49152                       :::0                 LISTENING        396      wininit.exe    
0x7de0d7b0         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        396      wininit.exe    
0x7de424e0         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        808      svchost.exe    
0x7de45ef0         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        808      svchost.exe    
0x7de45ef0         TCPv6    :::49153                       :::0                 LISTENING        808      svchost.exe    
0x7df3d270         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        868      svchost.exe    
0x7df3eef0         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        868      svchost.exe    
0x7df3eef0         TCPv6    :::49154                       :::0                 LISTENING        868      svchost.exe    
0x7e1f6010         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        712      svchost.exe    
0x7e1f6010         TCPv6    :::135                         :::0                 LISTENING        712      svchost.exe    
0x7e1f8ef0         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        712      svchost.exe    
0x7db000a0         TCPv4    -:50091                        93.142.197.107:32645 CLOSED           2836     BitTorrent.exe 
0x7db132e0         TCPv4    192.168.202.131:50280          72.55.154.81:80      CLOSED           3880     WebCompanionIn 
0x7dbc3010         TCPv6    -:0                            4847:d418:80fa:ffff:4847:d418:80fa:ffff:0 CLOSED           4076     chrome.exe     
0x7dc4bcf0         TCPv4    -:0                            104.240.179.26:0     CLOSED           3        ?4????       
0x7dc83080         TCPv4    192.168.202.131:50377          179.108.238.10:19761 CLOSED           2836     BitTorrent.exe 
0x7dd451f0         TCPv4    192.168.202.131:50321          45.27.208.145:51414  CLOSED           2836     BitTorrent.exe 
0x7ddae890         TCPv4    -:50299                        212.92.105.227:8999  CLOSED           2836     BitTorrent.exe 
0x7ddff010         TCPv4    192.168.202.131:50379          23.37.43.27:80       CLOSED           3856     WebCompanion.e 
0x7e0057d0         TCPv4    192.168.202.131:50353          85.242.139.158:51413 CLOSED           2836     BitTorrent.exe 
0x7e0114b0         TCPv4    192.168.202.131:50339          77.65.111.216:8306   CLOSED           2836     BitTorrent.exe 
0x7e042cf0         TCPv4    192.168.202.131:50372          83.44.27.35:52103    CLOSED           2836     BitTorrent.exe 
0x7e08a010         TCPv4    192.168.202.131:50374          89.46.49.163:20133   CLOSED           2836     BitTorrent.exe 
0x7e092010         TCPv4    192.168.202.131:50378          120.29.114.41:13155  CLOSED           2836     BitTorrent.exe 
0x7e094b90         TCPv4    192.168.202.131:50365          52.91.1.182:55125    CLOSED           2836     BitTorrent.exe 
0x7e09ba90         TCPv6    -:0                            68f0:181b:80fa:ffff:68f0:181b:80fa:ffff:0 CLOSED           2836     BitTorrent.exe 
0x7e0a8b90         TCPv4    192.168.202.131:50341          72.55.154.81:80      CLOSED           3880     WebCompanionIn 
0x7e0d6180         TCPv4    192.168.202.131:50349          196.250.217.22:32815 CLOSED           2836     BitTorrent.exe 
0x7e108100         TCPv4    192.168.202.131:50360          174.0.234.77:31240   CLOSED           2836     BitTorrent.exe 
0x7e124910         TCPv4    192.168.202.131:50366          89.78.106.196:51413  CLOSED           2836     BitTorrent.exe 
0x7e14dcf0         TCPv4    192.168.202.131:50363          122.62.218.159:11627 CLOSED           2836     BitTorrent.exe 
0x7e18bcf0         TCPv4    192.168.202.131:50333          191.177.124.34:21011 CLOSED           2836     BitTorrent.exe 
0x7e1f7ab0         TCPv4    -:0                            56.187.190.26:0      CLOSED           3        ?4????       
0x7e48d9c0         UDPv6    fe80::b06b:a531:ec88:457f:1900 *:*                                   164      svchost.exe    2018-08-04 19:28:42 UTC+0000
0x7e4ad870         UDPv4    127.0.0.1:1900                 *:*                                   164      svchost.exe    2018-08-04 19:28:42 UTC+0000
0x7e511bb0         UDPv4    0.0.0.0:60005                  *:*                                   620      svchost.exe    2018-08-04 19:34:22 UTC+0000
0x7e5dc3b0         UDPv6    fe80::b06b:a531:ec88:457f:546  *:*                                   808      svchost.exe    2018-08-04 19:33:28 UTC+0000
0x7e7469c0         UDPv4    0.0.0.0:50878                  *:*                                   4076     chrome.exe     2018-08-04 19:30:39 UTC+0000
0x7e7469c0         UDPv6    :::50878                       *:*                                   4076     chrome.exe     2018-08-04 19:30:39 UTC+0000
0x7e77cb00         UDPv4    0.0.0.0:50748                  *:*                                   4076     chrome.exe     2018-08-04 19:30:07 UTC+0000
0x7e77cb00         UDPv6    :::50748                       *:*                                   4076     chrome.exe     2018-08-04 19:30:07 UTC+0000
0x7e79f3f0         UDPv4    0.0.0.0:5353                   *:*                                   4076     chrome.exe     2018-08-04 19:29:35 UTC+0000
0x7e7a0ec0         UDPv4    0.0.0.0:5353                   *:*                                   4076     chrome.exe     2018-08-04 19:29:35 UTC+0000
0x7e7a0ec0         UDPv6    :::5353                        *:*                                   4076     chrome.exe     2018-08-04 19:29:35 UTC+0000
0x7e7a3960         UDPv4    0.0.0.0:0                      *:*                                   3880     WebCompanionIn 2018-08-04 19:33:30 UTC+0000
0x7e7dd010         UDPv6    ::1:58340                      *:*                                   164      svchost.exe    2018-08-04 19:28:42 UTC+0000
0x7e413a40         TCPv4    -:0                            -:0                  CLOSED           708      LunarMS.exe    
0x7e415010         TCPv4    192.168.202.131:50346          89.64.10.176:10589   CLOSED           2836     BitTorrent.exe 
0x7e4202d0         TCPv4    192.168.202.131:50217          104.18.21.226:80     CLOSED           3880     WebCompanionIn 
0x7e45f110         TCPv4    192.168.202.131:50211          104.18.20.226:80     CLOSED           3880     WebCompanionIn 
0x7e4cc910         TCPv4    192.168.202.131:50228          104.18.20.226:80     CLOSED           3880     WebCompanionIn 
0x7e512950         TCPv4    192.168.202.131:50345          77.126.30.221:13905  CLOSED           2836     BitTorrent.exe 
0x7e521b50         TCPv4    -:0                            -:0                  CLOSED           708      LunarMS.exe    
0x7e5228d0         TCPv4    192.168.202.131:50075          70.65.116.120:52700  CLOSED           2836     BitTorrent.exe 
0x7e52f010         TCPv4    192.168.202.131:50343          86.121.4.189:46392   CLOSED           2836     BitTorrent.exe 
0x7e563860         TCPv4    192.168.202.131:50170          103.232.25.44:25384  CLOSED           2836     BitTorrent.exe 
0x7e572cf0         TCPv4    192.168.202.131:50125          122.62.218.159:11627 CLOSED           2836     BitTorrent.exe 
0x7e5d6cf0         TCPv4    192.168.202.131:50324          54.197.8.177:49420   CLOSED           2836     BitTorrent.exe 
0x7e71b010         TCPv4    192.168.202.131:50344          70.27.98.75:6881     CLOSED           2836     BitTorrent.exe 
0x7e71d010         TCPv4    192.168.202.131:50351          99.251.199.160:1045  CLOSED           2836     BitTorrent.exe 
0x7e74b010         TCPv4    192.168.202.131:50385          209.236.6.89:56500   CLOSED           2836     BitTorrent.exe 
0x7e78b7f0         TCPv4    192.168.202.131:50238          72.55.154.82:80      CLOSED           3880     WebCompanionIn 
0x7e7ae380         TCPv4    192.168.202.131:50361          5.34.21.181:8999     CLOSED           2836     BitTorrent.exe 
0x7e7b0380         TCPv6    -:0                            4847:d418:80fa:ffff:4847:d418:80fa:ffff:0 CLOSED           2836     BitTorrent.exe 
0x7e7b9010         TCPv4    192.168.202.131:50334          188.129.94.129:25128 CLOSED           2836     BitTorrent.exe 
0x7e94b010         TCPv4    192.168.202.131:50356          77.126.30.221:13905  CLOSED           2836     BitTorrent.exe 
0x7e9ad840         TCPv4    192.168.202.131:50380          84.52.144.29:56299   CLOSED           2836     BitTorrent.exe 
0x7e9bacf0         TCPv4    192.168.202.131:50350          77.253.242.0:5000    CLOSED           2836     BitTorrent.exe 
0x7eaac5e0         TCPv4    192.168.202.131:50387          93.184.220.29:80     CLOSED           3856     WebCompanion.e 
0x7eab4cf0         TCPv4    -:0                            56.219.196.26:0      CLOSED           2836     BitTorrent.exe 
0x7fb9cec0         UDPv4    192.168.202.131:1900           *:*                                   164      svchost.exe    2018-08-04 19:28:42 UTC+0000
0x7fb9d430         UDPv4    127.0.0.1:58341                *:*                                   164      svchost.exe    2018-08-04 19:28:42 UTC+000
```

##### Flag: CTF{192.168.202.131}

We read the registry key for our PC Name
```
$ python vol.py -f OtterCTF.vmem --profile=Win7SP1x64 printkey -o 0xfffff8a000024010 -K 'ControlSet001\Control\ComputerName\ComputerName'
Volatility Foundation Volatility Framework 2.6
Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \REGISTRY\MACHINE\SYSTEM
Key name: ComputerName (S)
Last updated: 2018-06-02 19:23:00 UTC+0000

Subkeys:

Values:
REG_SZ                        : (S) mnmsrvc
REG_SZ        ComputerName    : (S) WIN-LO6FAF3DTFE
```

##### CTF{WIN-LO6FAF3DTFE}
