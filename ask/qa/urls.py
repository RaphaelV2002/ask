from django.urls import path, include
from django.http import HttpResponse
from . import views
urlpatterns = [                                 
   path('', views.home),                                                              
   path('login', views.test, name='login'),                                    
   path('signup', views.test, name='signup'),                                   
   path('question/<int:id>', views.question, name='question'),                 
   path('ask', views.ask, name='ask'),                                         
   path('popular', views.popular, name='popular'),                                 
   path('new', views.test, name='new'),                                         
]
