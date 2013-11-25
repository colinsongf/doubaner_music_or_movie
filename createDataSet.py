#coding:utf-8
import sys, os, time
import urllib, urllib2

APIkey = '0e8c9ef9ee3ce03b2ba5dcedcab6a0b1'

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

class UserInfo:
    
    def __init__(self):
        pass
        
if __name__=='__main__':
    user = '67258376'
    cp = ContactList(user)
    def test(cp):
        print cp
        cp_g = cp.getContactUrl()
        print cp_g.next()
        print cp_g.next()
        print cp_g.next()
        print cp_g.next()
        
    test(cp)
