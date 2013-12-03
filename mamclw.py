#coding:utf-8
import sys, os, time
from BeautifulSoup import BeautifulSoup
import urllib, urllib2
from urllib2 import URLError
import re

class ContactList:
    
    def __init__(self, username):
        self.url_contact = 'http://api.douban.com/people/%s/contacts'%username
        
    def __str__(self):
        return self.url_contact
    
    def getContactUrl(self):
        response = urllib2.urlopen(self.url_contact)
        xml_cont = response.read()
        node = ''
        sidx, eidx = 0, 0
        while xml_cont.find('<id>') != -1:
            sidx = xml_cont.find('<id>')
            if xml_cont.find('</id>') != -1:
                eidx = xml_cont.find('</id>')
                node = xml_cont[sidx+4:eidx]
                xml_cont = xml_cont[eidx+4:]
                yield node

class Clawer:
    
    def __init__(self, url, data = None, method = 'post'):
        self.params = urllib.urlencode(data) if isinstance(data,dict) else None
        self.method = method.upper()
        self.url = url
    
    def __str__(self):
        res = '''url : %s\nparams : %s\nmethod : %s'''%(self.url, self.params, self.method)
        return res
    
    def _doReq(self):
        try:
            if self.method == 'POST':
                req = urllib2.Request(self.url, self.params)
            else:
                req = urllib2.Request('%s?%s'%(self.url, self.params))
            response = urllib2.urlopen(req)
            html_con = response.read()
            ecode = response.code
            response.close()
            return html_con, ecode
        except URLError, e:
            print e

class MaMClawer(Clawer):
    
    def __init__(self, url, data = None, method = 'post'):
        Clawer.__init__(self, url, data, method)
        self.htmcon, self.code = self._doReq()
        
    def __str__(self):
        return str(self.code)
    
    def _isGood(self):
        if self.code == 200:
            return True
        else:
            return False
    
    def parseMaMData(self):
        if self._isGood():
            res = [0, 0]
            pat = re.compile('[0-9]*')
            hbs = BeautifulSoup(self.htmcon)
            #parse movie DATA
            mvtag = hbs.find('div', id = 'movie').find('h2').findAll('span')[0]
            for mt in mvtag.findAll('a'):
                match = pat.match(mt.string)
                if match:
                    res[0] += int(match.group())
            #parse music DATA
            mstag = hbs.find('div', id = 'music').find('h2').findAll('span')[0]
            for mt in mstag.findAll('a'):
                match = pat.match(mt.string)
                if match:
                    res[1] += int(match.group())
            return res


if __name__=='__main__':
    user = '67258376'
    cp = ContactList(user)
    def test(cp):
        print cp
        cp_g = cp.getContactUrl()
        url1 = cp_g.next()
        print cp_g.next()
        print cp_g.next()
        print cp_g.next()
        url1 = 'http://www.douban.com/people/%s/'%url1.split('/')[-1]
        print url1
        clw = Clawer(url1)
        print clw
        htmlc , ecode = clw._doReq()
        f=open('htmlcontent.html', 'w')
        f.write(htmlc)
        f.close()
        mmc = MaMClawer(url1)
        print mmc
        print mmc.parseMaMData()
    test(cp)

