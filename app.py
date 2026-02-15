import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import whois
import validators
import time
import plotly.graph_objects as go

st.set_page_config(page_title="PhishGuard AI", layout="wide", page_icon="🔍")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    .stTextInput > div > div > input { background-color: #1e293b; color: #38bdf8; }
    </style>
    """, unsafe_allow_html=True)

if 'scan_history' not in st.session_state:
    st.session_state.scan_history = []

st.title("🔍 PhishGuard Heuristic Scanner")
st.write("Software-Only Threat Intelligence Tool")

target_url = st.text_input("Enter URL to Analyze:", placeholder="https://example-secure-login.com")

def analyze_url(url):
    score = 0
    reasons = []
    
    if not validators.url(url):
        return None, ["Invalid URL Format"]

    if "@" in url:
        score += 30
        reasons.append("Contains '@' symbol (Common phishing tactic)")
    
    if len(url) > 75:
        score += 20
        reasons.append("URL length is excessive (>75 chars)")

    dots = url.count('.')
    if dots > 3:
        score += 20
        reasons.append(f"High subdomain count ({dots} dots detected)")

    return score, reasons

if st.button("Run Deep Scan"):
    if target_url:
        with st.spinner("Analyzing domain authority and HTML headers..."):
            score, reasons = analyze_url(target_url)
            time.sleep(1.5) # Simulate network lag
            
            if score is not None:
                st.session_state.scan_history.append({"url": target_url, "score": score})
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = score,
                        title = {'text': "Risk Score"},
                        gauge = {'axis': {'range': [0, 100]},
                                 'bar': {'color': "red" if score > 50 else "green"}}
                    ))
                    st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    st.subheader("Analysis Findings")
                    if not reasons:
                        st.success("No immediate malicious patterns detected.")
                    else:
                        for r in reasons:
                            st.warning(f"⚠️ {r}")
            else:
                st.error("Please enter a valid URL.")

st.divider()
st.subheader("Scan History")
if st.session_state.scan_history:
    st.table(pd.DataFrame(st.session_state.scan_history))
