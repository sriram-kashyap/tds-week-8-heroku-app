import streamlit as st
st.write(
  '''
  #Add 2 Numbers
  '''
)
st.header("User Input Parameters")

st.write("Enter the values for the two numbers and press Enter to apply")

num1 = st.number_input("NUM1", min_value = -9999999999, max_value=9999999999, key="num1")
num2 = st.number_input("NUM1", min_value = -9999999999, max_value=9999999999, key="num2")
answer = num1+num2

st.write("{} + {} = {}".format(num1, num2, answer))
