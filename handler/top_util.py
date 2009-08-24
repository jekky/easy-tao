'''
Created on 2009-8-13

@author: yiqun
'''
import md5
import time
import urllib
import urllib2


class TOPUtil():
    APP_KEY = "12004988";
    APP_SECRET = "760af36c5a602cf17742e1a4ab209ca6";
    USER_PID = "mm_13493956_0_0";
    USER_NICK = "jekky_yiqun";
    
    API_VERSION_VALUE = "1.0";
    API_FORMAT_JSON = "json";
    TOP_SANDBOX_REST_URL = "http://gw.sandbox.taobao.com/router/rest";
    TOP_REST_URL = "http://gw.api.taobao.com/router/rest";
    
    API_COMMAND_CATEGORY_GET = "taobao.itemcats.get.v2";
    API_COMMAND_ITEM_GET = "taobao.item.get";    
    API_COMMAND_SHOP_GET = "taobao.shop.get";
    API_COMMAND_TAOBAOKE_ITEM_GET = "taobao.taobaoke.items.get";
    API_COMMAND_TAOBAOKE_ITEM_CONVERT = "taobao.taobaoke.items.convert";
    API_COMMAND_TAOBAOKE_SHOPS_CONVERT = "taobao.taobaoke.shops.convert";
    
    def _sign(param,sercetCode):
        src = sercetCode + ''.join(["%s%s" % (k, v) for k, v in sorted(param.items())])
        return md5.new(src).hexdigest().upper()
    
    _sign = staticmethod(_sign)