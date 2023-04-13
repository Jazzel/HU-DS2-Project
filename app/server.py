from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import string
import random
import re


# Pagoda


# ? Creating app with Flask
app = Flask(__name__)

# Index route


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.htm')


@app.route('/products', methods=['GET', 'POST'])
def products():
    return render_template('products.htm')


@app.route('/addProduct', methods=['GET', 'POST'])
def addProduct():
    return render_template('addProduct.htm')


@app.route('/editProduct', methods=['GET', 'POST'])
def editProduct():
    return render_template('editProduct.htm')


@app.route('/deleteProduct', methods=['GET', 'POST'])
def deleteProduct():
    return render_template('deleteProduct.htm')
