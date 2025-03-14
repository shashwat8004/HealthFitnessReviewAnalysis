import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import scrape_reviews

# Step 1: Scrape Reviews
scrape_reviews.scrape_and_save()

# Step 2: Clean Reviews
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))
app_names = ["fitbit", "myfitnesspal", "nike", "yazio"]

df = pd.read_csv("data/health_reviews.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"\W+", " ", text)  # Remove special characters
    words = text.split()
    words = [word for word in words if word not in stop_words and word not in app_names]
    return " ".join(words)

df["cleaned_reviews"] = df["review_text"].apply(clean_text)
df.to_csv("data/cleaned_reviews.csv", index=False)
print("✅ Cleaned data saved to data/cleaned_reviews.csv")

# Step 3: Word Frequency Count
all_text = " ".join(df["cleaned_reviews"].dropna()).split()
word_freq = Counter(all_text)

word_count_df = pd.DataFrame(word_freq.items(), columns=["word", "count"]).sort_values(by="count", ascending=False)
word_count_df.to_csv("data/word_count.csv", index=False)
print("✅ Word count saved to data/word_count.csv")

# Step 4: Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(all_text))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in 5-Star Reviews")
plt.show()

print("✅ Word Cloud generated successfully!")
