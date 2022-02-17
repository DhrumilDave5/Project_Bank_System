def simple_interest():
    print("App To Calculate Your Interest")
    print("Fill Out The Following Form To Get Your Interest")
    p = float(input("Principal Amount:"))
    r = float(input("Rate Of Interest Per Annum:"))
    t = float(input("Time Period:"))
    Amount = p + p * r * t / 100
    print("The Following Is The Amount", Amount, "To Be Paid After", t, "Years")
    return Amount
