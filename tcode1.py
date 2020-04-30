from subprocess import call
import os

os.system("cp /dev/null tinfo1.txt")
os.system("cp /dev/null tinfo3.txt")
os.system("ls >> tinfo1.txt")

a = open("tinfo1.txt","r")
b = open("tinfo1.txt","r")
j = "/var/www/html/test/songs/"
l = "/var/www/html/"

for line in b:
	c = a.readline().rstrip('\n')
	d = "mediainfo " + c + " >> tinfo2.txt"
	os.system(d)
	e = open("tinfo2.txt","r")
	f = open("tinfo2.txt","r")
	m = open("tinfo2.txt","r")
	for line in e:
		g = f.readline().rstrip('\n')
		n = m.readline().rstrip('\n')
		if n[0:9]=="Track_more":
			n = n[43:]
			k = "sudo ln -s "+j+c+" "+l+n+"/"
		if g[0:5]=="Genre":
			g = g[43:]
			g = g.split(", ")
			for p in g:
				k = k + p
#				os.system(k)
				print(k)
#				i = open("tinfo3.txt","a+")
#				print(k,file = i)
				os.system("cp /dev/null tinfo2.txt")
