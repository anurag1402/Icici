import streamlit as st
import datetime

# Page configuration
st.set_page_config(
    page_title="ICICI BANK",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stApp {
        max-width: 480px;
        margin: 0 auto;
    }
    .header {
        background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
        padding: 30px 20px;
        border-radius: 0 0 20px 20px;
        margin: -70px -20px 20px -20px;
    }
    .logo {
        color: white;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .tab-container {
        display: flex;
        gap: 10px;
        margin: 20px 0;
    }
    .tab {
        flex: 1;
        padding: 15px;
        border-radius: 30px;
        text-align: center;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }
    .tab-active {
        background-color: #8b3a3a;
        color: white;
    }
    .tab-inactive {
        background-color: white;
        color: #666;
    }
    .portfolio-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .portfolio-title {
        color: #666;
        font-size: 14px;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .portfolio-amount {
        font-size: 42px;
        font-weight: bold;
        color: #333;
        margin: 10px 0;
    }
    .portfolio-date {
        color: #999;
        font-size: 13px;
    }
    .action-grid {
        background: #fff9f5;
        padding: 20px;
        border-radius: 20px;
        margin: 20px 0;
    }
    .action-item {
        display: flex;
        align-items: center;
        padding: 15px;
        gap: 15px;
    }
    .action-icon {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }
    .action-label {
        font-weight: 600;
        color: #333;
    }
    .account-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .account-name {
        color: #666;
        font-size: 14px;
        margin-bottom: 8px;
    }
    .account-amount {
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }
    .action-button {
        background: white;
        border: 2px solid #f7931e;
        padding: 15px 30px;
        border-radius: 30px;
        color: #f7931e;
        font-weight: 600;
        margin: 10px 5px;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 10px;
        transition: all 0.3s;
    }
    .action-button:hover {
        background: #f7931e;
        color: white;
    }
    .section-title {
        font-size: 16px;
        font-weight: 600;
        color: #333;
        margin: 30px 0 15px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header">
        <div class="logo">🏦 iBank</div>
    </div>
""", unsafe_allow_html=True)

# Tabs
col1, col2 = st.columns(2)
with col1:
    what_i_have = st.button("WHAT I HAVE", use_container_width=True, type="primary")
with col2:
    what_i_owe = st.button("WHAT I OWE", use_container_width=True)

# Portfolio Value Section
current_time = datetime.datetime.now().strftime("%b %d, %Y %H:%M IST")
st.markdown(f"""
    <div class="portfolio-card">
        <div class="portfolio-title">Portfolio Value</div>
        <div class="portfolio-amount">₹5,07,619.18</div>
        <div class="portfolio-date">(As of {current_time})</div>
    </div>
""", unsafe_allow_html=True)

# Quick Actions
st.markdown("""
    <div class="action-grid">
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; text-align: center;">
            <div>
                <div class="action-icon" style="margin: 0 auto; background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);">
                    💰
                </div>
                <div style="margin-top: 10px; font-weight: 600; font-size: 12px;">ACCOUNTS</div>
                <div style="font-weight: bold; color: #333; margin-top: 5px;">₹23,619.18</div>
            </div>
            <div>
                <div class="action-icon" style="margin: 0 auto; background: #e0e0e0; color: #999;">
                    📥
                </div>
                <div style="margin-top: 10px; font-weight: 600; font-size: 12px; color: #999;">START<br/>DEPOSIT</div>
            </div>
            <div>
                <div class="action-icon" style="margin: 0 auto; background: #e0e0e0; color: #999;">
                    📈
                </div>
                <div style="margin-top: 10px; font-weight: 600; font-size: 12px; color: #999;">START<br/>INVESTMENTS</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Account Details
st.markdown("""
    <div class="account-card">
        <div class="account-name">ANURA..-9277</div>
        <div class="account-amount">₹23,619.18</div>
    </div>
""", unsafe_allow_html=True)

# Action Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("💸 Send Money", use_container_width=True):
        st.info("Send Money feature")
with col2:
    if st.button("📄 View Statement", use_container_width=True):
        st.info("View Statement feature")

col3, col4, col5 = st.columns([1, 2, 1])
with col4:
    if st.button("🛍️ iShop", use_container_width=True):
        st.info("iShop feature")

# Recent Transactions
st.markdown('<div class="section-title">Recent Transactions</div>', unsafe_allow_html=True)

with st.expander("View Transactions", expanded=False):
    st.info("No recent transactions to display")

# Footer spacing
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
