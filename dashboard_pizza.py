import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sales Registration and Dashboard")

st.write("Enter the sales values below:")

sales_jan = st.number_input("Sales in January", min_value=0.0, step=100.0)
sales_feb = st.number_input("Sales in February", min_value=0.0, step=100.0)
sales_mar = st.number_input("Sales in March", min_value=0.0, step=100.0)
sales_apr = st.number_input("Sales in April", min_value=0.0, step=100.0)
sales_may = st.number_input("Sales in May", min_value=0.0, step=100.0)

if st.button("Charts"):
    st.write("### Sales Dashboard")

    data = {
        "Month": ["January", "February", "March", "April", "May"],
        "Sales": [sales_jan, sales_feb, sales_mar, sales_apr, sales_may]
    }
    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'red', 'purple', 'orange'])
    ax.set_title("Monthly Sales Pie Chart")

    st.pyplot(fig)