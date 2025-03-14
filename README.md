# Health & Fitness Review Analysis

## 📌 Project Overview

This project scrapes 5-star reviews from **Health & Fitness** apps on the Google Play Store, processes the text, and generates a **word cloud** to visualize the most frequently used words. It also provides a word frequency count for analysis.

---

## 📂 Folder Structure

```
📂 HealthFitnessReviewAnalysis/
│── 📂 data/                   # Stores all processed data
│   ├── health_reviews.csv     # Raw scraped reviews
│   ├── cleaned_reviews.csv    # Cleaned reviews (stopwords removed)
│   ├── word_count.csv         # Word frequency count
│── 📜 scrape_reviews.py       # Fetches reviews from Google Play
│── 📜 main.py                 # Cleans data, generates word cloud & word count
│── 📜 requirements.txt        # Python dependencies
│── 📜 README.md               # Documentation
```

---

## 🛠️ Installation & Setup

### **1️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **2️⃣ Run the Full Pipeline**

```bash
python main.py
```

This will:
✅ Scrape reviews → `data/health_reviews.csv`  
✅ Clean text → `data/cleaned_reviews.csv`  
✅ Count words → `data/word_count.csv`  
✅ Generate **Word Cloud** (shows common words in 5-star reviews) 🎨  

---

## 📜 Features

✅ **Scrapes Reviews** → Google Play Store reviews for selected health apps  
✅ **Cleans Data** → Removes stopwords & app names for better analysis  
✅ **Generates Word Count** → Counts frequency of words in reviews  
✅ **Creates Word Cloud** → Displays most common words visually  

---

## 📊 Example Output

After running `python main.py`, the terminal will show:

```
📥 Fetching reviews for com.fitbit.FitbitMobile...
✅ Reviews saved to data/health_reviews.csv
✅ Cleaned data saved to data/cleaned_reviews.csv
✅ Word count saved to data/word_count.csv
✅ Word Cloud generated successfully!
```

A **Word Cloud Image** will pop up showing the most used words in 5-star reviews. 🎨

---

## 🚀 Notes & Troubleshooting

1. **Slow Fetching?** → Use only **one app ID** in `scrape_reviews.py` & add `time.sleep(1)` in `fetch_reviews()`.
2. **Check Data Files** → Open CSV files using `notepad data/health_reviews.csv` or `python -c "import pandas as pd; print(pd.read_csv('data/health_reviews.csv').head(10))"`.
3. **Python Not Found?** → Make sure Python is installed (`python --version`).

---

## 🏆 Future Improvements

🔹 Add **Sentiment Analysis** to categorize reviews as positive/negative  
🔹 Expand to **more app categories** for better insights  
🔹 Improve **UI visualization** for displaying results interactively  

---

## 📌 Author

**Shawat Saxena** 🚀  
💡 Feel free to contribute & improve this project!
