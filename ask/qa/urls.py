from django.urls import re_path, include
from django.http import HttpResponse
from views import test, question_list_all
urlpatterns = [                                 
   re_path(r'^$', question_list_all),                                                              
   re_path(r'^login/.*$', test, name='login'),                                    
   re_path(r'^signup/.*', test, name='signup'),                                   
   re_path(r'^question/(?P<id>[0-9]+)/$', test, name='question'),                 
   re_path(r'^ask/.*', test, name='ask'),                                         
   re_path(r'^popular/.*', test, name='popular'),                                 
   re_path(r'^new/.*', test, name='new'),                                         
]
