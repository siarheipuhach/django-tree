from django.conf.urls import url
from django.contrib import admin
from menu.views import MenuView, MenuDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MenuView.as_view()),
    url(r'^(?P<page_url>[\w\d_/-]+)/$', MenuDetailView.as_view(), name='menu_detail'),
]
