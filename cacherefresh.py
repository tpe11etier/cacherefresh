#!/usr/bin/env python

import urllib
import urllib2
import cookielib
import ConfigParser
import sys


cj = cookielib.CookieJar()
ck = cookielib.Cookie(version=0,
                      name='killmenothing',
                      value='',
                      port=None,
                      port_specified=False,
                      domain='betacfg01',
                      domain_specified=False,
                      domain_initial_dot=False,
                      path='/',
                      path_specified=True,
                      secure=False,
                      expires=None,
                      discard=True,
                      comment=None,
                      comment_url=None,
                      rest={'HttpOnly': None},
                      rfc2109=False)
cj.set_cookie(ck)

CONF = ConfigParser.ConfigParser()


try:
    CONF.read("cacherefresh.props")
    try:
        server = CONF.get("cacherefresh", "server")
        username = CONF.get("cacherefresh", "username")
        password = CONF.get("cacherefresh", "password")
    except ConfigParser.NoSectionError as e:
        print '%s in cacherefresh.props found.' % e
        sys.exit()
except ConfigParser.NoOptionError as e:
    print '%s in cacherefresh.props found.' % e
    sys.exit()
except IOError as e:
    print 'File %s not found!' % e


def cache_refresh():
    try:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        login_data = urllib.urlencode({'MBLoginName': username,
                                       'MBPassword': password})
        resp = opener.open('http://%s/MBAdmin/DoConnect.asp' % server, login_data)
        resp = opener.open('http://%s/MBadmin/commands.asp' % server)
        resp = opener.open('http://%s/MBAdmin/docommand.asp?&returnpage=commands.asp' % server)
        form_data = urllib.urlencode({'command': 'TEMPLATE_DIR_TS', 'returnpage': 'commands.asp'})
        resp = opener.open('http://%s/MBAdmin/docommand.asp' % server, form_data)
        if "submit1" in resp.read():
            print "Login failed. Cache refresh unsuccessful."
        else:
            print "Cache refresh successful."
        print resp.read()
    except urllib2.URLError as e:
        print e
        print "Server not found."


def main():
    cache_refresh()


if __name__ == '__main__':
    main()