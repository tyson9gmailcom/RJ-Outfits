import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os
import urllib.parse
from PIL import Image

# Configures the dashboard
st.set_page_config(layout="wide", page_title="RJ OUTFITS")

# --- DATABASE & FILE LOGIC ---
INVENTORY_FILE = "inventory.csv"
ORDERS_FILE = "orders.csv"
UPLOAD_DIR = "assets"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def load_data():
    if os.path.exists(INVENTORY_FILE):
        return pd.read_csv(INVENTORY_FILE).to_dict('records')
    else:
        return [
            {"id": 1, "name": "Plain T-Shirt", "price": 15000, "stock": 10, "img": "assets/plain_tshirts.png"},
            {"id": 2, "name": "Long Sleeves", "price": 25000, "stock": 5, "img": "assets/long_sleeves.png"},
        ]

def save_all():
    pd.DataFrame(st.session_state.inventory).to_csv(INVENTORY_FILE, index=False)
    pd.DataFrame(st.session_state.orders, columns=["Order Details"]).to_csv(ORDERS_FILE, index=False)

if 'inventory' not in st.session_state:
    st.session_state.inventory = load_data()
if 'orders' not in st.session_state:
    st.session_state.orders = pd.read_csv(ORDERS_FILE)["Order Details"].tolist() if os.path.exists(ORDERS_FILE) else []

# --- SECTION 1: STYLES ---
html_start = """<!DOCTYPE html>
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

        .header-global { height: 80px; width: 100%; display: flex; justify-content: center; align-items: center; border-bottom: 3px solid var(--accent-yellow); background: #FFF; }
        .header-container { width: 95%; max-width: 1200px; display: flex; justify-content: space-between; align-items: center; }
        .logo-rj-outfits { height: 44px; }
        .nav-list { display: flex; list-style: none; gap: 15px; align-items: center; }
        .nav-list a { text-decoration: none; color: var(--text-charcoal); font-weight: 500; font-size: 15px; }
        .btn-shop-header { background-color: var(--primary-red); color: white; border: none; padding: 8px 18px; border-radius: 4px; font-weight: bold; cursor: pointer; }

        .section-hero { position: relative; width: 100%; height: 450px; display: grid; grid-template-columns: repeat(4, 1fr); }
        .hero-pane { background-size: cover; background-position: center; }
        .pane-1 { background-image: url('assets/hero_1.jpg'); }
        .pane-2 { background-image: url('assets/hero_2.jpg'); }
        .pane-3 { background-image: url('assets/hero_3.jpg'); }
        .pane-4 { background-image: url('assets/hero_4.jpg'); position: relative; }
        .headline-style { position: absolute; top: 15%; left: 8%; font-family: var(--font-hero); font-size: 65px; line-height: 0.9; color: var(--accent-yellow); text-shadow: 2px 2px 10px rgba(0,0,0,0.4); z-index: 10; }
        
        .section-products { width: 100%; display: flex; flex-direction: column; align-items: center; padding: 60px 0; }
        .section-title { color: var(--primary-red); font-size: 36px; margin-bottom: 40px; }

        .footer-contact { background-color: var(--primary-red); color: white; padding: 30px 0; width: 100%; }
        .footer-container { width: 95%; max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
        
        @media (max-width: 768px) {
            .section-hero { grid-template-columns: repeat(2, 1fr); }
            .headline-style { font-size: 40px; }
        }
    </style>
</head>
<body>
"""

# --- SECTION 2: HEADER (With Clickable Link) ---
header_block = """
    <header class="header-global">
        <div class="header-container">
            <img src="assets/rj_logo.png" class="logo-rj-outfits" alt="Logo">
            <nav>
                <ul class="nav-list">
                    <li><a href="#">Home</a></li>
                    <li><a href="#shop-now" target="_parent">Products</a></li>
                    <li><a href="#shop-now" target="_parent"><button class="btn-shop-header">Shop Now</button></a></li>
                </ul>
            </nav>
        </div>
    </header>
"""

hero_block = """
    <section class="section-hero">
        <div class="hero-pane pane-1"></div>
        <div class="hero-pane pane-2"></div>
        <div class="hero-pane pane-3"></div>
        <div class="hero-pane pane-4">
            <a href="#shop-now" target="_parent"><button style="position: absolute; bottom: 30px; right: 30px; background: #A51D1D; color: white; border: none; padding: 10px 22px; font-weight: bold; cursor: pointer;">SHOP NOW</button></a>
        </div>
        <h1 class="headline-style">STYLE<br>YOUR<br>STORY</h1>
    </section>
"""

footer_block = """
    <footer class="footer-contact">
        <div class="footer-container">
            <div><span>Contacts:</span> WhatsApp: 9994371233 | Phone: 0938607846</div>
            <div>RJ OUTFITS © 2024</div>
        </div>
    </footer>
</body>
</html>
"""

# --- RENDER TOP SECTION ---
website_code = html_start + header_block + hero_block + footer_block
components.html(website_code, height=600, scrolling=False)

# --- THE SHOP ANCHOR ---
st.markdown('<div id="shop-now"></div>', unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("RJ Navigation")
app_mode = st.sidebar.radio("Go to:", ["Storefront", "RJ Office (Admin)"])

if app_mode == "Storefront":
    st.header("🛍️ Our Collection")
    cols = st.columns(3)
    for i, item in enumerate(st.session_state.inventory):
        with cols[i % 3]:
            if os.path.exists(str(item['img'])):
                st.image(item['img'], use_container_width=True)
            st.subheader(item['name'])
            st.write(f"💰 MK {item['price']:,} | 📦 Stock: {item['stock']}")
            
            if item['stock'] > 0:
                if st.button(f"Buy {item['name']}", key=f"b_{i}"):
                    item['stock'] -= 1
                    st.session_state.orders.append(f"Order: {item['name']} - MK {item['price']}")
                    save_all()
                    msg = urllib.parse.quote(f"Hi RJ Outfits! I'm buying {item['name']} for MK {item['price']}. Send Agent Code!")
                    st.markdown(f'<a href="https://wa.me/2659994371233?text={msg}" target="_blank"><button style="background:#25D366; color:white; border:none; padding:10px; width:100%; border-radius:5px; font-weight:bold; cursor:pointer;">Confirm on WhatsApp</button></a>', unsafe_allow_html=True)
            else:
                st.error("Out of Stock")

elif app_mode == "RJ Office (Admin)":
    st.title("🛡️ Admin Panel")
    if st.text_input("Password", type="password") == "RJ2024":
        t1, t2, t3 = st.tabs(["Orders", "Stock", "Add New"])
        with t1:
            for o in reversed(st.session_state.orders): st.info(o)
        with t2:
            for idx, itm in enumerate(st.session_state.inventory):
                st.session_state.inventory[idx]['stock'] = st.number_input(f"Stock: {itm['name']}", value=itm['stock'], key=f"s_{idx}")
            if st.button("Save Changes"): save_all(); st.success("Updated!")
        with t3:
            with st.form("add_p"):
                name = st.text_input("Product Name")
                price = st.number_input("Price (MK)", min_value=0)
                img = st.file_uploader("Image", type=['jpg','png','jpeg'])
                if st.form_submit_button("List Product"):
                    if img and name:
                        path = os.path.join(UPLOAD_DIR, img.name)
                        with open(path, "wb") as f: f.write(img.getbuffer())
                        st.session_state.inventory.append({"id": len(st.session_state.inventory)+1, "name": name, "price": price, "stock": 5, "img": path})
                        save_all(); st.rerun()
