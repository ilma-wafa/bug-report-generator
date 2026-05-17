import streamlit as st
import datetime

st.title("Bug Report Generator")
st.subheader("Fill in the details below to generate a professional bug report")

st.divider()

title = st.text_input("Bug Title")
bug_type = st.selectbox("Bug Type", ["logic", "runtime", "syntax", "ui", "performance"])
severity = st.selectbox("Severity", ["low", "medium", "high", "critical"])
steps = st.text_area("Steps to Reproduce")
expected = st.text_area("Expected Behavior")
actual = st.text_area("Actual Behavior")

if st.button("Generate Report"):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    report = f"""
========================================
         BUG REPORT
========================================
Title:     {title}
Type:      {bug_type}
Severity:  {severity}
Date:      {date}
----------------------------------------
Steps to Reproduce:
  {steps}

Expected Behavior:
  {expected}

Actual Behavior:
  {actual}
========================================
"""
    st.code(report)
    
    st.download_button(
        label="Download Report",
        data=report,
        file_name=f"bug_report_{title.replace(' ', '_')}.txt",
        mime="text/plain"
    )