import matplotlib.pyplot as plt
import pandas as pd

file_path = '../model/sentiment_analysis/record.csv'

def read_record_file(file_path):
    # Baca file record.csv menggunakan Pandas
    df = pd.read_csv(file_path, header=None)
    df.columns = ['tanggal_waktu', 'intent', 'sentiment']

  

    # Hitung jumlah intent unik untuk setiap sentimen
    intents_positive = df[df['sentiment'] == 'positive']['intent'].value_counts().to_dict()
    intents_negative = df[df['sentiment'] == 'negative']['intent'].value_counts().to_dict()
    intents_neutral = df[df['sentiment'] == 'neutral']['intent'].value_counts().to_dict()

    return  intents_positive, intents_negative, intents_neutral

def plot_intent_sentiment():
    intents_positive, intents_negative, intents_neutral =  read_record_file(file_path)
    
    # Plot jumlah intent
    plt.figure(figsize=(18, 5))
    

    # Plot jumlah intent positif
    plt.subplot(1, 3, 1)
    plt.bar(intents_positive.keys(), intents_positive.values(), color='lightgreen')
    plt.xlabel('Intent')
    plt.ylabel('Jumlah')
    plt.title('Jumlah Intent dengan Sentimen Positif')
    plt.xticks(rotation=45)

    # Plot jumlah intent negatif
    plt.subplot(1, 3, 2)
    plt.bar(intents_negative.keys(), intents_negative.values(), color='salmon')
    plt.xlabel('Intent')
    plt.ylabel('Jumlah')
    plt.title('Jumlah Intent dengan Sentimen Negatif')
    plt.xticks(rotation=45)
    
     # Plot jumlah intent netral
    plt.subplot(1, 3, 3)
    plt.bar(intents_neutral.keys(), intents_neutral.values(), color='salmon')
    plt.xlabel('Intent')
    plt.ylabel('Jumlah')
    plt.title('Jumlah Intent dengan Sentimen Negatif')
    plt.xticks(rotation=45)

    plt.tight_layout()
    intents_plot_path = 'static/intents_plot.png'
    plt.savefig(intents_plot_path)
    plt.close()

    return intents_plot_path
