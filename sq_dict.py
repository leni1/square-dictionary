def sq_func():
    numbers = set(range(1, 15, 1))
    square_dict = {n: n**2 for n in numbers if n != 1}

    return square_dict
