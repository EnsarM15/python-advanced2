import streamlit as st

def main():
    st.title("hello world")

    st.button("click me")
st.checkbox("check me")

if st.checkbox("nil baba"):
    st.write("qiky tekst shfaqet blaa bla")

name = st.text_input("enter your name")
st.write("YOUR name is :", name)

age = st.number_input("mosha",min_value=0,max_value=100)
st.write("mosha:", age)

message = st.text_area("enter a message")

if st.button("success"):
    st.success("op was succ")

if st.button("click"):
    st.write("button clicked")

if __name__  == "__main__":
    main()