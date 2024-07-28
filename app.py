import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize the session state to store expenses
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = []

# Function to add a new expense
def add_expense():
    date = st.session_state['date']
    description = st.session_state['description']
    category = st.session_state['category']
    amount = st.session_state['amount']
    st.session_state['expenses'].append({'Date': date, 'Description': description, 'Category': category, 'Amount': amount})

# Streamlit app layout
st.title("Expense Tracker")

st.header("Add New Expense")
with st.form(key='expense_form'):
    st.date_input("Date", value=datetime.today(), key='date')
    st.text_input("Description", key='description')
    st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"], key='category')
    st.number_input("Amount", min_value=0.0, format="%.2f", key='amount')
    submit_button = st.form_submit_button(label='Add Expense', on_click=add_expense)

# Display expense list
st.header("Expense List")
if st.session_state['expenses']:
    expenses_df = pd.DataFrame(st.session_state['expenses'])
    st.dataframe(expenses_df)

    # Display summary
    st.header("Summary")
    total_expense = expenses_df['Amount'].sum()
    st.write(f"Total Expense: ${total_expense:.2f}")

    category_summary = expenses_df.groupby('Category')['Amount'].sum().reset_index()
    st.bar_chart(category_summary, x='Category', y='Amount')

else:
    st.write("No expenses added yet.")
