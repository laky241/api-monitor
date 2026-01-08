import streamlit as st
from pathlib import Path

LOG_FILE = Path("logs/monitor.log")

st.set_page_config(page_title="API Monitor", layout="wide")
st.title("📡 API Monitoring Dashboard")

st.caption("Lightweight API uptime & latency monitoring tool")

if not LOG_FILE.exists():
    st.warning("No logs found. Start the monitor first.")
    st.stop()

st.subheader("Recent Activity")

with open(LOG_FILE, "r") as f:
    lines = f.readlines()

last_lines = lines[-20:]

for line in last_lines:
    if "ALERT" in line:
        st.error(line.strip())
    else:
        st.text(line.strip())

st.info("Metrics are collected by a background monitoring process.")
