import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

def run_eda_app():
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


    st.subheader('데이터 요약')
    st.dataframe(df.describe())

    st.subheader('최대/최소 데이터 확인하기')
    df2=df.loc[:,['Price','Rating','ReviewCount']]
    status1 =st.radio('기준을 선택하세요',['가격','평점','리뷰수'])
    if status1 == '가격' :

        df_max1=df.loc[df['Price']==df['Price'].max(),]
        df_min1=df.loc[df['Price']==df['Price'].min(),]

        st.text('최대 데이터')
        st.dataframe(df_max1)
        st.text('최소 데이터')
        st.dataframe(df_min1)

    elif status1 == '평점' :

        df_max2=df.loc[df['Rating']==df['Rating'].max(),]
        df_min2=df.loc[df['Rating']==df['Rating'].min(),]

        st.text('최대 데이터')
        st.dataframe(df_max2)
        st.text('최소 데이터')
        st.dataframe(df_min2)

    elif status1 == '리뷰수' :

        df_max3=df.loc[df['ReviewCount']==df['ReviewCount'].max(),]
        df_min3=df.loc[df['ReviewCount']==df['ReviewCount'].min(),]

        st.text('최대 데이터')
        st.dataframe(df_max3)
        st.text('최소 데이터')
        st.dataframe(df_min3)
    



    st.subheader('컬럼 별 히스토그램와 파이차트')

    status2 =st.radio('기준을 선택하세요',['가격','평점','브랜드'])
    
    if status2 == '가격' :
        st.subheader("가격별 히스토그램")
        fig1=px.histogram(df, x=df['Price'],width=700, height=600)
        fig1.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig1)

    elif status2 == '평점' :
        st.subheader("평점별 히스토그램")
        fig2=px.histogram(df, x=df['Rating'],width=700, height=600)
        fig2.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig2)
    
    elif status2 == '브랜드' :
        st.subheader("브랜드별 히스토그램")
        fig3=px.histogram(df, x=df['brand'],width=700, height=600)
        fig3.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig3)

    st.subheader('컬럼 별 파이차트')

    status3 =st.radio('기준을 선택하세요',['브랜드','시리즈'])

    if status3 == '브랜드' :
        st.subheader("브랜드별 파이차트")
        fig4 = px.pie(df,names=df['brand'].value_counts().index,values=df['brand'].value_counts())
        
        st.plotly_chart(fig4)

    elif status3 == '시리즈' :
        st.subheader("시리즈별 파이차트")
        fig5 = px.pie(df,names=df['series'].value_counts().index,values=df['series'].value_counts())
        st.plotly_chart(fig5)
    
    
















