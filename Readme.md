# HU-DS2-Project

## Semester Project - Data Structurees 2

### WARE-HOUSE MANAGEMENT SYSTEM USING PAGODA DATASTRUCTURE &nbsp;&nbsp;[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg) &nbsp;![GitHub release](https://img.shields.io/github/release/Jazzel/HU-DS2-Project)](https://github.com/Jazzel/HU-DS2-Project)

This repository includes Python implementation of the Pagoda datastructure and a warehouse management application to exemplify its usage in real systems.

- **Paper:** https://ieeexplore.ieee.org/abstract/document/4567956
- **Java Implementation:** https://www.geeksforgeeks.org/implementing-pagoda-in-java/

#### Environment: &nbsp; [![Python](https://img.shields.io/badge/Python-3.8%20and%20above-blue.svg)](https://pypi.org/project/pip/)

## Description

### Data Structure

The Pagoda data structure is a binary search tree with two priority queues - one for the maximum priority and one for the minimum priority. Each node in the binary search tree contains an item, its priority, and a reference to its left and right children. The highest priority items are located at the root of the maximum priority queue, while the lowest priority items are located at the root of the minimum priority queue.
It allows efficient insertion and deletion of elements with both maximum and minimum priorities, making it useful for managing the priorities of items in a real-world application.

We will exemplify the usage of the Pagoda data structure by building a warehouse inventory system. The Pagoda data structure enables efficient management of the inventory line by ensuring that the most important items are shipped out first, which can help meet customer demands and increase overall customer satisfaction.

## Note:

We have used a diluted down version of Pagoda as the paper implementation was quite hard to modify according to our needs. But both the implementations, paper implementation and diluted one, are available in the code.

- Diluted-down version: [https://github.com/Jazzel/HU-DS2-Project/blob/main/app/server.py](https://github.com/Jazzel/HU-DS2-Project/blob/main/app/server.py) Line number: 15
- Paper implementation: [https://github.com/Jazzel/HU-DS2-Project/blob/main/app/Pagoda.py](https://github.com/Jazzel/HU-DS2-Project/blob/main/app/Pagoda.py)

### Application

Warehouse Inventory Management: As mentioned earlier, Pagoda data structure is a useful data structure for managing priorities of items in a warehouse inventory line. It allows efficient insertion and deletion of elements with both maximum and minimum priorities, ensuring that the most important items are shipped out first.

## Components:

- Web UI ( Frontend )
- Pagoda Implementation ( Backend )

## Frameworks/Libraries used:

- Web is built on Python Web Framework - Flask
- Pagoda is written on core Python

## Complexity Analysis

- **Initialization**: The insertion takes places in O(n logn) time since we first have to insert all the elements in linear time resulting in O(n) time and then heapify the tree to satisfy heap property hence a total of O(nlogn) time
- **Insertion**: Insertion itself takes O(log n) time since our data structure is derived from heap trees.
- **Deletion**: Deletion or extraction of elements is performed in linear time i.e O(1) since the heap is sorted and we only need to extract the element from the top.
- **Merge/Meld**: The merge operation also takes O(logn) time as we compare and recursively merge the sub-heaps hence the time is proportional to the tree height.

## Features:

- **Item Entry:** The interface allows users to enter new items into the inventory line. Each item can be assigned a name and a priority based on its importance or urgency to be shipped out.
- **Item Deletion:** Users can also delete items from the inventory line with the lowest priority. As it is considered expired in our system
- **Priority:** The interface displays the current priority queue of items in the inventory line. Users can see which items have the highest and lowest priorities, and which items are currently at the front of the queue.
- **Shipping:** The number of items (or all) can be shipped to next warehouse. Lowest priorities items will be selected and sent.

## Prerequisite

- python and pip ( version = "\*" )

  Visit [https://www.python.org/](https://www.python.org/) and download any version of python for your operating system.
  Open command prompt/powershell/terminal in default python environment.

  ```
  # For verification open command prompt or terminal and run
  python --version
  Output: Python 3.x.x
  ```

- virtualenv ( version = "\*" )
  ```
  pip install virtualenv
  # Again for verification
  virtualenv --version
  Output: pipenv, version 2020.x.x
  ```

## Available Scripts

- Download Project files

  - Clone using git
    ```
    git clone https://github.com/Jazzel/HU-DS2-Project
    cd HU-DS2-Project/
    ```
    #### Or
  - Download the repository from [https://github.com/Jazzel/HU-DS2-Project](https://github.com/Jazzel/HU-DS2-Project) then move to the directory where you downloaded or cloned the repository and cd into project directory.

    `cd HU-DS2-Project-main/`

- Launching in project's virtual environment

  ```
  virtual env
  ```

- Install dependencies via your powershell/terminal/cmd.

  ```
  pip install -r requirements.txt

  ```

- Testing

  ```
  python test.py
  Output: Test Passed ! All libraries working.

  ```

- Importing variables
- For linux users
  `export FLASK_APP=app/server.py && export FLASK_ENV=development`
- For windows users
  `SET FLASK_APP=app/server.py ; SET FLASK_ENV=development`
- Now for the final step

```

python wsgi.py
Output:

 * Serving Flask app 'app.server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 914-155-506


```

- Open browser and enter address [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and hit enter.

### Magic happens !!

## Application Usage

- Run locally by going through the <b> Available Scripts </b> section.

![index](https://github.com/Jazzel/HU-DS2-Project/blob/main/screenshots/HomePage.png?raw=true)

- Click on View Products button to view the products

![index](https://github.com/Jazzel/HU-DS2-Project/blob/main/screenshots/Products.png?raw=true)

- Here you can add product and delete the product with minimum priority.

![index](https://github.com/Jazzel/HU-DS2-Project/blob/main/screenshots/AddProduct.png?raw=true)

- Now let's move to shipping

![index](https://github.com/Jazzel/HU-DS2-Project/blob/main/screenshots/Shipping.png?raw=true)

- Here in the text box you can enter any number to send products and "all" to send all the products that are currently in the warehouse. The products will be sent according to priority.

Enjoyyy !!

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)&nbsp;![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
]()

```

```
