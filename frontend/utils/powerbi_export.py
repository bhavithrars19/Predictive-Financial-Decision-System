import pandas as pd
import os
from utils.db import get_connection


EXPORT_PATH = r"D:\SONATECH\Predictive_Financial_System\powerbi_exports\updated_financial_data.csv"


def export_powerbi_data():

    conn = get_connection()

    # Daily expenses
    expenses = pd.read_sql_query(
        """
        SELECT user_id, expense_date, category, amount
        FROM user_expenses
        """,
        conn
    )

    # Monthly financials
    monthly = pd.read_sql_query(
        """
        SELECT user_id, month, year, income, budget
        FROM user_monthly_financials
        """,
        conn
    )

    # Category priorities
    categories = pd.read_sql_query(
        """
        SELECT user_id, category_name, priority_level
        FROM user_categories
        """,
        conn
    )

    conn.close()

    if expenses.empty:
        return False

    # Convert expense_date into month/year
    expenses["expense_date"] = pd.to_datetime(expenses["expense_date"])
    expenses["month"] = expenses["expense_date"].dt.month
    expenses["year"] = expenses["expense_date"].dt.year

    # Merge monthly data
    merged = expenses.merge(
        monthly,
        on=["user_id", "month", "year"],
        how="left"
    )

    # Merge category priority
    merged = merged.merge(
        categories,
        left_on=["user_id", "category"],
        right_on=["user_id", "category_name"],
        how="left"
    )

    # Clean columns
    final_df = merged[[
        "user_id",
        "expense_date",
        "category",
        "amount",
        "month",
        "year",
        "income",
        "budget",
        "priority_level"
    ]]

    # Ensure folder exists
    os.makedirs(os.path.dirname(EXPORT_PATH), exist_ok=True)

    final_df.to_csv(EXPORT_PATH, index=False)

    return True
