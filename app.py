import streamlit as st

# Rules last checked: October 2026. Always verify on official sites.
PROPERTY_LIMIT = 100000      # pension schemes: property limit in Rs
INCOME_LIMIT = 250000        # Magalir Urimai Thogai: family income per year in Rs


# Each function checks ONE scheme.
# It returns a list of reasons why the person is NOT eligible.
# Empty list = eligible.

def check_pudhumai_penn(p):
    problems = []
    if not p["female"]:
        problems.append("Only for girls")
    if not p["govt_school"]:
        problems.append("Must have studied Classes 6-12 in a government school")
    if not p["in_college"]:
        problems.append("Must be studying in college (UG / Diploma / ITI / Professional)")
    return problems


def check_magalir_urimai(p):
    problems = []
    if not p["female"]:
        problems.append("Only for women")
    if p["age"] < 21:
        problems.append("Age must be 21 or above")
    if p["income"] >= INCOME_LIMIT:
        problems.append("Family income must be below Rs.2,50,000 per year")
    if not p["land_ok"]:
        problems.append("Land must be within 5 acres (wet) / 10 acres (dry)")
    if not p["electricity_ok"]:
        problems.append("Electricity use must be below 3,600 units per year")
    if p["govt_or_tax"]:
        problems.append("Government employees / income tax payers are not eligible")
    if p["four_wheeler"]:
        problems.append("Families with a car / jeep / tractor are not eligible")
    if p["gets_pension"]:
        problems.append("Families already getting a pension are not eligible")
    return problems


def check_widow_pension(p):
    problems = []
    if not p["female"]:
        problems.append("Only for women")
    if p["age"] < 18:
        problems.append("Age must be 18 or above")
    if p["marital"] != "widow":
        problems.append("Must be a widow")
    if not p["destitute"]:
        problems.append("Must be destitute")
    if p["property"] > PROPERTY_LIMIT:
        problems.append("Property must be within Rs.1,00,000")
    return problems


def check_deserted_pension(p):
    problems = []
    if not p["female"]:
        problems.append("Only for women")
    if p["age"] < 30:
        problems.append("Age must be 30 or above")
    if p["marital"] != "separated":
        problems.append("Must be divorced / deserted (5+ years) / legally separated")
    if not p["destitute"]:
        problems.append("Must be destitute")
    if p["property"] > PROPERTY_LIMIT:
        problems.append("Property must be within Rs.1,00,000")
    return problems


def check_unmarried_pension(p):
    problems = []
    if not p["female"]:
        problems.append("Only for women")
    if p["age"] < 50:
        problems.append("Age must be 50 or above")
    if p["marital"] != "unmarried":
        problems.append("Must be unmarried")
    if not p["destitute"]:
        problems.append("Must be destitute")
    if p["property"] > PROPERTY_LIMIT:
        problems.append("Property must be within Rs.1,00,000")
    return problems


def check_ig_widow_pension(p):
    problems = []
    if not p["female"]:
        problems.append("Only for women")
    if p["age"] < 40:
        problems.append("Age must be 40 or above")
    if p["marital"] != "widow":
        problems.append("Must be a widow")
    if not p["bpl"]:
        problems.append("Must have a BPL card")
    if not p["destitute"]:
        problems.append("Must be destitute")
    return problems


def check_ig_old_age_pension(p):
    problems = []
    if p["age"] < 60:
        problems.append("Age must be 60 or above")
    if not p["bpl"]:
        problems.append("Must have a BPL card")
    if not p["destitute"]:
        problems.append("Must be destitute")
    return problems


# (scheme name, checking function, official link)
SCHEMES = [
    ("Pudhumai Penn (higher education support for girls)",
     check_pudhumai_penn, "https://www.tn.gov.in"),
    ("Kalaignar Magalir Urimai Thogai (monthly aid for women heads of family)",
     check_magalir_urimai, "https://kmut.tn.gov.in"),
    ("Destitute Widow Pension",
     check_widow_pension, "https://www.cra.tn.gov.in/eleg_schemes.php"),
    ("Destitute / Deserted Wives Pension",
     check_deserted_pension, "https://www.cra.tn.gov.in/eleg_schemes.php"),
    ("Unmarried Women Pension",
     check_unmarried_pension, "https://www.cra.tn.gov.in/eleg_schemes.php"),
    ("Indira Gandhi National Widow Pension",
     check_ig_widow_pension, "https://www.cra.tn.gov.in/eleg_schemes.php"),
    ("Indira Gandhi National Old Age Pension",
     check_ig_old_age_pension, "https://www.cra.tn.gov.in/eleg_schemes.php"),
]

