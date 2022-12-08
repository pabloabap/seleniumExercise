'''
    Goals of this exercise:
        - Learn about Selenium library
        - Find web elements using different Selenium methods (css selectors, id, xpath, tag name)
        - Intereact with web elements throught clicking, sending keys and cleaning commands.
        - Extract data from the web
        - Read and write file

    Description:
        You have a dinner with some friends on your house tomorrow. You created a list of products that you need to prepare it
        and now is the moment to buy it online.
        From "purchase_list.csv" file which contains the category, the product and the amount of product to buy add all
        the products to the cart and extract its name, unit price and total price of each product and total price of the
        purchase. Export this details to a file named "purchase_ticket.txt".
        **IMPORTANT**: The product selected must have the cheapest unit price of its section.
        **IMPORTANT**: Use time.sleep function to create a delay between some actions. It would happen that you want to access
        an element before it is charged and the program breaks
'''

# 1.Import the following libraries
from selenium import webdriver                      # Allows to execute automated webdriver
from selenium.webdriver.common.keys import Keys     # Allows to send specific keys of the keyboard (ESC, Enter, SPACE...)
from selenium.webdriver.common.by import By         # Allows to find elements of the HTML code by diferent ways (XPATH, CSS SELECTOR...)
import time                                         # Allows to send delays between one action and the next
import re                                           # Allows to use regular expressions to find patterns
import math                                         # Allows to use math operations
import io                                           # Allows to write file with an specific encoding

'''
Define de URL you will use to start the exercise and the path and file of the shopping list and the web driver.
'''
INICIAL_URL = ''
SHOPPING_LIST_FILE = ''
DRIVER_PATH = ''

class purchase():
    '''
        2. Create "purchase" class which has the following attributes:
            - inicial_url: URL used to start the program, in this case the main page of Mercadona.
                This attribute must be passed as argument one purchase classe is invoked.
            - shopping_list: empty list by default. It will contains the list of elements that must be bought
            - shopping_cart: empty list by default. It will contains all the elements added in the shopping cart.
            - driver: None by default. It will contains the webdriver used to execute the program.
            - posta_code: None by default. It will contain the postal code where the purchase will be delivered using string format.
    '''
    def __init__(self, inicial_url):
        pass
        
    def set_shopping_list(self, purchase_list):
        '''
            3. Create "set_shopping_list" module which has as arguments the attributes of purchase class and "purchase_list".
                This module must open "purchase_list.csv" file and append each line as an item of "self.shopping_list" list.
                    *Tip: each item in the list  must be a list which contains each element of the line as an item) 
                "purchase_list" is a csv document passed as an input to the class to know the section, product
                and units of product you must buy. Some examples of a register of the csv are:
                    Sepia y calamar,Sepia,500 g
                    Verdura,tomate,3 ud            
        '''
        pass
    def browser_inicializer(self):
        '''
            4. Create "browser_inicializer" module which has purchase attributes as argument and define the webdriver to be used 
                in the exercise. This driver must be stored into self.driver attribute of the class to be used in the future.
                A part from that execute the inicial_url on the webdriver.
                *¡IMPORTANT!* To complete this step you must download a browser webdriver. In my case I downloaded Microsoft Edge 
                "Canal Dev" webdriver from this link: https://developer.microsoft.com/es-es/microsoft-edge/tools/webdriver/
        '''
        pass
    def set_postal_code_accept_cookies(self, postal_code):
        '''
            5. Create "set_postal_code_accept_cookies" module which:
                - Find the postal code text box element and write on it
                your posta code and hit enter (send_key).
                - Find the "Accept" button of the cookies pop up and click on it to hide the pop up
                - Sleep of 5 seconds to wait until the next page is loaded.
        '''
        pass
    def add_products(self):
        '''
            6. Create "add_products" module which have purchase attibutes as arguments.
                - Create a loop over self.shopping_list to extrat each item to buy
                - Introduce the name of the item (second element of the sub list) into the search bar and hit enter
                - Into category section (top left) find the category/section asociated to the item
                - Check all the unit prices of the section and add to cart the cheapest one
                - Check if the amount of the product needed is satisfied if not please add more unit of the item until
                the amount is satisfied.(for example if you nedd 3 tomatoes click on add to cart and then add 2 more 
                units of the product).
        _______________________________________________________________________________________________________________________
            *TIPS*
            - As this function would be very long you can split it three parts:
                1. add_products: find an item, its section and apply the following 3 modules to reach the finall result of add
                new element to the cart
                2. add_product_to_the_cart: add the first unit of a product in the char
                3. cheapest_product_of_the_section: compare the price of all the product of the section and identify the cheapest one.
                4. add_more_units: add more unit of an item if is needed.
            - It my happen that when you add the first item to a cart one the web show a pop up asking you about create an
            account. Send an "ESC" key to ignore it and continue with your purchase.
        _______________________________________________________________________________________________________________________
        '''
        pass
    def cheapest_product_of_the_section(self):
        pass
    def add_product_to_the_cart(self, product):
        pass
    def add_more_units(self, product):
                pass
    def cart_ticket(self):
        '''
            7. Create "cart_ticket" module which have attributes of purchase as arguments.
            This module must click on the shopping cart and extract the next info od each product:
                - name of the product
                - quantity of the product to bought
                - unit price of the product
                - total price product (unit price * quantity) 
                    *IMPORTANT*: Some products have its unit proce in grams instead of units
                    you must do the calculations needed to obtain the correct price.
            Once extracted create a dictionary with the info and append it to self.shopping_cart attribute of the purchase object.
            Also at the end you should append another dictionary which have the Total price of the purchase.
            To conclude self.shopping_cart should be a list of dictionarias (one dict per item + total purchase price).            
        '''
        pass
    def shopping_ticket(self):
        '''
            8. Create "shopping_ticket" module which have the attributes of the purchase object.
            This module must write a ".txt" file with the info of self.shopping_cart list (the purchase ticket) 
            *TIP* use the io library to define the encoding utf-8 to write the file and prevent strange characters.
        '''
        pass
if __name__ == "__main__":
    '''
        Delete "#" from the following lines to test the parts of your code
    '''
    # purchase1 = purchase(INICIAL_URL)
    # purchase1.set_shopping_list(SHOPPING_LIST_FILE)
    # purchase1.browser_inicializer()
    # purchase1.set_postal_code_accept_cookies('08014')
    # purchase1.add_products()
    # purchase1.cart_ticket()
