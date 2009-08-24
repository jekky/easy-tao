import urllib
import urllib2
import string
import time
import md5
import re
import types
import logging
import os
from django.utils import simplejson
from xml.dom import minidom
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from handler.category import Category
from handler.goods import Goods
from handler.search import Search
from handler.shop import Shop

#from category import Category
#from goods import Goods
#from search import Search

class MainPage(webapp.RequestHandler):
    def get(self):
                
        template_values = {
        }
        
        path = os.path.join(os.path.dirname(__file__), 
                            'template', 'index.html')
        self.response.out.write(template.render(path, template_values))


application = webapp.WSGIApplication([('/', MainPage),
                                      ('/category',Category),
                                      ('/goods',Goods),
                                      ('/search',Search),
                                      ('/shop',Shop)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
