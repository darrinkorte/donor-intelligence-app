import pandas as pd
import streamlit as st

st.set_page_config(page_title="Nonprofit Donor Intelligence", layout="wide")

st.title("Nonprofit Donor Intelligence")
st.caption("Upload your donation and donor CSVs to explore insights.")

donations_file = st.file_uploader("Upload donations.csv", type=["csv"])

if donations_file:
    df = pd.read_csv(donations_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Quick Stats")
    total = df["amount"].sum()
    donors = df["donor_id"].nunique()
    gifts = len(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Raised", f"${total:,.0f}")
    col2.metric("Unique Donors", f"{donors:,}")
    col3.metric("Number of Gifts", f"{gifts:,}")
else:
    st.info("Please upload a donations.csv file to get started.")
