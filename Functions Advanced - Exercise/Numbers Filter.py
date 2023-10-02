def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == 'even':
            result[key] = [num for num in value if num % 2 == 0]
        elif key == 'odd':
            result[key] = [num for num in value if num % 2 != 0]
    sorted_result = dict(sorted(result.items(), key=lambda x: len(x[1]), reverse=True))
    return sorted_result