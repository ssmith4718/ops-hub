import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Ops & CRM Hub", layout="wide")
st.title("📊 Operations & CRM Hub")

# 2. Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Your specific database URLs
KPI_URL = "https://docs.google.com/spreadsheets/d/1KpN1zyLK4164aTuxu4O-4UOhY4fJoGy9G0g2iXz2HWI/edit?usp=drive_web"
LEADS_URL = "https://docs.google.com/spreadsheets/d/1KwDaiO_kurvvvqlTqEWVPDQt0OoIdud1dX5KvpOwxcw/edit?usp=drive_web"
TASKS_URL = "https://docs.google.com/spreadsheets/d/1UDsAIsNsXkuBNbwPllQcR-WVCyypz8QTDjl3c0F03gk/edit?usp=drive_web"

# 3. Read the Data
df_kpi = conn.read(spreadsheet=KPI_URL)
df_leads = conn.read(spreadsheet=LEADS_URL)
df_tasks = conn.read(spreadsheet=TASKS_URL)

# 4. App Layout: Mobile-friendly Tabs
tab1, tab2, tab3 = st.tabs(["KPI Dashboard", "Lead Pipeline", "Task Tracker"])

with tab1:
    st.header("Daily & Weekly Targets")
    st.dataframe(df_kpi, use_container_width=True)
    
with tab2:
    st.header("Lead Pipeline")
    status_filter = st.selectbox("Filter Leads By:", ["All", "New", "Contacted", "Meeting Booked", "Do Not Contact"])
    
    if status_filter != "All":
        df_leads = df_leads[df_leads['Status'] == status_filter]
        
    st.dataframe(df_leads, use_container_width=True)

with tab3:
    st.header("Task Management")
    st.dataframe(df_tasks, use_container_width=True)
