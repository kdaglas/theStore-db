# theStore

[![Build Status](https://travis-ci.org/kdaglas/theStore-db.svg?branch=theStore)](https://travis-ci.org/kdaglas/theStore-db)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2b3deb95ad264145bcec8074434f1c57)](https://www.codacy.com/app/kdaglas/theStore-db?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kdaglas/theStore-db&amp;utm_campaign=Badge_Grade)

Store manager is a web application that helps store owners manage sales and product inventory records. This app is hosted at:
- [www.theStore.com](https://kdaglas.github.io/theStore/UI/index.html)

## theStore-api

The api allows the user(store attendant or store owner) to post and get data from the app through API end points that are creating a connection of the client with the database(datastructures). API is being hosted by heroku at: 
- [www.theStore-api.com](https://douglas-thestore.herokuapp.com)

## theStore-db

This application interacts with a PostgreSQL database to save user data and is meant for use in a single store. It should help store owners avoid selling products that have run out of stock. the database version is being hosted by heroku at: 
- [www.theStore-db.com](https://douglas-thestore-db.herokuapp.com/)

### Prerequisites

- Use a web browser preferrably Chrome.
- You need to have Python3 installed on your computer. To install it go to [www.python.org](https://www.python.org/). Note: Python needs to be installed globally (not in the virtual environment)

### Features

- User(store owner and store attendant) can signin/signout from the application
- User(store ownner) can Modify a product
- User(store owner) can Delete a product
- User(store owner) can create a store attendant user account
- User(store owner) can add a product
- User(store owner and store attendant) can view all added products
- User(store owner and store attendant) can view a specific added product
- User(store attendant) can create a sale record
- User(store owner) can view all created sale records
- User(store owner and store attendant) can view a single sale record

Additional features:

- Store owner can give admin right to a specific store attendant.
- Store admin should be able to create, modify and delete categories.
- Store admin should be able to add products to specific categories.

### Getting Started

Clone the project to your computer either by downloading the zip or using git. If you are downloading it then choose theStore-api branch and download that. To use git, run the code below:
```
    git clone https://github.com/kdaglas/theStore-db.git
```
If you have cloned the project, then change the branch by checking out to theStore-db branch. use this code:
```
    git checkout theStore-db
```
Go into the folder, create a virtual environment, activate it and then use a pip command to install the requirements necessary for the app to function. Below are the steps to take:
```
    $ cd theStore-db
    $ virtualenv envn <or any name of your choice>

    <!-- for ubuntu use this command-->
    $ source envn/bin/activate

    <!-- for windows use this command-->
    $ envn\Scripts\activate

    $ pip install -r requirements.txt
```
When this is done then run the application by typing this command
```
    $ python run.py
```
You can use Postman to checkout the functionality of the api endpoints that are interacting with that database, you can download here:
- [www.getpostman.com/apps](https://www.getpostman.com/apps) - Postman: An API testing tool for developers


### Tests

To run tests, make sure that pytest or nose is installed. you can run that command to install them
```
    $ pip install -r requirements.txt
```
Then run these commands to begin testing the API
```
    $ nosetests

    <!-- or -->
    $ pytest
```

### Endpoints covered.

 HTTP Method | End point | Action | Access
-------|-------|-------|-------
 POST | /api/v2/auth/signup | Register a user | only the store owner/admin 
 POST | /api/v2/auth/login | Login a user | 
 POST | /api/v2/products | Create a product | only the store owner/admin 
 PUT | /api/v2/products/<productId> | Modify a product | only the store owner/admin 
 DELETE | /apiv2//products/<productId> | Delete an existing product | both 
 GET | /api/v2/products | Fetch all products | both 
 GET | /api/v2/products/<productId> | Fetch a single product record | both 
 POST | /api/v2/sales | Create a sale order | only the store attendant 
 GET | /api/v2/sales | Fetch all sale records | only the store owner/admin 
 GET | /api/v2/sales/<saleId> | Fetch a single sale record | only the store owner/admin and the creator (store attendant) 

### Built With

- HTML5 and CSS3
- [Python](https://www.python.org/)

### Authors

Douglas Kato
