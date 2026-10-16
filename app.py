
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Hotel Analytics Dashboard",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 Hotel Revenue & Occupancy Analytics")
st.write(
    "Explore hotel booking patterns, cancellations, "
    "room rates and monthly demand using real historical data."
)

@st.cache_data
def load_data():
    url = (
        "https://raw.githubusercontent.com/"
        "rfordatascience/tidytuesday/master/data/2020/"
        "2020-02-11/hotels.csv"
    )
    data = pd.read_csv(url)

    # Handle missing categorical values without removing records
    for col in ["company", "agent", "country"]:
        data[col] = data[col].fillna("Unknown")

    return data

try:
    df = load_data()
except Exception as e:
    st.error("Could not load the dataset. Please refresh and try again.")
    st.stop()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

hotel_options = ["All"] + sorted(df["hotel"].unique().tolist())
selected_hotel = st.sidebar.selectbox("Hotel Type", hotel_options)

year_options = sorted(df["arrival_date_year"].unique().tolist())
selected_years = st.sidebar.multiselect(
    "Arrival Year",
    year_options,
    default=year_options
)

filtered = df.copy()

if selected_hotel != "All":
    filtered = filtered[filtered["hotel"] == selected_hotel]

if selected_years:
    filtered = filtered[
        filtered["arrival_date_year"].isin(selected_years)
    ]
else:
    filtered = filtered.iloc[0:0]

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# KPIs
total = len(filtered)
cancelled = int(filtered["is_canceled"].sum())
cancel_rate = cancelled / total * 100
avg_rate = filtered["adr"].mean()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Booking Records", f"{total:,}")
c2.metric("Cancelled Records", f"{cancelled:,}")
c3.metric("Cancellation Rate", f"{cancel_rate:.2f}%")
c4.metric("Average Daily Rate", f"{avg_rate:.2f}")

st.caption(
    "Booking records are not necessarily unique bookings. "
    "Average daily rate is shown in the dataset's recorded units. "
    "These metrics do not represent verified actual hotel revenue "
    "or exact room occupancy."
)

# Monthly booking chart
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly = (
    filtered.groupby("arrival_date_month")
    .size()
    .reindex(month_order, fill_value=0)
    .rename_axis("Month")
    .reset_index(name="Booking Records")
)

st.subheader("Monthly Booking Records")
fig_month = px.line(
    monthly,
    x="Month",
    y="Booking Records",
    markers=True,
    category_orders={"Month": month_order},
    template="plotly_white"
)
st.plotly_chart(fig_month, use_container_width=True)

# Hotel comparison
st.subheader("Hotel Type Comparison")

hotel_summary = (
    filtered.groupby("hotel")
    .agg(
        Booking_Records=("hotel", "size"),
        Cancelled_Records=("is_canceled", "sum"),
        Average_Daily_Rate=("adr", "mean")
    )
    .reset_index()
)

hotel_summary["Cancellation_Rate"] = (
    hotel_summary["Cancelled_Records"]
    / hotel_summary["Booking_Records"] * 100
).round(2)

left, right = st.columns(2)

with left:
    fig_hotels = px.bar(
        hotel_summary,
        x="hotel",
        y="Booking_Records",
        color="hotel",
        title="Booking Records by Hotel",
        template="plotly_white"
    )
    st.plotly_chart(fig_hotels, use_container_width=True)

with right:
    fig_cancel = px.bar(
        hotel_summary,
        x="hotel",
        y="Cancellation_Rate",
        color="hotel",
        title="Cancellation Rate by Hotel (%)",
        template="plotly_white"
    )
    st.plotly_chart(fig_cancel, use_container_width=True)

# Room rate analysis
st.subheader("Average Daily Rate by Arrival Month")

rate_data = (
    filtered.groupby("arrival_date_month")["adr"]
    .mean()
    .reindex(month_order)
    .dropna()
    .rename_axis("Month")
    .reset_index(name="Average Daily Rate")
)

fig_rate = px.bar(
    rate_data,
    x="Month",
    y="Average Daily Rate",
    category_orders={"Month": month_order},
    template="plotly_white"
)
st.plotly_chart(fig_rate, use_container_width=True)

# Cancellation status
st.subheader("Booking Cancellation Status")

status_data = (
    filtered["is_canceled"]
    .map({0: "Not Cancelled", 1: "Cancelled"})
    .value_counts()
    .rename_axis("Status")
    .reset_index(name="Records")
)

fig_status = px.pie(
    status_data,
    names="Status",
    values="Records",
    hole=0.45,
    template="plotly_white"
)
st.plotly_chart(fig_status, use_container_width=True)

# Data preview
with st.expander("View dataset sample"):
    st.dataframe(filtered.head(100), use_container_width=True)

st.caption(
    "Source: Hotel Booking Demand dataset. "
    "Original publication: https://doi.org/10.1016/j.dib.2018.11.126"
)
