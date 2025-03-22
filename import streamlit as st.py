import streamlit as st

st.title('Welcome to Loan Assessment')

# 模拟输入字段
emp_length = st.selectbox('Employment Length', ['< 1 year', '1 year', '2 years', '3 years', '4 years', '5 years', '6 years', '7 years', '8 years', '9 years', '10+ years'])
int_rate = st.slider('Loan Interest Rate', 5, 40, 10, 1)
annual_inc = st.text_input('Annual Income', placeholder="in '000$")
fico_range_high = st.slider('FICO Upper Boundary', 600, 800, 780, 50)
loan_amt = st.text_input('Loan Amount')

# 模拟按钮和输出
if st.button('Assess'):
    prediction = "Approved"  # 模拟预测结果
    st.write(f"Prediction: {prediction}")