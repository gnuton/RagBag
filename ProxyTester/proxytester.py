#!/usr/bin/python
import re
import random
import time
import sys
import urllib2
import json
import httplib
import socket
from  datetime import datetime
from subprocess import Popen, PIPE

#########################################################################                                           
#                                                                       #
# Copyright (C) 2013 GNUton                                             #
# Copyright (C) 2010 LeXeL                                              #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# any later version.                                                    #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#########################################################################

class Proxyworker(object):
    supportedsites=[ #"http://www.tubeincreaser.com/proxylist.txt", 
                    #"http://multiproxy.org/txt_all/proxy.txt",
                    "http://www.ip-adress.com/proxy_list/"]

    def __init__(self, checkedProxies):
        self.__useragents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
                             "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02",
                             "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0",
                             "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
                             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:19.0) Gecko/20100101 Firefox/19.0",
                             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.11 (KHTML, like Gecko)"]
        self.__checkedProxies = checkedProxies
        self.__setDefaultRandomUserAgent()

    def start(self, proxyList = "network"):
        proxies = set()
        
        #Get list of proxies to scan
        if proxyList != "network":
            try:
                f = open(proxyList, 'r')
            except IOError as e:
                print e
                sys.exit(1)

            buffer = "".join(f.readlines())
            proxies = re.findall("\d+.\d+.\d+.\d+:\d+", buffer)
            proxies = set(proxies)
            f.close()
        else:
            for i in self.supportedsites:
                proxies = set.union(proxies, self.__scraper(i))

        #Remove already scanned proxies from the list
        proxies -= self.__checkedProxies

        #Scan proxies
        self.__scan(proxies)
  
    def __setDefaultRandomUserAgent(self):
        opener = urllib2.build_opener(urllib2.HTTPHandler())
        userAgent = random.choice(self.__useragents)
        print "Using '%s' as user agent" % userAgent
        opener.addheaders = [('User-agent', userAgent)]
        urllib2.install_opener(opener)

    def __scraper(self, url):
        """ Download proxy IPs from the specified URL"""
        print "Getting URL list from %s" % url
        try:        
    	    source = urllib2.urlopen(url).read()
        except:
            return set()

    	proxies = re.findall("\d+.\d+.\d+.\d+:\d+", source)
        return set(proxies)
    
    def __scan(self,proxies):
        print "Scannig %d proxies" % len(proxies)
        for proxy in proxies:
            self.__checkedProxies.add(proxy)
            latency, isAnonimous = self.__tester(proxy)
            if not latency:
                continue    
            print "Proxy=%s, Latency=%f s, Anonimous=%s, %s" %(proxy, latency, isAnonimous, self.__geolocation(proxy)) 

    def __geolocation(self,ip):
        url = 'http://api.hostip.info/get_html.php?ip=%s&position=true' % ip
        response = urllib2.urlopen(url).read()
        a = response.split('\n')
        return a[0] + ", " + a[1]
  
    def __tester(self, proxyStr):
        """ Returns latency and type of proxy"""
        t = datetime.now()

        proxy_support = urllib2.ProxyHandler({"http" : proxyStr})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)

        try:
            reply = urllib2.urlopen("http://www.gnuton.org/proxychecker/index.php", timeout = 10).read()
        except (urllib2.URLError, httplib.BadStatusLine, socket.timeout, socket.error):
            print "Proxy= %s - Unable to read data. Host down or too slow?" % (proxyStr)
            return None, None

        j = json.loads(reply)
        host = proxyStr.split(":")[0]
        isAnonymous = host == j["ip"] and j["proxy_detected"] == 0
        latency = (datetime.now() - t).microseconds / 1e6
        #print "IP SHOWN" + j["ip"] + "PROXY DETECTED" +  str(j["proxy_detected"]) 
        return latency, isAnonymous 
  
if __name__ == '__main__':
    if len(sys.argv) < 2:
       print "***  Welcome to proxy scanner  ***  "
       print "This script checks the quality of proxies in a file:"
       print " %s proxies.txt" % sys.argv[0]
       print "or the ones available at %s" % str(Proxyworker.supportedsites)
       print " %s network" % sys.argv[0]
       sys.exit(1)

    proxyList = sys.argv[1]
    checkedProxies = set() 

    try: 
        while True:
            t = Proxyworker(checkedProxies)
            t.start(proxyList)

            if proxyList == "network":
                interval = 120
                print "Next check in %d secs" % interval 
                time.sleep(interval)
            else:
                sys.exit(0)
    except KeyboardInterrupt:
         print "Process terminated. %s proxies checked" % len(checkedProxies)
