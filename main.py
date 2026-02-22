import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="RJ OUTFITS | Official", 
    page_icon="👕", 
    layout="wide"
)

# --- 2. FULL BACKGROUND & CUSTOM STYLING ---
github_url = "https://raw.githubusercontent.com/tyson9gmailcom/RJ-Outfits/main"

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{github_url}/banner.jpg");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }}
    .stTabs [data-baseweb="tab-list"] {{
        background-color: rgba(178, 34, 34, 0.9); 
        border-radius: 10px;
        padding: 5px;
    }}
    .stTabs [data-baseweb="tab"] {{
        color: white !important;
        font-weight: bold;
    }}
    .glass-panel {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 15px;
        color: #000000;
        margin-top: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. TOP NAVIGATION BAR ---
tab_menu, tab_home, tab_products, tab_about, tab_shop = st.tabs([
    "📂 Menu", "🏠 Home", "🛍️ Products", "📖 About Us", "🛒 Shop Now"
])
# ==========================================
# 📂 MENU (Admin & Affiliate)
# ==========================================
with tab_menu:
    # Remove the glass-panel div and use minimal styling
    st.markdown("<h3>Internal Portal</h3>", unsafe_allow_html=True)
    
    # Create two columns for the buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏢 RJ Office (Admin)", use_container_width=True):
            st.session_state['menu_selection'] = "admin"
    
    with col2:
        if st.button("🤝 Affiliate Portal", use_container_width=True):
            st.session_state['menu_selection'] = "affiliate"
    
    # Add a thin line separator
    st.markdown("---")
    
    # Handle the selections
    if 'menu_selection' not in st.session_state:
        st.session_state['menu_selection'] = None
    
    if st.session_state['menu_selection'] == "admin":
        st.markdown("### 🔐 Admin Login")
        pw = st.text_input("Enter Admin Password", type="password", key="admin_pw")
        
        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("Login", key="admin_login"):
                if pw == "RJ2026":
                    st.success("✅ Welcome Tyson & Blessings. Dashboard active.")
                else:
                    st.error("❌ Incorrect password")
        
        with col2:
            if st.button("← Back", key="back_admin"):
                st.session_state['menu_selection'] = None
                st.rerun()
    
    elif st.session_state['menu_selection'] == "affiliate":
        st.markdown("### 🤝 Affiliate Portal")
        st.info("Affiliate Program Features:")
        st.markdown("""
        - 📈 Track your referrals
        - 💰 Commission earnings
        - 🔗 Your unique affiliate links
        - 📊 Performance dashboard
        """)
        st.warning("🚧 Portal is under construction. Coming soon!")
        
        if st.button("← Back to Menu", key="back_affiliate"):
            st.session_state['menu_selection'] = None
            st.rerun()
# ==========================================
# 🏠 HOME
# ==========================================
with tab_home:
    st.markdown(f"""
        <div class="glass-panel" style="text-align:center;">
            <h1 style="color:#b22222;">RJ OUTFITS</h1>
            <p>Style Your Story | Based at Bunda Campus, Malawi</p>
            <hr>
            <h3>Look Fresh Every Day</h3>
            <p>Premium quality streetwear designed for the student lifestyle.</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 🛍️ PRODUCTS (With Prices)
# ==========================================
with tab_products:
    st.markdown('<div class="glass-panel"><h2 style="text-align:center;">Our Collection</h2></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    wa_link = "https://wa.me/265994377233?text=I%20am%20interested%20in%20"

    with col1:
        st.image(f"{github_url}/img1.jpg", use_container_width=True)
        st.markdown("**Premium Tee - MK 15,000**")
        st.markdown(f"[![Order](https://img.shields.io/badge/Order-WhatsApp-25D366?style=for-the-badge)]({wa_link}Product%201)")
        st.divider()
        st.image(f"{github_url}/img3.jpg", use_container_width=True)
        st.markdown("**Urban Hoodie - MK 25,000**")
        st.markdown(f"[![Order](https://img.shields.io/badge/Order-WhatsApp-25D366?style=for-the-badge)]({wa_link}Product%203)")

    with col2:
        st.image(f"{github_url}/img2.jpg", use_container_width=True)
        st.markdown("**Exclusive Cap - MK 10,000**")
        st.markdown(f"[![Order](https://img.shields.io/badge/Order-WhatsApp-25D366?style=for-the-badge)]({wa_link}Product%202)")
        st.divider()
        st.image(f"{github_url}/img4.jpg", use_container_width=True)
        st.markdown("**Street Joggers - MK 20,000**")
        st.markdown(f"[![Order](https://img.shields.io/badge/Order-WhatsApp-25D366?style=for-the-badge)]({wa_link}Product%204)")

# ==========================================
# 📖 ABOUT US
# ==========================================
with tab_about:
    st.markdown('<div class="glass-panel"><h2>About RJ OUTFITS</h2><p>Founded by <b>Tyson & Blessings</b> at Bunda Campus.</p></div>', unsafe_allow_html=True)

# ==========================================
# 🛒 SHOP NOW
# ==========================================
with tab_shop:
    st.markdown(f"""
        <div class="glass-panel" style="text-align:center;">
            <h2>Ready to Order?</h2>
            <a href="https://wa.me/265994377233" style="text-decoration:none;">
                <button style="background-color: #25D366; color: white; border: none; padding: 20px 40px; border-radius: 50px; font-weight: bold; cursor: pointer;">
                    💬 CHAT ON WHATSAPP
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)
