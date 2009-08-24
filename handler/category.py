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
from handler.subpager import Subpager

class Category(webapp.RequestHandler):
    def get(self):
                
        if len(self.request.get('catid'))==0:
            catid = '0'
        else:
            catid = self.request.get('catid')
            
        if len(self.request.get('page'))==0:
            page = '1'
        else:
            page = self.request.get('page')
        
        t = time.localtime()

        paramArray = {
                      'app_key':    TOPUtil.APP_KEY,
                      'method':     TOPUtil.API_COMMAND_CATEGORY_GET,
                      'format':     TOPUtil.API_FORMAT_JSON,
                      'v':          TOPUtil.API_VERSION_VALUE,
                      'timestamp':  time.strftime('%Y-%m-%d %X', t),
                      'fields':     'cid,name',
                      'parent_cid': catid
        }
        
        sign = TOPUtil._sign(paramArray, TOPUtil.APP_SECRET);
        paramArray['sign'] = sign

        form_data = urllib.urlencode(paramArray)
        urlopen = urllib2.urlopen(TOPUtil.TOP_REST_URL, form_data)

        try:
            rsp = urlopen.read()
            obj = simplejson.loads(rsp)
            item_cats = obj['rsp']['item_cats']
            #rsp = rsp.decode('UTF-8');
        except KeyError, e:
            item_cats = {}
        
        t = time.localtime()
        page_size = '20'
        
        paramArray = {
                      'app_key':    TOPUtil.APP_KEY,
                      'method':     TOPUtil.API_COMMAND_TAOBAOKE_ITEM_GET,
                      'format':     TOPUtil.API_FORMAT_JSON,
                      'v':          TOPUtil.API_VERSION_VALUE,
                      'timestamp':  time.strftime('%Y-%m-%d %X', t),
                      'fields':     'iid,title,nick,pic_url,price,click_url,commission,commission_rate,commission_num',
                      'pid':        TOPUtil.USER_PID,
                      'cid':        catid,
                      'page_no':    page,
                      'page_size':  page_size
        }
        
        sign = TOPUtil._sign(paramArray, TOPUtil.APP_SECRET);
        paramArray['sign'] = sign

        form_data = urllib.urlencode(paramArray)
        urlopen = urllib2.urlopen(TOPUtil.TOP_REST_URL, form_data)

        try:
            rsp = urlopen.read()
            obj = simplejson.loads(rsp)
            taobaoke_items = obj['rsp']['taobaokeItems']      
            for item in taobaoke_items:
                item['commission_rate'] = float(item['commission_rate'])/200;
                item['commission'] = float(item['commission'])/2;
                total_results = obj['rsp']['totalResults']
        except KeyError, e:
            taobaoke_items = {}
            total_results = '0'
        
        # paging process
        sub_pages = 10
        subpage_link = u"category?catid="+catid+u"&page="
        
        pager = Subpager(int(page_size),int(total_results),
                         sub_pages,subpage_link,1)
        paging_html = pager._paging_html(int(page))

        template_values = {
                           'item_cats':         item_cats,
                           'taobaoke_items':    taobaoke_items,
                           'total_results':     total_results,
                           'total_pages':       int(math.ceil(int(total_results)/20)),
                           'paging_html':       paging_html
        }
        

        #self.response.headers['Content-Type'] = 'text/json'
        #self.response.out.write(rsp)
        #simplejson.dump(obj,self.response.out)
        
        path = os.path.join(os.path.dirname(os.pardir),
                            'template', 'category.html')
        self.response.out.write(template.render(path, template_values))