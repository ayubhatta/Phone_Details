import phonenumbers
from phonenumbers import timezone, geocoder, carrier 


number = input("Enter your number with +__:")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, 'en')

print(phone)
print(time)
print(car)
print(reg)



 # This is another way to do the same thing
''' 
**********************************************************************
# number = input("Enter the phone number with country code: ")
# ch_number = phonenumbers.parse(number, "CH")
# print("Country Name: ", geocoder.description_for_number(ch_number, "en"))

# service_number = phonenumbers.parse(number, "RO")
# print("Service Provider: ", carrier.name_for_number(service_number, "en"))

# gb_number = phonenumbers.parse(number, "GB")
# print("Timezone: ", timezone.time_zones_for_number(gb_number))

# Path: 2.%20Phone_Details/2.%20phone.py
***********************************************************************
'''

