#!/usr/bin/env python3
"""
Budget Automation Integration Script
This script demonstrates the complete workflow from budget creation to approval
"""

import os
import sys

def run_budget_creation():
    """Run the budget creation process"""
    print("="*60)
    print("STEP 1: BUDGET CREATION")
    print("="*60)
    
    try:
        import budget_automation
        print("Budget creation completed successfully!")
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

def main():
    """Main integration workflow"""
    print("BUDGET AUTOMATION - COMPLETE WORKFLOW")
    print("="*60)
    print("This script will guide you through:")
    print("1. Creating a budget (budget_automation.py)")
    print("2. Approving the budget (budget_approval.py)")
    print()
    
    choice = input("Do you want to run the complete workflow? (y/n): ").strip().lower()
    
    if choice in ['y', 'yes']:
        # Step 1: Create budget
        if run_budget_creation():
            # Step 2: Approve budget (if user wants)
            approve_choice = input("\nProceed to budget approval? (y/n): ").strip().lower()
            if approve_choice in ['y', 'yes']:
                run_budget_approval()
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

if __name__ == "__main__":
    main()
