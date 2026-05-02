
import streamlit as st
import datetime
import random

# Page configuration
st.set_page_config(
    page_title="ICICI Bank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for realistic styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        max-width: 480px;
        margin: 0 auto;
    }
    .header {
        background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
        padding: 25px 20px 35px 20px;
        border-radius: 0 0 25px 25px;
        margin: -70px -20px 20px -20px;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
    }
    .logo-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }
    .logo {
        color: white;
        font-size: 28px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    .notification-icon {
        color: white;
        font-size: 22px;
        cursor: pointer;
    }
    .greeting {
        color: rgba(255, 255, 255, 0.9);
        font-size: 14px;
        font-weight: 400;
    }
    .tab-container {
        display: flex;
        gap: 8px;
        margin: 20px 0;
        background: white;
        padding: 6px;
        border-radius: 35px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .portfolio-card {
        background: white;
        padding: 30px 25px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #f0f0f0;
    }
    .portfolio-title {
        color: #888;
        font-size: 13px;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        font-weight: 600;
    }
    .portfolio-amount {
        font-size: 44px;
        font-weight: 700;
        color: #1a1a1a;
        margin: 12px 0;
        letter-spacing: -1px;
    }
    .portfolio-change {
        color: #10b981;
        font-size: 14px;
        font-weight: 600;
        margin: 8px 0;
    }
    .portfolio-date {
        color: #aaa;
        font-size: 12px;
        margin-top: 8px;
    }
    .action-grid {
        background: white;
        padding: 25px 20px;
        border-radius: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #f0f0f0;
    }
    .action-item {
        text-align: center;
    }
    .action-icon {
        width: 56px;
        height: 56px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        margin: 0 auto 10px auto;
        transition: transform 0.2s;
    }
    .action-icon:hover {
        transform: scale(1.05);
    }
    .action-label {
        font-weight: 600;
        color: #333;
        font-size: 12px;
        line-height: 1.3;
    }
    .action-value {
        font-weight: 700;
        color: #1a1a1a;
        font-size: 16px;
        margin-top: 5px;
    }
    .account-card {
        background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
        padding: 25px;
        border-radius: 18px;
        margin: 15px 0;
        box-shadow: 0 6px 25px rgba(255, 107, 53, 0.3);
        color: white;
        position: relative;
        overflow: hidden;
    }
    .account-card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    }
    .account-type {
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1px;
        opacity: 0.9;
        font-weight: 600;
        margin-bottom: 5px;
    }
    .account-name {
        color: rgba(255, 255, 255, 0.95);
        font-size: 13px;
        margin-bottom: 15px;
        font-weight: 500;
    }
    .account-amount {
        font-size: 32px;
        font-weight: 700;
        color: white;
        margin: 10px 0;
        letter-spacing: -0.5px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .eye-icon {
        font-size: 22px;
        cursor: pointer;
        opacity: 0.9;
    }
    .account-number {
        font-size: 13px;
        opacity: 0.85;
        margin-top: 10px;
        letter-spacing: 1px;
        font-weight: 500;
    }
    .action-button {
        background: white;
        border: none;
        padding: 14px 24px;
        border-radius: 12px;
        color: #333;
        font-weight: 600;
        margin: 8px 5px;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        transition: all 0.3s;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        font-size: 14px;
    }
    .action-button:hover {
        background: #f0f0f0;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.12);
    }
    .section-title {
        font-size: 15px;
        font-weight: 700;
        color: #1a1a1a;
        margin: 30px 0 15px 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .transaction-item {
        background: white;
        padding: 18px 20px;
        border-radius: 14px;
        margin: 10px 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        border: 1px solid #f5f5f5;
    }
    .transaction-icon {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        margin-right: 15px;
    }
    .transaction-details {
        flex: 1;
    }
    .transaction-name {
        font-weight: 600;
        color: #1a1a1a;
        font-size: 14px;
        margin-bottom: 3px;
    }
    .transaction-date {
        font-size: 12px;
        color: #999;
    }
    .transaction-amount {
        font-weight: 700;
        font-size: 16px;
        text-align: right;
    }
    .amount-credit {
        color: #10b981;
    }
    .amount-debit {
        color: #ef4444;
    }
    .stButton button {
        width: 100%;
        border-radius: 12px;
        font-weight: 600;
        font-size: 14px;
        padding: 12px;
        transition: all 0.3s;
    }
    .stButton button:hover {
        transform: translateY(-2px);
    }
    .quick-link {
        background: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        cursor: pointer;
        transition: all 0.3s;
        border: 1px solid #f5f5f5;
    }
    .quick-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .badge {
        background: #10b981;
        color: white;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# Session state for balance visibility
if 'balance_visible' not in st.session_state:
    st.session_state.balance_visible = True

def toggle_balance():
    st.session_state.balance_visible = not st.session_state.balance_visible

# Header
st.markdown("""
    <div class="header">
        <div class="logo-container">
            <div class="logo">ICICI Bank</div>
            <div class="notification-icon">🔔</div>
        </div>
        <div class="greeting">Good Evening, Anura</div>
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
balance = 542355.67
st.markdown(f"""
    <div class="portfolio-card">
        <div class="portfolio-title">Portfolio Value</div>
        <div class="portfolio-amount">₹4,82,459.67</div>
    </div>
""", unsafe_allow_html=True)



# Account Details
balance_display = f"₹{balance:,.2f}" if st.session_state.balance_visible else "••••••"

st.markdown(f"""
    <div class="account-card">
        <div class="account-type">Savings Account</div>
        <div class="account-name">Premium Salary Account</div>
        <div class="account-amount">
            {balance_display}
        </div>
        <div class="account-number">XXXX XXXX XXXX 9277</div>
    </div>
""", unsafe_allow_html=True)

# Toggle balance visibility button
if st.button("👁️ Toggle Balance Visibility", use_container_width=True):
    toggle_balance()
    st.rerun()

# Action Buttons
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("💸 Send Money", use_container_width=True):
        st.success("Opening Send Money...")
with col2:
    if st.button("📄 View Statement", use_container_width=True):
        st.success("Opening Statement...")

col3, col4 = st.columns(2)
with col3:
    if st.button("📲 Pay Bills", use_container_width=True):
        st.success("Opening Bill Payment...")
with col4:
    if st.button("🛍️ iShop", use_container_width=True):
        st.success("Opening iShop...")

# Recent Transactions
st.markdown('<div class="section-title">Recent Transactions</div>', unsafe_allow_html=True)

# Sample transactions
transactions = [
    {
        "name": "Amazon Shopping",
        "date": "Today, 2:45 PM",
        "amount": -2499.00,
        "icon": "🛒",
        "bg_color": "#fee2e2"
    },
    {
        "name": "Amazon Subscription",
        "date": "Apr 17, 2026",
        "amount": -449.00,
        "icon": "📺",
        "bg_color": "#fee2e2"
    },
    {
        "name": "Gilani Kamil",
        "date": "Apr 27, 2026",
        "amount": -500000.00,
        "icon": "🍔",
        "bg_color": "#fee2e2"
    }
]

for txn in transactions:
    amount_class = "amount-credit" if txn["amount"] > 0 else "amount-debit"
    amount_symbol = "+" if txn["amount"] > 0 else ""
    
    st.markdown(f"""
        <div class="transaction-item">
            <div style="display: flex; align-items: center; flex: 1;">
                <div class="transaction-icon" style="background: {txn['bg_color']};">
                    {txn['icon']}
                </div>
                <div class="transaction-details">
                    <div class="transaction-name">{txn['name']}</div>
                    <div class="transaction-date">{txn['date']}</div>
                </div>
            </div>
            <div class="transaction-amount {amount_class}">
                {amount_symbol}₹{abs(txn['amount']):,.2f}
            </div>
        </div>
    """, unsafe_allow_html=True)

# Quick Links Section
st.markdown('<div class="section-title">Quick Links</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class="quick-link">
            <div style="font-size: 28px; margin-bottom: 8px;">🎁</div>
            <div style="font-size: 11px; font-weight: 600; color: #333;">Offers</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="quick-link">
            <div style="font-size: 28px; margin-bottom: 8px;">💳</div>
            <div style="font-size: 11px; font-weight: 600; color: #333;">Apply Card</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="quick-link">
            <div style="font-size: 28px; margin-bottom: 8px;">💬</div>
            <div style="font-size: 11px; font-weight: 600; color: #333;">Support</div>
        </div>
    """, unsafe_allow_html=True)

# Services Banner
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 25px; border-radius: 18px; color: white; text-align: center;
                box-shadow: 0 6px 25px rgba(102, 126, 234, 0.3);">
        <div style="font-size: 24px; margin-bottom: 8px;">✨</div>
        <div style="font-weight: 700; font-size: 16px; margin-bottom: 5px;">Upgrade to Premium Plus</div>
        <div style="font-size: 13px; opacity: 0.9;">Get zero balance requirement & exclusive rewards</div>
        <div style="margin-top: 15px;">
            <span class="badge">Limited Time Offer</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer spacing
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# Footer info
st.markdown("""
    <div style='text-align: center; color: #999; font-size: 11px; padding: 20px 0;'>
        <div>ICICI Bank Ltd. | CIN: L65190GJ1994PLC021012</div>
        <div style='margin-top: 5px;'>Toll Free: 1800 200 3344 | © 2026 ICICI Bank</div>
    </div>
""", unsafe_allow_html=True)
