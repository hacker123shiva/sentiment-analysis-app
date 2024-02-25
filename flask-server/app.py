# Using flask to make an API
# Import necessary libraries and functions
from flask import Flask, jsonify, request
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



# Creating a Flask app
app = Flask(__name__)

# Load the pre-trained model and vectorizer
model = joblib.load('d:\\telusko\\Communication-Server\\Sentiment-Analysis-App\\files\\sentiment_model.pkl')
vectorizer = joblib.load('d:\\telusko\\Communication-Server\\Sentiment-Analysis-App\\files\\vectorizer.pkl')

# Set up NLTK
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()


# Preprocess text for prediction
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum()]
    return ' '.join(filtered_tokens)

# On the terminal type: curl http://127.0.0.1:5080/
# Returns "hello world" when we use GET.
# Returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

# A simple function to calculate the square of a number
# The number to be squared is sent in the URL when we use GET
# On the terminal type: curl http://127.0.0.1:5080/analyze
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.json['text']  # Assuming the data is sent in JSON format
        cleaned_text = preprocess_text(text)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]
        
        # Create a JSON response with the sentiment analysis results
        response = {
             'prediction': prediction
        }
        return jsonify(response)

# Driver function
if __name__ == '__main__':
    # Run the app on port 5080
    app.run(debug=True, port=5080)
