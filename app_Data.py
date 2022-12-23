import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

def run_data_app():
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
    st.text('Price= 가격(단위 cent (￠)),Rating= 평점,ReviewCount= 리뷰수 등의 데이터의 요약 표입니다.')
    st.dataframe(df.describe())

    df_show =df.loc[:,['product name', 'Price', 'Rating', 'ReviewCount','brand','series']]
    df_show=df_show.drop_duplicates(['product name', 'Price'])
    st.subheader('최대/최소 데이터 확인하기')
    st.text('가격,평점,리뷰수 별로 최대,최소값을 사진과 데이터를 통해 볼수 있습니다.')
    status1 =st.radio('기준을 선택하세요',['가격(단위 cent (￠))','평점(리뷰수 최소 100명대비)','리뷰수'])
    if status1 == '가격(단위 cent (￠))' :

        df_max1=df_show.sort_values(by='Price',ascending=False)
        df_min1=df_show.sort_values(by='Price')

        st.text('가격(단위 cent (￠)) 최대 - {}'.format(df_max1['product name'].values[0]))
        st.image('https://i.expansys.net/img/b/363571/apple-iphone-13-pro-5g-dual-sim.jpg')
        st.dataframe(df_max1.head(5))
        
        st.text('가격(단위 cent (￠)) 최대 - {}'.format(df_min1['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/517tjy9KDhL._SY445_.jpg')
        st.dataframe(df_min1.head(5))

    elif status1 == '평점(리뷰수 최소 100명대비)' :
        df_rmax=df_show[df_show['ReviewCount']>100]

        df_max2=df_rmax.sort_values(by='Rating',ascending=False)
        df_min2=df_rmax.sort_values(by='Rating')

        st.text('평점 최대 (리뷰수 최소 100명대비) - {}'.format(df_max2['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/31RbHXz7-fL._AC_SY1000_.jpg')
        st.dataframe(df_max2.head(5))
        st.text('평점 최소 (리뷰수 최소 100명대비)- {}'.format(df_min2['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/417iF-mQUkL._SL1024_.jpg')
        st.dataframe(df_min2.head(5))

    elif status1 == '리뷰수' :

        df_max3=df_show.sort_values(by='ReviewCount',ascending=False)
        df_min3=df_show.sort_values(by='ReviewCount')

        st.text('리뷰수 최대 - {}'.format(df_max3['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/716nHhG9SWL._SY445_.jpg')
        st.dataframe(df_max3.head(5))
        st.text('리뷰수 최대 - {}'.format(df_min3['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/61vBPptSghL._SL1500_.jpg')
        st.dataframe(df_min3.head(5))

















