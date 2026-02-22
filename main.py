<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RJ OUTFITS | Responsive Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        /* CORE VARIABLES & RESET */
        :root {
            --primary-red: #A51D1D;
            --accent-yellow: #FBBF0D;
            --bright-red: #CF2027;
            --bg-off-white: #F5F5F5;
            --text-charcoal: #1A1A1A;
            --font-main: 'Roboto', sans-serif;
            --font-hero: 'Archivo Black', sans-serif;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: var(--font-main); background-color: #FFF; overflow-x: hidden; }

        /* HEADER - Optimized for all widths */
       .header-global {
            height: 80px; width: 100%;
            display: flex; justify-content: center; align-items: center;
            border-bottom: 3px solid var(--accent-yellow);
            background: #FFF; position: sticky; top: 0; z-index: 1000;
        }
       .header-container {
            width: 100%; max-width: 1200px;
            display: flex; justify-content: space-between; align-items: center;
            padding: 0 20px;
        }
       .logo-rj-outfits { height: 44px; }
       .nav-main { display: flex; align-items: center; gap: 20px; }
       .nav-list { display: flex; list-style: none; gap: 15px; }
       .nav-list a { text-decoration: none; color: var(--text-charcoal); font-weight: 500; font-size: 14px; white-space: nowrap; }
       .nav-list a.active { color: var(--primary-red); border-bottom: 2px solid var(--primary-red); }
       .btn-shop-header {
            background-color: var(--primary-red); color: white; border: none;
            padding: 8px 16px; border-radius: 4px; font-weight: bold; cursor: pointer;
        }

        /* HERO - Responsive 4-pane grid */
       .section-hero { position: relative; width: 100%; height: 500px; display: grid; grid-template-columns: repeat(4, 1fr); background: #eee; }
       .hero-pane { background-size: cover; background-position: center; border-right: 1px solid rgba(255,255,255,0.2); }
       .pane-1 { background-image: url('assets/hero_1.jpg'); }
       .pane-2 { background-image: url('assets/hero_2.jpg'); }
       .pane-3 { background-image: url('assets/hero_3.jpg'); }
       .pane-4 { background-image: url('assets/hero_4.jpg'); position: relative; }
        
       .headline-style {
            position: absolute; top: 15%; left: 10%;
            font-family: var(--font-hero); font-size: 72px; line-height: 0.9;
            color: var(--accent-yellow); text-shadow: 2px 2px 10px rgba(0,0,0,0.4); z-index: 10;
        }
       .btn-hero-shop {
            position: absolute; bottom: 30px; right: 30px;
            background-color: var(--bright-red); color: white; border: none;
            padding: 10px 25px; font-weight: bold; cursor: pointer;
        }

        /* PRODUCTS SECTION */
       .section-products { width: 100%; max-width: 1200px; margin: 40px auto; padding: 0 20px; }
       .section-title { color: var(--primary-red); font-size: 32px; margin-bottom: 30px; }
       .product-content-wrapper { display: flex; gap: 40px; align-items: flex-start; }

        /* Ribbon / Sidebar */
       .ribbon-sidebar {
            width: 380px; flex-shrink: 0; background-color: var(--primary-red); color: white;
            padding: 40px 30px; clip-path: polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0 100%);
        }
       .ribbon-title { font-size: 32px; margin-bottom: 25px; line-height: 1.1; }
       .list-features { list-style: none; }
       .list-features li { margin-bottom: 12px; display: flex; align-items: center; font-size: 18px; }
       .list-features li::before {
            content: '✓'; margin-right: 12px; border: 2px solid white; border-radius: 50%;
            width: 24px; height: 24px; display: flex; justify-content: center; align-items: center; font-size: 12px;
        }

        /* Hexagonal Grid Physics */
       .grid-honeycomb {
            flex-grow: 1; display: grid; grid-template-columns: repeat(auto-fill, 160px);
            grid-gap: 20px; justify-content: center;
        }
       .hex-container { display: flex; flex-direction: column; align-items: center; width: 160px; }
       .hex-shape {
            width: 140px; height: 160px; background-color: #f0f0f0;
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            border: 3px solid var(--accent-yellow); display: flex; justify-content: center; align-items: center;
            overflow: hidden; background-size: cover;
        }
       .hex-shape img { width: 90%; height: auto; }
       .hex-label { margin-top: 8px; font-size: 13px; font-weight: bold; color: #444; text-align: center; }
       .hex-item:nth-child(even) { transform: translateY(40px); }

        /* FOOTER */
       .footer-contact { background-color: var(--primary-red); color: white; padding: 40px 0; width: 100%; margin-top: 80px; }
       .footer-container {
            width: 100%; max-width: 1200px; margin: 0 auto;
            display: flex; justify-content: space-between; align-items: center; padding: 0 20px;
        }
       .footer-info { display: flex; gap: 40px; }
       .info-col span { color: var(--accent-yellow); font-weight: bold; display: block; margin-bottom: 5px; }
       .social-icons { display: flex; gap: 15px; align-items: center; }
       .social-circle {
            width: 32px; height: 32px; background: white; border-radius: 50%;
            display: flex; justify-content: center; align-items: center; color: var(--primary-red); font-weight: bold;
        }
       .spark-icon { width: 30px; margin-left: 15px; filter: brightness(0) invert(1); }

        /* PORTRAIT / MOBILE SQUEEZE LOGIC */
        @media (max-width: 800px) {
           .header-container { flex-direction: column; height: auto; padding: 10px; }
           .nav-main { margin-top: 10px; width: 100%; justify-content: space-between; }
           .nav-list { gap: 10px; }
           .nav-list a { font-size: 12px; }
            
           .section-hero { grid-template-columns: repeat(2, 1fr); height: 400px; }
           .headline-style { font-size: 42px; top: 10%; left: 5%; }
            
           .product-content-wrapper { flex-direction: column; align-items: center; }
           .ribbon-sidebar { width: 100%; clip-path: polygon(0 0, 100% 0, 100% 90%, 50% 100%, 0 90%); margin-bottom: 40px; }
            
           .grid-honeycomb { width: 100%; padding-bottom: 60px; }
           .hex-item:nth-child(even) { transform: none; margin-top: 10px; } /* Remove stagger for mobile readability */
            
           .footer-container { flex-direction: column; text-align: center; gap: 30px; }
           .footer-info { flex-direction: column; gap: 20px; }
        }
    </style>
</head>
<body>
    <header class="header-global">
        <div class="header-container">
            <img src="assets/rj_logo.png" class="logo-rj-outfits" alt="RJ OUTFITS">
            <div class="nav-main">
                <ul class="nav-list">
                    <li><a href="#" class="active">Home</a></li>
                    <li><a href="#">Products</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
                <button class="btn-shop-header">Shor Now</button>
            </div>
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
                <div class="info-col"><span>Cuntacts:</span>WhatsApp: 9994371233<br>Phone Call: 0938607846</div>
                <div class="info-col"><span>Location:</span>Bunda Campus,<br>Near Bunda COAP</div>
            </div>
            <div class="social-icons">
                <div class="social-circle">f</div><div class="social-circle">t</div><div class="social-circle">y</div>
                <img src="assets/spark.svg" class="spark-icon" alt="Spark">
            </div>
        </div>
    </footer>
</body>
</html>
