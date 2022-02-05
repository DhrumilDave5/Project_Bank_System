def simple_interest():
    print("App To Calculate Your Interest")
    print("Fill Out The Following Form To Get Your Interest")
    p=float(input("Principal Amount:"))
    r=float(input("Rate Of Interest Per Annum:"))
    t=float(input("Time Period:"))
    Amount=p*r*t/100
    print("The Following Is The Amount", Amount, "To Be Paid After", t,"Years"  )
    return Amount


def compound_interest():
    print('Application to calculate compound interest.')
    print('Principal amount is in rupees and time in years.')
    p=int(input('Enter principal amount='))
    t=float(input('Enter time in years='))
    r=float(input('Enter rate of interest='))
    amount=p*((1+r/100)**t)
    print('So you have to pay',amount, 'in', t,'years.')
    return amount
