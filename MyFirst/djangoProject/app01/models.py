from django.db import models

# Create your models here.

#该类会在数据库创建一个表，表名叫app01_userinfo()
#相当于执行 create table app01_userinfo()
class UserInfo(models.Model):
    #CharField字符串类型
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    #IntegerField是一个整型
    age = models.IntegerField()

#往表格里添加信息，找到这个类，相当于insert
#UserInfo.objects.create(name='wuaffg', password='123', age=18)

#相当于以下
"""
create table app01_userinfo(){
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int
}
"""

class Dapartment(models.Model):
    title = models.CharField(max_length=16)
