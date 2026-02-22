import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. PAGE SETUP & SEO ---
st.set_page_config(
    page_title="RJ OUTFITS | Look Fresh!", 
    page_icon="👕", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for the "Look Fresh" Brand (Red/White/Black theme)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-header { background-color: #b22222; padding: 20px; text-align: center; color: white; border-radius: 10px; margin-bottom: 20px; }
    .footer-container { background-color: #b22222; color: white; padding: 30px; text-align: center; margin-top: 50px; border-top: 5px solid #000; }
    .nav-btn { background-color: #b22222; color: white; border-radius: 5px; padding: 10px 20px; border: none; font-weight: bold; }
    .stat-card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #b22222; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA LOADERS (MOCKUP - Connect to GSheets later) ---
# Default Image Links (Can be changed in RJ Office)
if 'banner_url' not in st.session_state:
    st.session_state.banner_url = "https://via.placeholder.com/1200x400.png?text=RJ+OUTFITS+-+STYLE+YOUR+STORY"
if 'honeycomb_url' not in st.session_state:
    st.session_state.honeycomb_url = "https://via.placeholder.com/600x400.png?text=Product+Collection"

# --- 3. NAVIGATION MENU ---
st.sidebar.image("https://via.placeholder.com/150.png?text=RJ+LOGO") # Replace with your logo
st.sidebar.title("MENU")
page = st.sidebar.radio("Go to:", ["Home & Products", "Affiliate Portal", "RJ Office (Admin)"])

# ==========================================
# PAGE: HOME & PRODUCTS
# ==========================================
if page == "Home & Products":
    # Hero Banner
    st.image(st.session_state.banner_url, use_container_width=True)
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown(f"""
            <div style="background-color: #b22222; color: white; padding: 40px; border-radius: 0 50px 50px 0; margin-top: 20px;">
                <h2 style="margin: 0;">Why Choose Us?</h2>
                <hr style="border: 1px solid white; opacity: 0.3;">
                <p>✅ <b>Quality Fabrics:</b> Premium streetwear only.</p>
                <p>✅ <b>Latest Trends:</b> Always fresh stock.</p>
                <p>✅ <b>Fast Delivery:</b> Straight to your door.</p>
                <br>
                <a href="https://wa.me/265994377233" style="text-decoration:none;">
                    <button style="background-color: white; color: #b22222; border: none; padding: 12px 25px; font-weight: bold; border-radius: 5px; cursor: pointer;">SHOP NOW</button>
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.header("🔥 Our Collection")
        st.image(st.session_state.honeycomb_url, use_container_width=True)

# ==========================================
# PAGE: AFFILIATE PORTAL
# ==========================================
elif page == "Affiliate Portal":
    st.markdown('<div class="main-header"><h1>🚀 AFFILIATE PERFORMANCE</h1></div>', unsafe_allow_html=True)
    
    aff_id = st.text_input("Enter your Affiliate ID:", placeholder="e.g. RJ001")
    
    if aff_id:
        st.success(f"Performance report for {aff_id}")
        
        # Dashboard Metrics
        m1, m2, m3 = st.columns(3)
        with m1: st.markdown(f'<div class="stat-card"><h5>Total Commission</h5><h3>K25,500</h3></div>', unsafe_allow_html=True)
        with m2: st.markdown(f'<div class="stat-card"><h5>Days Active</h5><h3>14 / 30</h3></div>', unsafe_allow_html=True)
        with m3: st.markdown(f'<div class="stat-card"><h5>Current Rate</h5><h3>3.00%</h3></div>', unsafe_allow_html=True)
        
        # Performance Graph
        st.subheader("Daily Earnings (Day 1 - 30)")
        chart_data = pd.DataFrame({'Day': range(1,16), 'Earnings': [1000, 1500, 1200, 2000, 1800, 2500, 2100, 1900, 2800, 2400, 3000, 2700, 2500, 3100, 2900]})
        fig = px.area(chart_data, x='Day', y='Earnings', color_discrete_sequence=['#b22222'])
        st.plotly_chart(fig, use_container_width=True)
        
        # Cash Out Logic
        st.divider()
        if st.button("💰 REQUEST CASH OUT"):
            wa_link = f"https://wa.me/265984378233?text=Hello%20Management,%20I%20am%20{aff_id}%20and%20I%20would%20like%20to%20cashout%20my%20commission."
            st.markdown(f'<meta http-equiv="refresh" content="0;url={wa_link}">', unsafe_allow_html=True)

# ==========================================
# PAGE: RJ OFFICE (TYSON & BLESSINGS)
# ==========================================
elif page == "RJ Office (Admin)":
    st.markdown('<div class="main-header"><h1>🔐 RJ OFFICE: MANAGEMENT</h1></div>', unsafe_allow_html=True)
    
    pw = st.sidebar.text_input("Admin Password", type="password")
    
    if pw == "RJ2026":
        st.subheader("🤝 Partnership Split (50/50)")
        
        # Calculations
        inv = 400000; rev = 650000; prof = rev - inv
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Investment", f"K{inv:,}")
        c2.metric("Revenue", f"K{rev:,}")
        c3.metric("Net Profit", f"K{prof:,}", delta=f"K{prof/2:,} each")
        
        tab1, tab2 = st.tabs(["📦 Inventory & Orders", "🖼️ Website Manager"])
        
        with tab1:
            st.table(pd.DataFrame({
                'Item': ['Plain t-shirts', 'Golf shirts', 'Slides', 'Cargos'],
                'Ordered': [50, 20, 30, 15],
                'Sold': [25, 10, 5, 2],
                'Remaining': [25, 10, 25, 13]
            }))
            
            st.subheader("💸 Record Partner Withdrawal")
            with st.form("withdraw"):
                who = st.selectbox("Partner", ["Tyson Jere", "Blessings Mtegha"])
                amt = st.number_input("Amount (K)", min_value=0)
                if st.form_submit_button("Log Withdrawal"):
                    st.warning(f"Recorded K{amt} for {who}")

        with tab2:
            st.subheader("Update Website Images")
            new_banner = st.text_input("New Banner URL (boy/girl group photo)")
            new_honey = st.text_input("New Product URL (honeycomb)")
            if st.button("Save New Images"):
                if new_banner: st.session_state.banner_url = new_banner
                if new_honey: st.session_state.honeycomb_url = new_honey
                st.success("Images Updated!")

    elif pw != "":
        st.error("Incorrect Password.")

# --- 4. GLOBAL FOOTER WITH SOCIAL LINKS ---
st.markdown("""
    <div class="footer-container">
        <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 20px;">
            <a href="https://facebook.com/your-page" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="30" style="filter: brightness(0) invert(1);"></a>
            <a href="https://instagram.com/your-profile" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="30" style="filter: brightness(0) invert(1);"></a>
            <a href="https://twitter.com/your-handle" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/3256/3256013.png" width="30" style="filter: brightness(0) invert(1);"></a>
            <a href="https://wa.me/265994377233" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="30" style="filter: brightness(0) invert(1);"></a>
        </div>
        <p style="margin: 0; font-size: 14px;">📍 Bunda Campus, Near Bunda CCAP</p>
        <p style="margin: 0; font-size: 14px; opacity: 0.7;">© 2026 RJ OUTFITS - Built for Growth</p>
    </div>
""", unsafe_allow_html=True)
