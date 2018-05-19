from django.conf.urls import url
from web_api import views

urlpatterns = (
    url(r'^test', views.first_api),
)
