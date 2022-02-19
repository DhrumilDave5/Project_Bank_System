def simple(p: float, r: float, t: float) -> str:
    """Calculates Simple Interest"""
    amount = round(p + p * r * t / 100, 2)
    result = "The amount " + str(amount) + " is to be paid after " \
             + str(t) + " years"
    return result


def compound(p: float, r: float, t: float):
    """Calculates Compound Interest"""
    amount = round(p * ((1 + r / 100) ** t), 2)
    result = "The amount " + str(amount) + " is to be paid after " \
             + str(t) + " years"
    return result
