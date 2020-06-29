# SUPER MARKET EXAMPLE
supermarket = {
	'store1':{
		'name':'General Store',
		'items':[
		{'name' : 'soap', 'quantity' : 20},
		{'name' : 'brush', 'quantity' : 30},
		{'name' : 'paste', 'quantity' : 40}
		]
	},
	'store2':{
		'name':'Book Store',
		'items':[
		{'name' : 'python cook book', 'quantity' : 10},
		{'name' : 'hadoop definitive guide', 'quantity' : 50},
		{'name' : 'programming in scala ', 'quantity' : 70}
		]
	},
}
# PRINT NAME OF STORE 1
supermarket['store1']['name']
supermarket.get('store1').get('name')
supermarket['store1'].get('name')
supermarket.get('store1')['name']

# DISPALAY THE NAMES OF ALL ITEMS IN STORE1
supermarket['store1']['items']
for items in supermarket['store1']['items']: 
    print(items['name'])

# PRINT THE QUANTITY OF PYTHON COOK BOOKS
supermarket['store2']['items']
for books in supermarket['store2']['items']:
    if books['name'] == 'python cook book':
        print(books['quantity'])
