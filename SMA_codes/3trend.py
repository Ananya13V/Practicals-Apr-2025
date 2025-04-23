from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SMA_codes\\SMA 1-3 Dataset.csv")
print(df.head())

vectoriser = TfidfVectorizer(stop_words = 'english', max_features = 10)
X = vectoriser.fit_transform(df['Content'])

keywords = vectoriser.get_feature_names_out()

print("Top 10 Keywords: ", keywords)

keyword_count = X.sum(axis=0).A1

plt.figure(figsize=(10, 5))
plt.barh(keywords, keyword_count, color='skyblue')
plt.title('Top 10 Keywords in Content')
plt.xlabel('Keywords')
plt.ylabel('Frequency')
plt.show()

############
# Using data of likes, comment and hashtag

df['Post_Date'] = pd.to_datetime(df['Post_Date'])
df['Year'] = df['Post_Date'].dt.year
df['Month'] = df['Post_Date'].dt.month
df['Day'] = df['Post_Date'].dt.day

monthly_engagement = df.groupby(['Year','Month'])['Likes'].sum()
monthly_comments = df.groupby(['Year', 'Month'])['Comments'].mean()

### Hashtag Analysis ###

df['Hashtags'] = df['Hashtags'].fillna('')
hashtags = df['Hashtags'].str.lower().str.split('#').sum()
hashtags = [hashtag.strip() for hashtag in hashtags if hashtag.strip() != '']
hashtag_count = pd.Series(hashtags).value_counts()
print("Top 10 hashtags: ", hashtag_count.head(10))

plt.figure(figsize=(10, 5))
monthly_engagement.plot(kind = 'line', marker='o', color='blue')
plt.title('Monthly Engagement Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Total likes')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
monthly_comments.plot(kind="line", marker="o", color="blue")
plt.title("Average comments over a Month's time")
plt.xlabel("Year-Month")
plt.ylabel("Average Comments")
plt.show()

plt.figure(figsize=(10, 5))
hashtag_count.plot(kind="line", marker="o", color="blue")
plt.title("Hashtags by Freq")
plt.xlabel("Hashtags")
plt.ylabel("Frequency")
plt.show()
