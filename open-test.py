import csv
import os
import locale
from time import sleep


        #lista


def format_currency(value):
    return locale.currency(value,grouping=True)

def truncate(item, length):
    return item[:length]

def list_products(products):
    print(f"| idx |    Model   | Magazine |{" " * 33}  Description  {" " * 33}|")
    for idx, product in enumerate(products, 1):
        print(f"|{idx:^5}| {product['model']:<10} |{truncate(product['magazine'], 9):<9} |{truncate(product['desc'], 80):>80} |")

def add_product(products):

    find_max = max(products, key=lambda id: id['id'] )
    max_id = find_max['id']
    
    new_id = max_id + 1


    model = input("Model: ")
    desc = input("Beskrivning: ")
    magazine = int(input("Magasin:  "))
    pros = input("pros: ")
    cons = input("cons: ")

    product = {}

    product['id'] = new_id
    product['model'] = model
    product['desc'] = desc
    product['magazine'] = magazine
    product['pros'] = pros
    product['cons'] = cons

    products.append(product)

    return products

def save_products(products):

    csv_file_path = "db_products.csv"

# Write the products data to a CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "model", "desc", "magazine", "pros", "cons"])
        writer.writeheader()  # Write the header row
        writer.writerows(products)  # Write the product data

    print(f"Data successfully saved to {csv_file_path}")
    return f"OK"

def change_product(placeholder):

    print("du vill ändra produkt:", placeholder['model'])

    while True:
        try:
            model = input("Model: ")
            desc = input("Beskrivning: ")
            magazine = int(input("Magasin:  "))
            pros = input("pros: ")
            cons = input("cons: ")
            break
        except:
            print("wrong value")

    placeholder['model'] = model
    placeholder['desc'] = desc
    placeholder['magazine'] = magazine
    placeholder['pros'] = pros
    placeholder['cons'] = cons
    return placeholder
    


def view_products(idx, products):
    product = products[idx - 1]
    print(f"product: {product['model']} | {product['desc']} Comes with {product['magazine']} bullets in the magazine")
    return product

def load_data(filename): 
    products = [] 

    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            model = row['model']
            desc = row['desc']
            magazine = row['magazine']
            pros = row['pros']
            cons = row['cons']
            
            products.append(
                {                   
                    "id": id,       
                    "model": model,
                    "desc": desc,
                    "magazine": magazine,
                    "pros": pros,
                    "cons": cons
                }
            )
    return products



os.system('cls')
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')


while True:
    list_products(products)
    print("\n1: Visa ett vapen\n2: Lägga till ett vapen\n3: Ändra ett vapen\n4: Ta bort ett vapen\n5: Avsluta och spara")
    option = int(input())

    if option ==1:
        idx = int(input("Välj product med nummer: "))
        product = view_products(idx, products)
        input()

    elif option == 2:
        add_product(products)
        
    elif option == 3:
        try:
            index = int(input("vilken produkt (id) vill du ändra? "))
        except IndexError:
            print("Felaktigt index")

        if 1<= index <= len(products):
            placeholder = products[index -1]

        change_product(placeholder)
        

    elif option == 4:
        idx = int(input("Välj product med nummer: ")) - 1
        products.pop(idx)

    elif option == 5:
        save_products(products)
        break

    else:
        print("Felaktigt nummer")

