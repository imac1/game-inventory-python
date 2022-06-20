## CSV reader

>>> import csv
>>> f = open('price2.csv', 'r')
>>> rows = csv.reader(f) # read the file using csv
>>> for row in rows:
...     print(row)
...
['date', 'metal', 'radius', 'price', 'quantity']
['Jun 12, 2016', 'Gold', '5.5', '80.99', '1']
['Jul 13, 2015', 'Silver', '40.3', '5.5', '3']
['Jan 21, 2016', 'Iron', '9.2', '14.29', '8']
['Mar 23, 2014', 'Gold', '8', '120.30', '2']
['Sep 11, 2017', 'Copper', '4.1', '70.25', '12']
['Jan 20, 2011', 'Iron', '3.25', '10.99', '3']

## price calculation using csv module


import csv

total_price = 0 # for all items in the list

with open('price2.csv', 'r') as f: 
## open file in read mode
    rows = csv.reader(f)
    header = next(rows) 
## skip line 1 i.e. header
    for row in rows:
        row[3] = float(row[3]) # price
        row[4] = int(row[4]) # quantity

        total_price += row[3] * row[4]

print("Total price = %10.2f" % total_price)

## DictReader

>>> import csv
>>> f = list(csv.DictReader(open('price.csv'))) # read DictReader in list
>>> f[0]  # first item in the list

OrderedDict([('date', '2016-06-12'), ('metal', 'Gold'), ('radius', '5.5'),
    ('price', '80.99'), ('quantity', '1')])

>>> [row['metal'] for row in f] # display all values i.e. List
['Gold', 'Silver', 'Iron', 'Gold', 'Copper', 'Iron']

>>> {row['metal'] for row in f} # display unique values i.e. Set
{'Silver', 'Copper', 'Iron', 'Gold'}

>>> g = [row for row in f if row['metal'] == 'Gold'] # read Gold entries
>>> len(g)  # total gold entries
2

>>> for item in g:  # print radius, price and quantity
...     print(item['radius'], item['price'], item['quantity'])
...
5.5 80.99 1
8 120.3 2