#pylint:disable=W0312
#pylint:disable=W0312
def gettime():
	import datetime
	return  datetime.datetime.now()

character = input("Input clint name :\n")
food = input("input 1 for add food and 2 for excercize :\n")
if food == "1":
	item = input("enter the food name : \n")
elif food== "2":
	item = input("enter the excercize name : \n")
if character == "harry":
	if food == "1":
		f = open("harryfood.txt","a")
		get = item + "			 " +str(gettime()) +"\n"
		f.write(get)
		f.close()
	elif food =="2":
		f = open("harryexcercize.txt","a")
		get = item + "			 " +str(gettime()) +"\n"
		f.write(get)
		f.close()
	else:
		print("plese input a vaild no.")
elif character == "tanveer":
	if food == "1":
		f = open("tanveerfood.txt","a")
		get = item + "			 " +str(gettime()) +"\n"
		f.write(get)
		f.close()
	elif food =="2":
		f = open("tanveerexcercize.txt","a")
		get = item + "			 " +str(gettime()) +"\n"
		f.write(get)
		f.close()
	else:
		print("plese input a vaild no.")
elif character == "rohan":
	if food == "1":
		f = open("rohanfood.txt","a")
		get = item + "			 " +str(gettime()) +"\n"
		f.write(get)
		f.close()
	elif food =="2":
		f = open("rohanexcercize.txt","a")
		get = item + "			 " +str(gettime()) +"\n"
		f.write(get)
		f.close()
	else:
		print("plese input a vaild no.")
else:
	print("error")	
		
		
