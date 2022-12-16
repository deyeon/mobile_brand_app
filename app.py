import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app
from app_search import run_search_app


def main():

    st.title('월드 베스트 휴대폰 판매 분석앱!')

    menu = ['Home','EDA','SERCH']
    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == 'Home':
        run_home_app()
    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'SERCH':
        run_search_app()

if __name__ == '__main__':
    main()