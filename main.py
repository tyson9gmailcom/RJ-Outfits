import streamlit as st
import streamlit.components.v1 as components

# Set the dashboard to wide mode to fit the design
st.set_page_config(layout="wide")

# This is the complete code for your website
website_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RJ OUTFITS | Style Your Story</title>
    <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-red: #A51D1D;
            --accent-yellow: #FBBF0D;
            --bright-red: #CF2027;
            --text-charcoal: #1A1A1A;
            --font-main: 'Roboto', sans-serif;
            --font-hero: 'Archivo Black', sans-serif;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: var(--font-main); background-color: #FFF; overflow-x: hidden; }

        /* HEADER */
       .header-global { height: 80px; width: 100%; display: flex; justify-content: center; align-items: center; border-bottom: 2px solid #ddd; background: #FFF; }
       .header-container { width: 1200px; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; }
       .logo-rj-outfits { height: 44px; }
       .nav-list { display: flex; list-style: none; gap: 25px; align-items: center; }
       .nav-list a { text-decoration: none; color: var(--text-charcoal); font-weight: 500; font-size: 16px; }
       .nav-list a.active { color: var(--primary-red); border-bottom: 2px solid var(--primary-red); padding-bottom: 5px; }
       .btn-shop-header { background-color: var(--primary-red); color: white; border: none; padding: 10px 20px; border-radius: 4px; font-weight: bold; cursor: pointer; }

        /* HERO */
       .section-hero { position: relative; height: 400px; width: 100%; display: grid; grid-template-columns: repeat(4, 1fr); }
       .hero-pane { background-size: cover; background-position: center; border-right: 1px solid rgba(255,255,255,0.1); }
       .pane-1 { background-image: url('https://raw.githubusercontent.com/user/repo/main/assets/hero_1.jpg'); }
       .pane-2 { background-image: url('https://raw.githubusercontent.com/user/repo/main/assets/hero_2.jpg'); }
       .pane-3 { background-image: url('https://raw.githubusercontent.com/user/repo/main/assets/hero_3.jpg'); }
       .pane-4 { background-image: url('https://raw.githubusercontent.com/user/repo/main/assets/hero_4.jpg'); position: relative; }
       .headline-style { position: absolute; top: 80px; left: 10%; font-family: var(--font-hero); font-size: 70px; line-height: 0.9; color: var(--accent-yellow); z-index: 10; text-transform: uppercase; }
       .btn-hero-shop { position: absolute; bottom: 30px; right: 30px; background-color: var(--primary-red); color: white; border: none; padding: 10px 20px; font-weight: bold; cursor: pointer; font-size: 12px; }

        /* PRODUCTS */
       .section-products { width: 1200px; margin: 40px auto; padding: 0 20px; }
       .section-title { color: var(--primary-red); font-size: 32px; margin-bottom: 30px; font-weight: 700; }
       .product-content-wrapper { display: flex; gap: 40px; }
       .ribbon-sidebar { width: 350px; background-color: var(--primary-red); color: white; padding: 40px 30px; clip-path: polygon(0 0, 88% 0, 100% 50%, 88% 100%, 0 100%); }
       .ribbon-title { font-size: 32px; margin-bottom: 25px; line-height: 1.1; font-weight: 700; }
       .list-features { list-style: none; }
       .list-features li { margin-bottom: 12px; display: flex; align-items: center; font-size: 18px; font-weight: 500; }
       .list-features li::before { content: '✔'; margin-right: 12px; width: 22px; height: 22px; border: 2px solid white; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 12px; }

        /* HEX GRID */
       .grid-honeycomb { flex-grow: 1; display: grid; grid-template-columns: repeat(3, 150px); grid-gap: 20px; position: relative; }
       .hex-container { display: flex; flex-direction: column; align-items: center; position: relative; }
       .hex-shape { width: 140px; height: 160px; background-color: #eee; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); border: 3px solid var(--accent-yellow); display: flex; justify-content: center; align-items: center; overflow: hidden; }
       .hex-shape img { width: 90%; height: auto; }
       .hex-label { margin-top: 8px; font-size: 13px; font-weight: bold; text-align: center; color: #555; }
       .hex-item:nth-child(even) { margin-top: 60px; }

        /* FOOTER */
       .footer-contact { background-color: var(--primary-red); color: white; padding: 25px 0; width: 100%; margin-top: 60px; }
       .footer-container { width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; }
       .footer-info { display: flex; gap: 50px; font-size: 14px; }
       .info-col p { margin-bottom: 4px; }
       .info-col span { color: var(--accent-yellow); font-weight: bold; }
       .social-icons { display: flex; gap: 12px; align-items: center; }
       .social-circle { width: 28px; height: 28px; background: white; border-radius: 50%; display: flex; justify-content: center; align-items: center; color: var(--primary-red); font-size: 14px; font-weight: bold; }
       .spark-icon { width: 35px; margin-left: 15px; }
    </style>
</head>
<body>
    <header class="header-global">
        <div class="header-container">
            <img src="https://raw.githubusercontent.com/user/repo/main/assets/rj_logo.png" class="logo-rj-outfits" alt="RJ OUTFITS">
            <nav><ul class="nav-list">
                <li><a href="#" class="active">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Contact</a></li>
            </ul></nav>
            <button class="btn-shop-header">Shor Now</button>
        </div>
    </header>

    <section class="section-hero">
        <div class="hero-pane pane-1"></div><div class="hero-pane pane-2"></div><div class="hero-pane pane-3"></div>
        <div class="hero-pane pane-4"><button class="btn-hero-shop">SHOP NOW</button></div>
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
                <div class="hex-container hex-item"><div class="hex-shape"></div><p class="hex-label">Plain T-shirts</p></div>
                <div class="hex-container hex-item"><div class="hex-shape"></div></div>
                <div class="hex-container hex-item"><div class="hex-shape"></div><p class="hex-label">Long Sleeves</p></div>
                <div class="hex-container hex-item"><div class="hex-shape"></div></div>
                <div class="hex-container hex-item"><div class="hex-shape"></div><p class="hex-label">Boys Sleeves</p></div>
                <div class="hex-container hex-item"><div class="hex-shape"></div></div>
            </div>
        </div>
    </section>

    <footer class="footer-contact">
        <div class="footer-container">
            <div class="footer-info">
                <div class="info-col">
                    <p><span>Cuntacts:</span></p>
                    <p>WhatsApp: 9994371233</p>
                    <p>Phone Call: 0938607846</p>
                </div>
                <div class="info-col">
                    <p><span>Location:</span> Bunda Campus,</p>
                    <p>Near Bunda COAP</p>
                </div>
            </div>
            <div class="social-icons">
                <div class="social-circle">f</div><div class="social-circle">t</div><div class="social-circle">y</div>
                <img src="https://raw.githubusercontent.com/user/repo/main/assets/spark.svg" class="spark-icon">
            </div>
        </div>
    </footer>
</body>
</html>
"""

# Render the HTML
components.html(website_html, height=1200, scrolling=True)
