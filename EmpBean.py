class EmpBean:
	def __init__(self,id,name,salary):
		self.id=id
		self.name=name
		self.salary=salary
	def setEmpID(self,id):
		self.id=id	
	def setEmpName(self,name):
		self.name=name
	def setEmpSalary(self,salary):
		self.salary=salary
	def getEmpID(self):
		return self.id
	def getEmpName(self):
		return self.name
	def getEmpSalary(self):
		return self.salary