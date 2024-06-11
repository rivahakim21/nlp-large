from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np 

# __Intent Recognition__
IR_FOLDER = "../model/intent_recognition/"

# Load the saved model
loaded_model = keras.models.load_model(IR_FOLDER+"model.keras")
    
# Load the tokenizer
import pickle   
with open('../model/intent_recognition/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load the label encoder
import pickle
with open(IR_FOLDER+'label_encoder.pickle', 'rb') as enc:
    label_encoder = pickle.load(enc)

# Load the intents 
unique_intents = ['create_account', 'delete_account', 'edit_account',
       'recover_password', 'registration_problems', 'switch_account',
       'check_cancellation_fee', 'contact_customer_service',
       'contact_human_agent', 'delivery_options', 'delivery_period',
       'complaint', 'review', 'check_invoices', 'get_invoice',
       'newsletter_subscription', 'cancel_order', 'change_order',
       'place_order', 'track_order', 'check_payment_methods',
       'payment_issue', 'check_refund_policy', 'get_refund',
       'track_refund', 'change_shipping_address',
       'set_up_shipping_address'] 

def classify_intent(text_input, threshold=0.75) -> str:
    # Preprocess
    sequences = tokenizer.texts_to_sequences([text_input]) 
    X = pad_sequences(sequences, maxlen=100)
    
    # Predict
    prediction = loaded_model.predict(X)
    
    # Get the highest probability and its index
    max_prob = np.max(prediction)  # The highest probability
    max_index = np.argmax(prediction)  # The index of the highest probability

    print(prediction)
    # Check if the highest probability exceeds the threshold
    if max_prob >= threshold:
        # If yes, return the corresponding class
        predicted_class = label_encoder.inverse_transform([max_index])[0]
    else:
        # If not, return "Unknown" or some other default class
        predicted_class = "Unknown"

    return predicted_class


if __name__ == '__main__':
    print(classify_intent("contact human agent"))