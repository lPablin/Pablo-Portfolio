import csv
import snscrape.modules.twitter as sntwitter

tweets = []
max_tweets = 100  # Specify the desired number of tweets

query = 'La revuelta'  # Search query "name of the movie"
since_date = '2024-09-10'  # Specify the starting date for tweet retrieval

for tweet in sntwitter.TwitterSearchScraper(f'{query} since:{since_date} lang:en').get_items():
    tweets.append({
        'ids': tweet.id,
        'date': tweet.date.strftime('%Y-%m-%d'),
        'flag': query if query else 'NO QUERY',
        'user': tweet.user.username,
        'text': tweet.content,
        # Add other desired tweet attributes
    })

    if len(tweets) >= max_tweets:
        break

# Define CSV file path
csv_file = 'tweets.csv'

# Define field names for the CSV file
field_names = ['ids', 'date', 'flag', 'user', 'text']

# Write tweets to CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(tweets)

print(f'Tweets saved to {csv_file}') # completion of extraction

##############################################
##load the extracted data for confirmation
import numpy as np
import pandas as pd
df= pd.read_csv('./tweets.csv')