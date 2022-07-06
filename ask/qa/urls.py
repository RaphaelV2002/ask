from django.urls import re_path, include
urlpatterns = [
re_path(r'^$', views.test),
re_path(r'^login/', views.test),
re_path(r'^signup/', views.test),
re_path(r'^question/<123>/', views.test),
re_path(r'^ask/', views.test),
re_path(r'^popular/', views.test),
re_path(r'^new/', views.test),
]
