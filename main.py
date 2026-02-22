<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RJ OUTFITS</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {
    background: #f5f5f5;
}

/* NAVBAR */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 40px;
    background: white;
}

.logo {
    font-size: 22px;
    font-weight: bold;
    color: #c40000;
}

.nav-links {
    display: flex;
    gap: 25px;
}

.nav-links a {
    text-decoration: none;
    color: black;
    font-weight: 500;
}

.btn {
    background: #c40000;
    color: white;
    padding: 8px 15px;
    border-radius: 4px;
}

/* HERO */
.hero {
    display: flex;
    margin: 20px;
    background: #ddd;
}

.hero-left {
    flex: 2;
    background: url('https://images.unsplash.com/photo-1520975922203-b8d8d5b7c3c4') center/cover;
    height: 300px;
    display: flex;
    align-items: center;
    padding-left: 30px;
}

.hero-text {
    font-size: 40px;
    font-weight: bold;
    color: gold;
}

.hero-right {
    flex: 1;
    background: url('https://images.unsplash.com/photo-1521335629791-ce4aec67dd53') center/cover;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-right button {
    background: red;
    color: white;
    padding: 10px 20px;
    border: none;
}

/* PRODUCTS */
.section {
    padding: 30px;
}

.products {
    display: flex;
    gap: 20px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

.card img {
    width: 100px;
}

/* WHY US */
.why {
    background: red;
    color: white;
    padding: 20px;
    width: 250px;
}

/* FOOTER */
.footer {
    background: #c40000;
    color: white;
    padding: 15px;
    display: flex;
    justify-content: space-between;
}
</style>
</head>

<body>

<!-- NAVBAR -->
<div class="navbar">
    <div class="logo">RJ OUTFITS</div>
    <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">Products</a>
        <a href="#">About Us</a>
        <a href="#">Contact</a>
        <a href="#" class="btn">Shop Now</a>
    </div>
</div>

<!-- HERO -->
<div class="hero">
    <div class="hero-left">
        <div class="hero-text">STYLE YOUR STORY</div>
    </div>
    <div class="hero-right">
        <button>SHOP NOW</button>
    </div>
</div>

<!-- PRODUCTS SECTION -->
<div class="section">
    <h2 style="color:#c40000;">Our Products</h2>

    <div class="products">
        <div class="why">
            <h3>Why Choose Us?</h3>
            <ul>
                <li>Quality Fabrics</li>
                <li>Latest Trends</li>
                <li>Fast Delivery</li>
            </ul>
        </div>

        <div class="card">
            <img src="https://cdn-icons-png.flaticon.com/512/892/892458.png">
            <p>Plain T-shirts</p>
        </div>

        <div class="card">
            <img src="https://cdn-icons-png.flaticon.com/512/892/892458.png">
            <p>Long Sleeves</p>
        </div>

        <div class="card">
            <img src="https://cdn-icons-png.flaticon.com/512/892/892458.png">
            <p>Shorts</p>
        </div>
    </div>
</div>

<!-- FOOTER -->
<div class="footer">
    <div>
        WhatsApp: 0999437233 <br>
        Call: 0938607846
    </div>
    <div>
        Location: Bunda Campus
    </div>
</div>

</body>
</html>
