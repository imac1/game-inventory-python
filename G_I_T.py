import csv
file = open('/Users/macbook/Documents/CodeCool/game-inventory-python-imac1/test_inventory.csv')

# type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)

arr = ['do', 'do', 'lo', 'mo', 'mo']
# print(*arr, sep=': ', end='\n')
# [print(x) for x in arr]
counts = dict()
for i in arr:
    counts[i] = counts.get(i, 0) + 1
print(counts)
inventory = {'rope': 1, 'torch': 2}

added_items = ['rope']

# i = 0 
# while i < len(arr):
#     print(arr[i] + ': ')
#     i = i + 1

# rows = []
# for row in csvreader:
#     rows.append(row)

# print(rows)
# file.close()