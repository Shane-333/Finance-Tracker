from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY format.")
        return get_date(prompt, allow_default)
    

def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-zero positive number.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
        

def get_category():
    catagory = input("Enter category ('I' for Income, 'E' for Expense): ").upper()
    if catagory in CATEGORIES:
        return CATEGORIES[catagory]
    

    print("Invalid category. Please enter either 'I' for Income or 'E' for Expense.")
    return get_category()
def get_description():
    return input("Enter description: ")