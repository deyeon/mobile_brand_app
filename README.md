
# mobile_brand_app
# 설명!

- 아마존 닷컴에서 판매하는 상위 5위에 안에 든 휴대폰에 대한 가격과 평점 리뷰수에 대한 데이터 입니다.😉👍
- 휴대폰 최대/최소 데이터로 가격,평점,리뷰수 기준으로 어떤 휴대폰을 합리적인 가격으로 살수 있는지 알수 있습니다.
- 휴대폰 데이터를 가격,평점,리뷰수별로 plotly차트를 활용하여 시각적인 효과를 높였습니다.
- 휴대폰 데이터를 검색하여 검색한 휴대폰의 데이터와 url주소를 알수 있습니다.

# 진행과정

## 1. jupyter notebook에서 진행한 내용

  - csv형식의 데이터를 jupyter notebook으로 불러 작업하였습니다.
  - 데이터를 가공하는 과정에서 desription컬럼에 몰려있던 브랜드와 명칭을 split함수를 이용하여 분리하여 각각 컬럼으로 저
    장하였습니다.
  - 데이터의 상관분석과 차트를 만들어 진행하였습니다. 

## 2. visual studio code 에서 작업

  - visual studio code에서 작업하여 streamlit라이브러리로 웹대시보드를 로컬에서 생성하여 작업하였습니다.
  - 데이터를 설명하는 과정에서 최대/최소 상품별로 각각 이미지를 삽입하여 어떤 휴대폰인지 한눈에 알수 있게 하였습니다.
  - 기존 plt차트에서 발전된 plotly차트를 사용하여 사용하는 유저가 차트에 데이터를 마우스만 올리면 볼 수 있게 하였습니다.
  - 상관분석을 통해 각 컬럼간에 데이터는 어떤 상관관계가 있는지 분석해보았고 분석 결과 상관관계가 높지 않아서 인공지능은 사용하지 않았습니다.
  - 마지막으로 휴대폰을 검색하는 과정에서 검색한 데이터의 휴대폰 명칭과 url을 표시하여 데이터와 url를 한눈에 확인할 수 있게 하였습니다.

## 3. github에서 작업 
  
   - visual studio code에서 작업한 내용을 githubdesktop를 이용해 push하여 github레포지토리로 보냈습니다.
   - github 레포지토리를 ec2에 clone하여 서버에서 웹대시보드를 실행하게 하였습니다. 
   - github Actions 기능을 이용하여 visual studio code에서 작업한 내용을 ec2서버에 바로 pull되어 수정사항을
     서버에 실시간으로 보낼수 있게 하였습니다.


## 4. aws ec2에서 작업

  - aws에서 ec2를 생성하여 프리 티어 서버를 생성하였습니다.
  - 터미널 플랫폼 putty로 ec2에 접속하여 원격으로 작업하여 파이썬 환경을 구축하여 streamlit를 서버에서도 실행할 수 있게 하였습니다.
  - Ec2 서버에서 서버 연결이 끊겨도 접속이 가능하게 하였습니다.


## 문제해결
  - 웹대시보드에서 차트 부분에 영어로된 컬럼의 기준을 선택할때 한글로 선택할 수 있게 하였습니다. 
  - pie차트를 표시하는 과정에서 series컬럼에 어떤 브랜드인지 표시가 누락되어 있어 brand 컬럼과 series 컬럼을 합쳐 표시 되게 하여 
    해결하였습니다.



# 스크린샷!

![image](https://user-images.githubusercontent.com/120348521/208591410-05d24c65-133c-46c9-9270-b22d16bebf6a.png)

![image](https://user-images.githubusercontent.com/120348521/208591508-1931d8ef-f3c9-408b-a208-a09170677d97.png)

![image](https://user-images.githubusercontent.com/120348521/208591578-31be9953-0077-4041-a34e-2fbba607ddb3.png)

![image](https://user-images.githubusercontent.com/120348521/208591633-0ec23365-95fa-4817-a454-00e0526e636f.png)

![image](https://user-images.githubusercontent.com/120348521/208591751-d2d7e2cb-3951-4ec8-b07c-892416e84bc1.png)

![image](https://user-images.githubusercontent.com/120348521/208591784-7ae4d311-fad1-4711-bb9e-bbce14f85fad.png)

![image](https://user-images.githubusercontent.com/120348521/208591819-63ba5180-aec7-4282-aaab-ad4ba256ae30.png)



# 데이터 레퍼런스

https://www.kaggle.com/datasets/shreyamishra0307/top-5-mobile-brands-amazon-dataset
