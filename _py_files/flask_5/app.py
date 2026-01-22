from flask import Flask, render_template, jsonify

app = Flask(__name__)
products = {
    1:{
        "description": "Jeans",
        "price": 10.99,
        "amount": 5,
        "image_url": "https://example.com/product1.jpg"
    },
    2:{
        "description": "Stylish Jeans",
        "price": 19.99,
        "amount": 10,
        "image_url": "https://example.com/product2.jpg"
    },
    3:{
        "description": "Dress",
        "price": 15.50,
        "amount": 3,
        "image_url": "https://example.com/product3.jpg"
    }
}
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shop")
@app.route("/shop/<search_term>")
def shop(search_term=""):
    results = []
    for product in products.values():
        if search_term in product['description']:   #if "" => in all strings
            results.append( product )
    return jsonify(results)

@app.route("/order", methods=["GET"])
def order():
    return render_template('form_order.html')


@app.route("/order/<int:order_id>", methods=["POST"])
def order_post(order_id):
    product = products.get(order_id)
    if product['amount'] > 0:       #check in stock
        product['amount'] -= 1      # 'order' ~ simulate amount -= 1
        return product
    else:
        return 'Out of stock'
    
if __name__ == '__main__':
    app.run(debug=True, port=8080)