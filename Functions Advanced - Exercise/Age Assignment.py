def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            age = kwargs[first_letter]
            result.append(f"{name} is {age} years old.")
    return '\n'.join(sorted(result))
