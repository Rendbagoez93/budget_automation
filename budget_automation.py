import pandas as pd
import os
import sys
from datetime import datetime

# Import budget approval system
try:
    from budget_approval import BudgetApprovalSystem
    APPROVAL_SYSTEM_AVAILABLE = True
except ImportError:
    print("Warning: budget_approval.py not found. Approval system will be disabled.")
    APPROVAL_SYSTEM_AVAILABLE = False

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
    
    # Check for invalid amounts (NaN values)
    if df['Amount'].isna().any():
        invalid_entries = df[df['Amount'].isna()]['Name'].tolist()
        print(f"Warning: Invalid amounts detected for: {', '.join(invalid_entries)}")
        print("These entries will be excluded from calculations.")
        df = df.dropna(subset=['Amount'])
    
    if df.empty:
        print("Error: No valid budget entries found.")
        return pd.DataFrame()
    
    total = df['Amount'].sum()
    df['Percentage'] = round((df['Amount'] / total) * 100, 2)
    df['Formatted Amount'] = df.apply(lambda row: format_currency(row['Amount'], currency), axis=1)

    print(f"\nTotal Budget: {format_currency(total, currency)}\n")
    print(f"Created on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print("Budget Breakdown:")
    print("-" * 60)
    print(df[['Category', 'Name', 'Formatted Amount', 'Percentage']])

    return df


def save_budget_to_csv(budget_df, currency):
    """
    Save budget DataFrame to CSV file with enhanced naming
    """
    os.makedirs("output", exist_ok=True)
    
    # Generate default filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    default_filename = f"budget_{currency.lower()}_{timestamp}.csv"
    
    print(f"\nDefault filename: {default_filename}")
    custom_name = input("Enter custom filename (or press Enter to use default): ").strip()
    
    if custom_name:
        file_name = custom_name
        if not file_name.endswith('.csv'):
            file_name += '.csv'
    else:
        file_name = default_filename
    
    file_path = os.path.join("output", file_name)
    budget_df.to_csv(file_path, index=False, columns=['Category', 'Name', 'Formatted Amount', 'Percentage'])
    print(f"\nBudget saved to '{file_path}' successfully!")
    
    return file_path


def run_approval_process(csv_file_path):
    """
    Run the budget approval process if available
    """
    if not APPROVAL_SYSTEM_AVAILABLE:
        print("\nApproval system not available. Please ensure budget_approval.py exists.")
        return
    
    print("\n" + "="*60)
    print("STARTING BUDGET APPROVAL PROCESS")
    print("="*60)
    
    try:
        approval_system = BudgetApprovalSystem()
        approval_system.process_budget_approval(csv_file_path)
    except Exception as e:
        print(f"Error running approval process: {str(e)}")


def main():
    """
    Main budget automation workflow
    """
    print("="*60)
    print("BUDGET AUTOMATION SYSTEM")
    print("="*60)
    print("Create and optionally approve your budget")
    print()    
    # Get currency from user
    valid_currencies = ["IDR", "USD", "EUR", "JPY"]
    while True:
        currency_input = input("Enter currency (IDR, USD, EUR, JPY): ").upper()
        if currency_input in valid_currencies:
            break
        print(f"Invalid currency. Please choose from: {', '.join(valid_currencies)}")

    # Collect budget entries
    budget_items = []
    print(f"\nEnter budget items (currency: {currency_input})")
    print("Type 'done' when finished entering items")
    print("-" * 40)
    
    while True:
        category = input("Enter budget category (or type 'done' to finish): ").strip()
        if category.lower() == 'done':
            break
        if not category:
            print("Category cannot be empty. Please try again.")
            continue
        
        name = input("Enter budget name: ").strip()
        if not name:
            print("Budget name cannot be empty. Please try again.")
            continue
        
        while True:
            try:
                amount = input(f"Enter amount for '{name}': ").strip()
                if not amount:
                    print("Amount cannot be empty. Please try again.")
                    continue
                # Test if it's a valid number
                float(amount)
                break
            except ValueError:
                print("Please enter a valid number.")
        
        budget_items.append({'Category': category, 'Name': name, 'Amount': amount})
        print(f"✓ Added: {name} - {format_currency(float(amount), currency_input)}")

    if not budget_items:
        print("No budget items entered. Exiting.")
        return

    # Generate and display budget
    budget_df = create_budget(currency_input, budget_items)

    # Only proceed with export if we have valid data
    if not budget_df.empty:
        # Save budget to CSV
        csv_file_path = save_budget_to_csv(budget_df, currency_input)
        
        # Ask if user wants to run approval process
        if APPROVAL_SYSTEM_AVAILABLE:
            run_approval = input("\nWould you like to run the approval process? (y/n): ").strip().lower()
            if run_approval in ['y', 'yes']:
                run_approval_process(csv_file_path)
            else:
                print(f"Budget saved. You can run approval later using budget_approval.py")
        else:
            print("Approval system not available. Budget creation completed.")
    else:
        print("No valid budget data to save.")

if __name__ == "__main__":
    main()

# Get currency from user
valid_currencies = ["IDR", "USD", "EUR", "JPY"]
while True:
    currency_input = input("Enter currency (IDR, USD, EUR, JPY): ").upper()
    if currency_input in valid_currencies:
        break
    print(f"Invalid currency. Please choose from: {', '.join(valid_currencies)}")

# Collect budget entries
budget_items = []
while True:
    category = input("Enter budget category (or type 'done' to finish): ").strip()
    if category.lower() == 'done':
        break
    if not category:
        print("Category cannot be empty. Please try again.")
        continue
    
    name = input("Enter budget name: ").strip()
    if not name:
        print("Budget name cannot be empty. Please try again.")
        continue
    
    while True:
        try:
            amount = input(f"Enter amount for '{name}': ").strip()
            if not amount:
                print("Amount cannot be empty. Please try again.")
                continue
            # Test if it's a valid number
            float(amount)
            break
        except ValueError:
            print("Please enter a valid number.")
    
    budget_items.append({'Category': category, 'Name': name, 'Amount': amount})

if not budget_items:
    print("No budget items entered. Exiting.")
    exit()

# Generate and display budget
budget_df = create_budget(currency_input, budget_items)

# Only proceed with export if we have valid data
if not budget_df.empty:
    # Export to CSV
    os.makedirs("output", exist_ok=True)
    
    while True:
        file_name = input("\nEnter filename to save CSV (e.g. budget_report.csv): ").strip()
        if file_name:
            if not file_name.endswith('.csv'):
                file_name += '.csv'
            break
        print("Filename cannot be empty. Please try again.")
    
    file_path = os.path.join("output", file_name)
    budget_df.to_csv(file_path, index=False, columns=['Category', 'Name', 'Formatted Amount', 'Percentage'])
    print(f"\nBudget saved to '{file_path}' successfully!")
else:
    print("No valid budget data to save.")