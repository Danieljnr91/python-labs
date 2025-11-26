def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
           return True
    else:
        return False        
    
def days_in_months(year,month):
    if month == 'february':
        if leap_year(year):
            return f'{month.title()} has 29 days'
        else:
            return f'{month.title()} has 28 days'
        
    elif month in ['april' , 'september' , 'june' , 'november']:
        return f'{month.title()} has 30 days'
    else:
        return f"{month.title()} has 31 days"
    
year_input = int(input("Enter year:"))
month_input = input("Enter month:").lower()

leap_year(year_input)
print(days_in_months(year = year_input , month = month_input))
