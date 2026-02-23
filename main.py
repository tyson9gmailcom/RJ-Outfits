import streamlit as st
import streamlit.components.v1 as components

# 1. PAGE CONFIG
st.set_page_config(layout="wide", page_title="RJ OUTFITS")

# ---------------------------------------------------------
# 2. GLOBAL STYLES (The CSS "Brain")
# ---------------------------------------------------------
style_section = """
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

    /* Header Styles */
    .header-global { height: 80px; width: 100%; display: flex; justify-content: center; align-items: center; border-bottom: 3px solid var(--accent-yellow); background: #FFF; }
    .header-container { width: 95%; max-width: 1200px; display: flex; justify-content: space-between; align-items: center; }
    .logo-rj-outfits { height: 44px; }
    .nav-list { display: flex; list-style: none; gap: 15px; align-items: center; }
    .nav-list a { text-decoration: none; color: var(--text-charcoal); font-weight: 500; font-size: 15px; }
    .nav-list a.active { color: var(--primary-red); border-bottom: 2px solid var(--primary-red); }
    .btn-shop-header { background-color: var(--primary-red); color: white; border: none; padding: 8px 18px; border-radius: 4px; font-weight: bold; cursor: pointer; }

    /* Hero Styles */
    .section-hero { position: relative; width: 100%; height: 450px; display: grid; grid-template-columns: repeat(4, 1fr); }
    .hero-pane { background-size: cover; background-position: center; border-right: 1px solid rgba(255,255,255,0.1); }
    .pane-1 { background-image: url('assets/hero_1.jpg'); }
    .pane-2 { background-image: url('assets/hero_2.jpg'); }
    .pane-3 { background-image: url('assets/hero_3.jpg'); }
    .pane-4 { background-image: url('assets/hero_4.jpg'); position: relative; }
    .headline-style { position: absolute; top: 15%; left: 8%; font-family: var(--font-hero); font-size: 65px; line-height: 0.9; color: var(--accent-yellow); text-shadow: 2px 2px 10px rgba(0,0,0,0.4); z-index: 10; }
    .btn-hero-shop { position: absolute; bottom: 30px; right: 30px; background-color: var(--primary-red); color: white; border: none; padding: 10px 22px; font-weight: bold; cursor: pointer; }

    /* Product/Honeycomb Styles */
    .section-products { width: 100%; display: flex; flex-direction: column; align-items: center; padding: 60px 0; }
    .section-title { color: var(--primary-red); font-size: 36px; margin-bottom: 40px; text-align: center; }
    .pentagon-info { width: 280px; background-color: var(--primary-red); color: white; padding: 30px 20px; margin-bottom: -40px; clip-path: polygon(0% 0%, 100% 0%, 100% 80%, 50% 100%, 0% 80%); z-index: 20; text-align: center; }
    .honeycomb-cluster { display: flex; flex-direction: column; align-items: center; margin-top: 40px; width: 100%; }
    .hex-row { display: flex; justify-content: center; gap: 4px; width: 100%; }
    .hex-shape { width: 130px; height: 150px; background-color: #f5f5f5; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); display: flex; justify-content: center; align-items: center; border: 3px solid var(--accent-yellow); position: relative; }
    .hex-shape img { width: 80%; height: auto; object-fit: contain; }
    .row-2, .row-3 { margin-top: -35px; }

    /* Footer Styles */
    .footer-contact { background-color: var(--primary-red); color: white; padding: 30px 0; width: 100%; margin-top: 100px; }
    .footer-container { width: 95%; max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }

    @media (max-width: 768px) {
        .section-hero { grid-template-columns: repeat(2, 1fr); height: 350px; }
        .headline-style { font-size: 40px; }
    }
</style>
"""

# ---------------------------------------------------------
# 3. HTML COMPONENTS (The "Lego Bricks")
# ---------------------------------------------------------
header_html = """
<header class="header-global">
    <div class="header-container">
        <img src="assets/rj_logo.png" class="logo-rj-outfits" alt="Logo">
        <nav><ul class="nav-list">
            <li><a href="#" class="active">Home</a></li>
            <li><a href="#">Products</a></li>
            <li><a href="#">About Us</a></li>
            <li><button class="btn-shop-header">Shop Now</button></li>
        </ul></nav>
    </div>
</header>
"""

hero_html = """
<section class="section-hero">
    <div class="hero-pane pane-1"></div><div class="hero-pane pane-2"></div>
    <div class="hero-pane pane-3"></div><div class="hero-pane pane-4">
        <button class="btn-hero-shop">SHOP NOW</button>
    </div>
    <h1 class="headline-style">STYLE<br>YOUR<br>STORY</h1>
</section>
"""

# Imagine you want to add this later!
new_feature_placeholder = """
"""

products_html = """
<section class="section-products">
    <h2 class="section-title">Our Products</h2>
    <div class="pentagon-info">
        <h3>Why Choose Us?</h3>
        <p>Quality Fabrics • Latest Trends</p>
    </div>
    <div class="honeycomb-cluster">
        <div class="hex-row row-1">
            <div class="hex-shape"><img src="assets/folded.png"></div>
            <div class="hex-shape"><img src="assets/plain_tshirts.png"></div>
        </div>
    </div>
</section>
"""

footer_html = """
<footer class="footer-contact">
    <div class="footer-container">
        <div>WhatsApp: 9994371233</div>
        <div>Location: Bunda Campus</div>
    </div>
</footer>
"""

# ---------------------------------------------------------
# 4. THE ASSEMBLY (Building the Page)
# ---------------------------------------------------------

# This list defines the order of your Home Tab
home_page_elements = [
    style_section,
    header_html,
    hero_html,
    new_feature_placeholder, # Add new variables here!
    products_html,
    footer_html
]

# Join all parts into one string
final_website_code = "".join(home_page_elements)

# Render
components.html(final_website_code, height=2000, scrolling=True)
