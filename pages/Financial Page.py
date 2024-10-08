import streamlit as st
import yfinance as yf


st.title('Простое финансовое приложение')


tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1y', start='2010-5-31', end='2022-5-31')
st.write("""
## Окончательная цена акций *Apple*
""")
st.line_chart(tickerDf.Close)
st.write("""
## Общее количество акций *Apple*
""")

st.line_chart(tickerDf.Volume)