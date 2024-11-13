# 🔍 Final Project: Sentiment Analysis of Fan Reactions on Twitter Following Sports Results ⚽📊
After five months of intensive learning, I’m proud to present my final project from the Data Science course at Dicampus, focused on analyzing social media sentiment about second-division football coaches following matches. This project delves into the fascinating field of Natural Language Processing (NLP) and allowed me to explore the full Data Lifecycle 📈.

## Project Highlights
1️⃣ Data Collection
I gathered tweets about coaches in the days after each match, along with team statistics, using ETL techniques to build a comprehensive dataset.

2️⃣ Data Cleaning and Preparation
Ensuring data quality was essential for accurate analysis. I removed unnecessary symbols, mentions, hashtags, and URLs to create a clean dataset.

3️⃣ Sentiment Modeling
Using the VADER model, I conducted sentiment analysis to classify tweets as positive, negative, or neutral. However, this required significant adjustments:

Colloquial Phrases: Phrases like "the coach won’t eat his Christmas turrón here" (implying an impending dismissal) were not interpreted correctly without additional tuning.
Global Text Evaluation: VADER assigns an overall polarity score, which can misclassify mixed sentiments within complex sentences, such as, "We have the best roster but play terribly."
4️⃣ Correlation Analysis
As shown in the attached correlation matrix, I compared fan sentiment with sports metrics. Sentiment closely aligned with results (negative = loss) and ranking, but also with tweet volume: an increase in tweets about a coach often reflected negative sentiment. Early coaching changes often happened with teams with larger fanbases, as doubts arose quickly on social media.

5️⃣ Trend Analysis with Advanced Models
As a future step, I plan to analyze trend shifts using models inspired by magnetism (as outlined in a previous post) and explore solutions to counter negative sentiment trends.
