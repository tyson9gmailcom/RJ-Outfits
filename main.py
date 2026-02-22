import streamlit as st

st.set_page_config(page_title="RJ OUTFITS", layout="wide")

# --- CSS (FIXED PROPERLY) ---
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #f5f5f5;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 40px;
    background-color: white;
}

.logo {
    font-size: 22px;
    font-weight: bold;
    color: #c40000;
}

.nav-links a {
    margin: 0 15px;
    text-decoration: none;
    color: black;
    font-weight: 500;
}

.shop-btn {
    background-color: #c40000;
    color: white;
    padding: 8px 15px;
    border-radius: 5px;
}

/* Hero */
.hero {
    display: flex;
    margin: 20px;
}

.hero-left {
    flex: 2;
    background-image: url('https://images.unsplash.com/photo-1520975922203-b8d8d5b7c3c4');
    background-size: cover;
    height: 300px;
    display: flex;
    align-items: center;
    padding-left: 30px;
}

.hero-text {
    font-size: 40px;
    font-weight: bold;
    color: gold;
}

.hero-right {
    flex: 1;
    background-image: url('https://images.unsplash.com/photo-1521335629791-ce4aec67dd53');
    background-size: cover;
    display: flex;
    justify-content: center;
    align-items: center;
}

.hero-btn {
    background-color: red;
    color: white;
    padding: 10px 20px;
}

/* Products */
.section {
    padding: 30px;
}

.products {
    display: flex;
    gap: 20px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

.why {
    background: red;
    color: white;
    padding: 20px;
    width: 250px;
}

/* Footer */
.footer {
    background: #c40000;
    color: white;
    padding: 15px;
    display: flex;
    justify-content: space-between;
}

</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown("""
<div class="navbar">
    <div class="logo">RJ OUTFITS</div>
    <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">Products</a>
        <a href="#">About Us</a>
        <a href="#">Contact</a>
        <a class="shop-btn" href="#">Shop Now</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div class="hero">
    <div class="hero-left">
        <div class="hero-text">STYLE YOUR STORY</div>
    </div>
    <div class="hero-right">
        <button class="hero-btn">SHOP NOW</button>
    </div>
</div>
""", unsafe_allow_html=True)

# --- PRODUCTS ---
st.markdown("<h2 style='color:#c40000; padding-left:30px;'>Our Products</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="products">

        <div class="why">
            <h3>Why Choose Us?</h3>
            <ul>
                <li>Quality Fabrics</li>
                <li>Latest Trends</li>
                <li>Fast Delivery</li>
            </ul>
        </div>

        <div class="card">
            <p>Plain T-shirts</p>
        </div>

        <div class="card">
            <p>Long Sleeves</p>
        </div>

        <div class="card">
            <p>Shorts</p>
        </div>

    </div>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <div>
        WhatsApp: 0999437233 <br>
        Call: 0938607846
    </div>
    <div>
        Location: Bunda Campus
    </div>
</div>
""", unsafe_allow_html=True)
