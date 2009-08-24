'''
Created on 2009-8-13

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

class Goods(webapp.RequestHandler):
    def get(self):
                
        nick = self.request.get('nick')
        iid = self.request.get('id')
        click_url = self.request.get('click_url')
        click_url_parts = click_url.split("?e=");
        click_url = click_url_parts[0]+"?e="+click_url_parts[1].replace("/","%2F").replace("+","%2B").replace("=","%3D")
        click_url += "&c="+self.request.get('c')
        
        self.redirect(click_url)
        
        #t = time.localtime()

        #paramArray = {
        #              'app_key':    TOPUtil.APP_KEY,
        #              'method':     TOPUtil.API_COMMAND_ITEM_GET,
        #              'format':     TOPUtil.API_FORMAT_JSON,
        #              'v':          TOPUtil.API_VERSION_VALUE,
        #              'timestamp':  time.strftime('%Y-%m-%d %X', t),
        #              'fields':     'iid,title,nick,pic_path,price,cid,num,desc',
        #              'iid':        iid.encode('utf-8'),
        #              'nick':       nick.encode('utf-8')
        #}
        
        #sign = TOPUtil._sign(paramArray, TOPUtil.APP_SECRET);
        #paramArray['sign'] = sign

        #form_data = urllib.urlencode(paramArray)
        #urlopen = urllib2.urlopen(TOPUtil.TOP_REST_URL, form_data)

        #try:
        #    rsp = urlopen.read()
        #    obj = simplejson.loads(rsp)
        #    title = obj['rsp']['items'][0]['title']
        #    catid = obj['rsp']['items'][0]['cid']
        #    desc = obj['rsp']['items'][0]['desc']
        #    num = obj['rsp']['items'][0]['num']
        #    price = obj['rsp']['items'][0]['price']
        #    pic_path = obj['rsp']['items'][0]['pic_path'];
        #    cid = obj['rsp']['items'][0]['cid']
            #rsp = rsp.decode('UTF-8');
        #except KeyError, e:
        #    title = ''
        #    catid = ''
        #    desc = ''
        #    num = ''
        #    price = ''
        #    pic_path = ''
        #    cid = '0'      
        
        #t = time.localtime()

        #paramArray = {
        #              'app_key':    TOPUtil.APP_KEY,
        #              'method':     TOPUtil.API_COMMAND_CATEGORY_GET,
        #              'format':     TOPUtil.API_FORMAT_JSON,
        #              'v':          TOPUtil.API_VERSION_VALUE,
        #              'timestamp':  time.strftime('%Y-%m-%d %X', t),
        #              'fields':     'cid,name',
        #              'parent_cid': cid
        #}
        
        #sign = TOPUtil._sign(paramArray, TOPUtil.APP_SECRET);
        #paramArray['sign'] = sign

        #form_data = urllib.urlencode(paramArray)
        #urlopen = urllib2.urlopen(TOPUtil.TOP_REST_URL, form_data)
        
        #try:
        #    rsp = urlopen.read()
        #    obj = simplejson.loads(rsp)
        #    item_cats = obj['rsp']['item_cats']
        #    #rsp = rsp.decode('UTF-8');
        #except KeyError, e:
        #    item_cats = {}
        

        #template_values = {
        #                   'iid':               iid,
        #                   'nick':              nick,
        #                   'title':             title,
        #                   'catid':             catid,
        #                   'desc':              desc,
        #                   'num':               num,
        #                   'price':             price,
        #                   'pic_path':          pic_path,
        #                   'click_url':         click_url,
        #                   'item_cats':         item_cats
        #}     
        
        #path = os.path.join(os.path.dirname(os.pardir), 
        #                    'template', 'goods.html')
        #self.response.out.write(template.render(path, template_values))