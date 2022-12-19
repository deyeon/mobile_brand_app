import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px



def run_chart_app():
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


    st.subheader('컬럼 별 히스토그램와 파이차트')
    st.text('가격별,평점별,브랜드별 수량 분포를 히스토그램으로 나타내었습니다.')
    status2 =st.radio('기준을 선택하세요',['가격','평점','브랜드'])
    
    if status2 == '가격' :
        st.subheader("가격별 히스토그램")
        fig1=px.histogram(df, x=df['Price'],width=700, height=600,color_discrete_sequence=["red"])
        fig1.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig1)

    elif status2 == '평점' :
        st.subheader("평점별 히스토그램")
        fig2=px.histogram(df, x=df['Rating'],width=700, height=600,color_discrete_sequence=["green"])
        fig2.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig2)
    
    elif status2 == '브랜드' :
        st.subheader("브랜드별 히스토그램")
        fig3=px.histogram(df, x=df['brand'],width=700, height=600,color_discrete_sequence=["blue"])
        fig3.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig3)

    st.subheader('컬럼 별 파이차트')
    st.text('브랜드,시리즈별 점유률을 파이차트로 나타내었습니다.')
    status3 =st.radio('기준을 선택하세요',['브랜드','시리즈'])

    if status3 == '브랜드' :
        st.subheader("브랜드별 파이차트")
        fig4 = px.pie(df,names=df['brand'].value_counts().index,values=df['brand'].value_counts())
        
        st.plotly_chart(fig4)

    elif status3 == '시리즈' :
        st.subheader("시리즈별 파이차트")
        df5=df['series']+"-"+df['brand']
        fig5 = px.pie(df,names=df5.value_counts().head(10).index,values=df['series'].value_counts().head(10))
        st.plotly_chart(fig5)