'''
Created on 2009-8-16

@author: yiqun
'''
import math

class Subpager(object):
    #each_disNums;
    #nums;                  
    #current_page;            
    #sub_pages;  
    #pageNums;
    #subPage_link;   
    #subPage_type; 
 
    def __init__(self, each_disNums, nums, 
                 sub_pages, subPage_link, subPage_type):
        
        self.each_disNums = int(each_disNums)
        self.nums = int(nums)
        self.sub_pages = int(sub_pages)
        self.pageNums = int(math.ceil(int(nums)/int(each_disNums)))
        self.subPage_link = subPage_link;
        self.subPage_type = int(subPage_type)
        
    def _paging_html(self, current_page):
        if self.subPage_type==1:
            return self._paging_html_1(current_page)
        else:
            return u""#return self._paging_html_2(current_page)
    
    def _construct_num_page(self, current_page):
        if self.pageNums < self.sub_pages:
            current_list = range(1,self.pageNums)
        else:
            if current_page<=3:
                current_list = range(1,self.sub_pages+1)
            elif current_page<=self.pageNums and current_page>self.pageNums-self.sub_pages+1:
                current_list = range(self.pageNums-self.sub_pages+1,self.pageNums)                
            else:
                current_list = range(current_page-2,current_page-1+self.sub_pages)
        
        return current_list        

    def _paging_html_1(self, current_page):
        paging_html = u""
        
        current_list = self._construct_num_page(current_page);
        for x in current_list:
            if x==current_page:
                paging_html += u"<div class='curItem' title='curPage'>"+str(x)+u"</div>"
            else:
                url = self.subPage_link+str(x)
                paging_html += u"<a href='"+url+u"'>"+str(x)+u"</a>"
        
        return paging_html;