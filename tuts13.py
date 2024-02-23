#string are immutable
a="Ajay"
print(len(a))
#for making all string capital we used upper() and for small we use lower()
print(a.upper())
print(a.lower())
#rstrip() remove all the trailing character.
a="!!!!Ajay!!!!"
print(a.rstrip("!"))
#replace used to change your string.
print(a.replace("Ajay","Abhay"))
#split() it return the seperate srting and list them
a="!!!! Ajay !!!! Abhay"
print(a.split())
#capitalize character turn only first letter of string in capital rest will turn small
a="Ajay sINGh"
print(a.capitalize())
#center() is used to make your heading in center 
a="Introduction to maths"
print(a.center(50))
print(len(a))
print(len(a.center(50)))
#count() returns the no. of times given value occures in string
print(a.count("t"))
#endswith() return true if a string end with given value
#we can also check whether string in between end with the given value in given len
print(a.endswith("maths"))
print(a.endswith("to",4,15))
#startswith()
print(a.startswith("Intro"))
#find() is use to find is given value is present in the string or not  if present it will return the index of 
#the value if not then return -1
print(a.find("to"))
#index() is just like find but it show error if given value will not present in string
print(a.index("to"))
#isalnum() return true if all string consist only A-Z ,a-z,0-9 .if any special character will present it will
#return false
#isalpha() return true if all string consist only A-Z ,a-z.if any special character will present it will false
a="AjaySingh"
print(a.isalnum())
#space is also count as special character
print(a.isalpha())
#islower return true if all charcter in string is in lower case
#isupper return true if all charcter in string is in upper case
print(a.islower())
print(a.isupper())
#is printable return false when \n or other special char. come
a=("welcom\n")
print(a.isprintable())
#isspace return true if only and only if white space present
a="Ajay Singh"
print(a.isspace())
a=" "
print(a.isspace())
#istitle returns true if every first letter of every word in the string is upper case
a="Ajay Singh"
print(a.istitle())
#swapcase() it change all letter into upper case tolower and vice verse
print(a.swapcase())
#title capitalize each word of the string
a="i am ajay singh"
print(a.title())


