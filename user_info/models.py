from django.db import models


# Create your models here.

class UserInfo(models.Model):
    id = models.BigIntegerField(primary_key=True, max_length=20)
    Name = models.CharField(max_length=128)
    CardNo = models.CharField(max_length=32)
    Descriot = models.CharField(max_length=512)
    CtfTp = models.CharField(max_length=32)
    CtfId = models.CharField(max_length=64)
    Gender = models.CharField(max_length=2)
    Birthday = models.CharField(max_length=16)
    Address = models.CharField(max_length=128)
    Zip = models.CharField(max_length=60)
    Dirty = models.CharField(max_length=60)
    District1 = models.CharField(max_length=60)
    District2 = models.CharField(max_length=60)
    District3 = models.CharField(max_length=60)
    District4 = models.CharField(max_length=60)
    District5 = models.CharField(max_length=60)
    District6 = models.CharField(max_length=60)
    FirstNm = models.CharField(max_length=60)
    LastNm = models.CharField(max_length=60)
    Duty = models.CharField(max_length=60)
    Mobile = models.CharField(max_length=60)
    Tel = models.CharField(max_length=60)
    Fax = models.CharField(max_length=60)
    EMail = models.CharField(max_length=60)
    Nation = models.CharField(max_length=60)
    Taste = models.CharField(max_length=60)
    Education = models.CharField(max_length=60)
    Company = models.CharField(max_length=60)
    CTel = models.CharField(max_length=60)
    CAddress = models.CharField(max_length=60)
    CZip = models.CharField(max_length=60)
    Family = models.CharField(max_length=60)
    Version = models.CharField(max_length=60)

    def __str__(self):
        return "%s-%s" % (self.id, self.Name)

    class Meta:
        db_table = 'user_info'
