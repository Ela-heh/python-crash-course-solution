#cities
cities = {
'Tabriz' : {
'country' : 'Iran',
'pop' : 1000
} ,
'isfahan' :{
    'country' : 'iran',
    'pop' : 3400
},
'istanbul' : {
    'country' : 'turkey',
    'pop' : 3000
}
}
for city , info in cities.items():
    print (f"city name: {city.title()}")
    print (f"and it's located in {info['country'].title()} \n with {info['pop'].title()}people")