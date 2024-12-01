from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample product data
PRODUCTS = [
    {"name": "Elegance Blossom", "price": 14800, "description": "A floral blend with notes of jasmine and rose."},
    {"name": "Midnight Noir", "price": 15000, "description": "Rich, dark, and mysterious with a hint of vanilla."},
    {"name": "Ocean Breeze", "price": 12500, "description": "Fresh and invigorating, inspired by the sea."},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Process order details
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        items = request.form.getlist('items')  # Multiple items
        total = sum([int(item.split('-')[1]) for item in items])  # Assuming 'item-price'

        return render_template('order_summary.html', name=name, email=email, address=address, items=items, total=total)
    return render_template('checkout.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    results = [product for product in PRODUCTS if query in product['name'].lower()]
    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
