import csv

def main():
    
    products_dict = read_dictionary("products.csv", 0)
    request_dict = read_dictionary("request.csv", 1)
    
    print(products_dict)
    #print(request_dict)

    



def read_dictionary(filename, key_column_index):

    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
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
