import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="RJ OUTFITS | Official", 
    page_icon="👕", 
    layout="wide"
)

# --- 2. FULL BACKGROUND & CUSTOM STYLING ---
# Note: Replace 'tyson9gmailcom' if your GitHub username is different
github_url = "https://raw.githubusercontent.com/tyson9gmailcom/RJ-Outfits/main"

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{github_url}/banner.jpg");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }}
    /* Semi-transparent containers so text is readable */
    .glass-panel {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 15px;
        color: #000000;
        border: 1px solid rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }}
    .main-header {{
        background-color: rgba(178, 34, 34, 0.9); /* RJ Red */
        padding: 20px;
        text-align: center;
        color: white;
        border-radius: 15px;
        margin-bottom: 25px;
    }}
    h1, h2, h3 {{ color: #b22222 !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. NAVIGATION ---
st.sidebar.title("👕 RJ OUTFITS")
page = st.sidebar.radio("Navigate to:", ["Home", "Our Collection", "Affiliate Portal", "RJ Office"])

# ==========================================
# PAGE 1: HOME
# ==========================================
if page == "Home":
    st.markdown('<div class="main-header"><h1>RJ OUTFITS</h1><p>Style Your Story | Bunda Campus</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"""
            <div class="glass-panel">
                <h2>Look Fresh!</h2>
                <p>Welcome to the home of premium streetwear at Bunda. We bring the latest trends directly to you.</p>
                <p>✅ <b>Quality Fabrics</b><br>✅ <b>Exclusive Designs</b><br>✅ <b>Campus Delivery</b></p>
                <br>
                <a href="https://wa.me/265994377233" style="text-decoration:none;">
                    <button style="background-color: #b22222; color: white; border: none; padding: 10px 20px; border-radius: 5px; font-weight: bold; cursor: pointer;">
                        ORDER VIA WHATSAPP
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# PAGE 2: OUR COLLECTION (THE 5 IMAGES)
# ==========================================
elif page == "Our Collection":
    st.markdown('<div class="main-header"><h1>OUR LATEST COLLECTION</h1></div>', unsafe_allow_html=True)
    
    # Displaying your 5 images in a grid
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.image(f"{github_url}/img1.jpg", caption="New Arrival 1", use_container_width=True)
        st.image(f"{github_url}/img3.jpg", caption="New Arrival 3", use_container_width=True)
        st.image(f"{github_url}/img5.jpg", caption="Special Edition", use_container_width=True)
        
    with col_b:
        st.image(f"{github_url}/img2.jpg", caption="New Arrival 2", use_container_width=True)
        st.image(f"{github_url}/img4.jpg", caption="New Arrival 4", use_container_width=True)

# ==========================================
# PAGE 3: AFFILIATE & ADMIN (Basic Setup)
# ==========================================
elif page == "Affiliate Portal":
    st.markdown('<div class="glass-panel"><h2>Affiliate Login</h2><p>Coming soon for our marketing partners.</p></div>', unsafe_allow_html=True)

elif page == "RJ Office":
    st.markdown('<div class="glass-panel"><h2>🔐 Admin Access</h2></div>', unsafe_allow_html=True)
    pw = st.text_input("Enter Password", type="password")
    if pw == "RJ2026":
        st.success("Welcome Tyson & Blessings. Profits are split 50/50.")
