import json

import pandas as pd
import streamlit as st

code = st.text_input('Введите код доступа')
if code != st.secrets['auth']['password']:
    st.warning('Неверный код. Доступ запрещён.')
    st.stop()
    
st.success("Доступ разрешён!")

json_file_name = 'smartlab-stats.json'
with open(json_file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

st.title('Tickers corporate financial data explorer')

st.subheader('Выберите тикер:')
selected_key = st.selectbox('Тикеры', list(data.keys()))

if selected_key:
    ticker_stats = pd.DataFrame.from_dict(data[selected_key], orient='index')
    ticker_stats.columns = ticker_stats.loc['year']
    ticker_stats.drop('year', inplace=True)
    st.write(f'Выбранный тикер: {selected_key}')
    st.dataframe(ticker_stats)