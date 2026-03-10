def employee_ranking(monthly_scores):

    top_positive = (
        monthly_scores
        .sort_values(["month","score","from"], ascending=[True,False,True])
        .groupby("month")
        .head(3)
    )

    top_negative = (
        monthly_scores
        .sort_values(["month","score","from"], ascending=[True,True,True])
        .groupby("month")
        .head(3)
    )

    return top_positive, top_negative