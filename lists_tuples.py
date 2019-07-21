courses = ["history" , "math" , "physics" , "CompScie"]
print(courses)
print(len(courses))
print(courses[0])
print(courses[0:2])
print(courses[:2])
print(courses[2:])
courses.append("art")
print(courses)
courses.insert( 0 , "English")
print(courses)
courses_2 = ["Education" , "math" , "arabic"]
courses.extend(courses_2)
print(courses)
courses.remove("math")
print(courses)
popped = courses.pop()
print(popped)
print(courses)
courses.reverse()
print(courses)
sorted_courses = sorted(courses)
print(courses)
for course in courses:
   print(course)
print("---------------------------------------")
for index , course in enumerate(courses , start =1):
   print(index , course)
print("---------------------------------------")   
#tuples are like lists but we can't change them and they are with () not []
tuple_1 =("history" , "math" , "physics" , "compsci")
print(tuple_1)
print("---------------------------------------")   

#sets the same as lists but with {} not []
cs_courses = {"history" , "math" ,"physics" ,"compscie"}
print(cs_courses)
print("math" in cs_courses)
print("---------------------------------------")   

#to find the same variables that are in 2 tuples we use .intersection
#to find the diffrent variables that are in 2 tuples we use .difference
art_courses = {"history" ,"math" , "art" , "design"}
print(cs_courses.intersection(art_courses))
print("---------------------------------------")   
print(cs_courses.difference(art_courses))
print("---------------------------------------")   
 
#if we want to combine the two sets we use .union 
print(cs_courses.union(art_courses))
#creating empty list , tuple and set
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
empty_set = set()
# empty_set = {} that will make an empty dictionary not an empty set
