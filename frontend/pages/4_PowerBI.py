import streamlit as st
import os
from utils.powerbi_export import export_powerbi_data

st.set_page_config(page_title="Power BI Analytics")

st.title("📊 Power BI Analytics Dashboard")

st.markdown("""
### 🔎 Why Power BI?

Power BI is used as a **visualization layer** for advanced analytics.

- It consumes exported financial data.
- It does NOT perform machine learning.
- All ML logic runs in FastAPI backend.
- Power BI is used for:
  - Monthly analytics
  - Category-wise spending analysis
  - Budget vs Actual comparison
  - Trend visualization
""")

st.divider()

# -------- EXPORT BUTTON --------
st.subheader("📤 Export Updated Dataset")

if st.button("Export Data for Power BI"):

    success = export_powerbi_data()

    if success:
        st.success("Dataset exported successfully.")
    else:
        st.warning("No expense data available to export.")

EXPORT_PATH = r"D:\SONATECH\Predictive_Financial_System\powerbi_exports\updated_financial_data.csv"

st.write("📁 Export Location:")
st.code(EXPORT_PATH)

st.divider()

# -------- POWER BI INSTRUCTIONS --------
st.subheader("🧭 How to View Power BI Dashboard")

st.markdown("""
1. Open **Power BI Desktop**.
2. Click **Get Data → CSV**.
3. Select the exported file:
   `updated_financial_data.csv`
4. Load the dataset.
5. Refresh dashboard whenever new data is exported.

Power BI acts purely as a reporting tool.
All predictive and explainable AI logic runs inside the backend.
""")

st.info(
    "⚠ Power BI does not run machine learning models. "
    "It visualizes structured financial data exported from the system."
)
