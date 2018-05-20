from django.conf.urls import url
from web_api import views

urlpatterns = (
    url(r'^test', views.first_api),
    url(r'^user_reg', views.register),
    url(r'^send_reg_code', views.send_reg_code)
)
