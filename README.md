# Expense Tracker System

A menu-driven **Expense Tracker System built with Python** that allows users to record expenses, analyze spending patterns, generate reports, visualize financial data, manage savings, and export expense records to Excel.

The project uses Pandas and NumPy for data analysis, Matplotlib and Seaborn for visualization, and CSV files for persistent expense storage.

## Features

### 1. Add Expense
- Record expense date, amount, category, and description.
- Validate expense amounts and user inputs.
- Save expense records to `expense.csv`.
- Support eight expense categories.

### 2. Expense Summary
- Calculate total expenses.
- Calculate average expenses.
- Find maximum and minimum expenses.

### 3. Filter Expenses
Filter expense records by:
- Date
- Category
- Amount

### 4. Generate Expense Report
- Display total, average, maximum, and minimum expenses.
- Display the total number of records.
- Group expenses by category.
- Group expenses by date.

### 5. NumPy Analysis
- Calculate average spending.
- Calculate total expenses.
- Calculate percentage spending by category.

### 6. Pandas Analysis
- Group expenses by category.
- Group expenses by month.
- Find the highest-spending category.
- Identify the highest-spending month.

### 7. Data Visualization

**Matplotlib**
- Bar Chart: Compare total expenses by category.
- Line Graph: Analyze spending trends over time.
- Pie Chart: Visualize category-wise spending percentages.
- Histogram: Understand the distribution of expense amounts.

**Seaborn**
- Bar Plot: Visualize expenses by category.
- Line Plot: Analyze spending trends.
- Box Plot: Compare expense distributions across categories.

### 8. View All Expenses
Display all recorded expenses in a tabular format.

### 9. Savings Management
- Add money to savings.
- Display the current savings balance.

*Note: Savings are currently stored in memory and reset when the application restarts.*

### 10. Export to Excel
- Export the latest expense records to `latest_expense.xlsx`.
- Open the exported file using Microsoft Excel.
- Update the exported file whenever new expense records are added and the export option is selected.

## Expense Categories

- Education
- Transport
- Utilities
- Entertainment
- Shopping
- Health
- Household
- Food

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data handling and analysis |
| NumPy | Numerical calculations |
| Matplotlib | Charts and graphs |
| Seaborn | Statistical visualizations |
| OpenPyXL | Excel file export |
| CSV | Expense data storage |
| Datetime | Date processing |
| OS | File existence and path handling |

## Project Structure

```text
Expense-Tracker/
│
├── main.py
├── expense.csv
├── latest_expense.xlsx
└── README.md
```

The Excel file is generated when the export option is used. The CSV file is created automatically if it does not already exist.

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Folder

```bash
cd Expense-Tracker
```

### Step 3: Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

### Step 4: Run the Application

```bash
python main.py
```

## How to Use

1. Run the Python application.
2. Select an option from the main menu.
3. Add expenses with the required details.
4. View summaries, filter records, and generate reports.
5. Analyze spending using NumPy and Pandas.
6. Generate charts using Matplotlib or Seaborn.
7. Add savings and check the current savings balance.
8. Select **Download the Expense File** to create `latest_expense.xlsx`.
9. Select **Exit** to terminate the program.

## Data Storage

Expense records are stored in `expense.csv`.

Example:

```csv
date,amount,category,description
2026-07-05,150.0,food,Lunch
2026-07-06,500.0,education,Course Fees
2026-07-07,100.0,transport,Bus Fare
```

The Excel export creates a separate file named `latest_expense.xlsx`. Exporting again replaces the existing exported file with the current in-memory expense records.

## Learning Outcomes

This project demonstrates practical knowledge of:

- Object-oriented programming and Python classes
- Functions and exception handling
- CSV and Excel file handling
- Pandas DataFrames and data aggregation
- NumPy numerical operations
- Data filtering and grouping
- Data visualization with Matplotlib and Seaborn
- Building menu-driven applications

## Future Improvements

- Add monthly budgets and budget alerts.
- Save savings records permanently.
- Add monthly and yearly spending comparisons.
- Generate downloadable reports in PDF format.
- Add a graphical user interface.
- Improve input validation and error handling.
- Add expense editing and deletion features.

## Author

**Nidhesh Dubedi**

GitHub: [Nidhesh-Dubedi](https://github.com/Nidhesh-Dubedi)

## License

This project is intended for educational and learning purposes. You may extend its features and adapt it for personal expense management.
