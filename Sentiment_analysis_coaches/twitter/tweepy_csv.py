import tweepy

client = tweepy.Client(bearer_token='bearer_token')
query = 'La revuelta'
recent_tweets = client.search_recent_tweets(query=query, tweet_fields=['tweet_field_1', 'tweet_field_2'], max_results=100)


# Abre un archivo CSV para escribir
with open('tweets.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Escribe los encabezados (nombre de los campos)
    writer.writerow(['tweet_field_1', 'tweet_field_2'])
    
    # Escribe cada tweet en el archivo CSV
    for tweet in recent_tweets.data:
        writer.writerow([tweet['tweet_field_1'], tweet['tweet_field_2']])