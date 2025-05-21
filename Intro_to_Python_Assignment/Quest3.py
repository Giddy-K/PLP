def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage to apply.

    Returns:
        float: Final price after discount if discount_percent >= 20,
               otherwise the original price.
    """
    return price * (1 - discount_percent / 100) if discount_percent >= 20 else price


def main() -> None:
    """Prompt the user for price and discount and display the final price."""
    try:
        price = float(input("Enter the original price (e.g., 199.99): "))
        discount = float(input("Enter the discount percentage (e.g., 25): "))
    except ValueError:
        print("Please enter numeric values only.")
        return

    final_price = calculate_discount(price, discount)

    if final_price != price:
        print(f"Discount applied. Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {price:.2f}")


if __name__ == "__main__":
    main()
