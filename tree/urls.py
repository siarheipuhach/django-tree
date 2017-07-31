from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from menu.views import MenuView, MenuDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MenuView.as_view()),
    url(r'^(?P<page_url>[\w\d_/-]+)/$', MenuDetailView.as_view(), name='menu_detail'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
