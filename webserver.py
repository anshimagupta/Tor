# http://www.dev-explorer.com/articles/using-python-httplib
# /usr/bin/python 

from httplib import * 
from urllib import * 
from StringIO import * 
from gzip import * 
from datetime import datetime
import socks
import socket
from urllib2 import Request, urlopen
import json
from stem import CircStatus
from stem.control import Controller, EventType
import time
from stem import Signal

time_start = (datetime.now())
time_end = (datetime.now())

def webserver_connection( hostname, counter, connection_type ):
  for i in range(counter):
      print connection_type
      controller.authenticate()
      controller.signal(Signal.NEWNYM)
      socket.socket = socks.socksocket
      connection = HTTPConnection(hostname)  
      connection.request("GET", "") 
      time_start = (datetime.now())
      response = connection.getresponse() 
      time_end = (datetime.now())
      if response.status == 200: 
        print "Status : 200 OK"  
      elif response.status == 404: 
        print "Page Not Found"
      else: 
        print response.status, response.reason 
      connection.close()
      print str(int(round((((time_end - time_start).microseconds)/1000)))) + ' seconds'
  print "My Public IP: " + (json.load(urlopen('http://httpbin.org/ip'))['origin'])

def hidden_webserver_connection (hostname):
    try:
      s = socks.socksocket()
      time_start = datetime.now()
      s.connect((hostname, 80))
    except Exception as e:
      print e
print "My Public IP: " + (json.load(urlopen('http://httpbin.org/ip'))['origin'])

    
with Controller.from_port(port = 9051) as controller:
  webserver_connection('www.google.fr', 10, 'Making request for www.google.fr bypassing Tor')
  print
  webserver_connection('duckduckgo.com', 1, 'Making request for duckduckgo.com bypassing Tor')
  print
  socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
  print
  webserver_connection('www.google.fr', 10, 'With Tor')
  print
  webserver_connection('duckduckgo.com', 10, 'Making request for duckduckgo.com')
  print
  for i in range(10):
    hidden_webserver_connection('3g2upl4pq6kufc4m.onion')
    print 'Making request for 3g2upl4pq6kufc4m.onion' + str(i)
    time_end = datetime.now()
    print str(int(round((((time_end - time_start).microseconds)/1000)))) + ' seconds'