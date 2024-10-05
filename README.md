1. Features.py

The code performs the function of looping through multiple review pages, extracting review titles, texts, ratings, colors, style names, and verification statuses.
Used try-except to manage potential errors and absent data while extracting color and style information.
Collected and stored extracted review data into a list of dictionaries which is converted into Pandas DataFrame and saved in Excel file.


2. best&worst_keywords.py

Imported libraries for Pandas and NLTK libraries, and downloaded required NLTK resources.
Loaded the reviews from reviews.xlsx file.
Applied the VADER sentiment analyzer to calculate sentiment scores for each review, so as to classify words from positive and negative reviews.
Counted word frequencies in positive and negative reviews to identify the most common keywords associated with each sentiment.
Used Matplotlib to plot bar charts of the ten most frequent positive (best) and negative (worst) keywords.


3. features_api.py

Imported Pandas and Flask( for creating a web API) and initialised a Flask application instance.
Created a function to read reviews from the reviews.xlsx file and filter them based on given parameters: color, style name, and rating.
Created a GET endpoint (/fetch_reviews) that calls the fetch function to get the relevant reviews.
Function returns the filtered reviews as a JSON response using Flask's jsonify function.


4. sentiment_analysis_api.py

Imported TextBlob for sentiment analysis and initialized a Flask application instance.
Created a POST endpoint (/analyze_sentiment) that accepts JSON data containing a review text for sentiment analysis.
TextBlob is used to calculate the polarity of the review text, categorizing it as Positive, Negative, or Neutral based on the polarity score.
Returns a JSON response containing the original review text, its polarity score, and the corresponding sentiment label.
