import streamlit as st
import pandas as pd
import plotly.express as px
from groq import Groq

# --- Config ---
st.set_page_config(page_title="AI Finance Tracker", page_icon="💸", layout="centered")
st.title("💸 AI Personal Finance Tracker")
st.caption("Upload your expense CSV → get AI-powered insights & saving tips")

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Setup")
    api_key = st.text_input("Groq API Key", type="password", placeholder="gsk_...")
    st.markdown("---")
    st.markdown("**CSV Format Expected:**")
    st.code("Date, Category, Description, Amount")
    st.download_button(
        "📥 Download Sample CSV",
        data="""Date,Category,Description,Amount
2024-01-05,Food,Groceries,1200
2024-01-08,Transport,Uber,350
2024-01-10,Entertainment,Netflix,199
2024-01-12,Food,Restaurant,850
2024-01-15,Health,Gym,1500
2024-01-18,Shopping,Clothes,2200
2024-01-20,Food,Swiggy,650
2024-01-22,Utilities,Electricity,900
2024-01-25,Transport,Metro,200
2024-01-28,Entertainment,Movie,600""",
        file_name="sample_expenses.csv",
        mime="text/csv"
    )

# --- File Upload ---
uploaded_file = st.file_uploader("Upload Expense File", type=["csv", "xlsx"])

if not uploaded_file:
    st.info("👆 Upload a CSV or Excel file to get started. Download the sample from the sidebar.")
    st.stop()

if not api_key:
    st.warning("⚠️ Enter your Groq API Key in the sidebar.")
    st.stop()

# --- Load Data ---
if uploaded_file.name.endswith(".xlsx"):
    df = pd.read_excel(uploaded_file)
else:
    df = pd.read_csv(uploaded_file)
df.columns = df.columns.str.strip()

# Flexible column mapping
col_map = {}
for col in df.columns:
    cl = col.lower().strip()
    if "amount" in cl or "price" in cl or "cost" in cl: col_map["Amount"] = col
    elif "categ" in cl or "type" in cl: col_map["Category"] = col
    elif "date" in cl: col_map["Date"] = col
    elif "desc" in cl or "note" in cl or "item" in cl: col_map["Description"] = col

if "Amount" not in col_map or "Category" not in col_map:
    st.error("❌ Could not find Amount or Category columns. Check your CSV format.")
    st.stop()

df = df.rename(columns={v: k for k, v in col_map.items()})
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df = df.dropna(subset=["Amount"])

# --- Summary ---
total = df["Amount"].sum()
avg = df["Amount"].mean()
top_cat = df.groupby("Category")["Amount"].sum().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Spent", f"₹{total:,.0f}")
col2.metric("📊 Avg per Transaction", f"₹{avg:,.0f}")
col3.metric("🔥 Top Category", top_cat)

st.divider()

# --- Charts ---
col_a, col_b = st.columns(2)

with col_a:
    cat_data = df.groupby("Category")["Amount"].sum().reset_index()
    fig1 = px.pie(cat_data, values="Amount", names="Category",
                  title="Spending by Category", hole=0.4,
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    fig2 = px.bar(cat_data.sort_values("Amount", ascending=True),
                  x="Amount", y="Category", orientation="h",
                  title="Category Breakdown", color="Amount",
                  color_continuous_scale="Blues")
    st.plotly_chart(fig2, use_container_width=True)

# --- Raw Data ---
with st.expander("📋 View Raw Data"):
    st.dataframe(df, use_container_width=True)

st.divider()

# --- AI Insights ---
st.subheader("🤖 AI Insights & Recommendations")

if st.button("✨ Generate AI Analysis", type="primary", use_container_width=True):
    summary = df.groupby("Category")["Amount"].sum().to_string()
    prompt = f"""You are a personal finance advisor. Analyze this monthly expense data:

Total Spent: ₹{total:,.0f}
Transactions: {len(df)}

Category-wise Spending:
{summary}

Give a concise analysis with:
1. 🔍 Key spending patterns (2-3 observations)
2. ⚠️ Overspending alerts (flag categories >30% of total)
3. 💡 3 actionable saving tips specific to this data
4. 🎯 A monthly savings target suggestion

Keep it friendly, practical, and under 300 words."""

    with st.spinner("Analyzing your expenses..."):
        try:
            client = Groq(api_key=api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            insight = response.choices[0].message.content
            st.markdown(insight)
        except Exception as e:
            st.error(f"❌ Groq API Error: {e}")
