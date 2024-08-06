
gadgets=[
    ("Explosive Batarangs",3,True),
    ("Batarangs",5,True),
    ("Smoke Pellets",0,False),
    ("Tear Gas Grenades",2,True),
    ("Night Vision Goggles",1,True),
    ("Batclaw",0,False),
    ("Grapple Gun",3,True),
    ("Batsignal",0,False),
    ("Utility Belt",1,True),
    ("Batmobile Tires",4,True)
]


#product_name,quantity,in_stock=gadgets
sorted_array=sorted(gadgets,key=lambda x:(x[1],x[0]),reverse=True)
print(sorted_array)

#gadgets.sort(key=lambda x: (x[1],x[0]), reverse=True)
#print(gadgets)