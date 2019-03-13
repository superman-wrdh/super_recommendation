from django.db import models


# Create your models here.
class BlogType(models.Model):
    class Meta:
        db_table = "blog_type"

    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=128)
    order = models.IntegerField()
    """
    idint(11) NOT NULL
    typeNamevarchar(30) NULL
    orderNoint(11) NULL
    """


class Bloger(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=128)
    """
    idint(11) NOT NULL
    userNamevarchar(50) NULL
    passwordvarchar(100) NULL
    profiletext NULL
    nickNamevarchar(50) NULL
    signvarchar(100) NULL
    imageName
    """


class Blog(models.Model):
    class Meta:
        db_table = "blog"

    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=128)
    key_world = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)
    content = models.TextField()
    created_date = models.DateTimeField()
    updated_time = models.DateTimeField()
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    bloger = models.ForeignKey(Bloger, on_delete=models.CASCADE)
    """
    idint(11) NOT NULL
    titlevarchar(200) NULL
    summaryvarchar(400) NULL
    releaseDatedatetime NULL
    clickHitint(11) NULL
    replyHitint(11) NULL
    contenttext NULL
    typeIdint(11) NULL
    keyWord
    """


class Comment(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    """
    idint(11) NOT NULL
    userIpvarchar(50) NULL
    blogIdint(11) NULL
    contentvarchar(1000) NULL
    commentDatedatetime NULL
    stateint(11) NULL
    """


class Link(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    """
    idint(11) NOT NULL
    linkNamevarchar(100) NULL
    linkUrlvarchar(200) NULL
    orderNoint(11) NULL
    """


class LoginRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    """

    """


class Property(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    """

    """


class SearchWorld(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    """

    """
