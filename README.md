# Budget Automation System

A comprehensive budget creation and approval system with automated workflow integration.

## 📋 Overview

This system consists of three main components:
1. **Budget Creation** (`budget_automation.py`) - Create and save budgets
2. **Budget Approval** (`budget_approval.py`) - Process and approve budgets
3. **Workflow Integration** (`run_workflow.py`) - Complete end-to-end process

## 🚀 Features

### Budget Creation (`budget_automation.py`)
- ✅ Multi-currency support (IDR, USD, EUR, JPY)
- ✅ Input validation and error handling
- ✅ Automatic percentage calculations
- ✅ CSV export with timestamps
- ✅ Direct integration with approval system
- ✅ Enhanced user interface

### Budget Approval (`budget_approval.py`)
- ✅ Automated rule-based approval
- ✅ Manual override capabilities
- ✅ Comprehensive analysis and reporting
- ✅ Approval logging and audit trail
- ✅ Category and item validation
- ✅ Configurable approval rules

### Integration Features
- ✅ Seamless connection between creation and approval
- ✅ Automatic file handling
- ✅ Error handling and graceful degradation
- ✅ Complete workflow management

## 🛠️ Installation

1. Ensure you have Python 3.6+ installed
2. Install required dependencies:
```bash
pip install pandas
```

## 📝 Usage

### Option 1: Complete Workflow (Recommended)
```bash
python run_workflow.py
```
This runs the complete process from budget creation to approval.

### Option 2: Individual Components

#### Create Budget Only
```bash
python budget_automation.py
```

#### Approve Existing Budget
```bash
python budget_approval.py
```

## 📁 File Structure

```
Budget_Automation/
├── budget_automation.py    # Budget creation system
├── budget_approval.py      # Budget approval system  
├── run_workflow.py         # Complete workflow integration
├── main.py                # Legacy budget creation (original)
├── README.md              # This documentation
└── output/                # Generated files
    ├── *.csv             # Budget files
    ├── approval_log.json # Approval history
    └── approval_report_*.txt # Detailed reports
```

## ⚙️ Configuration

### Approval Rules (in `budget_approval.py`)
- **Maximum total amount**: 1,000,000
- **Maximum category percentage**: 50%
- **Maximum item percentage**: 30%
- **Required categories**: Emergency Fund, Savings
- **Minimum emergency fund**: 10%

To modify these rules, edit the `approval_rules` dictionary in the `BudgetApprovalSystem` class.

## 🔄 Workflow

1. **Budget Creation**
   - Input currency and budget items
   - Automatic validation and calculations
   - Save to CSV with timestamp
   - Optional immediate approval

2. **Budget Approval**
   - Load budget from CSV
   - Apply approval rules
   - Generate analysis report
   - Manual override if needed
   - Log decision and create reports

## 📊 Generated Reports

- **CSV Files**: Budget data with categories, amounts, and percentages
- **Approval Log**: JSON file with complete approval history
- **Analysis Reports**: Detailed text reports with recommendations

## 🔧 Improvements Made

### Fixed Inconsistencies:
- ✅ Removed redundant 'Total Amount' column
- ✅ Added proper error handling
- ✅ Enhanced input validation
- ✅ Improved user experience
- ✅ Added integration between systems
- ✅ Consistent file naming with timestamps

### Enhanced Features:
- ✅ Modular design with proper imports
- ✅ Graceful degradation if approval system unavailable
- ✅ Better visual formatting
- ✅ Complete workflow integration
- ✅ Comprehensive documentation

## 🤝 Contributing

Feel free to customize the approval rules, add new currencies, or enhance the reporting features based on your needs.

## 📞 Support

For issues or questions, review the error messages and logs in the output directory.
