# list datastructure
# list are mutable
# list are ordered
# list are indexed
from moses_datatype import student

fruits=['apple','banana', 'strawberries', 'blueberries', 'pineapple', 'pear',]
fruits[0] = "watermelon"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = [67, 5, 24, 5, 44, 8, -25, 2, 5, -8, 5, 5, 22, 6, -88, 5, 4, -2, 6252, 211, 588, 2, 6, 9355, 6444, 4896]
numbers2.sort( reverse=False)
print(fruits)
print(numbers)
print(numbers2)
numbers.append(10)
print(f"I love eating {fruits[2]}")
print(numbers)
# tuple datastructures
# tuple is immutable
# tuple is indexed
# tuple is ordered
cars=['Audi' ,'BMW' , 'Mercedes Benz' , 'Range Rover' , 'Peugeot' , 'Alfa Romeo' ,  ]
print(cars)
nambari= (54, 524, 5874, 696, 12251, 52542, 2, 425254215, 25215, 254125, 2, -5, 51, 55, 84, 1, 2, 4, 7, -947)
numbers3 = (0,2,2,5,3,6,6,3,6,4,7,8,7,5,7)
# nambari.sort(reverse=True)
print(sorted(nambari))
# set datastructure
# print(sorted())
# cars[2]="range"

print(numbers3)
# set are unordered
computers = {'hp' , 'dell' , 'microsoft' , 'samsung' , 'mac' , 'ibm' , 'toshiba'}
computers.add( 'google')
computers.remove('ibm')


print(computers)
num1={1,2,3}
num2={4,5,6}
union_set=num1.union(num2)
print(union_set)
# Dictionaries data structures
student={'Name' : 'John' , 'Age' : 5, 'Gender' : 'Male', 'School':"University of Nairobi"}
print(student['Name'])
print(f"Student name: {student['Name']}")
print(f"Student name: {student['Name']}"
      f" Student Age : {student['Age']}"
      f" Student Gender : {student['Gender']}"
      f" Student is from : {student['School']}")
