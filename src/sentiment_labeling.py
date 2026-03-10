import pandas as pd
from textblob import TextBlob

def label_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def apply_sentiment(df):

    df["sentiment"] = df["body"].apply(label_sentiment)

    return df