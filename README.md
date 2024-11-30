# Let's Track - Daily Expense Tracker

## Description

"Let's Track" is a simple and user-friendly daily expense tracker application built using Python and the Tkinter library. The application allows users to input their daily expenses, categorize them, and view their spending over different time periods (Today, This Week, and This Month). It helps users stay within their daily budget limit and track their financial health effectively.

Key Features:
- Add new expenses with category and amount.
- Set a daily expense limit and get notified if you exceed it.
- View total expenses for Today, This Week, and This Month.
- Display individual expenses based on time range selection.
- Simple, clean, and responsive graphical user interface (GUI).

## Requirements

- Python 3.x
- Tkinter (Usually comes pre-installed with Python)
- `csv` module (pre-installed with Python)
- `os` module (pre-installed with Python)
- `datetime` module (pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/lets-track.git
    ```

2. Navigate to the project directory:

    ```bash
    cd lets-track
    ```

3. Ensure that you have Python 3.x installed on your system.

4. You can run the script directly using Python:

    ```bash
    python expense_tracker.py
    ```

## Features

- **Add Expense**: Input the category and amount of an expense, and add it to the tracking system.
- **View Expenses**: View expenses for Today, This Week, or This Month with detailed information.
- **Show Total Expenses**: View the total expenses for Today, This Week, or This Month, displayed in a clean format.
- **Limit Check**: Set a daily expense limit and receive notifications if you exceed the limit.

## Technologies Used

- **Python**: The core language used to develop the application.
- **Tkinter**: The GUI toolkit used to create the user interface.
- **CSV**: Used to store and retrieve expense data in a simple CSV file.
- **Datetime**: Handles date and time for calculating expenses within selected date ranges.

## Usage

- Open the application and input your expense details such as category and amount.
- The application will automatically track the total expenses for the day, week, and month.
- You can set a daily expense limit, and the app will warn you if your expenses exceed the specified limit.
- You can also view the detailed expenses for specific time ranges.

## File Structure

- `expense_tracker.py`: The main Python script that contains the logic and GUI setup for the expense tracker.
- `expenses.csv`: The file where the expenses are saved and read from (created automatically if it doesn't exist).

## License

This project is open source and available under the MIT License.

## Acknowledgments

- The Tkinter library for GUI development.
- Python's standard libraries (`csv`, `os`, and `datetime`) for managing expenses.
