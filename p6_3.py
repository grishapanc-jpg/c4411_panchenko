def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry, we cant work with {type(var_1)}, we need class str")
    else:
        return var_1

first_var = 10
checker(first_var)