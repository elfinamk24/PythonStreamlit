import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price App Lite Version

Microsoft stock closing price and column yeay!

""")

#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2012-1-1', end='2021-1-25')

#show data
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
