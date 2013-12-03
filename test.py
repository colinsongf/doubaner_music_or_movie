#coding:utf-8
import sys, os, time

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
