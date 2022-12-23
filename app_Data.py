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
    st.text('Price= 가격,Rating= 평점,ReviewCount= 리뷰수 등의 데이터의 요약 표입니다.')
    st.text('각각 count = 총갯수,mean= 평균,std= 표준편차, min= 최소값, 25%= 4분위수의 25%값,')
    st.text('50%= 4분위수의 50%값, 75% = 4분위수의 75%값, max= 최대값을 나타냅니다.')
    st.dataframe(df.describe())

    st.subheader('최대/최소 데이터 확인하기')
    st.text('가격,평점,리뷰수 별로 최대,최소값을 사진과 데이터를 통해 볼수 있습니다.')
    status1 =st.radio('기준을 선택하세요',['가격','평점','리뷰수'])
    if status1 == '가격' :

        df_max1=df.loc[df['Price']==df['Price'].max(),]
        df_min1=df.loc[df['Price']==df['Price'].min(),]

        st.text('가격 최대 - {}'.format(df_max1['product name'].values[0]))
        st.image('https://i.expansys.net/img/b/363571/apple-iphone-13-pro-5g-dual-sim.jpg')
        st.dataframe(df_max1)
        
        st.text('가격 최대 - {}'.format(df_min1['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/517tjy9KDhL._SY445_.jpg')
        st.dataframe(df_min1)

    elif status1 == '평점' :

        df_max2=df.loc[df['Rating']==df['Rating'].max(),]
        df_min2=df.loc[df['Rating']==df['Rating'].min(),]

        st.text('평점 최대 - {}'.format(df_max2['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/51EknP3PutL._SX522_.jpg')
        st.dataframe(df_max2)
        st.text('평점 최소 - {}'.format(df_min2['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/517tjy9KDhL._SY445_.jpg')
        st.dataframe(df_min2)

    elif status1 == '리뷰수' :

        df_max3=df.loc[df['ReviewCount']==df['ReviewCount'].max(),]
        df_min3=df.loc[df['ReviewCount']==df['ReviewCount'].min(),]

        st.text('리뷰수 최대 - {}'.format(df_max3['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/716nHhG9SWL._SY445_.jpg')
        st.dataframe(df_max3)
        st.text('리뷰수 최대 - {}'.format(df_min3['product name'].values[0]))
        st.image('https://m.media-amazon.com/images/I/61vBPptSghL._SL1500_.jpg')
        st.dataframe(df_min3)
    

    
    st.subheader('상관관계 분석')
    st.text("각 컬럼간의 상관관계를 분석하였습니다.")
    st.text("컬럼을 선택하여 상관분석을 할수 있습니다.")
    
    c_list = df.columns[1:3+1]
    selected_list=st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', c_list)

    if len(selected_list) >= 2:
            df_corr=df[selected_list].corr()
            fig = plt.figure()
            sb.heatmap(data=df_corr,annot=True,fmt='.2f',cmap='coolwarm',
            vmin = -1,vmax=1,linewidths=0.5)
            st.pyplot(fig)

















