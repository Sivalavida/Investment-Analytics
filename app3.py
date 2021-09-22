import streamlit as st
import yfinance as yf
import pandas as pd

print('start')

st.title('Invest Dashboard v2')

tickers = ('TSLA', 'AAPL', 'MSFT', 'BTC-USD' )

dropdown = st.multiselect('Pick Asset : ', tickers)


start = st.date_input('Start', value=pd.to_datetime('2021-01-01'))
end = st.date_input('End', value=pd.to_datetime('today'))

def cumret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0) #first day is na
    return cumret

if len(dropdown) > 0:
    df = yf.download(dropdown, start,end)['Adj Close']
    # df
    df = cumret(df)
    # df
    st.header('Cumulative Returns of %s' % dropdown)
    st.line_chart(df)


print('done')










