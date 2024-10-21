import csv
from datetime import datetime
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
# Use an f-string to print the current
# day of the week and the current time.

def main():
    KEY_COLUMN_INDEX = 0
    NAME_INDEX = 1
    total_items = 0
    products_dict = read_dictionary("products.csv", KEY_COLUMN_INDEX)
    request_dict = read_dictionary("request.csv", KEY_COLUMN_INDEX)
    print(f"Inkom Emporium")
    total_items = 0
    subtotal = 0
    tax = 0.06
    total = 0
    tax_amount = 0

    try:

        products_dict = read_dictionary("products.csv", KEY_COLUMN_INDEX)
        request_dict = read_dictionary("request.csv", KEY_COLUMN_INDEX)

        for i in products_dict and request_dict:
        
            product = products_dict[i][1]
            price = products_dict[i][2]
            quantity_request = request_dict[i][1]
            total_items += float(quantity_request)
            subtotal += float(price)
            
            print(f"{product} {quantity_request} {price} ")
        print(f"Total of items: {total_items}")
        print(f"The subtotal is: {subtotal:.3f}$")
        total = subtotal + (subtotal * tax)
        tax_amount = subtotal * tax
        print(f"Sales tax: {tax_amount:.2f}")

        print(f"Total: {total:.3f}$")
        print("Thank you for shopping at: Inkom Emporeum")
        print(f"{current_date_and_time:%A %I:%M %p}")
    
    except KeyError as keyerr:
        print("Error: missing file")
        print("[Errno 2] No such file or directory: 'products.csv'")


def read_dictionary(filename, key_column_index):

    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            
            index = row_list[key_column_index]
            dictionary[index] = row_list


    return dictionary
if __name__ == "__main__":
    main()
