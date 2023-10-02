def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-sum(x[1]), x[0]))
    result = []
    for cheese, quantities in sorted_cheeses:
        sorted_quantities = sorted(quantities, reverse=True)
        result.append(cheese)
        result.extend(sorted_quantities)
    return "\n".join(map(str, result))
    
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135], 
        Camembert=[100, 100, 105, 500, 430], 
        Mozzarella=[50, 125],
    )
)
