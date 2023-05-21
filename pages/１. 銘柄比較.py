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


# side __________________________________________

st.sidebar.write("""
## 銘柄比較
こちらは銘柄比較ツールです。以下のオプションから表示日数を指定できます。
""")

st.sidebar.write("""
___
""")

days = st.sidebar.slider('Option. 表示日数を選択', 1, 50, 25)

st.sidebar.write("""
___
""")

# body __________________________________________

st.write("""
#### 複数銘柄を選択
""")

@st.cache
def get_data(days, tickers):
    horizonData = pd.DataFrame()
    for company in tickers.keys():
        try:
            tkr = yf.Ticker(tickers[company])
            hist = tkr.history(period=f'{days}d')
            hist.index = hist.index.strftime('%d %B %Y')
            hist = hist[['Close']]
            hist.columns = [company]
            hist = hist.T
            hist.index.name = 'Name'
            horizonData = pd.concat([horizonData, hist])
        except Exception:
            pass
    return horizonData

try:
    ymin, ymax = st.sidebar.slider(
        'Option. グラフのy軸の最大値を変更',
        0, 20000, (0, 5000)
    )

    filename = 'brand.csv'
    df = pd.read_csv(filename, encoding='shift-jis')

    tickers = {}
    names = df['銘柄名']
    i = 0
    for name in names:
        code = df[df['銘柄名']==name]['コード'][i]
        stockCode = str(code) + '.T'
        ticker = {
            name: stockCode
        }
        tickers.update(ticker)
        i += 1

    horizonData = get_data(days, tickers)

    companies = st.multiselect(
        '銘柄の選択をお願いします。',
        list(horizonData.index),
        ['九電工', 'きんでん', '関電工']
    )

    if not companies:
        st.error('1社以上の選択をお願いします。')
    else:
        selectData = horizonData.loc[companies]
        st.write("#### 各銘柄の株価を確認", selectData.sort_index())
        verticalData = selectData.T.reset_index()
        verticalData = pd.melt(verticalData, id_vars=['Date']).rename(
            columns={'Date': '日付', 'Name': '銘柄', 'value': '株価（円）'}
        )
        chart = (
            alt.Chart(verticalData)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="日付:T",
                y=alt.Y("株価（円）:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color="銘柄:N"
            )
        )

        st.altair_chart(chart, use_container_width=True)
except:
    st.error(
        "申し訳ございません、何かエラーが起きているようです。"
    )