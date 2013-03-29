#!/usr/bin/python
import re, random, time, sys, urllib2
from subprocess import Popen, PIPE
#########################################################################                                           
#                                                                       #
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
    def __init__(self):
        self.ip_port=[]
        suportedsites=["http://www.ip-adress.com/proxy_list/"]
        self.useragents 	= ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
					'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
					'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
					'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
				        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
				        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
				        'Microsoft Internet Explorer/4.0b1 (Windows 95)',
				        'Opera/8.00 (Windows NT 5.1; U; en)',
					'amaya/9.51 libwww/5.4.0',
					'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
					'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
					'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
					'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
					'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
					'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]'] 
        if sys.platform in ['linux-i386','linux2','darwin']:
            self.lin_win = True
        elif sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
            self.lin_win = False
        self.builder()
        for i in suportedsites:
            self.scraper(i)
        
    def builder(self):#Crea un opener con un random User-Agent
        opener = urllib2.build_opener(urllib2.HTTPHandler())
        opener.addheaders = [('User-agent',random.choice(self.useragents))]
        urllib2.install_opener(opener)

    def scraper(self,url):
        print "Getting URL list from %s" % url        
    	source = urllib2.urlopen(url).read()
    	founds = re.findall("\d+.\d+.\d+.\d+:[80]+",source)#saca los proxys del URL
    	self.order(founds)
    
    def order(self,l):
        for i in l:
            if i not in self.ip_port:
                self.ip_port.append(i)#Los guarda en una lista sin repetirse
        for i in self.ip_port:
            global donotrepeat#los revisa que no se ayan escaneado
            if i not in donotrepeat:
                
                donotrepeat.append(i)
                i = i.split(':')
                
                self.ping(i[0],i[1])

    def prnt(self,host,port,latency):#Imprime los proxy de acuerdo a su latency
            if int(latency) < 199:
                print "Proxy: %s:%s <----- Good Latency %s" %(host,port,str(latency))
            elif int(latency) > 200 and int(latency) < 499:
                print "Proxy: %s:%s <----- Slow Latency %s" %(host,port,str(latency))
            elif int(latency) > 500:
                print "Proxy: %s:%s <----- Bad Latency %s" %(host,port,str(latency))      

    def ping(self,host,port):
        ####PARTE DE WINDOWS####
        if self.lin_win == False:
            try:
                p = Popen('ping -n 1 ' + str(host), stdout=PIPE, shell = True)
                m = re.search('Average = (.*)ms', p.stdout.read())
                if m:
                    latency = m.group(1)
                    self.prnt(host,port,latency)
            except KeyboardInterrupt:
                print "!Quiting!"
                sys.exit(1)
        ####PARTE DE LINUX####    
        elif self.lin_win == True:
            try:
                process = Popen('ping -c 1 ' + str(host), stdout=PIPE, stderr=PIPE, shell = True)
                value = process.communicate()[0]
                pattern = re.compile(r'[\d|\.]+/([\d|\.]+)/[\d|\.]+')
                new_value = pattern.findall(value)
                m = ''.join(new_value)
                if m:
                    latency = m.split('.')
                    self.prnt(host,port,latency[0])

            except KeyboardInterrupt:
                print "!Quiting!"
                sys.exit(1)
        
if __name__ == '__main__':
    global donotrepeat
    donotrepeat=[]
    value1 = len(donotrepeat)
    while True:
        t = Proxyworker()
        value2 = len(donotrepeat)
        mat = value2 - value1
        value1 = len(donotrepeat)
        print "\nA total of "+str(mat)+" new proxy's where tested\n"
        time.sleep(120)
