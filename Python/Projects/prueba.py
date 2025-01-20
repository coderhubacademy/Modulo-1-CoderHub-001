import json

parsed_products = json.load(open('products.json', 'r'))
products_txt = open('products.txt', 'w')
    
for product in parsed_products:
    print(product['name'], product['price'])
    products_txt.write(f"{product['name']} - {product['price']} - {product['quantity']}\n")

products_txt.close()

products_txt = open('products.txt', 'r')

products = products_txt.readlines()

for product in products:
    pp = product.split(' - ')
    product = {
        'name': pp[0],
        'price': pp[1],
        'quantity': pp[2],
        'convertido': True
    }
    print(product)
    