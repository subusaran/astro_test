import json

product_dict={'B01':7.95,
              'G01':24.95,
              'R01':32.95}

delivery_cost ={'<=50' : '4.95',
                '<=90' :'2.95',
                '>90' : 'Free'}



cart_list =[]

def validate_product_code(prod_dict,prod_code):
    if prod_code in prod_dict.keys():
        return True
    else:
        return False

def add_cart(product_id):
    if validate_product_code(product_dict,product_id):
        cart_list.append(product_id)
    else:
        print("Invalid Product Code")




def checkout_cart():
    total_amt = 0
    for items in cart_list:
        total_amt = total_amt + product_dict.get(items)
    r01_cnt = cart_list.count('R01')
    if r01_cnt > 1:
        total_amt = total_amt - product_dict.get('R01')/2
    print("Total Cart Value :" + str(total_amt))
    if total_amt <= 50:
        print("Delivery Charge of $" + '4.95' +" applicable on this")
        total_amt = total_amt + 4.95
        return total_amt
    elif total_amt >50 and total_amt <=90:
        print("Delivery Charge of $" + '2.95' + " applicable on this")
        total_amt = total_amt + 2.95
        return total_amt
    else:
        print("Eligibile For Free Delivery")
        return total_amt

def main():
    print("{:<10} {:<10}".format('ProductCode', 'Price'))
    for key,value in product_dict.items():
        print("{:<10} {:<10}".format(key,value))
        #print ("Product Code:" + key + ' Price:' + str(value) )
    prd_code = str(input("Please Enter The Product Code : "))
    add_cart(prd_code)

if __name__ =='__main__':

    check_out=''
    while check_out != 'quit':
        main()
        check_out=str(input("Available Products in the Cart : " + ",".join(cart_list) +  "\nDo You Want To Check Out ? Y/N "))
        check_out = check_out.lower().strip()
        if check_out == 'y' or check_out =='yes':
            check_out = 'quit'
            print("Checkout Amount:" + str(checkout_cart()))
        elif check_out=='n' or check_out=='no':
            pass