# ---------------------------- Screen ----------------------------
st.set_page_config(page_title="TN Scheme Eligibility Checker", page_icon="✅")
st.title("TN Scheme Eligibility Checker")
st.caption("தமிழ்நாடு அரசு திட்டங்கள் - தகுதி சரிபார்ப்பு")

with st.form("my_form"):
    st.subheader("1. About you / உங்களைப் பற்றி")
    age = st.number_input("Age / வயது", min_value=1, max_value=120, value=25)
    gender = st.radio("Gender / பாலினம்", ["Female", "Male"], horizontal=True)
    marital_label = st.selectbox(
        "Marital status / திருமண நிலை",
        ["Unmarried", "Married", "Widow", "Divorced / Deserted / Legally separated"])

    st.subheader("2. Family / குடும்பம்")
    income = st.number_input("Family income per YEAR (Rs) / குடும்ப ஆண்டு வருமானம்",
                             min_value=0, value=0, step=10000)
    prop = st.number_input("Your property value (Rs) / சொத்து மதிப்பு",
                           min_value=0, value=0, step=10000)
    bpl = st.checkbox("We have a BPL card / BPL அட்டை உள்ளது")
    destitute = st.checkbox("I am destitute (no income, no family support) / ஆதரவற்றவர்")
    land_ok = st.checkbox("Land within 5 acres (wet) or 10 acres (dry) / நில வரம்புக்குள்", value=True)
    electricity_ok = st.checkbox("Electricity use below 3,600 units per year / மின் பயன்பாடு 3,600 யூனிட்டுக்குள்", value=True)
    govt_or_tax = st.checkbox("Government employee or income tax payer in family / அரசு ஊழியர் அல்லது வருமான வரி செலுத்துபவர்")
    four_wheeler = st.checkbox("Family owns car / jeep / tractor / கார், ஜீப், டிராக்டர் உள்ளது")
    gets_pension = st.checkbox("Family already gets a pension / ஏற்கனவே ஓய்வூதியம் பெறுகிறோம்")

    st.subheader("3. Education / கல்வி")
    govt_school = st.checkbox("I studied Classes 6-12 in a TN government school / அரசுப் பள்ளியில் படித்தேன்")
    in_college = st.checkbox("I am studying in college now / தற்போது கல்லூரியில் படிக்கிறேன்")

    submitted = st.form_submit_button("Check eligibility")

if submitted:
    # Convert the dropdown text into a short code
    if marital_label == "Unmarried":
        marital = "unmarried"
    elif marital_label == "Married":
        marital = "married"
    elif marital_label == "Widow":
        marital = "widow"
    else:
        marital = "separated"

    # Put all answers in one dictionary
    person = {
        "age": age,
        "female": gender == "Female",
        "marital": marital,
        "income": income,
        "property": prop,
        "bpl": bpl,
        "destitute": destitute,
        "land_ok": land_ok,
        "electricity_ok": electricity_ok,
        "govt_or_tax": govt_or_tax,
        "four_wheeler": four_wheeler,
        "gets_pension": gets_pension,
        "govt_school": govt_school,
        "in_college": in_college,
    }

    eligible_list = []
    not_eligible_list = []
    for name, check_function, link in SCHEMES:
        problems = check_function(person)
        if len(problems) == 0:
            eligible_list.append((name, link))
        else:
            not_eligible_list.append((name, problems))

    st.header("Result / முடிவு")
    if eligible_list:
        st.success(f"You may be eligible for {len(eligible_list)} scheme(s)")
        for name, link in eligible_list:
            st.markdown(f"### ✅ {name}")
            st.markdown(f"[Official site]({link})")
    else:
        st.warning("No matching scheme found for these details.")

    if not_eligible_list:
        with st.expander("Why not the other schemes? / மற்றவை ஏன் இல்லை?"):
            for name, problems in not_eligible_list:
                st.markdown(f"**{name}**")
                for reason in problems:
                    st.write("- " + reason)

    st.info("Preliminary check only. Please confirm final eligibility with the government office or tnesevai.tn.gov.in.")
