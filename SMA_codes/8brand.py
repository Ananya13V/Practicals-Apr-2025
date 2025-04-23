import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

data = {
    "Post_ID": [101, 102, 103, 104, 105],
    "Content": [
        "BrandX has the best products I've ever used!",
        "Terrible experience with BrandX customer service.",
        "Loving the new BrandX product range!",
        "Neutral about BrandX. Could be better.",
        "BrandX is doing a great job with sustainability!",
    ],
    "Likes": [100, 20, 300, 50, 450],
    "Comments": [10, 5, 40, 2, 20],
    "Shares": [5, 1, 5, 0, 5],
}
df = pd.DataFrame(data)

# Step 1 : Filter for the brand
brand = "BrandX"
brand_posts = df[df['Content'].str.contains(brand, case = False, na = False)]

# Step 2 : Sentiment Analysis
brand_posts['Polarity'] = brand_posts['Content'].apply(lambda text: TextBlob(text).sentiment.polarity)
brand_posts['Sentiment'] = brand_posts['Polarity'].apply(
    lambda polarity: 
    'Postive' if polarity > 0 
    else 'Negative' if polarity < 0 
    else 'Neutral')

# Step 3 : Calculate Total Engagement (Likes + Comments + Shares)
brand_posts['Total Engagement'] = brand_posts['Likes'] + brand_posts['Comments'] + brand_posts['Shares']

# Step 4 : Sentiment Distribution
sentiment_counts = brand_posts['Sentiment'].value_counts()

# Step 5 : Plot Sentiment Distribution

plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind = 'bar', color = ['green', 'red', 'gray'], edgecolor = 'black')
plt.title(f'Sentiment Distribution for {brand}')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Step 6 : Top - Engaging Posts
top_brand_posts = brand_posts.sort_values(by="Total_Engagement", ascending=False).head(5)
print(f"\nTop 5 Most Engaging Posts for {brand}:")
print(top_brand_posts[["Post_ID", "Content", "Total_Engagement", "Sentiment"]])
