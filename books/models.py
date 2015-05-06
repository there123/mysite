#coding:utf-8
from django.db import models

# Create your models here.
#每个数据模型都是 django.db.models.Model 的子类
#每个数据库表对应一个类,这条规则的例外情况是多对多关系
#Django会自动为每个模型生成一个自增长的整数主键字段每个Django模型都要求有单独的主键
class Publisher(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	city=models.CharField(max_length=60)
	state_province=models.CharField(max_length=30)
	country=models.CharField(max_length=50)
	website=models.URLField()

	# __unicode__() 方法告诉Python如何将对象以unicode的方式显示出来
	def __unicode__(self):
		return self.name

class Author(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=40)
	email=models.EmailField()

	def __unicode__(self):
		return u'%s %s' % self.first_name,self.last_name

class Book(models.Model):
	title=models.CharField(max_length=100)
	authors=models.ManyToManyField(Author)#Book数据库表没有authors字段，而是通过额外的多对多连接表来处理书籍和作者的映射关系
	publisher=models.ForeignKey(Publisher)
	publication_date=models.DateField()	

	def __unicode__(self):
		return self.title