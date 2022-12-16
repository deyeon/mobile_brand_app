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

    st.subheader('통계 데이터 확인')
    st.dataframe(df.head(3))

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

    st.subheader('최대/최소 데이터 확인하기')
    df2=df.loc[:,['Price','Rating','ReviewCount']]
    column_list1 = df2.columns
    select_coulmn=st.selectbox('최대 최소를 확인할 컬럼을 고르세요',column_list1)


    if select_coulmn !=0:
        df_max=df.loc[df[select_coulmn]==df[select_coulmn].max(),]
        df_min=df.loc[df[select_coulmn]==df[select_coulmn].min(),]

        st.text('최대 데이터')
        st.dataframe(df_max)
        st.text('최소 데이터')
        st.dataframe(df_min)

    st.subheader('컬럼 별 히스토그램와 파이차트')

    status1 =st.radio('기준을 선택하세요',['가격','평점','브랜드'])
    
    if status1 == '가격' :
        fig1=px.histogram(df, x=df['Price'],width=900, height=600)
        fig1.update_layout(bargap=0.2)
        st.plotly_chart(fig1)

    elif status1 == '평점' :
        fig2=px.histogram(df, x=df['Rating'],width=900, height=600)
        fig2.update_layout(bargap=0.2)
        st.plotly_chart(fig2)
    
    elif status1 == '브랜드' :
        fig3=px.histogram(df, x=df['brand'],width=900, height=600)
        fig3.update_layout(bargap=0.2)
        st.plotly_chart(fig3)

    st.subheader('컬럼 별 파이차트')

    status2 =st.radio('기준을 선택하세요',['브랜드','시리즈'])

    if status2 == '브랜드' :
        fig4 = px.pie(df,names=df['brand'].value_counts().index,values=df['brand'].value_counts())
        st.plotly_chart(fig4)

    elif status2 == '시리즈' :
        fig5 = px.pie(df,names=df['series'].value_counts().index,values=df['series'].value_counts())
        st.plotly_chart(fig5)
    
    
















