import streamlit as st

st.title("Streamlit 예제")
st.write("안녕하세요, Streamlit!")

if st.button('Say hello'):
    st.write('Hello!')
    
age = st.slider('Your age', 0, 100, 25)
st.write("Your age is", age)
