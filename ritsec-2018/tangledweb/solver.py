# Ripped of from my very old solution from a Hackerrank CTF :rollsafe:
from bs4 import BeautifulSoup
from sets import Set
import urllib2
import re

def crawlWeb(url,limit,bull):
    global visited_list
    if limit==0 :
        notvisited_list.add(url)            
        return
    if url not in visited_list :                
        visited_list.add(url)                
        try:
            print "Extracting URL : "+url
            content = urllib2.urlopen(url)        
            content1 = urllib2.urlopen(url).read()
                soup = BeautifulSoup(content, 'lxml')        
            if content1.find('Secret'):
                print content1
            for link in soup.findAll('a'):        
                hiperLink = link.get('href')
                if hiperLink and hiperLink[0] != '#' and hiperLink[0]!='/':
                    if re.match( r'http[s]?://.*', hiperLink , re.I) :
                        crawlWeb(hiperLink,limit-1,bull)
                    else :
                        crawlWeb(bull+hiperLink,limit-1,bull)
        except urllib2.URLError, e:
                print "Error while opening this link "+url

                        
visited_list = Set()
notvisited_list = Set()


crawlWeb("http://fun.ritsec.club:8007/", 1000, "http://fun.ritsec.club:8007/")
