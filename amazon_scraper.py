import requests
from bs4 import BeautifulSoup
import csv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_amazon_products(url):
    """Scrapes product details from an Amazon search results page."""

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    products = []
    for product_item in soup.find_all("div", {"data-component-type": "s-search-result"}):
        try:
            # Product Name
            product_name = product_item.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
            if product_name:
                product_name = product_name.find("span").text.strip()
            else:
                product_name = "N/A"

            # Price
            price = product_item.find("span", class_="a-price-whole")
            price = price.text.strip() if price else "N/A"

            # Rating
            rating = product_item.find("span", class_="a-icon-alt")
            rating = rating.text.strip() if rating else "N/A"

            # Seller Name
            seller_name = product_item.find("span", class_="a-size-small tabular-buybox-text-message")
            if seller_name:
                seller_name = seller_name.find("a").text.strip()
            else:
                seller_name = "N/A"

            # Stock Status
            stock_status = product_item.find("span", class_="a-size-small a-color-price")
            if stock_status:
                stock_status = stock_status.text.strip()
            else:
                stock_status = "In Stock"  # Default to "In Stock" if no out-of-stock indicator is found

            # Append product details to the list
            products.append({
                "Product Name": product_name,
                "Price": price,
                "Rating": rating,
                "Seller Name": seller_name,
                "Stock Status": stock_status,
            })
        except Exception as e:
            logging.warning(f"Error parsing a product: {e}")
            continue

    return products

def save_to_csv(products, filename="amazon_products.csv"):
    """Saves product data to a CSV file."""

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Product Name", "Price", "Rating", "Seller Name", "Stock Status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(products)

if __name__ == "__main__":
    url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"  # Hardcoded URL
    products = scrape_amazon_products(url)
    save_to_csv(products)
    print(f"Product details scraped and saved to amazon_products.csv")