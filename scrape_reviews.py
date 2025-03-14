from google_play_scraper import reviews_all, Sort
import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor
import time

app_ids = [
    "com.fitbit.FitbitMobile",
    # "com.myfitnesspal.android",
    # "com.nike.ntc",
    # "com.yazio.android",
]

def fetch_reviews(app_id):
    print(f"📥 Fetching reviews for {app_id}...")
    reviews = reviews_all(app_id, lang="en", country="us", sort=Sort.NEWEST, count=200)
    reviews = [r for r in reviews if r["score"] == 5]
    
    time.sleep(1)  # Delay to prevent rate limiting
    
    return [[app_id, r["content"], r["score"]] for r in reviews]

def scrape_and_save():
    all_reviews = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(fetch_reviews, app_ids)

    for result in results:
        all_reviews.extend(result)

    df = pd.DataFrame(all_reviews, columns=["app_id", "review_text", "rating"])
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/health_reviews.csv", index=False)
    print("✅ Reviews saved to data/health_reviews.csv")

if __name__ == "__main__":
    scrape_and_save()
