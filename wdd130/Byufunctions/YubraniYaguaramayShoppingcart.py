#For more personalization I added a third option to place the color you want the item in, I hope you find it interesting
#Shopping cart
Items_for_sell = ""
list_items_sell = []
items_price = ""
list_items_price = []
items_color = ""
list_items_color = []
sum = 0
user_selection = ["1. Add item", "2. View cart", "3. Remove item", "4. Compute total", "5. Quit"]
user_decision = ""
add_item = "yes"
user_selection_number = []
print("Welcome to the Developmart application, an exclusive store for programmers, to advance your purchase, enter the number of the option you want to take, welcome to our system")

print("Please select one of the following")

#for options in user_selection:
    #print(options)

#user_decision = int(input("Please enter an action: "))
while user_decision != 5:
    
    for options in user_selection:
        print(options)

    user_decision = int(input("Please enter an action: "))
    
    
    
        
            
        
    if user_decision == 1:
                
            Items_for_sell = str(input("What item would you like to add? "))
            list_items_sell.append(Items_for_sell)

            items_price = float(input(f"What is the price of the {Items_for_sell}? "))
            list_items_price.append(items_price)

            items_color = str(input("What color would you like it? "))
            list_items_color.append(items_color)

            print(f"{Items_for_sell} has been added to the cart.")

           
    
    

    if user_decision == 2:
        
            print("The contents of the shopping cart are:" )
            for i in range(0, len(list_items_sell)):
                list_sell = list_items_sell[i]
                list_price = list_items_price[i]
                list_color = list_items_color[i]
                print(f"{i + 1}. {list_color} {list_sell} .- ${list_price}")

        

    if user_decision == 3:
            item_remove = int(input("Which item do you want to remove? "))
            popped_item = list_items_sell.pop(item_remove -1)
            popped_cash = list_items_price.pop(item_remove -1)
            print(f"You removed {popped_item} from you shopping cart")

    if user_decision == 4:
            for list_price in list_items_price:
                sum += list_price
                
    
            print(f"The total price of the items in the shopping cart is: ${sum:.2f}")
            list_price = []
            sum = 0
   
    
        
    
       

print("Thank you. Goodbye.")


    






