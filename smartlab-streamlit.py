import json

import pandas as pd
import streamlit as st

json_file_name = 'smartlab-ticker-stats.json'
with open(json_file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

st.title('Tickers corporate financial data explorer')

st.subheader('Выберите тикер:')
selected_key = st.selectbox('Тикеры', list(data.keys()))

if selected_key:
    ticker_stats = pd.DataFrame.from_dict(data[selected_key], orient='index')
    ticker_stats.columns = ticker_stats.loc['date']
    if ticker_stats.columns[-2] == ticker_stats.columns[-1]:
        ticker_stats.columns = [*ticker_stats.columns[:-1]] + [f'LTM ({ticker_stats.columns[-1]})']
    ticker_stats.drop('date', inplace=True)
    st.write(f'Выбранный тикер: {selected_key}')
    st.dataframe(ticker_stats)