import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. PAGE CONFIGURATION & SEO ---
st.set_page_config(
    page_title="RJ OUTFITS | Official", 
    page_icon="👕", 
    layout="wide"
)

# Professional Styling (Red, White, Black Theme)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-header { background-color: #b22222; padding: 25px; text-align: center; color: white; border-radius: 10px; margin-bottom: 20px; }
    .footer-container { background-color: #b22222; color: white; padding: 30px; text-align: center; margin-top: 50px; border-top: 5px solid #000; }
    .stat-card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #b22222; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    .nav-btn { background-color: white; color: #b22222; border-radius: 5px; padding: 10px 20px; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA SYSTEM (Mock Database) ---
# In production, this would be replaced by: conn = st.connection("gsheets", type=GSheetsConnection)
users_db = pd.DataFrame({
    'ID': ['RJ001', 'RJ002'],
    'Pass': ['1234', '5678'],
    'Name': ['John Phiri', 'Mary Banda']
})

# --- 3. DYNAMIC IMAGE STATE ---
if 'banner' not in st.session_state:
    st.session_state.banner = "banner.jpg" # Uses uploaded file
if 'products' not in st.session_state:
    st.session_state.products = "honeycomb.png"

# --- 4. NAVIGATION SIDEBAR ---
st.sidebar.title("👕 RJ OUTFITS MENU")
page = st.sidebar.radio("Navigate to:", ["Home & Shop", "Affiliate Portal", "RJ Office (Admin)"])

# ==========================================
# PAGE 1: HOME & SHOP
# ==========================================
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

# ==========================================
# PAGE 2: AFFILIATE PORTAL (PRIVATE LOGIN)
# ==========================================
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
        # LOGGED IN DASHBOARD
        st.success(f"Welcome back, {st.session_state.user_name}!")
        
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="stat-card"><h5>Earned</h5><h3>K45,000</h3></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="stat-card"><h5>Active Days</h5><h3>18 / 30</h3></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="stat-card"><h5>Rate</h5><h3>3.00%</h3></div>', unsafe_allow_html=True)
        
        st.subheader("Daily Progress")
        chart_data = pd.DataFrame({'Day': range(1,19), 'Sales': [1500, 2000, 1800, 2200, 2500, 1900, 2100, 2400, 3000, 2800, 2600, 3100, 2900, 3500, 3200, 3400, 3600, 3300]})
        st.area_chart(chart_data.set_index('Day'), color="#b22222")
        
        if st.button("💰 REQUEST CASH OUT"):
            wa_link = f"https://wa.me/265984378233?text=Hello%20Management,%20I%20am%20{st.session_state.logged_in_user}%20requesting%20payout."
            st.markdown(f'<meta http-equiv="refresh" content="0;url={wa_link}">', unsafe_allow_html=True)
            
        if st.button("Logout"):
            del st.session_state.logged_in_user
            st.rerun()

# ==========================================
# PAGE 3: RJ OFFICE (TYSON & BLESSINGS)
# ==========================================
elif page == "RJ Office (Admin)":
    st.markdown('<div class="main-header"><h1>🔐 RJ OFFICE: MANAGEMENT</h1></div>', unsafe_allow_html=True)
    admin_pw = st.sidebar.text_input("Enter Admin Password", type="password")
    
    if admin_pw == "RJ2026":
        st.subheader("🤝 Partnership 50/50 Split")
        
        # Financial Summary
        prof = 500000 # Example
        st.info(f"Total Net Profit: K{prof:,}")
        c1, c2 = st.columns(2)
        c1.metric("Tyson Jere Share", f"K{prof/2:,}")
        c2.metric("Blessings Mtegha Share", f"K{prof/2:,}")
        
        tabs = st.tabs(["📦 Stock Control", "👥 Affiliate Troubleshooting", "🖼️ Edit Images"])
        
        with tabs[0]:
            st.table(pd.DataFrame({
                'Item': ['Plain t-shirts', 'Golf shirts', 'Slides'],
                'Stock': [50, 30, 20], 'Price': [10000, 15000, 12000]
            }))
            
        with tabs[1]:
            target = st.selectbox("View Performance of:", users_db['ID'])
            st.info(f"Viewing real-time data for {target}. (Help the affiliate with technical errors here)")
            
        with tabs[2]:
            st.subheader("Change Display Photos")
            banner_input = st.text_input("New Banner URL (Direct Link)")
            product_input = st.text_input("New Honeycomb URL (Direct Link)")
            if st.button("Update Website Photos"):
                if banner_input: st.session_state.banner = banner_input
                if product_input: st.session_state.products = product_input
                st.success("Website refreshed with new images!")
                
    elif admin_pw != "":
        st.error("Password Incorrect.")

# --- 5. GLOBAL FOOTER WITH SOCIAL LINKS ---
st.markdown("""
    <div class="footer-container">
        <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 20px;">
            <a href="https://facebook.com/rjoutfits" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="30" style="filter: brightness(0) invert(1);"></a>
            <a href="https://instagram.com/rjoutfits" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="30" style="filter: brightness(0) invert(1);"></a>
            <a href="https://twitter.com/rjoutfits" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/3256/3256013.png" width="30" style="filter: brightness(0) invert(1);"></a>
            <a href="https://wa.me/265994377233" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="30" style="filter: brightness(0) invert(1);"></a>
        </div>
        <p style="margin: 0; font-size: 14px;">📍 Bunda Campus, Near Bunda CCAP</p>
        <p style="margin: 0; font-size: 14px; opacity: 0.7;">© 2026 RJ OUTFITS | Tyson Jere & Blessings Mtegha</p>
    </div>
""", unsafe_allow_html=True)
