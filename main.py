import streamlit as st
import streamlit.components.v1 as components

# Sets the dashboard to fill the screen
st.set_page_config(layout="wide", page_title="RJ OUTFITS")

# This is the full website code with Portrait Squeeze Logic
website_code = """
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

        /* HEADER - Fluid for Portrait */
      .header-global {
            height: auto; min-height: 80px; width: 100%;
            display: flex; justify-content: center; align-items: center;
            border-bottom: 3px solid var(--accent-yellow);
            background: #FFF; padding: 10px 0;
        }
      .header-container {
            width: 95%; max-width: 1200px;
            display: flex; justify-content: space-between; align-items: center;
            flex-wrap: wrap; gap: 10px;
        }
      .logo-rj-outfits { height: 44px; }
      .nav-list { display: flex; list-style: none; gap: 15px; }
      .nav-list a { text-decoration: none; color: var(--text-charcoal); font-weight: 500; font-size: 14px; }
      .nav-list a.active { color: var(--primary-red); border-bottom: 2px solid var(--primary-red); }
      .btn-shop-header {
            background-color: var(--primary-red); color: white; border: none;
            padding: 10px 20px; border-radius: 4px; font-weight: bold; cursor: pointer;
        }

        /* HERO - Squeezes 4 panes into 2x2 on mobile */
      .section-hero { position: relative; width: 100%; height: 450px; display: grid; grid-template-columns: repeat(4, 1fr); }
      .hero-pane { background-size: cover; background-position: center; border-right: 1px solid rgba(255,255,255,0.2); }
      .pane-1 { background-image: url('assets/hero_1.jpg'); }
      .pane-2 { background-image: url('assets/hero_2.jpg'); }
      .pane-3 { background-image: url('assets/hero_3.jpg'); }
      .pane-4 { background-image: url('assets/hero_4.jpg'); position: relative; }
        
      .headline-style {
            position: absolute; top: 15%; left: 8%;
            font-family: var(--font-hero); font-size: 60px; line-height: 0.9;
            color: var(--accent-yellow); text-shadow: 2px 2px 8px rgba(0,0,0,0.5); z-index: 10;
        }
      .btn-hero-shop {
            position: absolute; bottom: 20px; right: 20px;
            background-color: var(--primary-red); color: white; border: none;
            padding: 12px 24px; font-weight: bold; cursor: pointer;
        }

        /* PRODUCTS - Stacks vertically in Portrait */
      .section-products { width: 95%; max-width: 1200px; margin: 40px auto; }
      .section-title { color: var(--primary-red); font-size: 32px; margin-bottom: 20px; }
      .product-content-wrapper { display: flex; gap: 30px; }

      .ribbon-sidebar {
            width: 350px; flex-shrink: 0; background-color: var(--primary-red); color: white;
            padding: 40px 30px; clip-path: polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0 100%);
        }
      .ribbon-title { font-size: 30px; margin-bottom: 20px; line-height: 1.1; }
      .list-features { list-style: none; }
      .list-features li { margin-bottom: 10px; display: flex; align-items: center; font-size: 16px; }
      .list-features li::before {
            content: '✓'; margin-right: 10px; border: 2px solid white; border-radius: 50%;
            width: 22px; height: 22px; display: flex; justify-content: center; align-items: center; font-size: 11px;
        }

        /* HONEYCOMB GRID - Responsive columns */
      .grid-honeycomb {
            flex-grow: 1; display: grid; grid-template-columns: repeat(auto-fit, 150px);
            grid-gap: 15px; justify-content: center; padding-top: 20px;
        }
      .hex-container { display: flex; flex-direction: column; align-items: center; width: 150px; }
      .hex-shape {
            width: 130px; height: 150px; background-color: #f9f9f9;
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            border: 3px solid var(--accent-yellow); display: flex; justify-content: center; align-items: center;
        }
      .hex-shape img { width: 85%; height: auto; }
      .hex-label { margin-top: 8px; font-size: 12px; font-weight: bold; color: #333; text-align: center; }
      .hex-item:nth-child(even) { transform: translateY(30px); }

        /* FOOTER */
      .footer-contact { background-color: var(--primary-red); color: white; padding: 30px 0; width: 100%; margin-top: 60px; }
      .footer-container {
            width: 95%; max-width: 1200px; margin: 0 auto;
            display: flex; justify-content: space-between; align-items: center;
        }
      .footer-info { display: flex; gap: 30px; font-size: 13px; }
      .info-col span { color: var(--accent-yellow); font-weight: bold; }
      .social-icons { display: flex; gap: 12px; align-items: center; }
      .social-circle {
            width: 30px; height: 30px; background: white; border-radius: 50%;
            display: flex; justify-content: center; align-items: center; color: var(--primary-red); font-weight: bold;
        }

        /* --- PORTRAIT SQUEEZE LOGIC --- */
        @media (max-width: 768px) {
          .header-container { flex-direction: column; text-align: center; }
          .nav-list { gap: 8px; margin: 10px 0; }
          .nav-list a { font-size: 12px; }

          .section-hero { grid-template-columns: repeat(2, 1fr); height: 350px; }
          .headline-style { font-size: 38px; top: 10%; }
            
          .product-content-wrapper { flex-direction: column; align-items: center; }
          .ribbon-sidebar { width: 100%; clip-path: polygon(0 0, 100% 0, 100% 85%, 50% 100%, 0 85%); margin-bottom: 30px; }
          .hex-item:nth-child(even) { transform: none; }
            
          .footer-container { flex-direction: column; gap: 20px; text-align: center; }
          .footer-info { flex-direction: column; gap: 15px; }
        }
    </style>
</head>
<body>
    <header class="header-global">
        <div class="header-container">
            <img src="assets/rj_logo.png" class="logo-rj-outfits" alt="Logo">
            <ul class="nav-list">
                <li><a href="#" class="active">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
            <button class="btn-shop-header">Shor Now</button>
        </div>
    </header>

    <section class="section-hero">
        <div class="hero-pane pane-1"></div>
        <div class="hero-pane pane-2"></div>
        <div class="hero-pane pane-3"></div>
        <div class="hero-pane pane-4">
            <button class="btn-hero-shop">SHOP NOW</button>
        </div>
        <h1 class="headline-style">STYLE<br>YOUR<br>STORY</h1>
    </section>

    <section class="section-products">
        <h2 class="section-title">Our Products</h2>
        <div class="product-content-wrapper">
            <div class="ribbon-sidebar">
                <h3 class="ribbon-title">Why Choose Us?<br>Us?</h3>
                <ul class="list-features">
                    <li>Quality Fabrics</li>
                    <li>Latest Trends</li>
                    <li>Latest Trends</li>
                    <li>Fast Delivery</li>
                </ul>
            </div>
            <div class="grid-honeycomb">
                <div class="hex-container hex-item"><div class="hex-shape"><img src="assets/plain_tshirts.png"></div><p class="hex-label">Plain T-shirts</p></div>
                <div class="hex-container hex-item"><div class="hex-shape"><img src="assets/folded.png"></div></div>
                <div class="hex-container hex-item"><div class="hex-shape"><img src="assets/long_sleeves.png"></div><p class="hex-label">Long Sleeves</p></div>
                <div class="hex-container hex-item"><div class="hex-shape"><img src="assets/shorts.png"></div></div>
                <div class="hex-container hex-item"><div class="hex-shape"><img src="assets/boys_sleeves.png"></div><p class="hex-label">Boys Sleeves</p></div>
                <div class="hex-container hex-item"><div class="hex-shape"><img src="assets/underwear.png"></div></div>
            </div>
        </div>
    </section>

    <footer class="footer-contact">
        <div class="footer-container">
            <div class="footer-info">
                <div class="info-col"><span>Cuntacts:</span><br>WhatsApp: 9994371233<br>Phone: 0938607846</div>
                <div class="info-col"><span>Location:</span><br>Bunda Campus,<br>Near Bunda COAP</div>
            </div>
            <div class="social-icons">
                <div class="social-circle">f</div><div class="social-circle">t</div><div class="social-circle">y</div>
            </div>
        </div>
    </footer>
</body>
</html>
"""

# Displays the website in the dashboard
components.html(website_code, height=1800, scrolling=True)
