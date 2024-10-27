#Data analisys
#SHOWING CREATIVITY: I added a search by country, which shows the maximum life expectancy and the minimum.



with open("life-expectancy.csv") as database1:
    year_select = int(input("Enter the year of interest: "))
    country_user_select = str(input("Enter the name of the country: "))
    
    max_expectancy = 0
    max_country = ""
    max_year = 0
    min_country = ""
    min_year = 100000000000
    sum = 0.0
    min_expectancy = 100000000000
    max_year_selected = 0
    expectancy_selected = 0
    country_selected = ""
    max_expectancy_selected = 0
    max_country_selected = ""
    min_expectancy_selected = 1000000000
    min_country_selected = ""
    average_expectancy = 0
    expectancy_user_selected = 0
    year_user_selected = 0
    country_user_selected = ""
    min_expectancy_user_selected = 1000000000
    max_expectancy_user_selected = 0
    min_year_user_selected = 0
    min_country_user_selected = ""
    max_year_user_selected = 0
    max_country_user_selected = ""
    sum1 = 0
    average_user_expectancy = 0
    


    
    for data in database1:

        clean_line = data.strip()

        parts = clean_line.split(",")
        
        country = str(parts[0])
        code = str(parts[1])
        year = int(parts[2])
        expectancy = float(parts[3])
       

        if expectancy > max_expectancy:
                
            max_expectancy = expectancy
            max_country = country
            max_year = year
        
        
                
        if expectancy < min_expectancy:

            min_expectancy = expectancy
            min_country = country
            min_year = year
        
        if year_select == year:
            year_select = year
            country_selected = country
            expectancy_selected = expectancy
            
            sum += expectancy_selected
            average_expectancy = sum
            

            if expectancy_selected > max_expectancy_selected:
                max_expectancy_selected = expectancy_selected
                max_year_selected = year_select
                max_country_selected = country_selected
            
            if expectancy_selected < min_expectancy_selected:
                min_expectancy_selected = expectancy_selected
                min_country_selected = country_selected
        
        sum = 0

        if country_user_select.lower() == country.lower():
            country_user_select = country
            year_user_selected = year
            expectancy_user_selected = expectancy
            sum1 += expectancy_user_selected
            

            if expectancy_user_selected > max_expectancy_user_selected:
                max_expectancy_user_selected = expectancy_user_selected
                max_country_user_selected = country_user_select
                max_year_user_selected = year_user_selected
            if expectancy_user_selected < min_expectancy_user_selected:
                min_expectancy_user_selected = expectancy_user_selected
                min_country_user_selected = country_user_select
                min_year_user_selected = year_user_selected
        sum1 = 0
                

            
        
       
    print(f"The overall max life expectancy is: {max_expectancy} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min_expectancy} from {min_country} in {min_year}")
    print(f"For the year {year_select}:" )
    print(f"The average life expectancy across all countries was {average_expectancy:.3f}")
    print(f"The max life expectancy was in {max_country_selected} with {max_expectancy_selected}")
    print(f"The min life expectancy was in {min_country_selected} with {min_expectancy_selected}")
    print(f"For the country: {country_user_select}:" )
    print(f"The max life expectancy in {country_user_select} was {max_expectancy_user_selected} in {max_year_user_selected}")
    print(f"The min life expectancy in {country_user_select} was {min_expectancy_user_selected} in {min_year_user_selected}")
    
    

       
      

