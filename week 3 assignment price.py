def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user to enter the original price
original_price = float(input("Enter the original price of the item: "))

# Prompt the user to enter the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
print("The final price after applying the discount is: {:.2f}".format(final_price))

# If no discount was applied, print the original price
if final_price == original_price:
    print("No discount was applied as the discount percentage was less than 20%.")