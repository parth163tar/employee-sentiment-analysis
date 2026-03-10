import matplotlib.pyplot as plt
import seaborn as sns

def sentiment_distribution(df):

    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x="sentiment")
    plt.title("Sentiment Distribution")
    plt.savefig("visualizations/sentiment_distribution.png")

def monthly_trend(df):

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    trend = df.groupby(["month","sentiment"]).size().unstack()

    trend.plot(kind="line", figsize=(10,5))
    plt.title("Monthly Sentiment Trend")
    plt.savefig("visualizations/monthly_sentiment.png")