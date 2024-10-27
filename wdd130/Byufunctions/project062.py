# I used a function to print a title and a personalized welcome message. I used two more functions
#I used emojis to better the visual of the program, frames added to show better the lowest, highest expectancy of life and search by year

# function to print a title and a welcome message
def welcome_user():
    print("◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇")
    print()
    print("✴︎  Welcome to the Life Expectancy Analyzer Program! ✴︎".center(120,' '))
    print()
    print("◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇ ◈◇")
    print()
    user_welcome = input("Hello dear visitor, please type your name: ")
    print()
    print(f"Hello dear {user_welcome}!, our program analize the Life expectancy through the last 100 years.\n")
    print('You can choose to see the entire list wiht more than 19,000 lines of information,\nor just use our search tools to simplify your navigation.\n')
    return user_welcome

# Function to read the file, split lines and give some spaces
def read_data(life_expectancy):
    data = []
    with open(life_expectancy, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) > 1:  
                data.append(parts)
    return data


#Function to stablish the variables that make the program work, menu to read the entire fire or choosing the search options
def analyze_data(data):
    while True:
        choice = input("What are you going to do?:\n\n(1) read the entire list or\n(2) go directly to the questions?\nEnter 1 or 2: ")
        
        if choice == '1':
            for row in data:
                print('|   |'.join(row))
            break
        elif choice == '2':
            while True:
                option = input("Choose an option:\n\n(1) Lowest life expectancy\n(2) Highest life expectancy\n"
                               "(3) Analyze by year\n(4) Exit: ")
                
                if option == '1':
                    min_life_exp = float('inf')
                    min_year, min_country = '', ''
                    for row in data[1:]: 
                        life_expectancy = float(row[3])
                        if life_expectancy < min_life_exp:
                            min_life_exp = life_expectancy
                            min_year, min_country = row[0], row[1]
                    print()        
                    print("----------------------------------------------------------------------------------")
                    print(f"The lowest life expectancy is {min_life_exp} years in {min_country} ({min_year}).")
                    print("----------------------------------------------------------------------------------")                   
                    print()


                elif option == '2':
                    max_life_exp = float('-inf')
                    max_year, max_country = '', ''
                    for row in data[1:]:
                        life_expectancy = float(row[3])
                        if life_expectancy > max_life_exp:
                            max_life_exp = life_expectancy
                            max_year, max_country = row[0], row[1]
                    print()        
                    print("-----------------------------------------------------------------------------------")
                    print(f"The highest life expectancy is {max_life_exp} years in {max_country} ({max_year}).")
                    print("-----------------------------------------------------------------------------------")  
                    print()


                elif option == '3':
                    year = input("\nType the year of your preference (e.g., 2000): ")
                    year_data = {}
                    for row in data[1:]:
                        if row[2] == year:
                            country = row[0]
                            life_expectancy = float(row[3])
                            year_data[country] = life_expectancy
                    if year_data:
                        avg_life_exp = sum(year_data.values()) / len(year_data)
                        min_country = min(year_data, key=year_data.get)
                        max_country = max(year_data, key=year_data.get)
                        print()
                        print("---------------------------------------------------------------")
                        print(f"Average life expectancy in {year} is {avg_life_exp:.2f} years.")
                        print(f"Lowest: {min_country} with {year_data[min_country]} years.")
                        print(f"Highest: {max_country} with {year_data[max_country]} years.")
                        print("---------------------------------------------------------------")
                        print()
                    else:
                        print("We could not find a data for the selected year.")
                        print()

                elif option == '4':
                    print("Finish the program.")
                    print()
                    return
                
                else:
                    print("Invalid option. Please choose a valid option.")
        else:
            print(f"Dear {user_welcome}. Please enter 1 or 2.")

if __name__ == "__main__":
    user_welcome = welcome_user()
    dataset = read_data('life-expectancy.csv')
    analyze_data(dataset)
