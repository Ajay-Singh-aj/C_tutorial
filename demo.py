#print("hello ajay",7)
#print(5)
#print(17*13)
import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.parse("+917856065541")
print("\n phone no. location\n")
print(geocoder.description_for_number(phone_number1,"en"));