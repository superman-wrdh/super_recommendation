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
