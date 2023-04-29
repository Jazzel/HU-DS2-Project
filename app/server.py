# imports
from flask import Flask, render_template, request, redirect, url_for
import string
import random
from datetime import date


# Pagoda
class Pagoda:
    def __init__(self):
        self.towers = []

    def insert(self, x):
        # Check if x is already in the towers
        if any(x['expiry'] == person['expiry'] and x['item'] == person['item'] for tower in self.towers for person in tower):
            return x

        # Append element x to the leftmost empty tower
        i = 0
        while i < len(self.towers) and self.towers[i]:
            i += 1
        if i == len(self.towers):
            self.towers.append([x])
        else:
            self.towers[i].append(x)

        # Merge any two towers of equal size
        for j in range(i - 1, -1, -1):
            if len(self.towers[j]) == len(self.towers[j + 1]):
                self.towers[j] = self.merge(self.towers[j], self.towers[j + 1])
                self.towers[j + 1] = []

        # Propagate the smaller of x and the root of the rightmost nonempty tower
        for j in range(len(self.towers) - 1, -1, -1):
            if self.towers[j] and isinstance(self.towers[j][0], dict) and x['expiry'] < self.towers[j][0]['expiry']:
                x, self.towers[j][0] = self.towers[j][0], x
                if j == 0:
                    break
                if len(self.towers[j - 1]) < len(self.towers[j]):
                    self.towers[j - 1] = self.merge(self.towers[j - 1], self.towers[j])
                    self.towers[j] = []
        return x

   # Find the minimum value in the pagoda
    def find_min(self):
        # Check if the pagoda is empty
        if not self.towers:
            raise ValueError('Pagoda is empty')
        # Check if the first tower is empty
        elif not self.towers[0]:
            # Remove the empty tower from the pagoda and recursively find the minimum in the remaining towers
            del self.towers[0]
            return self.find_min()
        else:
            # Return the minimum value, which is the first element of the first tower
            return self.towers[0][0]

    # Merge two lists of items based on their 'expiry' and 'item' properties
    def merge(self, a, b):
        result = []  # Create an empty list to store the merged result

        while a and b:  # Continue while both lists have elements
            # Compare the expiry of the first elements in both lists
            if a[0]['expiry'] < b[0]['expiry']:
                # Append the element from list 'a' to the result and remove it from 'a'
                result.append(a.pop(0))
            elif a[0]['expiry'] > b[0]['expiry']:
                # Append the element from list 'b' to the result and remove it from 'b'
                result.append(b.pop(0))
            else:
                # If the expiry values are equal, compare the 'item' property
                if a[0]['item'] < b[0]['item']:
                    # Append the element from list 'a' to the result and remove it from 'a'
                    result.append(a.pop(0))
                else:
                    # Append the element from list 'b' to the result and remove it from 'b'
                    result.append(b.pop(0))

        # Append the remaining elements from either list 'a' or 'b' to the result
        result.extend(a)
        result.extend(b)

        # Return the merged result
        return result


# Creating app with Flask
app = Flask(__name__)

# Create an instance of the Pagoda class called warehouseIndex
warehouseIndex = Pagoda()

# Create another instance of the Pagoda class called warehouseIndex2
warehouseIndex2 = Pagoda()

# Insert items into warehouseIndex
warehouseIndex.insert({'item': 'A', 'expiry': date(2023, 4, 27), 'city': None})
warehouseIndex.insert({'item': 'B', 'expiry': date(2023, 4, 25), 'city': None})
warehouseIndex.insert({'item': 'C', 'expiry': date(2023, 4, 28), 'city': None})

# Create an empty dictionary called warehouse
warehouse = dict()

# Add items to the warehouse dictionary with item names as keys and item details as values
warehouse["A"] = {'name': 'A', 'description': 'A', 'price': 'A', 'quantity': 'A', 'expiry': date(2023, 4, 27)}
warehouse["B"] = {'name': 'B', 'description': 'B', 'price': 'B', 'quantity': 'B', 'expiry': date(2023, 4, 25)}
warehouse["C"] = {'name': 'C', 'description': 'C', 'price': 'C', 'quantity': 'C', 'expiry': date(2023, 4, 28)}

# Create an empty dictionary called warehouse2
warehouse2 = dict()


# helper function to convert pagoda to list
def getProducts(warehouseIndex):
    data = []
    while True:
        try:
            min_person = warehouseIndex.find_min()
        except ValueError:
            break
        data.append(min_person)
        warehouseIndex.towers[0].pop(0)
        if not warehouseIndex.towers[0]:
            del warehouseIndex.towers[0]
    return data

# index route
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.htm')

# route to add products
@app.route('/products', methods=['GET'])
def products():
    data = getProducts(warehouseIndex)
    for item in data:
        print(item)
        warehouseIndex.insert(item)
    if len(data) > 0:
        print(data)
        return render_template('products.htm', data=(data), warehouse=warehouse, firstIndex=data[0] or None)
    return render_template('products.htm')

# route to send products  
@app.route('/send-products/<path:sent>/<path:received>', methods=['GET', "POST"])
def sendProducts(sent, received):
    sent = int(sent)
    received = int(received)
    if request.method == "POST":
        if request.form['product'] == 'all':
            noOfProducts = len(warehouseIndex.towers[0])
        else:
            noOfProducts = int(request.form['product'])
        for i in range(1, noOfProducts+1):
            min_person = warehouseIndex.find_min()
            warehouseIndex.towers[0].pop(0)
            if not warehouseIndex.towers[0]:
                del warehouseIndex.towers[0]
            warehouseIndex2.insert(min_person)
            return redirect(url_for('sendProducts', sent=noOfProducts - i, received=i))

    if (sent != 0):
        min_person = warehouseIndex.find_min()
        warehouseIndex.towers[0].pop(0)
        if not warehouseIndex.towers[0]:
            del warehouseIndex.towers[0]
        warehouseIndex2.insert(min_person)
        sent -= 1
        received += 1
        return redirect(url_for('sendProducts', sent=sent, received=received))

    data = getProducts(warehouseIndex)
    data2 = getProducts(warehouseIndex2)
    for item in data:
        warehouseIndex.insert(item)
    for item in data2:
        warehouseIndex2.insert(item)
    return render_template('sendProducts.htm', data=(data), data2=data2,  warehouse=warehouse)

# route to add products
@app.route('/addProduct', methods=['GET', 'POST'])
def addProduct():
    if request.method == 'POST':
        print("Wow")
        item = request.form['item']
        name = request.form['title']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']
        expiry = request.form['expiry']

        data = {'item': item, 'expiry': date(int(expiry[0:4]), int(expiry[5:7]), int(expiry[8:10])), 'city': None}
        warehouse[item] = {'name': name, 'description': description, 'price': price, 'quantity': quantity, 'expiry': expiry}
        warehouseIndex.insert(data)

        return redirect(url_for('products'))
    
    if request.method == 'GET':
        # generte random id
        itemID = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return render_template('addProduct.htm', itemID=itemID)

    return render_template('addProduct.htm')

# route to delete product with min index
@app.route('/deleteProduct/<path:id>', methods=['GET', 'POST'])
def deleteProduct(id):
    print("working")
    if request.method == "GET":
        print(id)
        if (id in warehouse):
            del warehouse[id]
            warehouseIndex.towers[0].pop(0)
            if not warehouseIndex.towers[0]:
                del warehouseIndex.towers[0]
    return redirect(url_for('products'))
