<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RJ OUTFITS | Style Your Story</title>
    <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        /* CSS ARCHITECTURAL SPECIFICATIONS */
        :root {
            --primary-red: #A51D1D;
            --accent-yellow: #FBBF0D;
            --bright-red: #CF2027;
            --bg-off-white: #F5F5F5;
            --text-charcoal: #1A1A1A;
            --footer-red: #A51D1D;
            --font-main: 'Roboto', sans-serif;
            --font-hero: 'Archivo Black', sans-serif;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-main);
            background-color: #FFFFFF;
            color: var(--text-charcoal);
            overflow-x: hidden;
        }

        /* I. GLOBAL HEADER */
       .header-global {
            height: 80px;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            border-bottom: 3px solid var(--accent-yellow);
            background: #FFF;
        }

       .header-container {
            width: 1200px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }

       .logo-rj-outfits {
            height: 44px; /* Exact height per report */
        }

       .nav-list {
            display: flex;
            list-style: none;
            gap: 30px;
        }

       .nav-list a {
            text-decoration: none;
            color: var(--text-charcoal);
            font-weight: 500;
            font-size: 16px;
        }

       .nav-list a.active {
            color: var(--primary-red);
            border-bottom: 2px solid var(--primary-red);
        }

       .btn-shop-header {
            background-color: var(--primary-red);
            color: white;
            border: none;
            padding: 10px 25px;
            border-radius: 4px;
            font-weight: bold;
            cursor: pointer;
            text-transform: uppercase;
        }

        /* II. HERO SECTION (4-PANE GRID) */
       .section-hero {
            position: relative;
            height: 450px;
            width: 100%;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
        }

       .hero-pane {
            background-size: cover;
            background-position: center;
            border-right: 1px solid rgba(255,255,255,0.2);
        }

        /* Image Placeholders based on GitHub naming request */
       .pane-1 { background-image: url('assets/hero_1.jpg'); }
       .pane-2 { background-image: url('assets/hero_2.jpg'); }
       .pane-3 { background-image: url('assets/hero_3.jpg'); }
       .pane-4 { 
            background-image: url('assets/hero_4.jpg'); 
            position: relative;
        }

       .headline-style {
            position: absolute;
            top: 100px;
            left: 15%;
            font-family: var(--font-hero);
            font-size: 72px;
            line-height: 0.9;
            color: var(--accent-yellow);
            text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
            z-index: 10;
        }

       .btn-hero-shop {
            position: absolute;
            bottom: 40px;
            right: 40px;
            background-color: var(--bright-red);
            color: white;
            border: none;
            padding: 12px 30px;
            font-weight: bold;
            cursor: pointer;
        }

        /* III. PRODUCT SHOWCASE SECTION */
       .section-products {
            width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }

       .section-title {
            color: var(--primary-red);
            font-size: 32px;
            margin-bottom: 30px;
        }

       .product-content-wrapper {
            display: flex;
            gap: 50px;
        }

        /* Why Choose Us Ribbon */
       .ribbon-sidebar {
            width: 380px;
            background-color: var(--primary-red);
            color: white;
            padding: 40px 30px;
            /* Creates the stylized arrow shape from the image */
            clip-path: polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0 100%);
        }

       .ribbon-title {
            font-size: 28px;
            margin-bottom: 25px;
            line-height: 1.2;
        }

       .list-features {
            list-style: none;
        }

       .list-features li {
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            font-size: 18px;
        }

       .list-features li::before {
            content: '✓';
            margin-right: 12px;
            background: white;
            color: var(--primary-red);
            width: 24px;
            height: 24px;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 50%;
            font-size: 14px;
            font-weight: bold;
        }

        /* Hexagonal Grid */
       .grid-honeycomb {
            flex-grow: 1;
            display: grid;
            grid-template-columns: repeat(3, 160px);
            grid-gap: 20px;
            padding-top: 20px;
        }

       .hex-container {
            position: relative;
            width: 180px;
            height: 200px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

       .hex-shape {
            width: 150px;
            height: 150px;
            background-color: white;
            /* Hexagon Clip Path */
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            border: 4px solid var(--accent-yellow); /* Yellow border from image */
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

       .hex-shape img {
            width: 80%;
            height: auto;
        }

       .hex-label {
            margin-top: 10px;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
        }

        /* Staggering the hexagons per image layout */
       .hex-item:nth-child(even) {
            margin-top: 50px;
        }

        /* IV. INFORMATION FOOTER */
       .footer-contact {
            background-color: var(--footer-red);
            color: white;
            padding: 30px 0;
            width: 100%;
            margin-top: 60px;
        }

       .footer-container {
            width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }

       .footer-info-group {
            display: flex;
            gap: 40px;
            font-size: 14px;
        }

       .contact-item {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

       .contact-label {
            font-weight: bold;
            color: var(--accent-yellow);
            margin-bottom: 5px;
        }

       .social-icons {
            display: flex;
            gap: 15px;
            align-items: center;
        }

       .social-icon {
            width: 32px;
            height: 32px;
            background: white;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: var(--primary-red);
            cursor: pointer;
        }

       .icon-spark {
            width: 30px;
            margin-left: 20px;
        }
    </style>
</head>
<body>

    <header class="header-global">
        <div class="header-container">
            <img src="assets/rj_logo.png" class="logo-rj-outfits" alt="RJ OUTFITS">
            <nav>
                <ul class="nav-list">
                    <li><a href="#" class="active">Home</a></li>
                    <li><a href="#">Products</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>
            <button class="btn-shop-header">Shop Now</button>
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
                <div class="hex-container hex-item">
                    <div class="hex-shape"><img src="assets/plain_tshirts.png" alt="Plain T-shirts"></div>
                    <p class="hex-label">Plain T-shirts</p>
                </div>
                <div class="hex-container hex-item">
                    <div class="hex-shape"><img src="assets/stack_folded.png" alt="Product"></div>
                </div>
                <div class="hex-container hex-item">
                    <div class="hex-shape"><img src="assets/long_sleeves.png" alt="Long Sleeves"></div>
                    <p class="hex-label">Long Sleeves</p>
                </div>
                <div class="hex-container hex-item">
                    <div class="hex-shape"><img src="assets/shorts.png" alt="Product"></div>
                </div>
                <div class="hex-container hex-item">
                    <div class="hex-shape"><img src="assets/boys_sleeves.png" alt="Boys Sleeves"></div>
                    <p class="hex-label">Boys Sleeves</p>
                </div>h
                <div class="hex-container hex-item">
                    <div class="hex-shape"><img src="assets/underwear.png" alt="Product"></div>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer-contact">
        <div class="footer-container">
            <div class="footer-info-group">
                <div class="contact-item">
                    <span class="contact-label">Contacts:</span>
                    <span>WhatsApp: 9994371233</span>
                    <span>Phone Call: 0938607846</span>
                </div>
                <div class="contact-item">
                    <span class="contact-label">Location:</span>
                    <span>Bunda Campus,</span>
                    <span>Near Bunda COAP</span>
                </div>
            </div>
            
            <div class="social-icons">
                <div class="social-icon">f</div>
                <div class="social-icon">t</div>
                <div class="social-icon">y</div>
                <img src="assets/spark.svg" class="icon-spark" alt="Spark">
            </div>
        </div>
    </footer>

</body>
</html>
H
