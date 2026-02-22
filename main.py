import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="RJ OUTFITS", 
    page_icon="👕", 
    layout="wide"
)

# --- 2. EXACT STYLING FROM SCREENSHOT ---
st.markdown("""
    <style>
    /* Completely black background */
    .stApp {
        background-color: black;
    }
    
    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .main-container {
        color: white;
        padding: 20px;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header/Navigation */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 0;
        border-bottom: 1px solid #333;
    }
    
    .logo {
        font-size: 28px;
        font-weight: bold;
        color: white;
    }
    
    .nav-links {
        display: flex;
        gap: 40px;
    }
    
    .nav-links a {
        color: white;
        text-decoration: none;
        font-size: 18px;
        font-weight: 500;
    }
    
    .nav-links a:hover {
        color: #cccccc;
    }
    
    /* Main content area */
    .hero-section {
        text-align: center;
        padding: 80px 0 40px 0;
    }
    
    .hero-title {
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 20px;
        letter-spacing: 2px;
    }
    
    .hero-subtitle {
        font-size: 24px;
        color: #cccccc;
        margin-bottom: 30px;
    }
    
    .shop-now-btn {
        background-color: transparent;
        color: white;
        border: 2px solid white;
        padding: 15px 50px;
        font-size: 20px;
        font-weight: bold;
        cursor: pointer;
        margin-bottom: 60px;
        transition: all 0.3s;
    }
    
    .shop-now-btn:hover {
        background-color: white;
        color: black;
    }
    
    /* Products section */
    .products-title {
        font-size: 36px;
        font-weight: bold;
        margin: 40px 0 30px 0;
    }
    
    .why-choose-title {
        font-size: 28px;
        font-weight: bold;
        margin: 30px 0 20px 0;
    }
    
    .features-list {
        list-style: none;
        padding: 0;
    }
    
    .features-list li {
        font-size: 18px;
        margin: 15px 0;
        color: #cccccc;
    }
    
    /* Contacts section */
    .contacts-title {
        font-size: 28px;
        font-weight: bold;
        margin: 40px 0 20px 0;
    }
    
    .contact-info {
        font-size: 18px;
        margin: 10px 0;
        color: #cccccc;
    }
    
    .location {
        font-size: 18px;
        margin: 20px 0;
        color: #cccccc;
    }
    
    /* Divider */
    .divider {
        border-top: 1px solid #333;
        margin: 40px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. MAIN DASHBOARD LAYOUT ---
st.markdown("""
<div class="main-container">
    <!-- Header with navigation -->
    <div class="header">
        <div class="logo">RJ OUTFITS</div>
        <div class="nav-links">
            <a href="#">Home</a>
            <a href="#">Products</a>
            <a href="#">About Us</a>
            <a href="#">Contact</a>
            <a href="#">Shop Now</a>
        </div>
    </div>
    
    <!-- Hero Section -->
    <div class="hero-section">
        <div class="hero-title">STYLE YOUR STORY</div>
        <button class="shop-now-btn">SHOP NOW</button>
    </div>
    
    <!-- Our Products Section -->
    <div class="products-title">Our Products</div>
    
    <!-- Why Choose Us Section -->
    <div class="why-choose-title">Why Choose Us?</div>
    <ul class="features-list">
        <li>✓ Quality Fabrics</li>
        <li>✓ Latest Trends</li>
        <li>✓ Latest Trends</li>
        <li>✓ Fast Delivery</li>
    </ul>
    
    <!-- Divider -->
    <div class="divider"></div>
    
    <!-- Contacts Section -->
    <div class="contacts-title">Contacts:</div>
    <div class="contact-info">✓ WhatsApp: 9994377233</div>
    <div class="contact-info">✓ Phone Call: 0938607846</div>
    <div class="location">✓ Location: Bunda Campus, Near Bunda COAP</div>
</div>
""", unsafe_allow_html=True)

# --- 4. HIDDEN FUNCTIONALITY (for the menu/admin section) ---
# This section is hidden but accessible via URL parameters or state
if st.query_params.get("admin") == "true":
    st.markdown("---")
    with st.expander("Admin Panel (Hidden)"):
        st.markdown("### Admin Login")
        pw = st.text_input("Password", type="password")
        if pw == "RJ2026":
            st.success("Welcome Admin")
            st.markdown("Dashboard access granted")
