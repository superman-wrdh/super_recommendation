from django.conf.urls import url
from web_api import views
from web_api import web_stroage

urlpatterns = (
    url(r'^test', views.first_api),
    url(r'^user_reg', views.register),
    url(r'^send_reg_code', views.send_reg_code),
    url(r'^upload', web_stroage.upload_file),
    url(r'^blog/list/$', web_stroage.blog_list)
)
