
import streamlit as st

st.title("TN Pension Scheme Eligibility Checker")

st.write("Check your pension scheme eligibility")

age = st.number_input("Enter your age", min_value=0, max_value=120)

status = st.selectbox(
    "Select your status",
    ["Widow", "Deserted", "Unmarried", "Other"]
)

bpl = st.checkbox("I have a BPL card")

st.write("### Pension Schemes")

schemes = [
    ["Destitute Widow Pension", 18, "Widow"],
    ["Deserted Women Pension", 30, "Deserted"],
    ["Unmarried Women Pension", 50, "Unmarried"],
    ["National Old Age Pension", 60, "Any"],
    ["National Widow Pension", 40, "Widow"]
]

if st.button("Check Eligibility"):

    found = False

    for scheme in schemes:

        name = scheme[0]
        min_age = scheme[1]
        required_status = scheme[2]

        if age >= min_age:

            if required_status == "Any" or status == required_status:

                if name == "National Old Age Pension" or name == "National Widow Pension":

                    if bpl:
                        st.success("You may qualify for " + name)
                        found = True

                else:
                    st.success("You may qualify for " + name)
                    found = True

    if not found:
        st.warning("No matching scheme found. Please check official rules.")

st.write("### Official Links")

st.markdown(
    "[Tamil Nadu CRA Website](https://www.cra.tn.gov.in/eleg_schemes.php)"
)

st.markdown(
    "[Tamil Nadu e-Sevai](https://www.tnesevai.tn.gov.in/citizen/Pages/ServiceList.aspx)"
)

st.caption("Final eligibility must be confirmed with government officials.")

