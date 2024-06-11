from flask import Flask, render_template, request, jsonify
import intent_recognition as ir
import sentiment_analysis as sa
import rbs
import calculate as clt

app = Flask(__name__)

# Function to get chatbot response
def chatbot_response(input_text):
    intent = ir.classify_intent(input_text)
    sentiment = sa.classify_sentiment(input_text)
    response = rbs.get_response(intent, sentiment)
    
    return response

# Route to serve the chatbot interface
@app.route('/')
def chatbot():
    return render_template('index.html')

# New route to process chatbot input and return response
@app.route('/get_response', methods=['POST'])
def get_chatbot_response():
    # Get user input from the POST request
    user_message = request.json.get('message')
    
    # Process the user input and get the chatbot response
    bot_response = chatbot_response(user_message)
    
    # Return the response as JSON
    return jsonify({"response": bot_response})

#calculate sentiment-intent
@app.route('/calculate')
def calculate():
    pos = clt.plot_intent_sentiment()
    return render_template('calculate.html', intents_plot_path=pos)


if __name__ == '__main__':
    app.run(debug=True)