from django.urls import path, include
from django.http import HttpResponse
from . import views
urlpatterns = [                                 
   path('', views.new_question_list_all),                                                              
   path('login/', views.test, name='login'),                                    
   path('signup/', views.test, name='signup'),                                   
   path('question/<int:id>/', views.question, name='question'),                 
   path('ask/', views.test, name='ask'),                                         
   path('popular/', views.rating_question_list_all, name='popular'),                                 
   path('new/', views.test, name='new'),                                         
]
