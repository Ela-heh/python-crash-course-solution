favorite_place = { 
    'eli' : ['japan' , 'US'],
    'ahmad' : ['iran' , 'afghanistan' , 'iraq'] ,
    'christ' : ['egypt' , 'srilanka' , 'india']
}
for name,language in favorite_place.items() :
    print (f"what's your fav place to visit {name} ?")
    for answer in language :
        print (f"{answer}\t")
