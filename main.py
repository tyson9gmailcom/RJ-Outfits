import streamlit as st
import streamlit.components.v1 as components

# Configures the dashboard to fill the phone/web screen
st.set_page_config(layout="wide", page_title="RJ OUTFITS")

# --- SECTION 1: HTML HEAD & CSS ---
html_start_and_css = """
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

     .hex-row
