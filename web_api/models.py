from django.db import models
from uuid import uuid4
from datetime import datetime
import random


# Create your models here.


class UserRegCode(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    user_id = models.CharField(max_length=36)
    reg_code = models.CharField(max_length=36)
    created_time = models.DateTimeField()

    def __str__(self):
        return "%s-%s" % (self.id, self.reg_code)

    class Meta:
        db_table = 'user_reg_code'


class Resource(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    type = models.IntegerField()  # 文件类型
    mime_type = models.CharField(max_length=64)  # 浏览器标识的类型
    reference_id = models.CharField(max_length=36)  # 根据业务关联的其他id 比如uer_id
    name = models.CharField(max_length=255)
    original_file_name = models.CharField(max_length=255)  # 文件原始名字
    description = models.CharField(max_length=255)  # 描叙
    extension = models.CharField(max_length=30)
    storage_type = models.CharField(max_length=30)
    storage_param = models.CharField(max_length=255)
    size = models.IntegerField()
    is_public = models.BooleanField()  # 文件能否被公开 需要权限认证才能看
    created_time = models.DateTimeField()


def add():
    x = random.randint(1, 999)
    user = UserRegCode(id=str(uuid4()), user_id='hc' + x + '@163.com', reg_code=str(uuid4()),
                       created_time=datetime.now())
    user.save()


def remove():
    pass


def update():
    pass


def query():
    pass


if __name__ == '__main__':
    add()
