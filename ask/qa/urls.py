from django.urls import url, include
urlpatterns = [
url(r'^$', views.test),
url(r'^login/', views.test),
url(r'^signup/', views.test),
url(r'^question/<123>/', views.test),
url(r'^ask/', views.test),
url(r'^popular/', views.test),
url(r'^new/', views.test),
]
