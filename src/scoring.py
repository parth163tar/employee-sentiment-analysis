def sentiment_score(row):

    if row["sentiment"] == "Positive":
        return 1
    elif row["sentiment"] == "Negative":
        return -1
    else:
        return 0

def monthly_scores(df):

    df["score"] = df.apply(sentiment_score, axis=1)

    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")

    monthly = df.groupby(["from","month"])["score"].sum().reset_index()

    return monthly