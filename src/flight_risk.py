def detect_flight_risk(df):

    df["date"] = pd.to_datetime(df["date"])

    negative = df[df["sentiment"] == "Negative"]

    risk = (
        negative
        .sort_values("date")
        .groupby("from")
        .rolling("30D", on="date")
        .size()
        .reset_index(name="neg_count")
    )

    flight_risk = risk[risk["neg_count"] >= 4]

    return flight_risk