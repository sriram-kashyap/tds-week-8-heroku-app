import streamlit as st
st.write(
  '''
  #Add 2 Numbers
  '''
)
st.header("User Input Parameters")

def user_input_parameters():
  num1 = st.number_input("NUM1", min_value = -9999999999, max_value=9999999999, key="num1")
  num2 = st.number_input("NUM1", min_value = -9999999999, max_value=9999999999, key="num2")

  data = {
    "NUM1" : num1,
    "NUM2" : num2
  }

  return num1, num2

num1, num2 = user_input_parameters()

answer = num1+num2

st.write(answer)
