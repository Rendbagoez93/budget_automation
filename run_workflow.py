#!/usr/bin/env python3
"""
Budget Automation Integration Script
This script demonstrates the complete workflow from budget creation to approval
"""

import os
import sys
import pandas as pd
from datetime import datetime

def run_budget_creation():
    """Run the budget creation process"""
    print("="*60)
    print("STEP 1: BUDGET CREATION")
    print("="*60)
    
    print("\nSelect budget creation method:")
    print("1. Basic Budget Creation (budget_automation.py)")
    print("2. Comprehensive Budget with Templates (comprehensive_budget.py)")
    
    while True:
        choice = input("\nSelect option (1 or 2): ").strip()
        if choice in ['1', '2']:
            break
        print("Invalid choice. Please enter 1 or 2")
    
    try:
        if choice == '1':
            import budget_automation
            print("Budget creation completed successfully!")
        else:
            import comprehensive_budget
            comprehensive_budget.main()
        return True
    except Exception as e:
        print(f"Error in budget creation: {str(e)}")
        return False

def run_budget_approval():
    """Run the budget approval process"""
    print("\n" + "="*60)
    print("STEP 2: BUDGET APPROVAL")
    print("="*60)
    
    try:
        import budget_approval
        budget_approval.main()
        return True
    except Exception as e:
        print(f"Error in budget approval: {str(e)}")
        return False

def export_budget_report(input_file='budget_with_approval.xlsx', output_file=None):
    """Export budget data as a neat report"""
    print("\n" + "="*60)
    print("STEP 3: EXPORT BUDGET REPORT")
    print("="*60)
    
    try:
        if not os.path.exists(input_file):
            print(f"Error: {input_file} not found. Please complete approval first.")
            return False
        
        # Read the approved budget
        df = pd.read_excel(input_file)
        
        # Create neat column titles for report
        column_mapping = {
            'Category': 'Budget Category',
            'Q1': 'Q1 Budget',
            'Q2': 'Q2 Budget',
            'Q3': 'Q3 Budget',
            'Q4': 'Q4 Budget',
            'Total': 'Annual Total',
            'Approval_Status': 'Approval Status',
            'Approved_By': 'Approved By',
            'Approval_Date': 'Approval Date',
            'Comments': 'Comments'
        }
        
        df_report = df.rename(columns=column_mapping)
        
        # Generate output filename with timestamp
        if output_file is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f'budget_report_{timestamp}.xlsx'
        
        # Export with formatting
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            df_report.to_excel(writer, sheet_name='Budget Report', index=False)
            
            # Get workbook and worksheet
            workbook = writer.book
            worksheet = writer.sheets['Budget Report']
            
            # Auto-adjust column widths
            for idx, col in enumerate(df_report.columns, 1):
                max_length = max(
                    df_report[col].astype(str).apply(len).max(),
                    len(col)
                ) + 2
                worksheet.column_dimensions[chr(64 + idx)].width = min(max_length, 50)
        
        print(f"✓ Budget report exported successfully: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error exporting report: {str(e)}")
        return False

def main():
    """Main integration workflow"""
    print("BUDGET AUTOMATION - COMPLETE WORKFLOW")
    print("="*60)
    print("This script will guide you through:")
    print("1. Creating a budget (budget_automation.py)")
    print("2. Approving the budget (budget_approval.py)")
    print("3. Exporting budget report (formatted Excel)")
    print()
    
    choice = input("Do you want to run the complete workflow? (y/n): ").strip().lower()
    
    if choice in ['y', 'yes']:
        # Step 1: Create budget
        if run_budget_creation():
            # Step 2: Approve budget
            approve_choice = input("\nProceed to budget approval? (y/n): ").strip().lower()
            if approve_choice in ['y', 'yes']:
                if run_budget_approval():
                    # Step 3: Export report
                    export_choice = input("\nExport budget report? (y/n): ").strip().lower()
                    if export_choice in ['y', 'yes']:
                        export_budget_report()
                else:
                    print("Budget approval failed.")
            else:
                print("Budget approval skipped. You can run it later using budget_approval.py")
        else:
            print("Budget creation failed. Cannot proceed to approval.")
    else:
        print("Workflow cancelled.")
        
        # Offer individual components
        print("\nYou can run individual components:")
        print("- python budget_automation.py (create budget)")
        print("- python budget_approval.py (approve existing budget)")
        print("- Run this script and export only (for existing approved budgets)")

if __name__ == "__main__":
    main()