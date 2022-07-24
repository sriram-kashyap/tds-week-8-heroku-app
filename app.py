import streamlit as st
st.write(
  '''
  #Add 2 Numbers
  '''
)
st.header("User Input Parameters")


num1 = st.number_input("NUM1", min_value = -9999999999, max_value=9999999999, key="num1")
num2 = st.number_input("NUM1", min_value = -9999999999, max_value=9999999999, key="num2")
answer = num1+num2

st.write(answer)
