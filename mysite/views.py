#coding:utf-8
#从 django.http 模块导入（import） HttpResponse 类

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
import datetime


#定义视图函数，每个视图函数至少有一个参数，通常为request，
#这是一个触发这个视图、包含当前Web请求信息的对象，是类django.http.HttpRequest的一个实例
#
#为了使一个Python的函数成为一个Django可识别的视图，它必须满足这两个条件：
#1）这个函数第一个参数的类型是HttpRequest；
#2）它返回一个HttpResponse实例
#
def hello(request):
	###函数的第一个语句可以是​​一个可选的声明 - 该函数或文档字符串的文档字符串
	return HttpResponse("Hello")

def home(request):
	return HttpResponse("home")

def current_datetime(request):
	current_time=datetime.datetime.now()
	current_region='Shanghai'
	# 字符串中的%s是占位符，字符串后面的百分号表示用它后面的变量now的值来代替%s,
	# 变量%s是一个datetime.datetime对象。它虽然不是一个字符串，但是%s（格式化字符串）会把它转换成字符串
	# 1. html="<html><head></head><body>It is now %s.</body></html>" % now
	# 1. return HttpResponse(html)
	# 2. t=get_template('time.html')
	# 2. html=t.render(Context({'current_time':now}))
	# 2. return HttpResponse(html)
	# 3. return render_to_response('time.html',{'current_time':now})
	#return render_to_response('time.html',locals())#locals返回的字典对所有局部变量的名称与值进行映射,局部变量名应与模板中的名称保持一致
	return render_to_response('current_datetime.html',locals())
def hours_ahead(request,offset):
	try:
		offset=int(offset);
	except ValueError:
		raise Http404()
	dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
	# 在你视图的任何位置，临时插入一个 assert False 来触发出错页。 然后就可以看到局部变量和程序语句了
	#assert False
	html="<html><head></head><body>In %s hours, it will be %s.</body></html>" % (offset,dt)
	return HttpResponse(html)