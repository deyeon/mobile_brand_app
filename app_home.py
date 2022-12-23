import streamlit as st
import pandas as pd
import numpy as np

df=pd.read_csv('data/Amazon_top5_mobilephones.csv')
df=df.dropna(axis=0)
Rating_split=df['Rating'].str.split(" out of 5 stars")
df['Rating']=Rating_split.str.get(0)
df["Rating"] = pd.to_numeric(df["Rating"])
df['ReviewCount']=df['ReviewCount'].str.replace(",","")
df['ReviewCount']=df['ReviewCount'].replace('No reviews',np.NaN)
df=df.dropna(axis=0)
df["ReviewCount"] = pd.to_numeric(df["ReviewCount"])
df.rename(columns = {'Description':'product name'},inplace=True)
brand_and_product=df['product name'].str.split(" ")
df['brand']=brand_and_product.str.get(0)
df['brand']=df['brand'].str.replace('SAMSUNG','Samsung')
df['brand']=df['brand'].str.replace('vivo','Vivo')
df['brand']=df['brand'].str.replace('OPPO','Oppo')
df['series']=brand_and_product.str.get(1)


def run_home_app():
    st.markdown('월드 베스트 휴대폰 판매 분석앱!')

    st.markdown('아마존 닷컴에서 판매하는 상위 5위에 안에 든 휴대폰에 대한 가격과 평점 리뷰수에 대한 데이터 입니다.')
    st.markdown('휴대폰 최대/최소 데이터로 가격,평점,리뷰수 기준으로 어떤 휴대폰을 합리적인 가격으로 살수 있는지 알수 있습니다.')
    st.markdown('휴대폰 데이터를 가격,평점,리뷰수별로 plotly차트를 활용하여 시각적인 효과를 높였습니다.')
    st.markdown('휴대폰 데이터를 검색하여 검색한 휴대폰의 데이터와 url주소를 알수 있습니다.')

    st.image('https://cdn.pixabay.com/photo/2016/11/10/16/03/android-1814556_960_720.jpg')

    st.dataframe(df.head(5))
    st.text('Price(단위 cent (￠))')