import pandas as pd
import os

def format_currency(amount, currency):
    """Format amount with currency symbol and comma separator"""
    symbols = {
        "IDR": "Rp",
        "USD": "$",
        "EUR": "€",
        "JPY": "¥"
        # Add more if needed
    }
    symbol = symbols.get(currency.upper(), currency + " ")
    return f"{symbol}{float(amount):,.0f}"

def create_budget(currency, entries):
    """
    Create a budget DataFrame with percentage breakdown and formatted currency amounts.
    :param currency: str, currency code (e.g. 'IDR', 'USD')
    :param entries: list of dicts with 'Category', 'Name', and 'Amount'
    :return: pandas DataFrame
    """
    df = pd.DataFrame(entries)
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    total = df['Amount'].sum()
    df['Percentage'] = round((df['Amount'] / total) * 100, 2)
    df['Formatted Amount'] = df.apply(lambda row: format_currency(row['Amount'], currency), axis=1)
    df['Total Amount'] = format_currency(total, currency)

    print(f"\nTotal Budget: {format_currency(total, currency)}\n")
    print("Budget Breakdown:\n")
    print(df[['Category', 'Name', 'Formatted Amount', 'Percentage', 'Total Amount']])

    return df

# Get currency from user
currency_input = input("Enter currency (e.g. IDR, USD): ")

# Collect budget entries
budget_items = []
while True:
    category = input("Enter budget category (or type 'done' to finish): ")
    if category.lower() == 'done':
        break
    name = input("Enter budget name: ")
    amount = input(f"Enter amount for '{name}': ")
    budget_items.append({'Category': category, 'Name': name, 'Amount': amount})

# Generate and display budget
budget_df = create_budget(currency_input, budget_items)

# Export to CSV
os.makedirs("output", exist_ok=True)
file_name = input("\nEnter filename to save CSV (e.g. budget_report.csv): ")
file_name = os.path.join("output", file_name)
budget_df.to_csv(file_name, index=False, columns=['Category', 'Name', 'Formatted Amount', 'Percentage', 'Total Amount'])
print(f"\nBudget saved to '{file_name}' successfully!")