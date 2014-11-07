from os import listdir
#from os.path import isfile, join
import json
import os
from random import randint

mypath = "../assets/img/products/"

products = [] 

for cat_fldr in listdir(mypath):
	if cat_fldr != ".DS_Store":
		print cat_fldr	
   		for filename in listdir(mypath + cat_fldr):
			if filename != ".DS_Store":
				title = os.path.splitext(filename)[0]				
				print title
				price = randint(35,600)
				print price
				p = {}
				p["title"] = title
				p["category"] = cat_fldr
				p["price"] = price
			        p["path"] = mypath + cat_fldr + "/" + filename	
				products.append(p)

data ={}
data["products"] = products

with open('products.json', 'w') as outfile:
  json.dump(data, outfile)

#onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
