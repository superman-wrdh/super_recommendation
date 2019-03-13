from django.conf import settings
from django.apps import apps
import pymysql

import pandas as pd
from datetime import datetime

db_conf = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'user_info',
    'USER': 'root',
    'PASSWORD': 'wsw@2018',
    'HOST': '47.98.146.17',
    'PORT': 8612,
}


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
            'user_info'
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


def read_date_from_csv():
    df = pd.read_csv(r"D:\资料\2000W开房数据\2000W\1-200W.csv")
    return df


def main():
    set_up()

    from user_info.models import UserInfo

    df = read_date_from_csv()
    df = df.where(df.notnull(), None)
    count = 0
    insert_start = datetime.now()
    print('start insert index')
    for _, rows in df.iterrows():
        try:
            u = rows.to_dict()
            UserInfo(**u).save()
        except Exception as e:
            print("Exception", str(e), u)
        if count > 0 and count % 10000 == 0:
            print("insert data rows ", count, " take times ", ((datetime.now()) - insert_start).seconds)
        count = count + 1
    print('finished', count)


def query():
    set_up()
    from user_info.models import UserInfo
    qr = UserInfo.objects.filter(Gender=None).all()
    arr = [i for i in qr]
    for i in arr:
        if len(str(i.CtfId)) == 18 and int(str(i.CtfId)[16:17]) % 2 == 0:
            i.Gender = 'F'
            print("F")
        else:
            i.Gender = 'M'
            print("M")
        i.save()


if __name__ == '__main__':
    query()
