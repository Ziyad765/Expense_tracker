import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime, timedelta

# File to store expenses
EXPENSE_FILE = "expenses.csv"
EXPENSE_LIMIT = 500.00  # Set a fixed limit for daily expense

# Function to create a new file if it doesn't exist
def create_expense_file():
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])

# Function to add a new expense
def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()

    if not category or not amount:
        messagebox.showerror("Input Error", "Please fill out both fields!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number!")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the expense to the CSV file
    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    # Check if the expense exceeds the daily limit
    check_limits(amount)

    messagebox.showinfo("Success", f"Expense added: {category} - ₹{amount:.2f}")

# Function to check if the expense exceeds the daily limit
def check_limits(amount):
    daily_expenses = calculate_total("Today")

    if daily_expenses + amount > EXPENSE_LIMIT:
        messagebox.showwarning("Limit Exceeded", f"You have exceeded your daily limit of ₹{EXPENSE_LIMIT:.2f}!")
        messagebox.showwarning("Warning", "Please reduce your expenses!")
    else:
        total_label.config(text=f"Total Expenses Today: ₹{daily_expenses + amount:.2f}")

# Function to calculate total expenses for the selected time range
def calculate_total(time_range="Today"):
    total = 0

    if time_range == "Today":
        start_date = datetime.now().date()
        end_date = start_date
    elif time_range == "This Week":
        start_date = (datetime.now() - timedelta(days=datetime.now().weekday())).date()
        end_date = start_date + timedelta(days=6)
    elif time_range == "This Month":
        start_date = datetime.now().replace(day=1).date()
        end_date = datetime.now().replace(day=28).date() + timedelta(days=4)  # To ensure it covers the entire month
        end_date = end_date.replace(day=1) - timedelta(days=1)

    # Calculate total within the selected date range
    with open(EXPENSE_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            expense_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").date()
            if start_date <= expense_date <= end_date:
                total += float(row[2])

    return total

# Function to show total expenses for Today, This Week, and This Month
def show_total_expenses():
    total_today = calculate_total("Today")
    total_week = calculate_total("This Week")
    total_month = calculate_total("This Month")

    # Display the total expenses in a message box or in the label
    expenses_list.delete(1.0, tk.END)  # Clear the listbox before displaying new data
    expenses_list.insert(tk.END, f"Total Expenses for Today: ₹{total_today:.2f}\n")
    expenses_list.insert(tk.END, f"Total Expenses for This Week: ₹{total_week:.2f}\n")
    expenses_list.insert(tk.END, f"Total Expenses for This Month: ₹{total_month:.2f}\n")

# Function to view expenses based on time range
def view_expenses():
    time_range = time_range_var.get()
    expenses_list.delete(1.0, tk.END)  # Clear the listbox before displaying new data

    if time_range == "Today":
        start_date = datetime.now().date()
        end_date = start_date
    elif time_range == "This Week":
        start_date = (datetime.now() - timedelta(days=datetime.now().weekday())).date()
        end_date = start_date + timedelta(days=6)
    elif time_range == "This Month":
        start_date = datetime.now().replace(day=1).date()
        end_date = datetime.now().replace(day=28).date() + timedelta(days=4)  # To ensure it covers the entire month
        end_date = end_date.replace(day=1) - timedelta(days=1)

    # Show expenses in the selected date range
    with open(EXPENSE_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            expense_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").date()
            if start_date <= expense_date <= end_date:
                expenses_list.insert(tk.END, f"{row[0]} | {row[1]} | ₹{float(row[2]):.2f}\n")

# GUI Setup
root = tk.Tk()
root.title("Let's Track - Daily Expense Tracker")

# Create file if it doesn't exist
create_expense_file()

# Set window size
root.geometry("800x750")
root.config(bg="#F0F0F0")  # Soft pastel gray background

# Header Label
header_label = tk.Label(root, text="Let's Track Your Expenses", font=("Helvetica", 18), bg="#F0F0F0", fg="#4CAF50")
header_label.pack(pady=20)

# Category Input
category_label = tk.Label(root, text="Category:", font=("Helvetica", 14), bg="#F0F0F0", fg="#555555")
category_label.pack(pady=5)
category_entry = tk.Entry(root, font=("Helvetica", 14))
category_entry.pack(pady=5)

# Amount Input
amount_label = tk.Label(root, text="Amount (₹):", font=("Helvetica", 14), bg="#F0F0F0", fg="#555555")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root, font=("Helvetica", 14))
amount_entry.pack(pady=5)

# Expense Limit Input (Fixed)
limit_label = tk.Label(root, text=f"Set Limit: ₹{EXPENSE_LIMIT:.2f}", font=("Helvetica", 14), bg="#F0F0F0", fg="#555555")
limit_label.pack(pady=10)

# Add Expense Button
add_button = tk.Button(root, text="Add Expense", font=("Helvetica", 14), bg="#FFABAB", fg="black", command=add_expense, relief="raised")
add_button.pack(pady=20)

# Time Range Dropdown
time_range_var = tk.StringVar(value="Today")
time_range_menu = tk.OptionMenu(root, time_range_var, "Today", "This Week", "This Month")
time_range_menu.config(font=("Helvetica", 12), width=20, relief="solid")
time_range_menu.pack(pady=10)

# View Expenses Button
view_button = tk.Button(root, text="View Expenses", width=20, font=("Helvetica", 14), bg="#D1C4E9", fg="black", command=view_expenses, relief="raised")
view_button.pack(pady=10)

# Show Total Expenses Button
show_total_button = tk.Button(root, text="Show Total Expenses", width=20, font=("Helvetica", 14), bg="#A8E6CF", fg="black", command=show_total_expenses, relief="raised")
show_total_button.pack(pady=10)

# Total Label
# total_label = tk.Label(root, text="Total Expenses: ₹0.00", font=("Helvetica", 16), bg="#F0F0F0", fg="#A8E6CF")
# total_label.pack(pady=10)

# Text Area to Display Expenses
expenses_list = tk.Text(root, width=60, height=10, font=("Helvetica", 12), bd=2, relief="solid", wrap="word")
expenses_list.pack(pady=20)

# Start the GUI event loop
root.mainloop()
