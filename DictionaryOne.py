__author__ = 'ravichawla'
__author__ = 'ravichawla'

stuff={"name":"rock","age":34,"city":"Texas","MaritalStatus":"Married"}

name=stuff["name"]
print(name)
del stuff["MaritalStatus"]
stuff[1] = "rating"
stuff[1] = "kids"
del stuff[1]
print(stuff)

states={
    'Florida':'FL',
    'California':'CA',
    'Texas':'TX',
    'Newyork':'NY',
    'Oregon':'OR'
}

cities={
    'FL':'Miami',
    'TX':'Dallas'
}

cities['NY']='Boston'
cities['OR']='Portland'
cities['CA']='SanFrancisco'
print ('-') * 50

# Some cities
print("Newyork States has ") +cities['NY']
print("Oregon has state ") + cities['OR']

print('*')*50
# Some states

print("Texas's abbreviation is ")+ states['Texas']
print("Newyork's abbreivations is ") + states["Newyork"]

print("=")*50

# every the abbreivations from states
print(states)
for state,abbr in states.items():
     print("%s state has abbreiveation %s ") %(state,abbr)

print(states)
# print every city in state

print("+")*50


for abbr,city in cities.items():
    print("%s has the city %s") %(abbr,city)

# map the values
# now do both at the same time


print '^' * 50
print(states)
#
# for dstate,abbr in states.items():
#     print state,abbr,
print(cities)

for state,abbr in states.items():
    print ("%s abbreivated as %s has city %s") %(state,abbr,cities[abbr])



state=states.get("California")

if not state:
    print ("%s not present")

city=cities.get("TX","does not exist")

