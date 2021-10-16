# How It Works

I have initialized the products catalogue as a dictonary which can be replaced with a NoSQL database like MongoDB or DynamoDB 

This doesn't have an interactive UI , rather it can be used as a python utility 
Python file : acme_widget.py
On running the code , it would display the list of products and it's price and ask to enter the code to add to the cart

ProductCode Price     
B01        7.95      
G01        24.95     
R01        32.95     
Please Enter The Product Code : 

Once entered it will display the available items in the cart and would let the user to decide if they want to proceed further or checkout
ProductCode Price     
B01        7.95      
G01        24.95     
R01        32.95     
Please Enter The Product Code : B01
Available Products in the Cart : B01
Do You Want To Check Out ? Y/N

Once checked out it would display the cart value and the checkout value with the delivery charges 

ProductCode Price     
B01        7.95      
G01        24.95     
R01        32.95     
Please Enter The Product Code : B01
Available Products in the Cart : B01
Do You Want To Check Out ? Y/N Y
Total Cart Value :7.95
Delivery Charge of $4.95 applicable on this
Checkout Amount:12.9

# Possible Improvements

For the Delivery charges and offers could implement a proper rules engine , currently it is tied to the application logic