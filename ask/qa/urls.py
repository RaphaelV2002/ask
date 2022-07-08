from views import test
from django.urls import url, include
urlpatterns = patterns('qa.views',                                              
   re_path(r'^$', test),                                                              
   re_path(r'^login/.*$', test, name='login'),                                    
   re_path(r'^signup/.*', test, name='signup'),                                   
   re_path(r'^question/(?P<id>[0-9]+)/$', test, name='question'),                 
   re_path(r'^ask/.*', test, name='ask'),                                         
   re_path(r'^popular/.*', test, name='popular'),                                 
   re_path(r'^new/.*', test, name='new'),                                         
)
