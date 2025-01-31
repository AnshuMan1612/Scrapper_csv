# Scrapper_csv


📌 Code Breakdown
1. Importing Required Libraries
python
Copy
Edit
import requests
from bs4 import BeautifulSoup
import csv
import logging
requests → Fetches the Amazon webpage.
BeautifulSoup → Parses the HTML content.
csv → Saves the extracted data into a CSV file.
logging → Handles logging messages (errors, warnings, info).
2. Setting Up Logging
python
Copy
Edit
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
Configures logging to show timestamps and message levels (INFO, ERROR, WARNING, etc.).
Helps track errors when the scraper runs.
3. Defining the scrape_amazon_products(url) Function
This function fetches product details from an Amazon search results page.

🔹 Step 1: Set Headers & Make Request
python
Copy
Edit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
Amazon blocks bots, so we pretend to be a real browser using a User-Agent string.
Accept-Language ensures results are in English.
python
Copy
Edit
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an error for failed requests (e.g., 404, 503)
except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching the URL: {e}")
    return []
Uses requests.get() to fetch the webpage.
raise_for_status() stops execution if the request fails.
If an error occurs, it logs the issue and returns an empty list.
🔹 Step 2: Parse the HTML Page
python
Copy
Edit
soup = BeautifulSoup(response.content, "html.parser")
Converts the raw HTML into a structured format using BeautifulSoup.
Now, we can search for specific product details in the HTML.
🔹 Step 3: Extract Product Data
python
Copy
Edit
products = []
for product_item in soup.find_all("div", {"data-component-type": "s-search-result"}):
Finds all product containers in the search results page.
Each product is inside a <div> tag with data-component-type="s-search-result".
🔹 Step 4: Extract Product Name
python
Copy
Edit
product_name = product_item.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
if product_name:
    product_name = product_name.find("span").text.strip()
else:
    product_name = "N/A"
Looks for <h2> containing the product name.
If found, extracts the text and removes extra spaces using .strip().
If not found, assigns "N/A".
🔹 Step 5: Extract Price
python
Copy
Edit
price = product_item.find("span", class_="a-price-whole")
price = price.text.strip() if price else "N/A"
Finds the price container (<span class="a-price-whole">).
Extracts text, removes spaces, and assigns "N/A" if missing.
🔹 Step 6: Extract Rating
python
Copy
Edit
rating = product_item.find("span", class_="a-icon-alt")
rating = rating.text.strip() if rating else "N/A"
Finds customer rating in <span class="a-icon-alt">.
Example output: "4.5 out of 5 stars".
Assigns "N/A" if the rating isn’t available.
🔹 Step 7: Extract Seller Name (Problematic)
python
Copy
Edit
seller_name = product_item.find("span", class_="a-size-small tabular-buybox-text-message")
if seller_name:
    seller_name = seller_name.find("a").text.strip()
else:
    seller_name = "N/A"
Amazon doesn’t always show the seller’s name on the search page.
This selector often doesn’t work (which is why "N/A" is returned).
Fix: Seller details are usually on the product detail page, not in search results.
🔹 Step 8: Extract Stock Status
python
Copy
Edit
stock_status = product_item.find("span", class_="a-size-small a-color-price")
if stock_status:
    stock_status = stock_status.text.strip()
else:
    stock_status = "In Stock"
If a-size-small a-color-price is present, extracts stock status (e.g., "Only 2 left in stock").
Otherwise, assumes "In Stock" by default.
🔹 Step 9: Store Product Data
python
Copy
Edit
products.append({
    "Product Name": product_name,
    "Price": price,
    "Rating": rating,
    "Seller Name": seller_name,
    "Stock Status": stock_status,
})
Stores each product's details as a dictionary in the products list.
4. Save Data to CSV
python
Copy
Edit
def save_to_csv(products, filename="amazon_products.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Product Name", "Price", "Rating", "Seller Name", "Stock Status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write column headers
        writer.writerows(products)  # Write all product data
Opens a CSV file in write mode.
Uses csv.DictWriter to write column headers and product data.
Each row contains extracted product details.
5. Running the Script
python
Copy
Edit
if __name__ == "__main__":
    url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"  # Hardcoded URL
    products = scrape_amazon_products(url)
    save_to_csv(products)
    print(f"Product details scraped and saved to amazon_products.csv")
Calls the function with an Amazon URL.
Scrapes product details and saves them to a CSV file.
Prints a message when done.
📌 Key Takeaways
✅ Uses requests to fetch Amazon pages.
✅ Uses BeautifulSoup to extract product details.
✅ Saves structured data into a CSV file.
✅ Handles errors (e.g., missing prices, request failures).
✅ Seller Name Issue → Amazon does not always show sellers in search results.

🔥 Possible Improvements
🚀 Use Selenium to handle JavaScript-loaded content.
🔄 Extract product URLs and scrape seller details separately.
📊 Analyze pricing trends by scraping multiple pages.
