from django.urls import url, include
urlpatterns = [
url(r'^$', include('qa.urls')),
url(r'^login/', include('qa.urls')),
url(r'^signup/', include('qa.urls')),
url(r'^question/<123>/', include('qa.urls')),
url(r'^ask/', include('qa.urls')),
url(r'^popular/', include('qa.urls')),
url(r'^new/', include('qa.urls')),
]
