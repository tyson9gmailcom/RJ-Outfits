Import streamlit as st
import streamlit.components.v1 as components

# Configures the dashboard to fill the phone/web screen
st.set_page_config(layout="wide", page_title="RJ OUTFITS")

# Updated website code with 3-2-1 Centered Pyramid Honeycomb and Minimalist UI
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

        /* HEADER SECTION */
     .header-global {
            height: 80px; width: 100%;
            display: flex; justify-content: center; align-items: center;
            border-bottom: 3px solid var(--accent-yellow);
            background: #FFF;
        }
     .header-container {
            width: 95%; max-width: 1200px;
            display: flex; justify-content: space-between; align-items: center;
        }
     .logo-rj-outfits { height: 44px; }
     .nav-list { display: flex; list-style: none; gap: 15px; align-items: center; }
     .nav-list a { text-decoration: none; color: var(--text-charcoal); font-weight: 500; font-size: 15px; }
     .nav-list a.active { color: var(--primary-red); border-bottom: 2px solid var(--primary-red); }
     .menu-dashes { font-size: 24px; font-weight: bold; cursor: pointer; color: var(--text-charcoal); margin-right: 10px; }
     .btn-shop-header {
            background-color: var(--primary-red); color: white; border: none;
            padding: 8px 18px; border-radius: 4px; font-weight: bold; cursor: pointer;
            font-size: 14px; margin-left: 5px;
        }

        /* HERO SECTION */
     .section-hero { position: relative; width: 100%; height: 450px; display: grid; grid-template-columns: repeat(4, 1fr); }
     .hero-pane { background-size: cover; background-position: center; border-right: 1px solid rgba(255,255,255,0.1); }
     .pane-1 { background-image: url('assets/hero_1.jpg'); }
     .pane-2 { background-image: url('assets/hero_2.jpg'); }
     .pane-3 { background-image: url('assets/hero_3.jpg'); }
     .pane-4 { background-image: url('assets/hero_4.jpg'); position: relative; }
     .headline-style {
            position: absolute; top: 15%; left: 8%;
            font-family: var(--font-hero); font-size: 65px; line-height: 0.9;
            color: var(--accent-yellow); text-shadow: 2px 2px 10px rgba(0,0,0,0.4); z-index: 10;
        }
     .btn-hero-shop {
            position: absolute; bottom: 30px; right: 30px;
            background-color: var(--primary-red); color: white; border: none;
            padding: 10px 22px; font-weight: bold; cursor: pointer;
        }

        /* PRODUCTS SECTION */
     .section-products { width: 100%; display: flex; flex-direction: column; align-items: center; padding: 60px 0; }
     .section-title { color: var(--primary-red); font-size: 36px; margin-bottom: 40px; text-align: center; }

        /* CENTERED PENTAGON - Plugs into Cluster Gaps */
     .pentagon-info {
            width: 280px; background-color: var(--primary-red); color: white;
            padding: 30px 20px; margin-bottom: -40px;
            clip-path: polygon(0% 0%, 100% 0%, 100% 80%, 50% 100%, 0% 80%);
            z-index: 20; text-align: center;
        }
     .pentagon-title { font-size: 24px; margin-bottom: 15px; }
     .list-features { list-style: none; display: inline-block; text-align: left; }
     .list-features li { margin-bottom: 8px; display: flex; align-items: center; font-size: 15px; }
     .list-features li::before {
            content: '✓'; margin-right: 10px; width: 20px; height: 20px;
            border: 2px solid white; border-radius: 50%; display: flex;
            justify-content: center; align-items: center; font-size: 10px;
        }

        /* CENTERED 3-2-1 PYRAMID CLUSTER */
     .honeycomb-cluster {
            display: flex; flex-direction: column; align-items: center;
            margin-top: 40px; width: 100%;
        }

     .hex-row { display: flex; justify-content: center; gap: 4px; width: 100%; }
     .hex-item {
            width: 140px; height: 160px; position: relative;
            display: flex; flex-direction: column; align-items: center;
        }
     .hex-shape {
            width: 130px; height: 150px; background-color: #f5f5f5;
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            display: flex; justify-content: center; align-items: center; overflow: hidden;
            border: 3px solid var(--accent-yellow); position: relative;
        }
     .hex-shape::after {
            content: ""; position: absolute; inset: 0; pointer-events: none;
            border: 5px solid var(--accent-yellow); 
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        }
     .hex-shape img { width: 80%; height: auto; object-fit: contain; }

        /* Interlock Calculation: -35px vertical pull to stack the points */
     .row-2 { margin-top: -35px; }
     .row-3 { margin-top: -35px; }

        /* FOOTER */
     .footer-contact { background-color: var(--primary-red); color: white; padding: 30px 0; width: 100%; margin-top: 100px; }
     .footer-container { width: 95%; max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
     .footer-info { display: flex; gap: 40px; font-size: 14px; }
     .info-col span { color: var(--accent-yellow); font-weight: bold; }
     .social-icons { display: flex; gap: 15px; align-items: center; }
     .social-circle { width: 32px; height: 32px; background: white; border-radius: 50%; display: flex; justify-content: center; align-items: center; color: var(--primary-red); font-weight: bold; }

        /* PORTRAIT SQUEEZE LOGIC */
        @media (max-width: 768px) {
         .header-container { flex-direction: column; gap: 10px; }
         .nav-list { font-size: 12px; gap: 10px; flex-wrap: wrap; justify-content: center; }
         .section-hero { grid-template-columns: repeat(2, 1fr); height: 350px; }
         .headline-style { font-size: 40px; }
         .honeycomb-cluster { transform: scale(0.85); width: 100%; }
         .footer-container { flex-direction: column; gap: 20px; text-align: center; }
         .footer-info { flex-direction: column; gap: 15px; }
        }
    </style>
</head>
<body>
    <header class="header-global">
        <div class="header-container">
            <img src="assets/rj_logo.png" class="logo-rj-outfits" alt="Logo">
            <nav>
                <ul class="nav-list">
                    <li><span class="menu-dashes">&#9776;</span></li>
                    <li><a href="#" class="active">Home</a></li>
                    <li><a href="#">Products</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Contact</a></li>
                    <li><button class="btn-shop-header">Shop Now</button></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="section-hero">
        <div class="hero-pane pane-1"></div>
        <div class="hero-pane pane-2"></div>
        <div class="hero-pane pane-3"></div>
        <div class="hero-pane pane-4"><button class="btn-hero-shop">SHOP NOW</button></div>
        <h1 class="headline-style">STYLE<br>YOUR<br>STORY</h1>
    </section>

    <section class="section-products">
        <h2 class="section-title">Our Products</h2>
        
        <div class="pentagon-info">
            <h3 class="pentagon-title">Why Choose Us?</h3>
            <ul class="list-features">
                <li>Quality Fabrics</li>
                <li>Latest Trends</li>
                <li>Fast Delivery</li>
            </ul>
        </div>

        <div class="honeycomb-cluster">
            <div class="hex-row row-1">
                <div class="hex-item"><div class="hex-shape"><img src="assets/folded.png"></div></div>
                <div class="hex-item"><div class="hex-shape"><img src="assets/plain_tshirts.png"></div></div>
                <div class="hex-item"><div class="hex-shape"><img src="assets/long_sleeves.png"></div></div>
            </div>

            <div class="hex-row row-2">
                <div class="hex-item"><div class="hex-shape"><img src="assets/shorts.png"></div></div>
                <div class="hex-item"><div class="hex-shape"><img src="assets/boys_sleeves.png"></div></div>
            </div>

            <div class="hex-row row-3">
                <div class="hex-item"><div class="hex-shape"><img src="assets/underwear.png"></div></div>
            </div>
        </div>
    </section>

    <footer class="footer-contact">
        <div class="footer-container">
            <div class="footer-info">
                <div class="info-col"><span>Cuntacts:</span>WhatsApp: 9994371233<br>Phone: 0938607846</div>
                <div class="info-col"><span>Location:</span>Bunda Campus,<br>Near Bunda COAP</div>
            </div>
            <div class="social-icons">
                <div class="social-circle">f</div><div class="social-circle">t</div><div class="social-circle">y</div>
            </div>
        </div>
    </footer>
</body>
</html>
"""

# Renders the website code into your dashboard environment
components.html(website_code, height=2000, scrolling=True)
