def recursive_power(number, power):
    if power == 0:
        return 1
    elif power > 0:
        return number * recursive_power(number, power - 1)
    else:
        return 1 / (number * recursive_power(number, abs(power) - 1))