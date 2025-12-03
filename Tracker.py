# -----------------------------------------------
#      PERSONAL MONTHLY BUDGET TRACKER
#                 by Ansh
# -----------------------------------------------

def print_header():
    print("=" * 50)
    print(" PERSONAL MONTHLY BUDGET TRACKER ".center(50))
    print("=" * 50)
    print()


def get_positive_int(message):
    """
    Safely takes a positive integer from the user.
    If the user enters something invalid, it asks again.
    """
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("Please enter a positive value only.\n")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")


def print_expense_table(expenses, income, total_expenditure, saving):
    """
    Prints a clean table of all expenses with
    their amount and percentage of income.
    """
    print("\n" + "-" * 50)
    print(" EXPENSE BREAKDOWN ".center(50, "-"))
    print("-" * 50)

    # Header
    print(f"{'Category':<25} {'Amount (₹)':>12} {'% of Income':>12}")
    print("-" * 50)

    for category, amount in expenses.items():
        if income > 0:
            percent = (amount / income) * 100
        else:
            percent = 0
        print(f"{category:<25} {amount:>12} {percent:>11.1f}%")

    print("-" * 50)
    print(f"{'Total Expenditure':<25} {total_expenditure:>12}")
    print(f"{'Saving':<25} {saving:>12}")
    print("-" * 50)


def print_saving_analysis(saving, income):
    """
    Gives a message based on savings and a small analysis.
    """
    print("\n" + "=" * 50)
    print(" SUMMARY ".center(50))
    print("=" * 50)

    if saving > 0:
        saving_percent = (saving / income) * 100 if income > 0 else 0
        print(f"✅ Your expenses are under control!")
        print(f"   You saved ₹{saving} this month ({saving_percent:.1f}% of your income).")

        if saving_percent < 10:
            print("💡 Try to increase your savings to at least 10% of your income.")
        elif saving_percent < 20:
            print("👍 Good! Try to reach 20% savings if possible.")
        else:
            print("🌟 Excellent! You are saving very well. Keep it up!")
    elif saving == 0:
        print("⚠ You are breaking even. You are not saving anything.")
        print("💡 Try to cut down small unnecessary expenses to start saving.")
    else:
        print("❌ Your expenses are NOT under control!")
        print(f"   You overspent by ₹{-saving}.")
        print("💡 Reduce some non-essential expenses like outings, shopping, etc.")

    print("=" * 50)
    print("        THANK YOU FOR USING THE TRACKER        ")
    print("=" * 50)


def main():
    print_header()

    # --- INPUT SECTION ---
    income = get_positive_int("Enter your Monthly Income (₹): ")

    print("\nEnter your monthly expenses:\n")

    rent = get_positive_int("🏠 Rent (₹): ")
    clothing = get_positive_int("👕 Clothing (₹): ")
    child_education = get_positive_int("📚 Child Education (₹): ")
    salon = get_positive_int("💇 Salon (₹): ")
    electricity = get_positive_int("💡 Electricity (₹): ")
    recharge = get_positive_int("📱 Mobile Recharge (₹): ")
    gas = get_positive_int("⛽ Gas (₹): ")
    food = get_positive_int("🍽 Food (₹): ")

    # Store all expenses in a dictionary
    expenses = {
        "Rent": rent,
        "Clothing": clothing,
        "Child Education": child_education,
        "Salon": salon,
        "Electricity": electricity,
        "Mobile Recharge": recharge,
        "Gas": gas,
        "Food": food
    }

    # Calculate total expenditure and saving
    total_expenditure = sum(expenses.values())
    saving = income - total_expenditure

    # --- OUTPUT SECTION ---
    print_expense_table(expenses, income, total_expenditure, saving)
    print_saving_analysis(saving, income)


# Runs only when the file is executed directly
if _name_ == "_main_":
    main()