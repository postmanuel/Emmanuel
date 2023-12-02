import phonenumbers
from phonenumbers import geocoder

from phonenumbers import carrier

number = "+233271263294"
check_number = phonenumbers.parse(number)
location = geocoder.description_for_number(check_number,"en")
print(location)
service_provider = phonenumbers.parse(number)
