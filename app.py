
import streamlit as st

st.set_page_config(page_title="TN Pension Scheme Checker")

st.title("Tamil Nadu Pension Scheme Eligibility Checker")
st.write("Enter your details to check possible pension schemes.")

# Applicant details
name = st.text_input("Applicant Name")
age = st.number_input("Age", min_value=0, max_value=120, value=18)
gender = st.selectbox("Gender", ["Female", "Male", "Other"])

status = st.selectbox(
    "Marital Status",
    ["Unmarried", "Married", "Widow", "Deserted", "Legally Separated"]
)

destitute = st.checkbox("Are you destitute / without sufficient support?")
bpl = st.checkbox("Do you have a BPL (Below Poverty Line) card?")
property = st.number_input(
    "Total fixed property value (₹)",
    min_value=0,
    value=0,
    step=10000
)

deserted_years = st.number_input(
    "Years since deserted (if applicable)",
    min_value=0,
    value=0
)

legal_document = st.checkbox(
    "Do you have the required legal document?"
)

disability = st.checkbox("Are you a person with a disability?")
disability_percent = st.number_input(
    "Disability percentage",
    min_value=0,
    max_value=100,
    value=0
)

employment = st.selectbox(
    "Employment Status",
    ["Unemployed", "Private / Self-employed", "Government employed"]
)

monthly_income = st.number_input(
    "Monthly income (₹)",
    min_value=0,
    value=0,
    step=1000
)

# Check button
if st.button("Check Eligible Schemes"):

    schemes = []

    if (
        gender == "Female"
        and status == "Widow"
        and age >= 18
        and destitute
        and property <= 100000
    ):
        schemes.append("Destitute Widow Pension Scheme")

    if (
        gender == "Female"
        and status in ["Deserted", "Legally Separated"]
        and age >= 30
        and destitute
        and deserted_years >= 5
        and legal_document
        and property <= 100000
    ):
        schemes.append("Destitute / Deserted Wives Pension Scheme")

    if (
        gender == "Female"
        and status == "Unmarried"
        and age >= 50
        and destitute
        and property <= 100000
    ):
        schemes.append("Pension for Poor Unmarried Women")

    if age >= 60 and destitute and bpl:
        schemes.append("Indira Gandhi National Old Age Pension Scheme")

    if (
        age >= 18
        and disability
        and disability_percent >= 40
        and (
            employment == "Unemployed"
            or (
                employment == "Private / Self-employed"
                and monthly_income * 12 <= 300000
            )
        )
    ):
        schemes.append("Differently Abled Pension Scheme")

    st.subheader("Result")

    if schemes:
        st.success("Possible matching schemes found!")

        for scheme in schemes:
            st.markdown("### ✅ " + scheme)

        st.info(
            "This is a preliminary check only. "
            "The government department must confirm final eligibility."
        )

    else:
        st.warning(
            "No schemes matched the details entered. "
            "Check your details or contact e-Sevai for guidance."
        )

st.divider()

st.subheader("Official Links")

st.markdown(
    "[Tamil Nadu Pension Eligibility Details](https://www.cra.tn.gov.in/eleg_schemes.php)"
)

st.markdown(
    "[Tamil Nadu Pension Portal](https://oap.tn.gov.in/)"
)

st.markdown(
    "[Tamil Nadu e-Sevai](https://www.tnesevai.tn.gov.in/)"
)

