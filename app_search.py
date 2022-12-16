import streamlit as st
import pandas as pd
import numpy as np

def run_search_app():
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


    st.subheader('휴대폰을 검색해보세요')


    brand_word = st.text_input('휴대폰 이름 입력(영어로)')


    st.text(brand_word)
    
    df_brand=df[df['product name'].str.contains(brand_word,case=False)]

    if len(brand_word)!= 0:
        st.dataframe(df_brand)