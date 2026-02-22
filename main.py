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
    
    /* Top Navigation Bar Styling */
    .top-nav {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(5px);
        border-radius: 10px;
        margin: 1rem;
    }}
    
    .brand {{
        color: white;
        font-size: 2rem;
        font-weight: 900;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    
    .nav-items {{
        display: flex;
        gap: 2rem;
        align-items: center;
    }}
    
    .nav-link {{
        color: white !important;
        font-weight: 600;
        text-decoration: none;
        font-size: 1.1rem;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: all 0.3s ease;
        cursor: pointer;
    }}
    
    .nav-link:hover {{
        background-color: #b22222;
    }}
    
    .menu-icon {{
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0.5rem 1rem;
        border-radius: 5px;
    }}
    
    .menu-icon:hover {{
        background-color: #b22222;
    }}
    
    /* Content Area Styling */
    .content-area {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem;
        color: #000000;
    }}
    
    /* Glass panel for special sections */
    .glass-panel {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 15px;
        color: #000000;
        margin-top: 20px;
    }}
    
    /* Hide default streamlit elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Hide the default tabs */
    .stTabs [data-baseweb="tab-list"] {{
        display: none;
    }}
    </style>
    
    <!-- Top Navigation Bar -->
    <div class="top-nav">
        <div class="brand">RJ OUTFITS</div>
        <div class="nav-items">
            <a class="nav-link" onclick="document.querySelectorAll('[data-baseweb=tab]')[0].click()">Home</a>
            <a class="nav-link" onclick="document.querySelectorAll('[data-baseweb=tab]')[1].click()">Products</a>
            <a class="nav-link" onclick="document.querySelectorAll('[data-baseweb=tab]')[2].click()">About Us</a>
            <a class="nav-link" onclick="document.querySelectorAll('[data-baseweb=tab]')[3].click()">Contact</a>
            <a class="nav-link" onclick="document.querySelectorAll('[data-baseweb=tab]')[4].click()">Shop Now</a>
            <span class="menu-icon" onclick="document.querySelectorAll('[data-baseweb=tab]')[5].click()">☰</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. HIDDEN TABS FOR NAVIGATION (Behind the scenes) ---
tab_home, tab_products, tab_about, tab_contact, tab_shop, tab_menu = st.tabs([
    "Home", "Products", "About Us", "Contact", "Shop Now", "Menu"
])

# ==========================================
# 🏠 HOME
# ==========================================
with tab_home:
    st.markdown("""
        <div class="content-area" style="text-align:center;">
            <h2 style="color:#b22222;">Style Your Story</h2>
            <p style="font-size:1.2rem;">Premium quality streetwear designed for the student lifestyle.</p>
            <p>Based at Bunda Campus, Malawi</p>
            <br>
            <h3>Look Fresh Every Day</h3>
            <p>Discover our latest collection of urban fashion essentials.</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 🛍️ PRODUCTS (With Prices)
# ==========================================
with tab_products:
    st.markdown('<div class="content-area"><h2 style="text-align:center;">Our Collection</h2></div>', unsafe_allow_html=True)
    wa_link = "https://wa.me/265994377233?text=I%20am%20interested%20in%20"
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(f"{github_url}/img1.jpg", use_container_width=True)
        st.markdown("**Premium Tee - MK 15,000**")
        st.markdown(f"[![Order](https://img.shields.io/badge/Order-WhatsApp-25D366?style=for-the-badge)]({wa_link}Premium%20Tee)")
        st.divider()
        st.image(f"{github_url}/img3.jpg", use_container_width=True)
        st.markdown("**Urban Hoodie - MK 25,000**")
        st.markdown(f"[![Order](https://img.shields.io/badge/Order-WhatsApp-25D366?style=for-the-badge)]({wa_link}Urban%20Hoodie)")
    
    with col2:
        st.image(f"{github_url}/img2.jpg", use_container_width=True)
        st.markdown("**Exclusive Cap - MK 10,000**")
        st.markdown(f"[![Order](https://img.shields.io/badge/Order-WhatsApp-25D366?style=for-the-badge)]({wa_link}Exclusive%20Cap)")
        st.divider()
        st.image(f"{github_url}/img4.jpg", use_container_width=True)
        st.markdown("**Street Joggers - MK 20,000**")
        st.markdown(f"[![Order](https://img.shields.io/badge/Order-WhatsApp-25D366?style=for-the-badge)]({wa_link}Street%20Joggers)")

# ==========================================
# 📖 ABOUT US
# ==========================================
with tab_about:
    st.markdown("""
        <div class="content-area">
            <h2>About RJ OUTFITS</h2>
            <p>Founded by <b>Tyson & Blessings</b> at Bunda Campus, Malawi.</p>
            <p>We're on a mission to bring premium streetwear to students, combining comfort with style.</p>
            <h3>Our Vision</h3>
            <p>To become Malawi's leading student fashion brand, known for quality and authenticity.</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 📞 CONTACT
# ==========================================
with tab_contact:
    st.markdown("""
        <div class="content-area">
            <h2>Contact Us</h2>
            <p>📍 <b>Location:</b> Bunda Campus, Malawi</p>
            <p>📞 <b>Phone:</b> +265 994 377 233</p>
            <p>📧 <b>Email:</b> rjoutfits@bunda.mw</p>
            <p>⏰ <b>Hours:</b> Mon-Fri: 9am - 5pm</p>
            <br>
            <h3>Follow Us</h3>
            <p>📱 Instagram: @rj.outfits</p>
            <p>📱 Facebook: RJ Outfits Malawi</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 🛒 SHOP NOW
# ==========================================
with tab_shop:
    st.markdown("""
        <div class="content-area" style="text-align:center;">
            <h2>Ready to Order?</h2>
            <p>Click the button below to chat with us on WhatsApp</p>
            <a href="https://wa.me/265994377233" style="text-decoration:none;">
                <button style="background-color: #25D366; color: white; border: none; padding: 20px 40px; border-radius: 50px; font-weight: bold; cursor: pointer; font-size: 1.2rem;">
                    💬 CHAT ON WHATSAPP
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 📂 MENU (Admin & Affiliate) - Three Dashes Icon
# ==========================================
with tab_menu:
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    st.markdown("### 📋 Menu Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏢 RJ Office (Admin)", use_container_width=True):
            st.session_state['menu_selection'] = "admin"
    
    with col2:
        if st.button("🤝 Affiliate Portal", use_container_width=True):
            st.session_state['menu_selection'] = "affiliate"
    
    st.markdown("---")
    
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
    
    st.markdown('</div>', unsafe_allow_html=True)
