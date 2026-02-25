import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body {
    margin:0;
    font-family: Arial, sans-serif;
    background-color:#f5f5f5;
}

/* ===== NAVBAR ===== */
.navbar {
    width:100%;
    height:70px;
    background:white;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:0 60px;
    box-shadow:0 2px 5px rgba(0,0,0,0.1);
}

.logo {
    font-size:26px;
    font-weight:bold;
    color:#c40000;
}

.nav-links {
    display:flex;
    gap:40px;
    align-items:center;
}

.nav-links a {
    text-decoration:none;
    color:#333;
    font-weight:600;
}

.shop-btn {
    background:#c40000;
    color:white;
    padding:10px 25px;
    border-radius:4px;
    font-weight:bold;
}

/* ===== HERO SECTION ===== */
.hero {
    width:100%;
    height:400px;
    display:flex;
    justify-content:center;
    align-items:center;
    background:url('images/hero1.jpg');
    background-size:cover;
    background-position:center;
    position:relative;
}

.hero-text {
    position:absolute;
    left:120px;
    color:#f4c20d;
    font-size:60px;
    font-weight:900;
    line-height:70px;
}

/* ===== PRODUCTS SECTION ===== */
.section {
    padding:60px 100px;
}

.products-container {
    display:flex;
    gap:50px;
}

/* Why Choose Shape */
.why-box {
    width:350px;
    height:320px;
    background:#c40000;
    color:white;
    padding:30px;
    clip-path:polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0 100%);
}

.why-box h2 {
    margin-bottom:20px;
}

.why-box ul {
    list-style:none;
    padding:0;
}

.why-box li {
    margin-bottom:15px;
}

/* HEXAGON GRID */
.hex-grid {
    display:grid;
    grid-template-columns:repeat(3, 200px);
    gap:40px;
}

.hex {
    width:200px;
    height:230px;
    position:relative;
    clip-path:polygon(
        50% 0%, 
        100% 25%, 
        100% 75%, 
        50% 100%, 
        0% 75%, 
        0% 25%
    );
    background:#f4c20d;
    display:flex;
    justify-content:center;
    align-items:center;
}

.hex img {
    width:90%;
    height:90%;
    object-fit:cover;
    clip-path:polygon(
        50% 0%, 
        100% 25%, 
        100% 75%, 
        50% 100%, 
        0% 75%, 
        0% 25%
    );
}

/* ===== FOOTER ===== */
.footer {
    background:#c40000;
    color:white;
    padding:20px 100px;
    display:flex;
    justify-content:space-between;
}

</style>
</head>

<body>

<!-- NAVBAR -->
<div class="navbar">
    <div class="logo">RJ OUTFITS</div>
    <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">Products</a>
        <a href="#">About Us</a>
        <a href="#">Contact</a>
        <div class="shop-btn">Shop Now</div>
    </div>
</div>

<!-- HERO -->
<div class="hero">
    <div class="hero-text">
        STYLE<br>YOUR<br>STORY
    </div>
</div>

<!-- PRODUCTS -->
<div class="section">
<h1>Our Products</h1>

<div class="products-container">

<div class="why-box">
<h2>Why Choose Us?</h2>
<ul>
<li>✔ Quality Fabrics</li>
<li>✔ Latest Trends</li>
<li>✔ Affordable Prices</li>
<li>✔ Fast Delivery</li>
</ul>
</div>

<div class="hex-grid">
<div class="hex"><img src="images/plain.jpg"></div>
<div class="hex"><img src="images/long.jpg"></div>
<div class="hex"><img src="images/sweater.jpg"></div>
<div class="hex"><img src="images/pants.jpg"></div>
<div class="hex"><img src="images/short.jpg"></div>
<div class="hex"><img src="images/plain.jpg"></div>
</div>

</div>
</div>

<!-- FOOTER -->
<div class="footer">
<div>
WhatsApp: 0994377233<br>
Phone: 0996807846
</div>
<div>
Location: Bunda Campus, Near Bunda COAP
</div>
</div>

</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)