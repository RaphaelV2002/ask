from django.urls import re_path, include
from django.http import HttpResponse
from . import views
urlpatterns = [                                 
   re_path(r'^$', views.new_question_list_all),                                                              
   re_path(r'^login/.*$', views.test, name='login'),                                    
   re_path(r'^signup/.*', views.test, name='signup'),                                   
   re_path(r'^question/(?P<id>[0-9]+)/$', views.test, name='question'),                 
   re_path(r'^ask/.*', views.test, name='ask'),                                         
   re_path(r'^popular/.*', views.rating_question_list_all, name='popular'),                                 
   re_path(r'^new/.*', views.test, name='new'),                                         
]
