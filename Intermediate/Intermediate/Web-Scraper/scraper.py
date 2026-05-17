"""
Web Scraper for ShadowFox Internship
Simple scraper for books.toscrape.com
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime

def scrape_books_page(url):
    """Scrape books from a single page"""
    
    # Headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    print(f"\n🌐 Accessing: {url}")
    
    try:
        # Send request to website
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print(f" Connected! (Status: {response.status_code})")
        else:
            print(f"Failed. Status: {response.status_code}")
            return []
            
    except Exception as e:
        print(f" Error: {e}")
        return []
    
    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all books on the page
    books = soup.find_all("article", class_="product_pod")
    print(f" Found {len(books)} books")
    
    all_books = []
    
    # Extract data from each book
    for book in books:
        # Get title
        title_tag = book.h3.a if book.h3 else None
        title = title_tag.get('title', 'No Title') if title_tag else 'No Title'
        
        # Get price
        price_tag = book.find("p", class_="price_color")
        price = price_tag.text.strip() if price_tag else 'N/A'
        
        # Get rating
        rating_tag = book.find("p", class_="star-rating")
        if rating_tag:
            rating_classes = rating_tag.get('class', [])
            rating = rating_classes[1] if len(rating_classes) > 1 else 'Unknown'
        else:
            rating = 'Unknown'
        
        # Get availability
        avail_tag = book.find("p", class_="instock")
        availability = avail_tag.text.strip() if avail_tag else 'Unknown'
        
        # Store book data
        book_data = {
            'title': title,
            'price': price,
            'rating': rating,
            'availability': availability,
            'scraped_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        all_books.append(book_data)
        print(f"  {title[:50]} - {price}")
    
    return all_books

def save_to_csv(data, filename):
    """Save scraped data to CSV file"""
    if not data:
        print("No data to save")
        return False
    
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"\n Saved to: {filename}")
    return True

def print_summary(data):
    """Print summary of scraped data"""
    if not data:
        return
    
    print("\n" + "="*50)
    print("  SUMMARY")
    print("="*50)
    print(f"Total books: {len(data)}")
    
    # Count by rating
    rating_count = {}
    for book in data:
        rating = book['rating']
        rating_count[rating] = rating_count.get(rating, 0) + 1
    
    print("\nRatings:")
    for rating, count in rating_count.items():
        print(f"  {rating}: {count} books")
    
    # Show first 3 books
    print("\nFirst 3 books:")
    for i, book in enumerate(data[:3], 1):
        print(f"  {i}. {book['title'][:40]} - {book['price']}")

# ============ MAIN PROGRAM ============
if __name__ == "__main__":
    print("="*50)
    print("  WEB SCRAPER - ShadowFox Internship")
    print("="*50)
    print(f" Started: {datetime.now().strftime('%H:%M:%S')}")
    
    # Scrape first page
    url = "https://books.toscrape.com/catalogue/page-1.html"
    books_data = scrape_books_page(url)
    
    # Save results
    if books_data:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"books_{timestamp}.csv"
        save_to_csv(books_data, filename)
        print_summary(books_data)
        
        print("\n" + "="*50)
        print(f" SUCCESS! Check {filename}")
        print("="*50)
    else:
        print("\n No data scraped. Check your internet connection.")
    
    print(f" Finished: {datetime.now().strftime('%H:%M:%S')}")