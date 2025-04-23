import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv(r"SMA_codes\SMA 1-3 Dataset.csv")

vectoriser = TfidfVectorizer(max_features=10, stop_words = 'english')

X = vectoriser.fit_transform(df['Content'])

keywords = vectoriser.get_feature_names_out()

print("Top Keywords : ", keywords)

lda = LatentDirichletAllocation(n_components = 3, random_state = 42)
lda.fit(X)

for idx, topic in enumerate(lda.components_):
    print(f"Topic #{idx}: ")
    top_words = [vectoriser.get_feature_names_out()[i] for i in topic.argsort()[:-11:-1]]
    print(", ".join(top_words))

wordcloud = WordCloud(width = 800, height = 400, background_color='white').generate(' '.join(df['Content']))

plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
