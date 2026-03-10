📊 Employee Sentiment Analysis
Overview

This project analyzes employee email/message data to evaluate sentiment trends, employee engagement levels, and identify potential flight risks. Using Natural Language Processing (NLP) techniques and statistical analysis, the project processes raw employee communication data to derive meaningful insights about workplace sentiment.

The workflow includes sentiment labeling, exploratory data analysis (EDA), employee sentiment scoring, ranking employees based on sentiment trends, flight risk identification, and predictive modeling.

🎯 Project Objectives

The primary objectives of this project are:

Perform sentiment analysis on employee messages.

Conduct exploratory data analysis (EDA) to understand patterns in communication.

Calculate monthly sentiment scores for employees.

Rank employees based on sentiment trends.

Identify flight risk employees based on negative sentiment behavior.

Build a linear regression model to analyze factors influencing sentiment scores.

⚙️ Technologies Used

Python

Pandas

NumPy

TextBlob (Sentiment Analysis)

Scikit-learn (Machine Learning)

Matplotlib & Seaborn (Visualization)

Jupyter Notebook

📁 Project Structure
employee-sentiment-analysis
│
├── data
│   └── test.csv
│
├── notebooks
│   └── employee_sentiment_analysis.ipynb
│
├── visualizations
│   ├── sentiment_distribution.png
│   ├── monthly_sentiment_trend.png
│   ├── employee_score_distribution.png
│
├── requirements.txt
├── README.md
└── .env.example

🔧 Setup Instructions

1️⃣ Clone the Repository
git clone https://github.com/parth163tar/employee-sentiment-analysis.git
cd employee-sentiment-analysis
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Notebook
jupyter notebook notebooks/employee_sentiment_analysis.ipynb

🧠 Methodology

1️⃣ Data Preprocessing

The dataset contains employee email communications with attributes such as sender, message body, and timestamp.

Key preprocessing steps include:

Converting date column to datetime format

Extracting month from timestamp

Cleaning text data for analysis

2️⃣ Sentiment Analysis

Sentiment analysis is performed using TextBlob, which calculates polarity scores ranging from -1 to +1.

Sentiment classification rules:

Polarity Score	Sentiment
> 0.1	Positive
< -0.1	Negative
Otherwise	Neutral

Each message is labeled accordingly.

3️⃣ Sentiment Score Calculation

Each sentiment label is mapped to a numerical score:

Sentiment	Score
Positive	+1
Negative	-1
Neutral	0

Monthly sentiment scores are computed by aggregating scores for each employee.

4️⃣ Exploratory Data Analysis (EDA)

EDA helps understand sentiment patterns and employee communication behavior.

Visualizations include:

Sentiment distribution across all emails

Monthly sentiment trends

Employee sentiment score distribution

Top positive employee rankings

Observations

Most employee messages are neutral, indicating professional communication.

Some employees exhibit consistently positive sentiment patterns.

Periods with increased negative sentiment may indicate organizational stress or workload spikes.

5️⃣ Employee Ranking

Employees are ranked monthly based on their aggregated sentiment scores.

Two lists are generated:

Top 3 Positive Employees (highest sentiment score)

Top 3 Negative Employees (lowest sentiment score)

6️⃣ Flight Risk Identification

An employee is flagged as a flight risk if they send 4 or more negative emails within a rolling 30-day window.

This rolling window approach captures sustained negative sentiment behavior rather than isolated negative messages.

7️⃣ Predictive Modeling

A Linear Regression model is built to analyze factors influencing sentiment scores.

Features used:

Average message length

Average word count

Message frequency per employee

Target variable

Monthly sentiment score

Evaluation metric

Mean Squared Error (MSE)

This model helps understand how communication patterns correlate with sentiment.

📈 Key Insights

Employee communication is predominantly neutral.

A small subset of employees consistently shows strong positive or negative sentiment.

Negative sentiment clusters may indicate potential engagement issues.

Flight risk detection helps identify employees who may require attention from management.

🚀 Conclusion

This project demonstrates how Natural Language Processing and data analysis can be used to monitor employee sentiment and engagement patterns.

By analyzing communication data, organizations can identify potential issues early and take proactive steps to improve employee satisfaction and retention.

👤 Author

Parth Sharma

GitHub:
https://github.com/parth163tar
