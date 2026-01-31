# 파일명 : mat_app.py

# 라이브러리 import
import streamlit as st
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 출력 테스트
# st.title("Matplotlib 튜토리얼")
# 실행 : streamlit run mat_app.py -> 이메일 작성하라고 나옴 -> 그냥 엥ㄴ터
# 크롬에 Matplotlib 튜토리얼이라고 적인 사이트 하나 나옴.


# ======================================== 
# 1. 한글 폰트 설정하기
# ======================================== 


# matplotlib의 전역 설정(rcParams)에서 기본 글꼴(font.family)을 설정
# → 모든 matplotlib/seaborn 그래프에서 'Malgun Gothic' 폰트를 기본으로 사용
plt.rcParams['font.family'] = 'Malgun Gothic'

# matplotlib에서 음수 기호(-)를 유니코드 문자 대신 ASCII '-'로 출력
# → 한글 폰트 사용 시 음수 부호가 깨지는 문제 방지
plt.rcParams['axes.unicode_minus'] = False

# seaborn의 테마(theme)를 설정하는 함수 (sns.set()의 최신 대체)
sns.set_theme(
    # 어두운 격자 배경 (데이터 분석용으로 가장 많이 사용)
    style='darkgrid',
    # seaborn 내부에서 matplotlib rcParams를 추가/덮어쓰기
    # axes.unicode_minus=False를 다시 지정하여
    # seaborn + matplotlib 환경 모두에서 음수 기호 깨짐 방지
    rc={'axes.unicode_minus': False}
)


# ======================================== 
# 2. 페이지 설정
# ======================================== 


# Streamlit 앱의 기본 페이지 설정을 지정하는 함수
st.set_page_config(
    # 브라우저 탭(tab)에 표시될 페이지 제목
    page_title='Matplotlib & Seaborn 튜토리얼',
    
    # 페이지 레이아웃 설정
    # 'wide' : 화면 전체 폭을 사용 (대시보드, 시각화에 적합)
    # 'centered' : 가운데 정렬된 기본 레이아웃
    layout='wide'
)

# Streamlit 페이지 상단에 가장 큰 제목(h1 수준)을 출력
# → 웹 페이지의 메인 타이틀 역할
st.title("Matplotlib & Seaborn 튜토리얼")


# ======================================== 
# 3. 데이터셋 불러오기
# ======================================== 

# seaborn 라이브러리에 내장된 'tips' 데이터셋을 불러오기
tips = sns.load_dataset('tips')

# 데이터 미리보기
# Streamlit 페이지에 소제목(subheader)을 출력
# → title보다 작은 제목(h2~h3 수준)
st.subheader("데이터셋 미리보기")

# pandas DataFrame을 Streamlit의 인터랙티브 테이블로 출력
# tips.head() : 데이터프레임의 상위 5개 행을 반환
# → 스크롤, 열 정렬, 열 너비 조절 가능
st.dataframe(tips.head())


# 기본 막대 그래프 (matplotlib + seaborn 조합)
# → Streamlit에서 시각화를 보여주기 위한 코드 블록

# Streamlit 페이지에 섹션 제목(subheader) 출력
# → 여러 그래프 중 "1번 그래프"임을 명확히 구분
st.subheader("1. 기본 막대 그래프")

# matplotlib는 객체 지향(Object-Oriented) 방식으로 그래프를 그리는 것이 권장됨
# → fig : 전체 그림(캔버스)
# → ax  : 실제 그래프가 그려지는 좌표축(Axes)
# figsize=(10,6) : 그래프 크기(가로 10, 세로 6 인치)
fig, ax = plt.subplots(figsize=(10, 6))

# seaborn의 barplot 함수
# data=tips        : 사용할 pandas DataFrame
# x='day'          : x축에 요일 변수
# y='total_bill'   : y축에 평균 계산 대상 변수
# ax=ax            : matplotlib의 Axes 객체 위에 그래프를 그림
# → seaborn은 내부적으로 평균값(mean)을 계산하여 막대 그래프를 생성
sns.barplot(
    data=tips,
    x='day',
    y='total_bill',
    ax=ax
)

# matplotlib Axes 객체의 제목 설정
# → 해당 그래프 하나에 대한 제목
ax.set_title(
    "요일별 평균 지불 금액",
    fontname="Malgun Gothic" # 표 위에 네모만 뜰 경우 작성
)


# Streamlit에 matplotlib Figure 객체를 출력
# → Jupyter의 plt.show() 역할
st.pyplot(fig)

# 산점도
st.subheader("2. 산점도")
fig1, ax1 = plt.subplots(figsize=(7,5))

sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='day',
    size='size',
    ax=ax1
)

st.pyplot(fig1)

# 히트맵
st.subheader('3. 히트맵')

# 요일과 시간별 평균 팁 계산
pivot_df = tips.pivot_table(values = 'tip', index='day', columns='time', aggfunc='mean')
fig2, ax2 = plt.subplots(figsize = (7,5))
sns.heatmap(pivot_df, annot=True, fmt='.2f', ax=ax2)
st.pyplot(fig2)

# 회귀선이 있는 산점도
st.subheader('4. 회귀선이 있는 산점도')
fig3, ax3 = plt.subplots(figsize = (7,5))
sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'alpha' : 0.5}, ax=ax3)
st.pyplot(fig3, use_container_width=True)