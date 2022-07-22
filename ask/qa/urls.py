from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [                                 
   path('', views.home, name='home'),                                                              
   path('login', views.views.LoginView.as_view(), name='login'),                                    
   path('signup', views.SignUpView.as_view(), name='signup'),                                   
   path('question/<int:id>', views.answer, name='question'),                 
   path('ask/', views.ask, name='ask'),                                         
   path('popular', views.popular, name='popular'),                                 
   path('new', views.test, name='new'),                                         
]