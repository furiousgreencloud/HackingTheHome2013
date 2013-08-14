import urllib2
import json


def dump(thing) :
	print(type(thing))
	print(thing)

def kelvin2celius(k) :
	return k - 273.15

print("Fetching Weather...");
response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Vancouver&mode=json')
decoded = json.load(response)
#print(json.dumps(decoded, sort_keys=True, indent=2))
print(decoded["name"] + " Weather: " + decoded["weather"][0]["description"])
maxTemp = kelvin2celius(decoded["main"]["temp_max"])
minTemp = kelvin2celius(decoded["main"]["temp_min"])
print("Max Temp: " + str(maxTemp) + u"\u00B0C")
print("Min Temp: " + str(minTemp) + u"\u00B0C")
