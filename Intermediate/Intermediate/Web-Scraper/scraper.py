"""
Web Scraper for ShadowFox Internship
Simple scraper for books.toscrape.com
"""
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_books_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print(f"\n Accessing: {url}")

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Failed. Status: {response.status_code}")
            return []

        print(f"Connected! (Status: {response.status_code})")

    except Exception as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all("article", class_="product_pod")

    print(f"Found {len(books)} books")

    all_books = []

    for book in books:
        title_tag = book.h3.a if book.h3 else None
        title = title_tag.get('title', 'No Title') if title_tag else 'No Title'

        price_tag = book.find("p", class_="price_color")
        price = price_tag.text.strip() if price_tag else 'N/A'

        rating_tag = book.find("p", class_="star-rating")
        if rating_tag:
            rating_classes = rating_tag.get('class', [])
            rating = rating_classes[1] if len(rating_classes) > 1 else 'Unknown'
        else:
            rating = 'Unknown'

        avail_tag = book.find("p", class_="instock availability")
        availability = avail_tag.text.strip() if avail_tag else 'Unknown'

        all_books.append({
            'title': title,
            'price': price,
            'rating': rating,
            'availability': availability,
            'scraped_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        print(f"{title[:40]} - {price}")

    return all_books


def save_to_csv(data, filename="output.csv"):
    if not data:
        print("No data to save")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"\nSaved to: {filename}")


def print_summary(data):
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"Total books: {len(data)}")

    rating_count = {}
    for book in data:
        rating = book['rating']
        rating_count[rating] = rating_count.get(rating, 0) + 1

    print("\nRatings:")
    for k, v in rating_count.items():
        print(f"{k}: {v}")

    print("\nFirst 3 books:")
    for i, book in enumerate(data[:3], 1):
        print(f"{i}. {book['title'][:40]} - {book['price']}")


# ============ MAIN ============
if __name__ == "__main__":
    print("="*50)
    print("WEB SCRAPER - ShadowFox Internship")
    print("="*50)

    url = "https://books.toscrape.com/catalogue/page-1.html"

    books_data = scrape_books_page(url)

    if books_data:
        save_to_csv(books_data, "output.csv")   
        print_summary(books_data)

        print("\nSUCCESS! Check output.csv")
    else:
        print("No data scraped. Check internet connection.")

   
  
