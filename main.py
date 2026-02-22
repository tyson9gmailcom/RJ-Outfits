import streamlit as st
import pandas as pd
import plotly.express as px

--- 1. PAGE CONFIGURATION & SEO ---

st.set_page_config(
page_title="RJ OUTFITS | Official",
page_icon="👕",
layout="wide"
)

Full Page Background Styling

st.markdown(f"""
<style>
.stApp {{
background-image: url("https://raw.githubusercontent.com/tyson9gmailcom/RJ-Outfits/main/banner.jpg");
background-attachment: fixed;
background-size: cover;
}}
/* This makes your text boxes readable over the background */
.stMarkdown, .main-header {{
background-color: rgba(255, 255, 255, 0.8);
padding: 20px;
border-radius: 15px;
color: black;
}}
</style>
""", unsafe_allow_html=True)

--- 2. DATA SYSTEM (Mock Database) ---

This is where your affiliate logins are stored

users_db = pd.DataFrame({
'ID': ['RJ001', 'RJ002'],
'Pass': ['1234', '5678'],
'Name': ['John Phiri', 'Mary Banda']
})

--- 3. DYNAMIC IMAGE STATE ---

if 'banner' not in st.session_state:
st.session_state.banner = "https://via.placeholder.com/1200x400.png?text=RJ+OUTFITS+-+STYLE+YOUR+STORY"
if 'products' not in st.session_state:
st.session_state.products = "https://via.placeholder.com/600x400.png?text=Our+Collection"

--- 4. NAVIGATION SIDEBAR ---

st.sidebar.title("👕 RJ OUTFITS MENU")
page = st.sidebar.radio("Navigate to:", ["Home & Shop", "Affiliate Portal", "RJ Office (Admin)"])

==========================================

PAGE 1: HOME & SHOP

==========================================

if page == "Home & Shop":
# Hero Section
st.image(st.session_state.banner, use_container_width=True)

col1, col2 = st.columns([1, 1.2])  
with col1:  
    st.markdown(f"""  
        <div style="background-color: #b22222; color: white; padding: 40px; border-radius: 0 50px 50px 0; margin-top: 20px;">  
            <h2 style="margin: 0;">Look Fresh!</h2>  
            <p>Premium streetwear based at Bunda Campus.</p>  
            <hr style="border: 1px solid white; opacity: 0.3;">  
            <p>✅ <b>Quality Fabrics</b></p>  
            <p>✅ <b>Fast Delivery</b></p>  
            <p>✅ <b>Latest Trends</b></p>  
            <br>  
            <a href="https://wa.me/265994377233" style="text-decoration:none;">  
                <button class="nav-btn">SHOP NOW ON WHATSAPP</button>  
            </a>  
        </div>  
    """, unsafe_allow_html=True)  

with col2:  
    st.header("Our Collection")  
    st.image(st.session_state.products, use_container_width=True)

==========================================

PAGE 2: AFFILIATE PORTAL (PRIVATE LOGIN)

==========================================

elif page == "Affiliate Portal":
st.markdown('<div class="main-header"><h1>🚀 AFFILIATE PORTAL</h1></div>', unsafe_allow_html=True)

if 'logged_in_user' not in st.session_state:  
    with st.container():  
        st.subheader("Login to your Dashboard")  
        u_id = st.text_input("Affiliate ID")  
        u_pw = st.text_input("Password", type="password")  
        if st.button("Enter Dashboard"):  
            match = users_db[(users_db['ID'] == u_id) & (users_db['Pass'] == u_pw)]  
            if not match.empty:  
                st.session_state.logged_in_user = u_id  
                st.session_state.user_name = match['Name'].values[0]  
                st.rerun()  
            else:  
                st.error("Access Denied. Check ID/Password.")  
else:  
    st.success(f"Welcome back, {st.session_state.user_name}!")  
    c1, c2, c3 = st.columns(3)  
    with c1: st.markdown('<div class="stat-card"><h5>Earned</h5><h3>K45,000</h3></div>', unsafe_allow_html=True)  
    with c2: st.markdown('<div class="stat-card"><h5>Active Days</h5><h3>18 / 30</h3></div>', unsafe_allow_html=True)  
    with c3: st.markdown('<div class="stat-card"><h5>Rate</h5><h3>3.00%</h3></div>', unsafe_allow_html=True)  
      
    if st.button("Logout"):  
        del st.session_state.logged_in_user  
        st.rerun()

==========================================

PAGE 3: RJ OFFICE (TYSON & BLESSINGS)

==========================================

elif page == "RJ Office (Admin)":
st.markdown('<div class="main-header"><h1>🔐 RJ OFFICE: MANAGEMENT</h1></div>', unsafe_allow_html=True)
admin_pw = st.sidebar.text_input("Enter Admin Password", type="password")

if admin_pw == "RJ2026":  
    st.subheader("🤝 Partnership 50/50 Split")  
    prof = 500000   
    st.info(f"Total Net Profit: K{prof:,}")  
    c1, c2 = st.columns(2)  
    c1.metric("Tyson Jere Share", f"K{prof/2:,}")  
    c2.metric("Blessings Mtegha Share", f"K{prof/2:,}")  
      
    st.subheader("🖼️ Change Display Photos")  
    banner_input = st.text_input("New Banner URL")  
    product_input = st.text_input("New Collection URL")  
    if st.button("Update Website Photos"):  
        if banner_input: st.session_state.banner = banner_input  
        if product_input: st.session_state.products = product_input  
        st.success("Website refreshed!")  
              
elif admin_pw != "":  
    st.error("Password Incorrect.")

--- 5. GLOBAL FOOTER WITH SOCIAL LINKS ---

st.markdown("""
<div class="footer-container">
<div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 20px;">
<a href="https://facebook.com" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="30" style="filter: brightness(0) invert(1);"></a>
<a href="https://instagram.com" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="30" style="filter: brightness(0) invert(1);"></a>
<a href="https://wa.me/265994377233" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="30" style="filter: brightness(0) invert(1);"></a>
</div>
<p style="margin: 0; font-size: 14px;">📍 Bunda Campus, Malawi</p>
<p style="margin: 0; font-size: 14px; opacity: 0.7;">© 2026 RJ OUTFITS | Tyson & Blessings</p>
</div>
""", unsafe_allow_html=True)
