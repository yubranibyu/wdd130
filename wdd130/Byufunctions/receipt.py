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
    print("All products")
    print(products_dict)
    total_items = 0
    subtotal = 0
    tax = 0.06
    total = 0
    tax_amount = 0

   
    
    for i in products_dict and request_dict:
        key = products_dict[i][0]
        product = products_dict[i][1]
        price = products_dict[i][2]
        key_request = products_dict[i][0]
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

    
    
  
    # Get an I-Number from the user.
    

    # The I-Numbers are stored in the CSV efile as digits only (without
    # any dashes), so we remove all dashes from the user's input.
    

    # Determine if the user input is formatted correctly.


                
                        
   # if products_dict == request_dict:         




       # value = products_dict[inumber]
        #index_dict = value[NAME_INDEX]
        #value_request = request_dict[inumber][1]
        #price_value = value[2] 
        
        #print(f"{index_dict} @ {value_request} {price_value}")

    



def read_dictionary(filename, key_column_index):

    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            
            index = row_list[key_column_index]
            dictionary[index] = row_list

    """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters

      
  
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
    return dictionary
if __name__ == "__main__":
    main()
