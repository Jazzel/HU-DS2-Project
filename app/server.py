from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import string
import random
import re

from datetime import date, datetime

import time



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

    def find_min(self):
        if not self.towers:
            raise ValueError('Pagoda is empty')
        elif not self.towers[0]:
            del self.towers[0]
            return self.find_min()
        else:
            return self.towers[0][0]

        
    def merge(self, a, b):
        result = []
        while a and b:
            if a[0]['expiry'] < b[0]['expiry']:
                result.append(a.pop(0))
            elif a[0]['expiry'] > b[0]['expiry']:
                result.append(b.pop(0))
            else:
                if a[0]['item'] < b[0]['item']:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))
        result.extend(a)
        result.extend(b)
        return result

# ? Creating app with Flask
app = Flask(__name__)

# Index route

warehouseIndex = Pagoda()
warehouseIndex2 = Pagoda()

warehouseIndex.insert({'item': 'A', 'expiry': date(2023, 4, 27), 'city': None})
warehouseIndex.insert({'item': 'B', 'expiry': date(2023, 4, 25), 'city': None})
warehouseIndex.insert({'item': 'C', 'expiry': date(2023, 4, 28), 'city': None})

warehouse = dict()

warehouse["A"] = {'name': 'A', 'description': 'A', 'price': 'A', 'quantity': 'A', 'expiry': date(2023, 4, 27)}
warehouse["B"] = {'name': 'B', 'description': 'B', 'price': 'B', 'quantity': 'B', 'expiry': date(2023, 4, 25)}
warehouse["C"] = {'name': 'C', 'description': 'C', 'price': 'C', 'quantity': 'C', 'expiry': date(2023, 4, 28)}

warehouse2 = dict()


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

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.htm')


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


    print(sent, received)
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


@app.route('/editProduct', methods=['GET', 'POST'])
def editProduct():
    return render_template('editProduct.htm')


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
