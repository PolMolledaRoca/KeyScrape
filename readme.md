# Web Scraper (Extractor de Datos Web)

This script extracts **text from a webpage based on a keyword search** and saves it to a CSV file.

---

## 🛠 Features (Características)
- ✅ **Searches for any text containing a specified keyword.**
- ✅ **Extracts relevant content from any webpage.**
- ✅ **Saves extracted data to a CSV file.**
- ✅ **Uses `requests` for web requests and `BeautifulSoup` for parsing.**
- ✅ **Command-line interface (CLI) for easy use.**

---

## 🚀 How to Use (Cómo Usarlo)

### 🔹 **Installation (Instalación)**
Ensure you have Python 3 installed, then install the required dependencies:
```bash
pip install requests beautifulsoup4
```

### 🔹 **Run the Scraper (Ejecutar el Scraper)**
```bash
python web_scraper.py https://example.com "Python" output.csv
```

### 🔹 **Example (Ejemplo)**
```bash
python web_scraper.py https://news.ycombinator.com "AI" hacker_news.csv
```
This extracts all text that contains the keyword "AI" from the page and saves it to `hacker_news.csv`.

---

## 🏗 Requirements (Requisitos)
- Python 3.x
- `requests` (for HTTP requests)
- `beautifulsoup4` (for HTML parsing)

---

## 🔥 Contributing (Contribuir)
Feel free to improve the project by adding features like:
- ✅ Extracting structured data (paragraphs, links, etc.).
- ✅ Exporting data in JSON format.
- ✅ Support for multiple pages.

---

## 📜 License (Licencia)
MIT License - Free to use and modify.
