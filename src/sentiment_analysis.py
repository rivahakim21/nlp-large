from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
from scipy.special import softmax
import pickle   

with open('../model/sentiment_analysis/model_tokenizer.pkl', 'rb') as f:
    loaded_model, loaded_tokenizer = pickle.load(f)
model = loaded_model
tokenizer = loaded_tokenizer

def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def predict_sentiment(text, model, tokenizer):
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = scores.argsort()
    predicted_label = model.config.id2label[ranking[-1]]  # Mengambil label dengan skor tertinggi
    return predicted_label

def classify_sentiment(text):
    return predict_sentiment(text, model, tokenizer)