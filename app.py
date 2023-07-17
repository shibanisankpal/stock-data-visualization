import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, date


def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def get_company_name(symbol):
    company = yf.Ticker(symbol)
    return company.info['longName']

def main():
    st.title("Finance Project with Streamlit")
    st.write("Welcome to our finance app!")

    # Get user inputs
    symbol = st.text_input("Enter the stock symbol (e.g., AAPL):", "AAPL")
    start_date = st.date_input("Start date:", datetime(2022, 1, 1))
    end_date = date.today()

    # Fetch and display stock data
    stock_data = get_stock_data(symbol, start_date, end_date)
    company_name = get_company_name(symbol)


    st.subheader(f"{symbol} Stock Prices from {start_date} to {end_date}")
    st.line_chart(stock_data["Adj Close"])



if __name__ == "__main__":
    main()

