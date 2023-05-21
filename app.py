from unicodedata import name
import pandas as pd
import time
import yfinance as yf
import altair as alt
import streamlit as st
# import matplotlib.pyplot as plt
# import japanize_matplotlib
import mplfinance as mpf
import warnings
from datetime import date, datetime

st.title("企業価値トレンドアプリ")

st.write("""
    ___
    企業価値トレンド可視化ツールです！\n
    企業価値の向上を重視した経営を図るための指標を提供します。
    ___
""")

filename = 'brand.csv'
df = pd.read_csv(filename, encoding='shift-jis')


st.write("""
### アプリの説明
""")
st.write("""
- 銘柄比較：複数銘柄の比較にお役立て頂けます。
- 銘柄分析：株価変動の分析にお役立て頂けます。
""")

st.write("""
### 日経225銘柄一覧\n
- 九電工：1959｜プライム（内国株式）
""")
st.dataframe(df, 800, 500)