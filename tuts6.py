a = complex(8, 2)
b = True
c = "Harry"
d = None
print(a)
print(b)
a1 = 9
print(a + a1)
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))

#list start with large bracket in which we can use append and insert function
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

#tuple start with small bracket and we cannot add or insert item in it
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

#set also start with {} it remove the repeated term in it
#also we cannnot add another number in set
set1 ={76,98,89,89,76,90}
print(set1)


#dictionary is also start with  {} it is used to store pair data
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
print(dict1["canVote"])
dict1["sex"]="female"
print(dict1)
ajay = {"kuch bhi likh diya"}
print(ajay)