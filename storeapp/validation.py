import re


class Validator():

    @classmethod
    def validate_store_user_credentials(cls, attendant_name, contact, password, role):

        '''method to validate the data of the store user input'''
        if attendant_name == '':
            return "Username is missing"
        elif not re.search(r"^([a-zA-Z]{5,}\s)?[a-zA-Z]{5,}$", attendant_name):
            return "Username should be one or two words of 5 or more characters each"
        elif contact == '':
            return "Contact is missing"
        elif not re.search(r"^\+256[-]\d{3}[-]\d{6}$", contact):
            return "Contact should be in this format '+256-755-598090'"
        elif password == '':
            return "Password is missing"
        elif not re.search(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{7}$", password):
            return "Password must have 7 characters with atleast a lowercase, uppercase letter and a number"
        elif role == '':
            return "Role is missing"
        elif not re.search(r"^[a-zA-Z]{5,9}$", role):
            return "Role must be either admin or attendant"
        else:
            return True
        

    @classmethod
    def validate_product_inputs(cls, product_name, unit_price, quantity, category):

        '''method to validate the data of the product from the store owner input'''
        if product_name == '':
            return "Product name is missing"
        elif not re.search(r"^([a-zA-Z]{5,}\s)?[a-zA-Z]{5,}$", product_name):
            return "Product name should be one or two words of 5 or more characters each"
        elif unit_price == '':
            return "Unit_price is missing"
        elif int(unit_price) < 1:
            return "Unit_price should be more than 0"
        elif not re.search(r"^[0-9]{3,}$", unit_price):
            return "Unit_price should have no spaces, be 3 or more integers and be in numbers"
        elif quantity == '':
            return "Quantity is missing"
        elif int(quantity) < 1:
            return "Quantity should be more than 0"
        elif not re.search(r"^[0-9]+$", quantity):
            return "Quantity should have no spaces and be in numbers"
        elif category == '':
            return "Category is missing"
        elif not re.search(r"^[a-zA-Z]{5,}$", category):
            return "Category should be 5 or more characters and be in characters"
        else:
            return True


    @classmethod
    def validate_input_type(cls, input):
        try:
            _input = int(input)
        except ValueError:
            return "Input should be an integer"


    @classmethod
    def validate_sale_record_inputs(cls, product_name, quantity, pay_amount, attendant):

        ''' method to validate the data of the product from the store owner input '''
        if product_name == '':
            return "Product name is missing"
        elif not re.search(r"^([a-zA-Z]{5,}\s)?[a-zA-Z]{5,}$", product_name):
            return "Product should be either one word with more than 5 characters or two words and in characters"
        elif quantity == '':
            return "Quantity is missing"
        elif int(quantity) < 1:
            return "Quantity should be more than 0"
        elif not re.search(r"^[0-9]+$", quantity):
            return "Quantity should have no spaces and be in numbers"
        elif pay_amount == '':
            return "The amount paid is missing"
        elif int(pay_amount) < 1:
            return "The amount paid should be more than 0"
        elif not re.search(r"^[0-9]{3,}$", pay_amount):
            return "The amount paid should have no spaces and be in numbers"
        elif attendant == '':
            return "Attendant name is missing"
        elif not re.search(r"^[a-zA-Z]{3,}$", attendant):
            return "Attendant name should be more than 3 characters and be in characters"
        else:
            return True
