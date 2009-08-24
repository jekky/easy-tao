'''
Created on 2009-8-20

@author: yiqun
'''
import urllib
import urllib2
import string
import time
import md5
import math
import re
import types
import logging
import os
from django.utils import simplejson
from xml.dom import minidom
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from handler.top_util import TOPUtil

class Shop(webapp.RequestHandler):
    def get(self):
        nick = self.request.get('nick')
        
        t = time.localtime()

        paramArray = {
                      'app_key':    TOPUtil.APP_KEY,
                      'method':     TOPUtil.API_COMMAND_SHOP_GET,
                      'format':     TOPUtil.API_FORMAT_JSON,
                      'v':          TOPUtil.API_VERSION_VALUE,
                      'timestamp':  time.strftime('%Y-%m-%d %X', t),
                      'fields':     'sid,cid,nick,title,desc,bulletin',
                      'nick':       nick.encode('utf-8')
        }
        
        sign = TOPUtil._sign(paramArray, TOPUtil.APP_SECRET);
        paramArray['sign'] = sign

        form_data = urllib.urlencode(paramArray)
        urlopen = urllib2.urlopen(TOPUtil.TOP_REST_URL, form_data)
        
        try:
            rsp = urlopen.read()
            obj = simplejson.loads(rsp)
            sid = obj['rsp']['shops'][0]['sid']
            #rsp = rsp.decode('UTF-8');
        except KeyError, e:
            sid = '';
        
        t = time.localtime()

        paramArray = {
                      'app_key':    TOPUtil.APP_KEY,
                      'method':     TOPUtil.API_COMMAND_TAOBAOKE_SHOPS_CONVERT,
                      'format':     TOPUtil.API_FORMAT_JSON,
                      'v':          TOPUtil.API_VERSION_VALUE,
                      'timestamp':  time.strftime('%Y-%m-%d %X', t),
                      'fields':     'click_url',
                      'sids':       sid.encode('utf-8'),
                      'nick':       TOPUtil.USER_NICK
        }
        
        sign = TOPUtil._sign(paramArray, TOPUtil.APP_SECRET);
        paramArray['sign'] = sign

        form_data = urllib.urlencode(paramArray)
        urlopen = urllib2.urlopen(TOPUtil.TOP_REST_URL, form_data)
        
        try:
            rsp = urlopen.read()
            obj = simplejson.loads(rsp)
            click_url = obj['rsp']['taobaokeShops'][0]['click_url']
            #rsp = rsp.decode('UTF-8');
        except KeyError, e:
            click_url = '';
        
        self.redirect(click_url)