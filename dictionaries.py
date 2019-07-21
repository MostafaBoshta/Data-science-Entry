#dictionaries are same as arrays but with different data types 

student = {"name" : "john" , "age" : 19 , "courses" : ["English" , "Math"] }
print(student)
print("----------------------------")
print(student["name"])
print("----------------------------")
print(student["age"])
print("----------------------------")
print(student["courses"])
print("----------------------------")
#if we want to search of a key not in the dictionary without error we can use .get
print(student.get("phone"))
print("----------------------------")
#to add key to the dictionary 
student["phone"] = "555-5555"
print(student)
print("----------------------------")
#if we want to update more than one key word in the dictionary 
student.update({"name" : "mostafa" , "age" : 15 })
print(student)
print("----------------------------")

#if we want to remove a key
phone =student.pop("phone")
print(phone)
print("----------------------------")

#to know the length of the dictionary
print(len(student))
print("----------------------------")

#to know the key words of the dictionary
print(student.keys())
print("----------------------------")

#to know the values of the dictionary
print(student.values())
print("----------------------------")


#to print the values and the keys togeather
print(student.items())
print("----------------------------")
#using loops 
for key , value in student.items() :
    print(key , value)