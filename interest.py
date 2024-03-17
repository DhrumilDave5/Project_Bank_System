def simple():
    print("Enter the required details to calculate simple interest\n")

    while True:
        p = input("\nPrincipal amount: ")
        if "." in p:
            decimal_index = p.find(".")
            if (p[:decimal_index] + p[decimal_index + 1:]).isnumeric():
                p = round(float(p), 2)
                break
            else:
                print("Please enter a positive numeric value")
        elif p.isnumeric():
            p = round(float(p), 2)
            break
        else:
            print("Please enter a positive numeric value")

    while True:
        r = input("\nRate of interest (per annum): ")
        if "." in r:
            decimal_index = r.find(".")
            if (r[:decimal_index] + r[decimal_index + 1:]).isnumeric():
                r = float(r)
                break
            else:
                print("Please enter a positive numeric value")
        elif r.isnumeric():
            r = float(r)
            break
        else:
            print("Please enter a positive numeric value")

    while True:
        t = input("\nTime period (in years): ")
        if t.isnumeric():
            t = int(t)
            break
        else:
            print("Please enter a positive integer value")

    amount = round(p + (p * r * t / 100), 2)
    print("\n" + "-" * 75 + "\n")
    print("The amount", amount, "is to be paid after", t, "years")


def compound():
    print("Enter the required details to calculate compound interest\n")

    while True:
        p = input("\nPrincipal amount: ")
        if "." in p:
            decimal_index = p.find(".")
            if (p[:decimal_index] + p[decimal_index + 1:]).isnumeric():
                p = round(float(p), 2)
                break
            else:
                print("Please enter a positive numeric value")
        elif p.isnumeric():
            p = round(float(p), 2)
            break
        else:
            print("Please enter a positive numeric value")

    while True:
        r = input("\nRate of interest (per annum): ")
        if "." in r:
            decimal_index = r.find(".")
            if (r[:decimal_index] + r[decimal_index + 1:]).isnumeric():
                r = float(r)
                break
            else:
                print("Please enter a positive numeric value")
        elif r.isnumeric():
            r = float(r)
            break
        else:
            print("Please enter a positive numeric value")

    while True:
        t = input("\nTime period (in years): ")
        if t.isnumeric():
            t = int(t)
            break
        else:
            print("Please enter a positive integer value")

    amount = round(p * ((1 + r / 100) ** t), 2)
    print("\n" + "-" * 75 + "\n")
    print("The amount", amount, "is to be paid after", t, "years")
