Amazon Product Scraper 🛒
📌 Project Overview

This project is a web scraper that extracts product details from Amazon search results using Python, BeautifulSoup, and Requests. The extracted data includes product name, price, rating, seller name, and stock status, which is saved into a CSV file.

🛠 Technologies Used

Python 🐍
Requests (for fetching web pages)
BeautifulSoup (for parsing HTML)
CSV (for storing extracted data)
Logging (for error tracking)
📂 Project Structure
bash
Copy
Edit
📂 Amazon-Scraper
 ├── amazon_scraper.py   # Main script
 ├── amazon_products.csv # Extracted product data
 ├── README.md           # Project documentation
 ├── requirements.txt    # Required dependencies
🚀 Features
✅ Extracts product details (name, price, rating, seller, stock status)
✅ Saves data in CSV format for easy analysis 📊
✅ Handles errors gracefully using logging
✅ Customizable (change the URL to scrape different product categories)

🔧 Setup & Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/yourusername/Amazon-Scraper.git
cd Amazon-Scraper
2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Scraper
sh
Copy
Edit
python amazon_scraper.py
After running the script, product details will be saved in amazon_products.csv.

⚠️ Limitations & Notes
⚠ Amazon blocks frequent bot requests → Use rotating User-Agents or Proxies for large-scale scraping.
⚠ Seller names may not always appear → Requires deeper scraping or Selenium.
⚠ Dynamic content may not load → Consider using Selenium if needed.

💡 Future Improvements
🚀 Use Selenium for dynamic content loading.
📊 Analyze price trends by scraping at regular intervals.
🔄 Scrape multiple pages instead of a single page.

