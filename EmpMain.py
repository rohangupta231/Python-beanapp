from EmpBean import EmpBean 
from EmpServices import EmpServices
while(True):
	print("=========================")
	print("Select a Option")
	print("1. Add Record")
	print("2. List All")
	print("3. Search By ID")
	print("4. Update By ID")
	print("5. Delete By ID")
	print("6. Search By Name")
	print("7. Update By Name")
	print("8. Exit");
	print("=========================")
	choice=int(input("Enter Your Choice(1-8)="))
	if choice==1:
		id=int(input("Enter ID"))
		name=input("Enter Name")
		salary=float(input("Enter Salary"))
		objbean=EmpBean(0," ",0)
		objbean.setEmpID(id)
		objbean.setEmpName(name)
		objbean.setEmpSalary(salary)
		#print(objbean.getEmpID())
		empser= EmpServices()
		if (empser.addEmployee(objbean)):
			print("Record Inserted Successfully\n")
		else :
			print("Result Not Inserted\n")
	elif choice==2:
		#print("2nd")
		empser=EmpServices()
		list=empser.getAllEmployees()
		if len(list)==0:
			print("||NO RECORD FOUND\n")
		else :
			for i in range(len(list)):
				objbean=list[i]
				print("||ID= ",objbean.getEmpID())
				print("||Name= ",objbean.getEmpName())
				print("||Salary= ",objbean.getEmpSalary())
				print("==========================")
	elif choice==3:
		#print("3rd")
		id=int(input("Enter ID= "))
		empser=EmpServices()
		objbean=empser.searchById(id)
		if objbean==None:
			print("NO SUCH ID!!!!!!\n")
		else:
			print("||ID= ",objbean.getEmpID())
			print("||Name= ",objbean.getEmpName())
			print("||Salary= ",objbean.getEmpSalary())
			print("==========================")
	elif choice==4:
		#print("4th")
		id=int(input("Enter ID= "))
		empser=EmpServices()
		objbean= empser.searchById(id)
		if objbean==None:
			print("No such record exist\n")
		else:
			print("||ID= ",objbean.getEmpID())
			print("||Name= ",objbean.getEmpName())
			print("||Salary= ",objbean.getEmpSalary())
			print("==========================")
			newobjbean= EmpBean(0," ",0)
			newobjbean.setEmpID(objbean.getEmpID())
			newobjbean.setEmpName(input("Enter Updated Name="))
			newobjbean.setEmpSalary(float(input("Enter Updated Salary=")))
			empser.updateEmployee(newobjbean)
			print("Record updated!!!!!!!!!!!")
	elif choice==5:
		#print("5th")
		id=int(input("Enter the ID of Record to be deleted= "))
		empser=EmpServices()
		if empser.deleteByID(id):
			print("Record Deleted\n")
		else:	
			print("NO SUCH RECORD")
	elif choice==6:
		name=input("Enter the Name")
		empser=EmpServices()
		name_list=empser.searchByName(name)
		if name_list==None:
			print("No Such Record")
		else:
			for i in range(0,len(name_list)):
				print("id =",name_list[i].getEmpID())
				print("name =",name_list[i].getEmpName())
				print("salary =",name_list[i].getEmpSalary())
				print("==================================")
	elif choice==7:
		name=input("Enter the Name")
		empser=EmpServices()
		name_list=empser.searchByName(name)
		if name_list==None:
			print("No Such Record")
		else:	
			if(len(name_list)==1):
				print("id =",name_list[0].getEmpID())
				print("name =",name_list[0].getEmpName())
				print("salary =",name_list[0].getEmpSalary())
				print("==================================\n")
				newobjbean= EmpBean(0," ",0)
				newobjbean.setEmpID(name_list[0].getEmpID())
				newobjbean.setEmpName(input("Enter Updated Name="))
				newobjbean.setEmpSalary(float(input("Enter Updated Salary=")))
				empser.updateEmployee(newobjbean)
				print("Record updated!!!!!!!!!!!")
			else:
				for i in range(0,len(name_list)):
					print("id =",name_list[i].getEmpID())
					print("name =",name_list[i].getEmpName())
					print("salary =",name_list[i].getEmpSalary())
					print("==================================\n")
				id=int(input("MULTIPLE RECORDS ENTER ID!!="))
				newobjbean= EmpBean(0," ",0)
				newobjbean.setEmpID(id)
				newobjbean.setEmpName(input("Enter Updated Name="))
				newobjbean.setEmpSalary(float(input("Enter Updated Salary=")))
				empser.updateEmployee(newobjbean)
				print("Record updated!!!!!!!!!!!")	
	elif choice==8:
		print("==============\nTHANK YOU\n===============")
		exit()