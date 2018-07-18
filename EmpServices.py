from EmpBean import EmpBean
list=[]
#def __len__():
#	return len(list)=
class EmpServices:
	def searchById(self,id):
		for i in range(0,len(list)):
			#objbean=EmpBean(0,"",0)
			objbean = list[i]
			if id == objbean.getEmpID():
				return objbean
		return 	None
		
	def addEmployee(self,objbean):
		id=objbean.getEmpID()
		if (EmpServices.searchById(self,id) == None):
			list.append(objbean)
			return True
		return False
		
	def getAllEmployees(self):
		return list
		
	def deleteByID(self,id):
		objbean = EmpServices.searchById(self,id)
		if objbean != None:
			list.remove(objbean)
			return True
		else:
			return False
			
	def updateEmployee(self,newobjbean):
		for i in range(0,len(list)):
			objbean = list[i]
			if  objbean.getEmpID() == newobjbean.getEmpID():
				list[i] = newobjbean
				
	def searchByName(self,name):
		name_list=[]
		flag=0
		for i in range(0,len(list)):
			objbean = list[i]
			if name == objbean.getEmpName():
				name_list.append(objbean)
				flag=1
		if flag==1:		
			return name_list
		else:
			return None		
		
		