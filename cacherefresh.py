#!/usr/bin/env python

import urllib, urllib2, cookielib

cj = cookielib.CookieJar()
ck = cookielib.Cookie(version=0, name='killmenothing', value='', port=None, port_specified=False, domain='betacfg01', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
cj.set_cookie(ck)

def beta3():
    username = 'qatest'
    password = '12345'
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    login_data = urllib.urlencode({'MBLoginName' : username, 'MBPassword' : password})
    resp = opener.open('http://beta3cfg01/MBAdmin/DoConnect.asp', login_data)
    resp = opener.open('http://beta3cfg01/MBadmin/commands.asp')
    resp = opener.open('http://beta3cfg01/MBAdmin/docommand.asp?&returnpage=commands.asp')
    form_data = urllib.urlencode({'command' : 'TEMPLATE_DIR_TS', 'returnpage' : 'commands.asp'})
    resp = opener.open('http://beta3cfg01/MBAdmin/docommand.asp', form_data)
    result = resp.read()
    print result

def beta4():
    username = 'tpelletier'
    password = '12345'
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    login_data = urllib.urlencode({'LoginName' : username, 'Password' : password})
    resp = opener.open('http://beta4cfg01/MBAdmin/DoConnect.asp', login_data)
    resp = opener.open('http://beta4cfg01/MBadmin/commands.asp')
    resp = opener.open('http://beta4cfg01/MBAdmin/docommand.asp?&returnpage=commands.asp')
    form_data = urllib.urlencode({'command' : 'TEMPLATE_DIR_TS', 'returnpage' : 'commands.asp'})
    resp = opener.open('http://beta4cfg01/MBAdmin/docommand.asp', form_data)
    result = resp.read()
    print result
    
def main():
    beta3()
    beta4()
    
main()