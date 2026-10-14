import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class ExpenseTracker:
    categories = ["education","transport","utilities","entertainment","shopping","health","household","food"]

    def __init__(self):
        if os.path.exists("expense.csv"):
            self.df = pd.read_csv("expense.csv")
            # Normalize column names to lowercase
            self.df.columns = [col.lower() for col in self.df.columns]
            # Convert 'date' column and format it back to a clean string YYYY-MM-DD
            if "date" in self.df.columns:
                self.df["date"] = pd.to_datetime(self.df["date"], errors="coerce").dt.strftime('%Y-%m-%d')
        else:
            self.df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            self.df.to_csv("expense.csv", index=False)

        self.savings = 0.0
        print("===========================================")
        print("WELCOME TO THE EXPENSE TRACKER SYSTEM....")
        print("===========================================")


    def add_expense(self):
            try:
                user_date = input("Enter the Expense Date (dd/mm/yyyy): ")
                ex_date = datetime.datetime.strptime(user_date, "%d/%m/%Y").date()

                amount = float(input("Enter your Amount here: "))
                if amount <= 0:
                    print("Please Enter a positive number greater than 0")
                    return

                print("Choose Your Expense category:")
                print("1. education")
                print("2. transport")
                print("3. utilities")
                print("4. entertainment")
                print("5. shopping")
                print("6. health")
                print("7. household")
                print("8. food")

                cat_choice = int(input("Enter category number: "))
                if cat_choice == 1:
                    category = "education"
                elif cat_choice == 2:
                    category = "transport"
                elif cat_choice == 3:
                    category = "utilities"
                elif cat_choice == 4:
                    category = "entertainment"
                elif cat_choice == 5:
                    category = "shopping"
                elif cat_choice == 6:
                    category = "health"
                elif cat_choice == 7:
                    category = "household"
                elif cat_choice == 8:
                    category = "food"
                else:
                    print("Invalid choice! Please select a valid number.")
                    return

                description = input("Give a proper Description (max 30 characters): ")
                if len(description) > 30:
                    print("Description too long! Must be within 30 characters.")
                    return

                new_entry = pd.DataFrame({
                    "date": [ex_date.strftime("%Y-%m-%d")],
                    "amount": [amount],
                    "category": [category],
                    "description": [description]
                })
                self.df = pd.concat([self.df, new_entry], ignore_index=True)
                self.df.to_csv("expense.csv", index=False)
                print("Expense Added Successfully!")

            except ValueError:
                print("Invalid input format! Please check your entries.")
            except Exception as e:
                print(f"Error adding expense: {e}")


    def get_summary(self):
        print("\n===== Summary =====")
        print(f"Total Expense: {self.df['amount'].sum():.2f}")
        print(f"Average Expense: {self.df['amount'].mean():.2f}")
        print(f"Maximum Expense: {self.df['amount'].max():.2f}")
        print(f"Minimum Expense: {self.df['amount'].min():.2f}")

    def filter_exp(self):
        """Filter expenses by date, category, or amount."""
        choice = input("Filter by (date/category/amount): ").lower()

        try:
            if choice == "date":
                dt = input("Enter date (dd/mm/yyyy): ")
                # Convert directly to Pandas Timestamp
                dt_ob = pd.to_datetime(dt, format="%d/%m/%Y")
                result = self.df[self.df["date"] == dt_ob]
                if result.empty:
                    print("No expenses found for that date.")
                else:
                    print("\n--- Expenses on", dt, "---")
                    print(result.to_string(index=False))

            elif choice == "category":
                cat = input("Enter category: ").lower()
                # Normalize categories to lowercase
                self.df["category"] = self.df["category"].str.lower()
                result = self.df[self.df["category"] == cat]
                if result.empty:
                    print("No expenses found for that category.")
                else:
                    print(f"\n--- Expenses in category: {cat} ---")
                    print(result.to_string(index=False))

            elif choice == "amount":
                amt = float(input("Enter amount: "))
                result = self.df[self.df["amount"] == amt]
                if result.empty:
                    print("No expenses found for that amount.")
                else:
                    print(f"\n--- Expenses with amount: {amt} ---")
                    print(result.to_string(index=False))

            else:
                print("Please choose only date, category, or amount.")

        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error filtering expenses: {e}")


    def generate_report(self):
        if self.df.empty:
            print("No expenses recorded yet!")
            return

        print("\n===== Expense Report =====")
        print(f"Total Expenses: {self.df['amount'].sum():.2f}")
        print(f"Average Expense: {self.df['amount'].mean():.2f}")
        print(f"Maximum Expense: {self.df['amount'].max():.2f}")
        print(f"Minimum Expense: {self.df['amount'].min():.2f}")
        print(f"Number of Records: {len(self.df)}")

        print("\n--- Expense by Category ---")
        print(self.df.groupby("category")["amount"].sum().sort_values(ascending=False))

        print("\n--- Expense by Date ---")
        print(self.df.groupby("date")["amount"].sum().sort_index())

        print("==========================\n")

    def Num_pan_Analysis(self):
        print("--------------------------------------------")
        print("Welcome to the Numpy and Pandas Analysis: ")
        print("---------------------------------------------")
        choice = input("Enter a tool for Analysis (Numpy/Pandas): ").lower()
        if choice == "numpy":
          while True:
            print("-------------------------------------")
            print("Numpy Analysis.....")
            print("-------------------------------------")
            
            print(""" 
                    What you want to Analyze 
                    1. Average Spending
                    2. Total Expense
                    3. Percentage Spending by category
                    4. Main Menu """)
            try:
                user = int(input("Enter your choice: "))
            except ValueError:
                print("Enter a Valid Input")
                return

            if user == 1:
                print(f"Average Spending: {np.mean(self.df['amount']):.2f}")
            elif user == 2:
                print(f"Total Expense: {np.sum(self.df['amount']):.2f}")
            elif user == 3:
                print("\n--- Expense by Category (Percentage) ---")
                print(self.df.groupby("category")["amount"].sum() / self.df["amount"].sum() * 100)
            elif user == 4:
                print("Returning to Main Menu...")
                return
            else:
                print("Invalid choice!")


        elif choice == "pandas":
         while True:
            print("-------------------------------------")
            print("Welcome to the Pandas Analysis: ")
            print("-------------------------------------")
            user = int(input("""What you want to do: 
                        
                        1. Group by Category
                        2. Group by Month
                        3. Top Spending Category
                        4. Top Spending period
                        5. Main menu...."""))
            if user == 1:
                    print("\n--- Expense by Category ---")
                    print(self.df.groupby("category")["amount"].sum())
            elif user == 2:
                print("\n--- Expense by Month ---")
                print(self.df.groupby(self.df['date'].dt.strftime("%B"))["amount"].sum())
            elif user == 3:
                print("\n--- Top Spending Category ---")
                # Top Spending Category
                top_category = self.df.groupby("category")["amount"].sum().idxmax()
                top_category_amount = self.df.groupby("category")["amount"].sum().max()
                print(f"\nTop Spending Category: {top_category} ({top_category_amount:.2f})")
            elif user == 4:
                # Top Spending Period (Month)
                top_month = self.df.groupby(self.df["date"].dt.strftime("%B"))["amount"].sum().idxmax()
                top_month_amount = self.df.groupby(self.df["date"].dt.strftime("%B"))["amount"].sum().max()
                print(f"Top Spending Period: {top_month} ({top_month_amount:.2f})")
            elif user == 5:
                print("Return to the Main Menu...")
                return

    def Visualization(self):
        print("---------------------------------------")
        print("Welcome to the Visualization Part....")
        print("----------------------------------------")
        print("""
              From which one you want to going Forward:.
              1. Matplotlib
              2. Seaborn
              3. Main Menu
            """)
        option = int(input("Enter your choice here: "))
        if option == 1:
            while True:  
                print("-------------------------------")
                print("Visualization using Matplotlib")
                print("-------------------------------")
                print("""
                        1. Bar Chart
                        2. Line Graph
                        3. Pie Chart
                        4. Histogram 
                        5. Main Menu....
                        """)
            

                user = int(input("Enter your choice here: "))
                df = self.df.copy()
                df["date"] = pd.to_datetime(df["date"], errors="coerce")
                df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
                df = df.dropna(subset=["date", "amount"])

                if df.empty:
                    print("No valid expense data available.")
                    continue

                colors = [
                    "#800080", "#9370DB", "#8A2BE2", "#BA55D3",
                    "#D8BFD8", "#DA70D6", "#E6E6FA", "#C71585"
                ]

                # Apply global themes
                plt.style.use("seaborn-v0_8-darkgrid")   # Matplotlib theme


                if user == 1:
                    totals = df.groupby("category")["amount"].sum()

                    plt.figure(figsize=(10, 6))
                    plt.bar(
                        totals.index,
                        totals.values,
                        color=colors[:len(totals)]
                    )
                    plt.title("Total Expense by Category")
                    plt.xlabel("Category")
                    plt.ylabel("Amount (₹)")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()

                elif user == 2:
                    df = df.sort_values("date")

                    plt.figure(figsize=(10, 6))
                    plt.plot(
                        df["date"],
                        df["amount"],
                        color="#8A2BE2",
                        linestyle="--",
                        linewidth=2,
                        marker="*"
                    )
                    plt.title("Spending Trends Over Time")
                    plt.xlabel("Date")
                    plt.ylabel("Amount (₹)")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()

                elif user == 3:
                    totals = df.groupby("category")["amount"].sum()

                    plt.figure(figsize=(8, 8))
                    plt.pie(
                        totals,
                        labels=totals.index,
                        colors=colors[:len(totals)],
                        autopct="%1.1f%%",
                        startangle=140
                    )
                    plt.title("Expense Distribution by Category")
                    plt.tight_layout()
                    plt.show()

                elif user == 4:
                    plt.figure(figsize=(9, 6))
                    plt.hist(
                        df["amount"],
                        bins=6,
                        color="#9370DB",
                        edgecolor="black"
                    )
                    plt.title("Expense Amount Distribution")
                    plt.xlabel("Amount (₹)")
                    plt.ylabel("Frequency")
                    plt.tight_layout()
                    plt.show()
        if option == 2:
          if self.df.empty:
                print("No data available for visualization.")
                return
          while True:
                print("-------------------------------")
                print("Visualization using Seaborn")
                print("-------------------------------")
                print("""
                        1. Category-wise Bar Plot
                        2. Spending Trend Line Plot
                        3. Box Plot of Amounts
                        4. Main Menu....  """)
                
                user = int(input("Enter your choice here: "))
                sns.set_theme(style="whitegrid", palette="muted")  # Seaborn theme
                if user == 1:
                    plt.figure(figsize=(10, 6))
                    sns.barplot(
                        data=self.df,
                        x="category",
                        y="amount",
                        color="#9370DB",
                        errorbar=None
                    )
                    plt.title("Expense by Category")
                    plt.xlabel("Category")
                    plt.ylabel("Amount (₹)")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()

                elif user == 2:
                    df = self.df.sort_values("date")

                    plt.figure(figsize=(10, 6))
                    sns.lineplot(
                        data=df,
                        x="date",
                        y="amount",
                        marker="o",
                        color="purple"
                    )
                    plt.title("Spending Trend Over Time")
                    plt.xlabel("Date")
                    plt.ylabel("Amount (₹)")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()
                    
                elif user == 3:
                    plt.figure(figsize=(10, 6))
                    sns.boxplot(
                        data=self.df,
                        x="category",
                        y="amount",
                        color="#D8BFD8"
                    )
                    plt.title("Expense Amounts by Category")
                    plt.xlabel("Category")
                    plt.ylabel("Amount (₹)")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()

                elif user == 4:
                    print("Going to the main menu...")
                    return
        elif option == 3:
                print("Going to the main menu...")
                return
        else:
                print("Enter the valid option....")

    def get_all_expenses(self):
        """Display all recorded expenses."""
        try:
            if self.df.empty:
                print("No expenses recorded yet!")
                return
            print("\n===== All Expenses =====")
            print(self.df.to_string(index=False))  # shows the full DataFrame neatly
            print("========================\n")
        except Exception as e:
            print(f"Error displaying expenses: {e}")

    def add_savings(self):
        """Add money to savings."""
        try:
            amount = float(input("Enter the amount you want to save: "))
            if amount <= 0:
                print("Please enter a positive number greater than 0")
                return
            self.savings += amount
            print(f"Savings updated successfully! Current savings: {self.savings:.2f}")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except Exception as e:
            print(f"Error adding savings: {e}")

    def show_savings(self):
        """Display current savings amount."""
        print(f"Your current savings amount is: {self.savings:.2f}")

    def download_excel(self):
        if self.df.empty:
            print("No expense data available to export.")
            return

        self.df.to_excel("latest_expense.xlsx", index=False)
        print("Excel file created successfully: latest_expense.xlsx")
        print("File location:", os.path.abspath("latest_expense.xlsx"))


def main_menu():
    """Main interactive menu for the Expense Tracker."""
    tracker = ExpenseTracker()
    while True:
        try:
            print("""
            ===== Expense Tracker Menu =====
            1. Add Expense
            2. Get Summary
            3. Filter Expenses
            4. Generate Report
            5. NumPy/Pandas Analysis
            6. Visualization
            7. Show all Expenses
            8. Add Savings
            9. Show savings
            10. Download the Expense file
            11. Exit
            """)
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                tracker.add_expense()
            elif choice == 2:
                tracker.get_summary()
            elif choice == 3:
                tracker.filter_exp()
            elif choice == 4:
                tracker.generate_report()
            elif choice == 5:
                tracker.Num_pan_Analysis()
            elif choice == 6:
                tracker.Visualization()
            elif choice == 7:
                tracker.get_all_expenses()
            elif choice == 8:
                tracker.add_savings()
            elif choice == 9:
                tracker.show_savings()
            elif choice == 10:
                tracker.download_excel()
            elif choice == 11:
                print("TERMINATE THE PROGRAM.....")
                break
            else:
                print("Invalid choice, try again.")
        except ValueError as e:
            print("ERROR DETAILS:", repr(e))
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main_menu()






                    
