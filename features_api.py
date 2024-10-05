import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

def fetch_reviews(color=None, style_name=None, rating=None):

    df = pd.read_excel('reviews.xlsx')

    if color:
        df = df[df['color'].str.lower() == color.lower()]
    if style_name:
        df = df[df['style_name'].str.lower() == style_name.lower()]
    if rating:
        df = df[df['rating'] == int(rating)]
    

    return df.to_dict(orient='records')


@app.route('/fetch_reviews', methods=['GET'])
def fetch_reviews_api():
    color = request.args.get('color')
    storage_size = request.args.get('storage_size')
    rating = request.args.get('rating')
    
    reviews = fetch_reviews(color, storage_size, rating)
    
    return jsonify({
        "reviews": reviews
    })
if __name__ == '__main__':
    app.run(debug=True)