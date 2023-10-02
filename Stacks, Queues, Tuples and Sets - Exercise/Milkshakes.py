"""
Read input
"""
chocolates = list(map(int, input().split(", ")))
milk_cups = list(map(int, input().split(", ")))

"""
Initialize milkshakes made counter
"""
milkshakes_made = 0

"""
Loop until 5 milkshakes are made or no more ingredients left
"""
while milkshakes_made < 5 and chocolates and milk_cups:
    """
    Get the last chocolate and the first milk cup
    """
    chocolate = chocolates[-1]
    milk = milk_cups[0]

    """
    Check if either chocolate or milk is less than or equal to 0
    """
    if chocolate <= 0:
        chocolates.pop()
        continue
    if milk <= 0:
        milk_cups.pop(0)
        continue

    """
    Attempt to make a milkshake
    """
    if chocolate == milk:
        milkshakes_made += 1
        chocolates.pop()
        milk_cups.pop(0)
    else:
        """
        Move the milk cup to the end and decrease chocolate value by 5
        """
        milk_cups.append(milk_cups.pop(0))
        chocolates[-1] -= 5

"""
Output results
"""
print("Great! You made all the chocolate milkshakes needed!" if milkshakes_made == 5 else "Not enough milkshakes.")
print(f"Chocolate: {'empty' if not chocolates else ', '.join(map(str, chocolates))}")
print(f"Milk: {'empty' if not milk_cups else ', '.join(map(str, milk_cups))}")
