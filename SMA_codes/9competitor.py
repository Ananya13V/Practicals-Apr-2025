import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"SMA_codes\sma_ques9_dataset.csv")

print(df.groupby("competitor")[['likes', 'comments', 'shares']].mean())

platform_dist = df.groupby(['competitor', 'platform']).size().unstack()
print(platform_dist)

sentiment_dist = df.groupby(['competitor', 'sentiment']).size().unstack(fill_value=0)
print(sentiment_dist)

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="competitor", y="likes", estimator="mean")
plt.title("Average Likes by Competitor")
plt.ylabel("Average Likes")
plt.show()

## cutie
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="competitor", hue="sentiment")
plt.title("Sentiment Distribution by Competitor")
plt.ylabel("Number of Posts")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="competitor", y="shares")
plt.title("Shares Distribution by Competitor")
plt.ylabel("Shares")
plt.show()
