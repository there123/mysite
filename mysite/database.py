#coding:utf-8
from django.shortcuts import render_to_response
import MySQLdb

#def book_list(request):
#	#创建数据库连接、创建数据库游标、执行某个语句、然后关闭数据库 
#	db=MySQLdb.connect(user='me',db='mydb',passwd='passw0rd',host='localhost')
#	cursor=db.cursor()
#	cursor.excute('SELECT name FROM books ORDER BY name')
#	names=[row[0] for row in cursor.fetchall()]
#	db.close()
#	return render_to_response('book_list.html',{'names':names})

from mysite.books.models import books

def book_list(request):
 	books=Book.objects.order_by('name')
 	return render_to_response('book_list.html',{'books':books})