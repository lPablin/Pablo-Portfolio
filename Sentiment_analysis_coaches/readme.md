# 🔍 Final Project: Sentiment Analysis of Fan Reactions on Twitter Following Sports Results ⚽📊
.
This project represents the culmination of five months of focused study in the Data Science course at Dicampus. It applies Natural Language Processing (NLP) to analyze Twitter sentiment around second-division football coaches following match outcomes. Covering the full Data Lifecycle—from data acquisition to model implementation and correlation analysis—it provides insight into how sports performance influences social media sentiment📈.

Currently, this project is a work in progress and will be enhanced after further study in NLP as part of my Master’s in Artificial Intelligence.

## Project Highlights
1️⃣ Data Collection
I gathered tweets about coaches in the days after each match, along with team statistics, using ETL techniques to build a comprehensive dataset.

2️⃣ Data Cleaning and Preparation
Ensuring data quality was essential for accurate analysis. I removed unnecessary symbols, mentions, hashtags, and URLs to create a clean dataset.

3️⃣ Sentiment Modeling
Using the VADER model, I conducted sentiment analysis to classify tweets as positive, negative, or neutral. However, this required significant adjustments:

Colloquial Phrases: Phrases like "the coach won’t eat his Christmas turrón here" (implying an impending dismissal) were not interpreted correctly without additional tuning.
Global Text Evaluation: VADER assigns an overall polarity score, which can misclassify mixed sentiments within complex sentences, such as, "We have the best team but we play terribly."

4️⃣ Correlation Analysis
As shown in the attached correlation matrix, I compared fan sentiment with sports metrics. Sentiment closely aligned with results (negative = loss) and ranking, but also with tweet volume: an increase in tweets about a coach often reflected negative sentiment. Early coaching changes often happened with teams with larger fanbases, as doubts arose quickly on social media.

5️⃣ Trend Analysis with Advanced Models
As a future step, I plan to analyze shifts in public opinion using models inspired by the Ising spin model from statistical mechanics. This approach can help to simulate how individual fan sentiments—particularly when polarized—interact and influence broader shifts in public opinion, much like spins aligning in a magnetic field. By understanding these interactions, we can better observe how localized sentiment trends spread across the network and explore potential solutions to counteract or stabilize negative sentiment cascades.
