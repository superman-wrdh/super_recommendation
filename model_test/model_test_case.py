from django.conf import settings
from django.apps import apps
import pymysql
from super_recommendation.settings import DATABASES

db_conf = DATABASES.get('default')


def set_up():
    # windows system mysql driver
    pymysql.install_as_MySQLdb()

    conf = {
        'INSTALLED_APPS': [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.messages',
            'django.contrib.sessions',
            'django.contrib.sitemaps',
            'django.contrib.sites',
            'django.contrib.staticfiles',
            'web_api',
        ],
        'DATABASES': {
            'default': {
                'ENGINE': db_conf.get('ENGINE'),
                'NAME': db_conf.get('NAME'),
                'USER': db_conf.get('USER'),
                'PASSWORD': db_conf.get('PASSWORD'),
                'HOST': db_conf.get('HOST'),
                'PORT': db_conf.get('PORT')
            }
        },
        'TIME_ZONE': 'UTC'
    }

    settings.configure(**conf)
    apps.populate(settings.INSTALLED_APPS)


set_up()

if __name__ == '__main__':
    # import you models
    from web_api.models import UserRegCode
    # operation
    hosts = UserRegCode.objects.all()
    print(len(hosts))
