import streamlit as st

# Title and Header
st.title("Retail Business Dashboard")
st.header("Manager Input Section")


# Instruction

st.title("Please enter the monthly sales target and select the region")

# Number input for sales target
target = st.number_input("Enter Monthly Sales Target(in USD):",
                      min_value=0,
                      max_value=50000,
                      value=1000)


# Dropdown for region selection

region = st.selectbox("Select Region:",
                      ["North","South","East","West"])

# Submit button
if st.button("Submit"):
    # Display entered values
    st.write(f"The sales target is {target}, The selected region is {region}")


    # Success message

st.success("Dashboard updated successfully!")

    # Extra message for ambitious target


