"""
Budget Templates and Comprehensive Budget Creation
Provides pre-defined templates and advanced budget creation features
"""

import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional

class BudgetTemplates:
    """Pre-defined budget templates for various use cases"""
    
    @staticmethod
    def get_personal_budget_template() -> List[Dict]:
        """Personal/Household budget template"""
        return [
            {'Category': 'Housing', 'Name': 'Rent/Mortgage', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Housing', 'Name': 'Utilities', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Housing', 'Name': 'Home Maintenance', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Transportation', 'Name': 'Car Payment/Lease', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Transportation', 'Name': 'Fuel', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Transportation', 'Name': 'Insurance', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Transportation', 'Name': 'Maintenance', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Food', 'Name': 'Groceries', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Food', 'Name': 'Dining Out', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'Healthcare', 'Name': 'Insurance', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Healthcare', 'Name': 'Medications', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Healthcare', 'Name': 'Doctor Visits', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Insurance', 'Name': 'Life Insurance', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Insurance', 'Name': 'Health Insurance', 'Amount': 0, 'Priority': 'High'},
            
            {'Category': 'Savings', 'Name': 'Emergency Fund', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Savings', 'Name': 'Retirement', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Savings', 'Name': 'Investments', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Debt Payments', 'Name': 'Credit Cards', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Debt Payments', 'Name': 'Student Loans', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Debt Payments', 'Name': 'Personal Loans', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Entertainment', 'Name': 'Subscriptions', 'Amount': 0, 'Priority': 'Low'},
            {'Category': 'Entertainment', 'Name': 'Hobbies', 'Amount': 0, 'Priority': 'Low'},
            {'Category': 'Entertainment', 'Name': 'Vacations', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'Personal Care', 'Name': 'Clothing', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Personal Care', 'Name': 'Haircare', 'Amount': 0, 'Priority': 'Low'},
            {'Category': 'Personal Care', 'Name': 'Gym/Fitness', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'Education', 'Name': 'Tuition', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Education', 'Name': 'Books/Supplies', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Education', 'Name': 'Online Courses', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'Miscellaneous', 'Name': 'Gifts', 'Amount': 0, 'Priority': 'Low'},
            {'Category': 'Miscellaneous', 'Name': 'Charity', 'Amount': 0, 'Priority': 'Low'},
        ]
    
    @staticmethod
    def get_business_budget_template() -> List[Dict]:
        """Business/Company budget template"""
        return [
            {'Category': 'Personnel', 'Name': 'Salaries', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Personnel', 'Name': 'Benefits', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Personnel', 'Name': 'Training', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Personnel', 'Name': 'Recruitment', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Operations', 'Name': 'Rent/Lease', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Operations', 'Name': 'Utilities', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Operations', 'Name': 'Office Supplies', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Operations', 'Name': 'Equipment', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Technology', 'Name': 'Software Licenses', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Technology', 'Name': 'Hardware', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Technology', 'Name': 'IT Support', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Technology', 'Name': 'Cloud Services', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Marketing', 'Name': 'Digital Advertising', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Marketing', 'Name': 'Content Creation', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Marketing', 'Name': 'Events/Conferences', 'Amount': 0, 'Priority': 'Low'},
            {'Category': 'Marketing', 'Name': 'Public Relations', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'Sales', 'Name': 'Commissions', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Sales', 'Name': 'Travel', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Sales', 'Name': 'Client Entertainment', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'Professional Services', 'Name': 'Legal', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Professional Services', 'Name': 'Accounting', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Professional Services', 'Name': 'Consulting', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'Insurance', 'Name': 'Liability Insurance', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Insurance', 'Name': 'Property Insurance', 'Amount': 0, 'Priority': 'High'},
            
            {'Category': 'R&D', 'Name': 'Product Development', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'R&D', 'Name': 'Research', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'Contingency', 'Name': 'Emergency Fund', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Contingency', 'Name': 'Reserve', 'Amount': 0, 'Priority': 'Medium'},
        ]
    
    @staticmethod
    def get_project_budget_template() -> List[Dict]:
        """Project-based budget template"""
        return [
            {'Category': 'Labor', 'Name': 'Project Manager', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Labor', 'Name': 'Developers/Engineers', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Labor', 'Name': 'Designers', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Labor', 'Name': 'QA/Testing', 'Amount': 0, 'Priority': 'High'},
            
            {'Category': 'Materials', 'Name': 'Raw Materials', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Materials', 'Name': 'Equipment', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Materials', 'Name': 'Consumables', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Software/Tools', 'Name': 'Licenses', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Software/Tools', 'Name': 'Development Tools', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Software/Tools', 'Name': 'Testing Tools', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Infrastructure', 'Name': 'Hosting', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Infrastructure', 'Name': 'Domain/SSL', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Infrastructure', 'Name': 'Storage', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Third Party Services', 'Name': 'APIs', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Third Party Services', 'Name': 'Contractors', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Training', 'Name': 'Team Training', 'Amount': 0, 'Priority': 'Low'},
            {'Category': 'Training', 'Name': 'Documentation', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Contingency', 'Name': 'Risk Reserve', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Contingency', 'Name': 'Change Requests', 'Amount': 0, 'Priority': 'Medium'},
        ]
    
    @staticmethod
    def get_event_budget_template() -> List[Dict]:
        """Event planning budget template"""
        return [
            {'Category': 'Venue', 'Name': 'Venue Rental', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Venue', 'Name': 'Setup/Breakdown', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Venue', 'Name': 'Parking', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Catering', 'Name': 'Food', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Catering', 'Name': 'Beverages', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Catering', 'Name': 'Service Staff', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Entertainment', 'Name': 'Performers', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Entertainment', 'Name': 'DJ/Music', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Decorations', 'Name': 'Flowers', 'Amount': 0, 'Priority': 'Low'},
            {'Category': 'Decorations', 'Name': 'Signage', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Decorations', 'Name': 'Table Settings', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'AV Equipment', 'Name': 'Sound System', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'AV Equipment', 'Name': 'Projection/Screens', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'AV Equipment', 'Name': 'Lighting', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Marketing', 'Name': 'Invitations', 'Amount': 0, 'Priority': 'Medium'},
            {'Category': 'Marketing', 'Name': 'Promotional Materials', 'Amount': 0, 'Priority': 'Low'},
            
            {'Category': 'Staff', 'Name': 'Event Coordinator', 'Amount': 0, 'Priority': 'High'},
            {'Category': 'Staff', 'Name': 'Security', 'Amount': 0, 'Priority': 'Medium'},
            
            {'Category': 'Contingency', 'Name': 'Emergency Fund', 'Amount': 0, 'Priority': 'High'},
        ]
    
    @staticmethod
    def get_template_by_name(template_name: str) -> Optional[List[Dict]]:
        """Get template by name"""
        templates = {
            'personal': BudgetTemplates.get_personal_budget_template,
            'business': BudgetTemplates.get_business_budget_template,
            'project': BudgetTemplates.get_project_budget_template,
            'event': BudgetTemplates.get_event_budget_template,
        }
        
        template_func = templates.get(template_name.lower())
        return template_func() if template_func else None
    
    @staticmethod
    def list_available_templates() -> Dict[str, str]:
        """List all available templates with descriptions"""
        return {
            'personal': 'Personal/Household budget with categories for daily living expenses',
            'business': 'Business/Company budget with operational and strategic categories',
            'project': 'Project-based budget for development, construction, or initiatives',
            'event': 'Event planning budget for conferences, parties, or gatherings',
        }


class QuarterlyBudget:
    """Create budgets with quarterly breakdown"""
    
    @staticmethod
    def create_quarterly_breakdown(items: List[Dict], distribution: str = 'equal') -> pd.DataFrame:
        """
        Create quarterly breakdown of budget items
        
        Args:
            items: List of budget items with Category, Name, Amount
            distribution: 'equal', 'weighted', or 'custom'
        
        Returns:
            DataFrame with Q1, Q2, Q3, Q4 columns
        """
        df = pd.DataFrame(items)
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
        
        if distribution == 'equal':
            # Equal distribution across quarters
            df['Q1'] = df['Amount'] / 4
            df['Q2'] = df['Amount'] / 4
            df['Q3'] = df['Amount'] / 4
            df['Q4'] = df['Amount'] / 4
        
        elif distribution == 'weighted':
            # Common business weighting (Q1: 20%, Q2: 25%, Q3: 25%, Q4: 30%)
            df['Q1'] = df['Amount'] * 0.20
            df['Q2'] = df['Amount'] * 0.25
            df['Q3'] = df['Amount'] * 0.25
            df['Q4'] = df['Amount'] * 0.30
        
        elif distribution == 'seasonal':
            # Seasonal weighting for retail/consumer (Q1: 15%, Q2: 20%, Q3: 25%, Q4: 40%)
            df['Q1'] = df['Amount'] * 0.15
            df['Q2'] = df['Amount'] * 0.20
            df['Q3'] = df['Amount'] * 0.25
            df['Q4'] = df['Amount'] * 0.40
        
        else:
            # Default to equal
            df['Q1'] = df['Amount'] / 4
            df['Q2'] = df['Amount'] / 4
            df['Q3'] = df['Amount'] / 4
            df['Q4'] = df['Amount'] / 4
        
        # Calculate total
        df['Total'] = df['Amount']
        
        return df


class BudgetAnalyzer:
    """Analyze and provide insights on budget"""
    
    @staticmethod
    def analyze_budget(df: pd.DataFrame) -> Dict:
        """Comprehensive budget analysis"""
        total = df['Amount'].sum()
        
        # Category analysis
        category_totals = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
        category_percentages = (category_totals / total * 100).round(2)
        
        # Priority analysis
        if 'Priority' in df.columns:
            priority_totals = df.groupby('Priority')['Amount'].sum()
            priority_percentages = (priority_totals / total * 100).round(2)
        else:
            priority_totals = pd.Series()
            priority_percentages = pd.Series()
        
        # Top expenses
        top_5_expenses = df.nlargest(5, 'Amount')[['Name', 'Category', 'Amount']]
        
        analysis = {
            'total_budget': total,
            'total_items': len(df),
            'total_categories': df['Category'].nunique(),
            'category_breakdown': category_totals.to_dict(),
            'category_percentages': category_percentages.to_dict(),
            'priority_breakdown': priority_totals.to_dict(),
            'priority_percentages': priority_percentages.to_dict(),
            'top_expenses': top_5_expenses.to_dict('records'),
            'average_item_cost': df['Amount'].mean(),
            'median_item_cost': df['Amount'].median(),
        }
        
        return analysis
    
    @staticmethod
    def get_recommendations(df: pd.DataFrame, budget_type: str = 'personal') -> List[str]:
        """Get budget recommendations based on best practices"""
        recommendations = []
        total = df['Amount'].sum()
        
        if budget_type == 'personal':
            # Check for emergency fund
            savings_pct = df[df['Category'].str.contains('Savings', case=False, na=False)]['Amount'].sum() / total * 100
            if savings_pct < 10:
                recommendations.append("⚠️ Consider allocating at least 10-20% to savings and emergency funds")
            
            # Check for debt payments
            debt_pct = df[df['Category'].str.contains('Debt', case=False, na=False)]['Amount'].sum() / total * 100
            if debt_pct > 30:
                recommendations.append("⚠️ Debt payments exceed 30% - consider debt consolidation strategies")
            
            # Check housing costs
            housing_pct = df[df['Category'].str.contains('Housing', case=False, na=False)]['Amount'].sum() / total * 100
            if housing_pct > 35:
                recommendations.append("⚠️ Housing costs exceed 35% - this may limit financial flexibility")
        
        elif budget_type == 'business':
            # Check personnel costs
            personnel_pct = df[df['Category'].str.contains('Personnel', case=False, na=False)]['Amount'].sum() / total * 100
            if personnel_pct > 70:
                recommendations.append("⚠️ Personnel costs exceed 70% - ensure adequate budget for growth")
            
            # Check contingency
            contingency_pct = df[df['Category'].str.contains('Contingency', case=False, na=False)]['Amount'].sum() / total * 100
            if contingency_pct < 5:
                recommendations.append("⚠️ Consider allocating 5-10% for contingency/emergency funds")
        
        # General recommendations
        category_counts = df.groupby('Category')['Amount'].count()
        if category_counts.max() > 10:
            recommendations.append("💡 Some categories have many items - consider subcategorizing for better tracking")
        
        if len(recommendations) == 0:
            recommendations.append("✅ Budget allocation looks balanced!")
        
        return recommendations


class BudgetComparison:
    """Compare budgets and track changes"""
    
    @staticmethod
    def compare_budgets(old_df: pd.DataFrame, new_df: pd.DataFrame) -> pd.DataFrame:
        """Compare two budget versions"""
        # Merge on Category and Name
        comparison = old_df.merge(
            new_df,
            on=['Category', 'Name'],
            how='outer',
            suffixes=('_Old', '_New')
        )
        
        # Fill NaN with 0
        comparison['Amount_Old'] = comparison['Amount_Old'].fillna(0)
        comparison['Amount_New'] = comparison['Amount_New'].fillna(0)
        
        # Calculate change
        comparison['Change'] = comparison['Amount_New'] - comparison['Amount_Old']
        comparison['Change_Pct'] = ((comparison['Amount_New'] - comparison['Amount_Old']) / 
                                    comparison['Amount_Old'].replace(0, 1) * 100).round(2)
        
        return comparison
    
    @staticmethod
    def import_budget_from_csv(file_path: str) -> Optional[pd.DataFrame]:
        """Import budget from CSV file"""
        try:
            df = pd.read_csv(file_path)
            required_cols = ['Category', 'Name', 'Amount']
            
            # Check for required columns
            if not all(col in df.columns for col in required_cols):
                print(f"Error: CSV must contain columns: {required_cols}")
                return None
            
            return df
        except Exception as e:
            print(f"Error importing CSV: {str(e)}")
            return None
