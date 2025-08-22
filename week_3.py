def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount.
    If discount is 20% or higher, apply it.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Get final price
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")
