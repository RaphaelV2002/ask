from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [                      
   path('', views.home, name='home'),                                                              
   path('login/', views.views.LoginView.as_view(), name='login'),                                    
   path('signup/', views.signup, name='signup'),
   path('logout/', views.log_out, name='logout'),                                   
   path('question/<int:question_id>/', views.question, name='question'),
   path('question/<int:question_id>/delete/',
         views.delete_question,
         name='delete_question'),
   path('question/delete_answer/<int:answer_id>/',
         views.delete_answer,
         name='delete_answer'),
   path('ask/', views.ask, name='ask'),                                         
   path('popular/', views.popular, name='popular'),   
   path('questions/ajax/load_more/', views.load_questions,
         name='load_more')                                                                       
]