#coding:utf-8
class Employee: #Employee.__name__
	'Common base class for all employees' #可选文档说明字符串,Employee.__doc__
	empCount=0  #类变量，类的所有实例共享的变量

	def __init__(self,name,salary):
		#类构造函数
		self.name=name;
		self.salary=salary
		Employee.empCount+=1
		print "this is base class"

	@classmethod
	def getCount(self):
		print "Total Employee %d" % self.empCount

	def getEmployee(self):
		print "Name : ",self.name, ", Salary: ",self.salary

	@staticmethod
	def add(a): #当一个函数逻辑上属于一个类又不依赖与类的属性的时候，可以使用 staticmethod
		Employee.empCount+=a

emp=Employee("Tom",3000)
emp.getEmployee()
Employee.add(3)
emp.age=25 #在任何时候可以添加，删除或修改类和对象的属性
print "Age: ",getattr(emp,'age')
print Employee.getCount() #@classmethod
print id(emp),id(Employee)

class Manager(Employee): #括号中代表所继承的父类
	def __init__(self):
		print "this is child class"

	def initNewProgram(self):
		print "do something"

mgr=Manager()
mgr.getCount()
#每个Python类会继续并带有内置属性.__dict__,__doc__,__name__,__module__,__bases__

