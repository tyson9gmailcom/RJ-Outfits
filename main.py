import streamlit as st
import streamlit.components.v1 as components

# 1. PAGE CONFIG
st.set_page_config(layout="wide", page_title="RJ OUTFITS")

# ---------------------------------------------------------
# 2. STYLES & HEAD (Preserving all your original CSS)
# ---------------------------------------------------------
html_start = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-red: #A51D1D;
            --accent-yellow: #FBBF0D;
            --text-charcoal: #1A1A1A;
            --font-main: 'Roboto', sans-serif;
            --font-hero: 'Archivo Black', sans-serif;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: var(--font-main); background-color: #FFF; overflow-x: hidden; }

        /* ALL YOUR ORIGINAL CSS CLASSES */
        .header-global { height: 80px; width: 100%; display: flex; justify-content: center; align-items: center; border-bottom: 3px solid var(--accent-yellow); background: #FFF; }
        .header-container { width: 95%; max-width: 1200px; display: flex; justify-content: space-between; align-items: center; }
        .logo-rj-outfits { height: 44px; }
        .nav-list { display: flex; list-style: none; gap: 15px; align-items: center; }
        .nav-list a { text-decoration: none; color: var(--text-charcoal); font-weight: 500; font-size: 15px; cursor: pointer; }
        .menu-dashes { font-size: 24px; font-weight: bold; cursor: pointer; color: var(--text-charcoal); margin-right: 10px; }
        .btn-shop-header { background-color: var(--primary-red); color: white; border: none; padding: 8px 18px; border-radius: 4px; font-weight: bold; cursor: pointer; }

        /* HERO & HONEYCOMB (Your specific styles) */
        .section-hero { position: relative; width: 100%; height: 450px; display: grid; grid-template-columns: repeat(4, 1fr); }
        .hero-pane { background-size: cover; background-position: center; border-right: 1px solid rgba(255,255,255,0.1); }
        .pane-1 { background-image: url('assets/hero_1.jpg'); }
        .pane-2 { background-image: url('assets/hero_2.jpg'); }
        .pane-3 { background-image: url('assets/hero_3.jpg'); }
        .pane-4 { background-image: url('assets/hero_4.jpg'); position: relative; }
        .headline-style { position: absolute; top: 15%; left: 8%; font-family: var(--font-hero); font-size: 65px; line-height: 0.9; color: var(--accent-yellow); text-shadow: 2px 2px 10px rgba(0,0,0,0.4); z-index: 10; }
        .section-products { width: 100%; display: flex; flex-direction: column; align-items: center; padding: 60px 0; }
        .pentagon-info { width: 280px; background-color: var(--primary-red); color: white; padding: 30px 20px; margin-bottom: -40px; clip-path: polygon(0% 0%, 100% 0%, 100% 80%, 50% 100%, 0% 80%); z-index: 20; text-align: center; }
        .honeycomb-cluster { display: flex; flex-direction: column; align-items: center; margin-top: 40px; width: 100%; }
        .hex-row { display: flex; justify-content: center; gap: 4px; width: 100%; }
        .hex-shape { width: 130px; height: 150px; background-color: #f5f5f5; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); display: flex; justify-content: center; align-items: center; border: 3px solid var(--accent-yellow); position: relative; }
        .hex-shape img { width: 80%; height: auto; object-fit: contain; }
        .row-2, .row-3 { margin-top: -35px; }
        .footer-contact { background-color: var(--primary-red); color: white; padding: 30px 0; width: 100%; margin-top: 100px; }

        /* NEW MENU OVERLAY STYLES */
        .menu-overlay { height: 100%; width: 0; position: fixed; z-index: 1000; top: 0; left: 0; background-color: rgba(26,26,26,0.98); overflow-x: hidden; transition: 0.5s; }
        .menu-content { position: relative; top: 20%; width: 100%; text-align: center; }
        .menu-content a { padding: 15px; text-decoration: none; font-size: 32px; color: white; display: block; font-family: 'Archivo Black'; cursor: pointer; }
        .menu-content a:hover { color: var(--accent-yellow); }
        .close-btn { position: absolute; top: 20px; right: 45px; font-size: 50px; color: white; cursor: pointer; }

        /* SWITCHER LOGIC */
        .content-section { display: none; }
        .active-section { display: block; }
    </style>
</head>
<body>
"""

# ---------------------------------------------------------
# 3. THE MENU & HEADER
# ---------------------------------------------------------
header_block = """
<div id="sideMenu" class="menu-overlay">
    <span class="close-btn" onclick="toggleMenu(0)">&times;</span>
    <div class="menu-content">
        <a onclick="showScreen('home-screen')">Home</a>
        <a onclick="showScreen('office-screen')">RJ Office</a>
        <a onclick="showScreen('affiliate-screen')">Affiliate Portal</a>
    </div>
</div>

<header class="header-global">
    <div class="header-container">
        <img src="assets/rj_logo.png" class="logo-rj-outfits" alt="Logo">
        <nav>
            <ul class="nav-list">
                <li><span class="menu-dashes" onclick="toggleMenu(300)">&#9776;</span></li>
                <li><a onclick="showScreen('home-screen')">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><button class="btn-shop-header">Shop Now</button></li>
            </ul>
        </nav>
    </div>
</header>
"""

# ---------------------------------------------------------
# 4. INSERT YOUR CONTENT BELOW
# ---------------------------------------------------------

# --- SCREEN 1: HOME ---
home_screen = """
<div id="home-screen" class="content-section active-section">
    <section class="section-hero">
        <div class="hero-pane pane-1"></div><div class="hero-pane pane-2"></div>
        <div class="hero-pane pane-3"></div><div class="hero-pane pane-4"><button class="btn-hero-shop">SHOP NOW</button></div>
        <h1 class="headline-style">STYLE<br>YOUR<br>STORY</h1>
    </section>

    <section class="section-products">
        <h2 class="section-title">Our Products</h2>
        <div class="pentagon-info">
            <h3>Why Choose Us?</h3>
            <ul style="list-style:none; font-size:14px;"><li>✓ Quality Fabrics</li><li>✓ Latest Trends</li></ul>
        </div>
        <div class="honeycomb-cluster">
            <div class="hex-row row-1">
                <div class="hex-shape"><img src="assets/folded.png"></div>
                <div class="hex-shape"><img src="assets/plain_tshirts.png"></div>
                <div class="hex-shape"><img src="assets/long_sleeves.png"></div>
            </div>
            <div class="hex-row row-2">
                <div class="hex-shape"><img src="assets/shorts.png"></div>
                <div class="hex-shape"><img src="assets/boys_sleeves.png"></div>
            </div>
            <div class="hex-row row-3">
                <div class="hex-shape"><img src="assets/underwear.png"></div>
            </div>
        </div>
    </section>
</div>
"""

# --- SCREEN 2: RJ OFFICE ---
office_screen = """
<div id="office-screen" class="content-section" style="padding: 100px 20px; text-align: center;">
    <h1 style="color: #A51D1D; font-family: 'Archivo Black'; font-size: 50px;">RJ OFFICE</h1>
    <p>Management dashboard coming soon...</p>
    </div>
"""

# --- SCREEN 3: AFFILIATE PORTAL ---
affiliate_screen = """
<div id="affiliate-screen" class="content-section" style="padding: 100px 20px; text-align: center;">
    <h1 style="color: #A51D1D; font-family: 'Archivo Black'; font-size: 50px;">AFFILIATE PORTAL</h1>
    <p>Partner dashboard coming soon...</p>
    </div>
"""

# ---------------------------------------------------------
# 5. FOOTER & JAVASCRIPT LOGIC
# ---------------------------------------------------------
footer_block = """
    <footer class="footer-contact">
        <div class="footer-container">
            <div class="footer-info">
                <div><span>Contacts:</span> WhatsApp: 9994371233</div>
                <div><span>Location:</span> Bunda Campus</div>
            </div>
        </div>
    </footer>

    <script>
    function toggleMenu(width) {
        document.getElementById("sideMenu").style.width = width + "px";
    }

    function showScreen(screenId) {
        // 1. Hide all sections
        var sections = document.getElementsByClassName('content-section');
        for (var i = 0; i < sections.length; i++) {
            sections[i].classList.remove('active-section');
        }
        // 2. Show the one you clicked
        document.getElementById(screenId).classList.add('active-section');
        // 3. Close the menu
        toggleMenu(0);
        // 4. Scroll to top
        window.scrollTo(0,0);
    }
    </script>
</body>
</html>
"""

# --- FINAL COMBINATION ---
full_website_code = html_start + header_block + home_screen + office_screen + affiliate_screen + footer_block

# Render
components.html(full_website_code, height=2000, scrolling=True)
