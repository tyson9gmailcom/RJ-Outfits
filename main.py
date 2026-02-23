import streamlit as st
import streamlit.components.v1 as components

# Configures the dashboard to fill the phone/web screen
st.set_page_config(layout="wide", page_title="RJ OUTFITS")

# Final website code with Aligned Footer, Symbols, and Pyramid Honeycomb
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

        /* CENTERED PENTAGON */
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

        /* 3-2-1 CENTERING PYRAMID CLUSTER */
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
     .row-2 { margin-top: -35px; }
     .row-3 { margin-top: -35px; }

        /* FOOTER - Aligned Grid with Symbols */
     .footer-contact { background-color: var(--primary-red); color: white; padding: 40px 0; width: 100%; margin-top: 100px; }
     .footer-container {
            width: 95%; max-width: 1200px; margin: 0 auto;
            display: grid; grid-template-columns: 1.5fr 1fr; align-items: flex-start; gap: 40px;
        }
     .footer-grid-col { display: flex; flex-direction: column; gap: 10px; }
     .footer-grid-col span { color: var(--accent-yellow); font-weight: bold; font-size: 16px; margin-bottom: 5px; }
     .footer-text { display: flex; align-items: center; gap: 10px; font-size: 15px; margin: 2px 0; }
      
     .icon-inline { width: 18px; height: 18px; fill: white; }

     .social-icons { display: flex; gap: 15px; align-items: center; grid-column: span 2; justify-content: flex-end; margin-top: 20px; }
     .social-circle {
            width: 36px; height: 36px; background: white; border-radius: 50%;
            display: flex; justify-content: center; align-items: center; color: var(--primary-red);
        }
     .social-svg { width: 20px; height: 20px; fill: var(--primary-red); }

        /* PORTRAIT SQUEEZE */
        @media (max-width: 768px) {
         .header-container { flex-direction: column; gap: 10px; }
         .section-hero { grid-template-columns: repeat(2, 1fr); height: 350px; }
         .honeycomb-cluster { transform: scale(0.85); }
         .footer-container { grid-template-columns: 1fr; text-align: left; }
         .social-icons { justify-content: center; }
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
            <div class="footer-grid-col">
                <span>Cuntacts:</span>
                <div class="footer-text">WhatsApp: 9994371233 
                    <svg class="icon-inline" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.025 3.207l-.695 2.54 2.597-.682c.912.579 1.817.935 2.844.935 3.181 0 5.767-2.586 5.767-5.766 0-3.18-2.587-5.766-5.77-5.766zm3.377 8.203c-.145.405-.845.74-1.164.786-.348.05-1.576.25-3.036-.353-1.46-.603-2.392-2.097-2.465-2.193-.072-.096-.603-.801-.603-1.528 0-.727.382-1.085.518-1.23.136-.145.298-.182.397-.182h.262c.088 0.197.001.284.209.1.238.348.847.379.912.031.065.051.14.01.223-.041.083-.062.135-.124.207-.063.073-.131.161-.188.223-.058.063-.119.13-.051.248.067.119.3.498.644.805.443.393.818.514.933.571.115.057.183.048.25-.03.068-.078.29-.339.367-.454.077-.115.155-.097.262-.057.106.04 1.133.535 1.133.535s.114.054.145.107c.031.053.031.307-.114.712z"/></svg>
                </div>
                <div class="footer-text">Phone: 0938607846
                    <svg class="icon-inline" viewBox="0 0 24 24"><path d="M17 1H7c-1.1 0-2.9-2 2v18c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V3c0-1.1-.9-2-2-2zm-5 20c-.55 0-1-.45-1-1s.45-1 1-1 1.45 1 1-.45 1-1 1zm5.25-4H6.75V4h10.5v13z"/></svg>
                </div>
            </div>
            
            <div class="footer-grid-col">
                <span>Location: 
                    <svg class="icon-inline" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                </span>
                <div class="footer-text">Bunda Campus,</div>
                <div class="footer-text">Near Bunda COAP</div>
            </div>
            
            <div class="social-icons">
                <div class="social-circle">
                    <svg class="social-svg" viewBox="0 0 24 24"><path d="M22.675 0h-21.35c-.732 0-1.325.593-1.325 1.325v21.351c0.731.593 1.324 1.325 1.324h11.495v-9.294h-3.128v-3.622h3.128v-2.671c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.504 0-1.795.715-1.795 1.763v2.313h3.587l-.467 3.622h-3.12v9.293h6.116c.73 0 1.323-.593 1.323-1.325v-21.35c0-.732-.593-1.325-1.325-1.325z"/></svg>
                </div>
                <div class="social-circle">
                    <svg class="social-svg" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 0 1-2.825.775 4.958 4.958 0 0 0 2.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 0 0-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 0 0-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 0 1-2.228-.616v.06a4.923 4.923 0 0 0 3.946 4.84 4.996 4.996 0 0 1-2.212.085 4.936 4.936 0 0 0 4.604 3.417 9.867 9.867 0 0 1-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 0 0 7.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0 0 24 4.59z"/></svg>
                </div>
                <div class="social-circle">
                    <svg class="social-svg" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
"""

# Renders the website code into your dashboard environment
components.html(website_code, height=2000, scrolling=True)
