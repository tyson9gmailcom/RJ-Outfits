import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body{
margin:0;
font-family:Arial;
background:#f2f2f2;
display:flex;
justify-content:center;
}

/* MAIN PORTRAIT CONTAINER */
.main{
width:420px;   /* Portrait width */
background:white;
}

/* NAVBAR */
.navbar{
height:65px;
display:flex;
justify-content:space-between;
align-items:center;
padding:0 20px;
background:white;
box-shadow:0 2px 4px rgba(0,0,0,0.1);
}

.logo{
color:#c40000;
font-weight:bold;
font-size:20px;
}

.nav-links{
display:flex;
gap:15px;
font-size:14px;
}

.shop-btn{
background:#c40000;
color:white;
padding:6px 12px;
border-radius:3px;
font-size:13px;
}

/* HERO */
.hero{
position:relative;
height:260px;
background:url('images/hero1.jpg');
background-size:cover;
background-position:center;
}

.hero-text{
position:absolute;
left:20px;
top:70px;
color:#f4c20d;
font-weight:900;
font-size:36px;
line-height:38px;
}

/* SECTION */
.section{
padding:20px;
}

.section h2{
color:#c40000;
margin-bottom:15px;
}

/* WHY BOX */
.why-box{
width:100%;
height:200px;
background:#c40000;
color:white;
padding:20px;
clip-path:polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0 100%);
margin-bottom:30px;
}

.why-box h3{
margin:0 0 10px 0;
}

.why-box li{
margin-bottom:8px;
font-size:14px;
}

/* HONEYCOMB */
.honeycomb{
position:relative;
width:100%;
height:450px;
}

/* HEXAGON */
.hex{
position:absolute;
width:120px;
height:138px; /* 120 * 1.15 */
clip-path:polygon(
50% 0%,
100% 25%,
100% 75%,
50% 100%,
0% 75%,
0% 25%);
background:#f4c20d;
overflow:hidden;
}

.hex img{
width:100%;
height:100%;
object-fit:cover;
}

/* TOP ROW */
.hex1{left:20px; top:0;}
.hex2{left:150px; top:0;}
.hex3{left:280px; top:0;}

/* BOTTOM ROW (offset by 60px up and 65px right) */
.hex4{left:85px; top:90px;}
.hex5{left:215px; top:90px;}
.hex6{left:150px; top:180px;}

/* FOOTER */
.footer{
background:#c40000;
color:white;
padding:15px;
font-size:12px;
}

</style>
</head>

<body>

<div class="main">

<div class="navbar">
<div class="logo">RJ OUTFITS</div>
<div class="nav-links">
Home
Products
Contact
<div class="shop-btn">Shop</div>
</div>
</div>

<div class="hero">
<div class="hero-text">
STYLE<br>YOUR<br>STORY
</div>
</div>

<div class="section">
<h2>Our Products</h2>

<div class="why-box">
<h3>Why Choose Us?</h3>
<ul>
<li>✔ Quality Fabrics</li>
<li>✔ Latest Trends</li>
<li>✔ Affordable Prices</li>
<li>✔ Fast Delivery</li>
</ul>
</div>

<div class="honeycomb">

<div class="hex hex1"><img src="images/plain.jpg"></div>
<div class="hex hex2"><img src="images/long.jpg"></div>
<div class="hex hex3"><img src="images/sweater.jpg"></div>

<div class="hex hex4"><img src="images/pants.jpg"></div>
<div class="hex hex5"><img src="images/short.jpg"></div>
<div class="hex hex6"><img src="images/plain.jpg"></div>

</div>

</div>

<div class="footer">
WhatsApp: 0994377233<br>
Phone: 0996807846<br>
Location: Bunda Campus, Near Bunda COAP
</div>

</div>

</body>
</html>
"""

components.html(html, height=900)