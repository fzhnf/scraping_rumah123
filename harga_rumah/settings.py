BOT_NAME = "harga_rumah"

SPIDER_MODULES = ["harga_rumah.spiders"]
NEWSPIDER_MODULE = "harga_rumah.spiders"

# Rotate User-Agents to avoid detection
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Respect robots.txt
ROBOTSTXT_OBEY = True

# Enable cookies (some sites require cookies for session management)
COOKIES_ENABLED = True

# Limit concurrent requests to avoid overwhelming the server
CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# Retry failed requests (including 429 errors)
RETRY_TIMES = 5
RETRY_HTTP_CODES = [
    429,
    500,
    502,
    503,
    504,
]  # Add 429 to the list of retryable status codes

# Add a delay between requests
DOWNLOAD_DELAY = 5  # Increase this if you're still getting 429 errors

# Enable AutoThrottle to dynamically adjust request rate
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 120
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Close spider after a certain number of errors
CLOSESPIDER_ERRORCOUNT = 3

# Middleware settings
SPIDER_MIDDLEWARES = {
    "harga_rumah.middlewares.HargaRumahSpiderMiddleware": 543,
}

DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,  # Disable default UserAgentMiddleware
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,  # Enable random user agents
    "harga_rumah.middlewares.HargaRumahDownloaderMiddleware": 543,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": 550,
}

# Extensions
EXTENSIONS = {
    "scrapy.extensions.closespider.CloseSpider": 500,
}

# Request fingerprinting
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

# Use asyncio reactor for better performance
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Feed export settings
FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    "rumah123.json": {"format": "jsonlines"},
}
