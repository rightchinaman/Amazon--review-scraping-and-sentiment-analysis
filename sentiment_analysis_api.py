from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    review = data.get("review")
    
    if not review:
        return jsonify({"error": "Review text is missing"}), 400

    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

    return jsonify({
        "review": review,
        "polarity": polarity,
        "sentiment": sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)
