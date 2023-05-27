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


import streamlit as st
import streamlit_authenticator as stauth


def create_form():
    # 別途ログアウトボタンを実装
    if st.button("ログアウト"):
        st.session_state['authentication_status'] = None
        # 再度処理を実行する関数. これが無いと二回ボタンを押す必要がある
        st.experimental_rerun()
        login_form()
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
    
    
    
def login_form():
    # Create an empty container
    placeholder = st.empty()

    actual_ID = "kyudenko"
    actual_password = "kdk2023"

    # Insert a form in the container
    with placeholder.form("login"):
        st.markdown("#### ログイン画面")
        ID = st.text_input("ID")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit and ID == actual_ID and password == actual_password:
        placeholder.empty()
        st.session_state['authentication_status'] = 1
        create_form()
#     elif submit and email != actual_email and password != actual_password:
#         st.error("Login failed")
    else:
        pass
    
if 'authentication_status' in st.session_state and st.session_state['authentication_status'] == 1:
    create_form()
else:
    login_form()


# メソッドを使う場合
#authenticator.logout('Logout', 'sidebar')
