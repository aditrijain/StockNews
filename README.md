# Stock News Notifier

A Python script to monitor stock price changes and send relevant news articles via email when significant price fluctuations occur.

---

## Features
- Fetches daily stock price data from [Alpha Vantage](https://www.alphavantage.co/).
- Determines if the stock price change exceeds a specified threshold (default is 5%).
- Retrieves the top 3 news articles about the company using [News API](https://newsapi.org/).
- Sends an email notification with the stock price change and news articles.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- `requests` library
- `smtplib` for sending emails

---

## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/aditrijain/StockNews.git
   cd stock-news-notifier
   ```

2. **Install required libraries:**
   ```bash
   pip install requests
   ```

3. **Environment Variables:**
   Create environment variables to store sensitive information securely:
   - `SENDER_EMAIL`: Email address of the sender.
   - `EMAIL_PASS`: Password or app-specific password for the sender's email.
   - `RECEIVER_EMAIL`: Email address of the receiver.
   - `API_KEY`: API key from Alpha Vantage.
   - `API_KEY_NEWS`: API key from News API.

   Example (Linux/MacOS):
   ```bash
   export SENDER_EMAIL="youremail@example.com"
   export EMAIL_PASS="yourpassword"
   export RECEIVER_EMAIL="receiver@example.com"
   export API_KEY="your_alpha_vantage_api_key"
   export API_KEY_NEWS="your_news_api_key"
   ```

4. **Configuration:**
   Update the following variables in the script to monitor the desired stock/company:
   ```python
   STOCK = "TSLA"  # Stock symbol
   COMPANY_NAME = "Tesla Inc"  # Full company name
   ```

---

## Usage
Run the script:
```bash
python main.py
```
If the stock price changes by 5% or more (up or down), an email will be sent to the receiver with:
- The stock's percentage change and direction.
- Titles, descriptions, and URLs of the top 3 relevant news articles.

---

## Example Email
**Subject:** News related to TSLA stock 🔺 by 5.2%

**Body:**
```

Here are the top news articles:

1. Article Title 1
Description 1
URL 1

2. Article Title 2
Description 2
URL 2

3. Article Title 3
Description 3
URL 3
```

---

## Notes
- The stock price threshold is hardcoded to 5%. You can modify it in the `is_relevant` function.

---

## Limitations
- API usage is subject to rate limits of Alpha Vantage and News API. Refer to their documentation for details.
- Emails are sent in plain text format. Future enhancements could include HTML formatting.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.


---

## Acknowledgments
- [Alpha Vantage](https://www.alphavantage.co/)
- [News API](https://newsapi.org/)



