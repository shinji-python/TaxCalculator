def tax_calculator(amount,tax_rate):
    tax_amount= str(round(amount + (tax_rate*amount),2))
    print('Your value including tax is: $',tax_amount)

def input_value():
    amount = int(input('What is your value amount?'))
    return amount

def input_tax():
    tax = float(input('What is your tax rate?'))
    return tax * .01


while True:
    print('Welcome to the Tax Calculator!')

    # Ask the user the input the amount
    amount = input_value()

    # Ask the user to provide the country or state tax rate
    tax_rate = input_tax()

    # Calculate the total amount taxed
    tax_calculator(amount, tax_rate)

    # Ask if the user wants another calculation
    new_calculation = input('Do you want another calculation? Y or N')

    if new_calculation == 'Y':
        continue
    else:
        print('Thanks for Calculating!')
    break