def compound_interest():
    print('Application to calculate compound interest.')
    print('Principal amount is in rupees and time in years.')
    p = int(input('Enter principal amount='))
    t = float(input('Enter time in years='))
    r = float(input('Enter rate of interest='))
    amount = p * ((1 + r / 100) ** t)
    print('So you have to pay', amount, 'in', t, 'years.')
    return amount
