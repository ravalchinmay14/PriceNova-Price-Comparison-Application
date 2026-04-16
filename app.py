from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pricenova.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100))
    original_price = db.Column(db.Integer) 
    amazon_price = db.Column(db.Integer, nullable=False)
    flipkart_price = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(500))
    amazon_url = db.Column(db.String(1000))   
    flipkart_url = db.Column(db.String(1000)) 

# Initialize Database with MIXED Market Trends
with app.app_context():
    db.create_all()
    if not Product.query.first():
        defaults = [
            # --- PHONES ---
            Product(name="iPhone 15 Pro", category="Phones", original_price=125000, amazon_price=127990, flipkart_price=129900, img_url="https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400"),
            Product(name="Samsung S24 Ultra", category="Phones", original_price=135000, amazon_price=134999, flipkart_price=129999, img_url="https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"), 
            Product(name="Google Pixel 8", category="Phones", original_price=75999, amazon_price=75999, flipkart_price=79999, img_url="https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            Product(name="OnePlus 12", category="Phones", original_price=60000, amazon_price=69999, flipkart_price=64999, img_url="https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400"), 
            Product(name="Nothing Phone 2", category="Phones", original_price=49999, amazon_price=44999, flipkart_price=49999, img_url="https://images.unsplash.com/photo-1678911820864-e2c567c655d7?w=400"),
            
            # --- LAPTOPS ---
            Product(name="MacBook Air M2", category="Laptops", original_price=94990, amazon_price=94990, flipkart_price=96990, img_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"), 
            Product(name="Dell XPS 13", category="Laptops", original_price=110000, amazon_price=120000, flipkart_price=115000, img_url="https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400"), 
            Product(name="HP Spectre x360", category="Laptops", original_price=140000, amazon_price=135000, flipkart_price=140000, img_url="https://images.unsplash.com/photo-1544006659-f0b21f04cb1d?w=400"), 
            Product(name="Lenovo Legion 5", category="Laptops", original_price=89990, amazon_price=92990, flipkart_price=89990, img_url="https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"), 
            Product(name="ASUS ROG Zephyrus", category="Laptops", original_price=140000, amazon_price=145000, flipkart_price=150000, img_url="https://images.unsplash.com/photo-1611078489935-0cb964de46d6?w=400"), 
            
            # --- TVs ---
            Product(name="Sony Bravia 55", category="TVs", original_price=69990, amazon_price=68990, flipkart_price=65990, img_url="https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"), 
            Product(name="Samsung Crystal", category="TVs", original_price=32990, amazon_price=32990, flipkart_price=34990, img_url="https://images.unsplash.com/photo-1552533231-699885121937?w=400"), 
            Product(name="LG OLED C3", category="TVs", original_price=120000, amazon_price=130000, flipkart_price=124990, img_url="https://images.unsplash.com/photo-1509281373149-e957c6296406?w=400"), 
            Product(name="Mi TV 5X", category="TVs", original_price=33999, amazon_price=31999, flipkart_price=33999, img_url="https://images.unsplash.com/photo-1461151304267-38535e770d79?w=400"), 
            Product(name="TCL 4K TV", category="TVs", original_price=28990, amazon_price=30990, flipkart_price=28990, img_url="https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=400"), 
            
            # --- SHOES ---
            Product(name="Nike Air Jordan", category="Shoes", original_price=11500, amazon_price=12295, flipkart_price=13500, img_url="https://images.unsplash.com/photo-1584735175315-9d5df23860e6?w=400"), 
            Product(name="Adidas Ultraboost", category="Shoes", original_price=17999, amazon_price=17999, flipkart_price=15999, img_url="https://images.unsplash.com/photo-1556906781-9a412961c28c?w=400"), 
            Product(name="Puma RS-X", category="Shoes", original_price=6999, amazon_price=6999, flipkart_price=8999, img_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"), 
            
            # --- HEADPHONES ---
            Product(name="Sony XM5", category="Headphones", original_price=29990, amazon_price=31999, flipkart_price=29990, img_url="https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=400"), 
            Product(name="Bose QC Ultra", category="Headphones", original_price=34000, amazon_price=35900, flipkart_price=37999, img_url="https://images.unsplash.com/photo-1546435770-a3e426da4717?w=400"), 
            Product(name="AirPods Max", category="Headphones", original_price=59900, amazon_price=59999, flipkart_price=54900, img_url="https://images.unsplash.com/photo-1613040819022-b43a38aa896b?w=400"), 
            
            # --- ELECTRONICS ---
            Product(name="Apple Watch 9", category="Electronics", original_price=40000, amazon_price=41900, flipkart_price=44999, img_url="https://images.unsplash.com/photo-1434493566906-db97d9fd7142?w=400"), 
            Product(name="iPad Air", category="Electronics", original_price=62900, amazon_price=62990, flipkart_price=59900, img_url="https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"), 
            Product(name="GoPro 12", category="Electronics", original_price=37990, amazon_price=37990, flipkart_price=41000, img_url="https://images.unsplash.com/photo-1565153322059-4d6411516766?w=400") 
        ]
        db.session.bulk_save_objects(defaults)
        db.session.commit()

@app.route('/')
def index():
    products = Product.query.all()
    total = len(products)
    
    drops = 0
    for p in products:
        if p.original_price:
            lowest = min(p.amazon_price, p.flipkart_price)
            if lowest < p.original_price:
                drops += 1
                
    savings = sum(abs(p.amazon_price - p.flipkart_price) for p in products)
    return render_template('index.html', products=products, total=total, drops=drops, savings=savings)

# ROUTE TO ADD NEW ITEMS
@app.route('/add', methods=['POST'])
def add():
    a_price = int(request.form.get('a_price'))
    f_price = int(request.form.get('f_price'))
    o_price = request.form.get('o_price')
    
    baseline = int(o_price) if o_price else max(a_price, f_price)

    new_p = Product(
        name=request.form.get('name'),
        category=request.form.get('category'),
        amazon_price=a_price,
        flipkart_price=f_price,
        original_price=baseline,
        img_url=request.form.get('img'),
        amazon_url=request.form.get('a_url'),     
        flipkart_url=request.form.get('f_url')    
    )
    db.session.add(new_p)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Running on 0.0.0.0 for mobile network testing
    app.run(host='0.0.0.0', port=5000, debug=True)