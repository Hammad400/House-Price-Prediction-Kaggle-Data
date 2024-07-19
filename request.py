import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Rates the overall material and finish of the house':10, 
	'GrLivArea: Above grade (ground) living area square feet':200,
	'Size of garage in car capacity':3,
	'Size of garage in square feet':255,
	'Total square feet of basement area':800,
	'First Floor square feet':600,
	'Full bathrooms above grade':4,
	'Total rooms above grade (does not include bathrooms)':78,
	'price in dollers':1000000})

print(r.json())