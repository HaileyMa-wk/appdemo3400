import streamlit as st

st.title("Welcome to Streamlit")

st.header("ISOM3400")
st.write("**Bold Text** and *Italic Text*")

age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
st.write(f"Your age is {age}")

option = st.selectbox("Choose your favorite color:",
                      ["Red", "Blue", "Green"])
st.write(f"You selected: {option}")
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

if st.button("Click Me"):
    st.session_state.click_count += 1

if st.session_state.click_count == 1:
    st.write("Button clicked!")
elif st.session_state.click_count >= 2:
    st.write("click too much!")
else:
    st.write("why you dont click???")
st.success("Operation completed successfully!")
st.write("Operation completed successfully!")
st.header("Operation completed successfully!")
