def func_executor(*args):
    results = []
    for func, arguments in args:
        result = func(*arguments)
        results.append(f"{func.__name__} - {result}")
    return '\n'.join(results)
