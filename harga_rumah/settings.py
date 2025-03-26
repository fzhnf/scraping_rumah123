import os
from datetime import datetime

# Project Metadata
BOT_NAME = "harga_rumah"
SPIDER_MODULES = ["harga_rumah.spiders"]
NEWSPIDER_MODULE = "harga_rumah.spiders"

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FILE = f"logs/scrapy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
os.makedirs("logs", exist_ok=True)

# User-Agent Strategy
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Robots.txt and Crawling Ethics
ROBOTSTXT_OBEY = True
ROBOTSTXT_PARSER = "scrapy.robotstxt.RobotParser"

# Request Configurations
CONCURRENT_REQUESTS = 2  # Increased from 1, but still conservative
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 3  # Seconds between requests to same domain
DEPTH_LIMIT = 3  # Prevent deep crawling

# Retry and Error Handling
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [
    429,  # Too Many Requests
    500,
    502,
    503,
    504,  # Server Errors
    408,  # Request Timeout
    522,  # CloudFlare Connection Timeout
    524,  # CloudFlare Timeout Occurred
]

# Auto-Throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# Cookies and Sessions
COOKIES_ENABLED = True
COOKIES_DEBUG = False

# Downloader Middleware Configuration
DOWNLOADER_MIDDLEWARES = {
    # Disable default User-Agent middleware
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    # Random User-Agent Rotation
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
    # Custom Proxy Middleware (if using proxies)
    # 'harga_rumah.middlewares.RandomProxyMiddleware': 750,
    # Retry Middleware with Enhanced Logging
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": 550,
    # Recommended for handling various download scenarios
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
}

# Spider Middleware
SPIDER_MIDDLEWARES = {
    "harga_rumah.middlewares.HargaRumahSpiderMiddleware": 543,
}

# Extensions
EXTENSIONS = {
    # Close spider after critical errors
    "scrapy.extensions.closespider.CloseSpider": 500,
    # Memory Usage Monitoring (optional)
    "scrapy.extensions.memusage.MemoryUsage": 800,
}

# Memory Usage Settings (if MemoryUsage extension is enabled)
MEMUSAGE_LIMIT_MB = 2048  # 2GB memory limit
MEMUSAGE_NOTIFY_MAIL = None  # Add email if you want notifications
MEMUSAGE_WARNING_MB = 1024  # Warning at 1GB

# Performance and Compatibility
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Feeding and Export Configuration
FEED_EXPORT_ENCODING = "utf-8"
FEED_EXPORT_INDENT = 2  # Pretty-print JSON
FEEDS = {
    # Multiple output formats
    "outputs/rumah123_%(time)s.jsonl": {
        "format": "jsonlines",
        "overwrite": False,
    },
    "outputs/rumah123_%(time)s.csv": {
        "format": "csv",
        "overwrite": False,
    },
}

# Optional: Splash Configuration for JavaScript-rendered sites
# SPLASH_URL = 'http://localhost:8050'
# DOWNLOADER_MIDDLEWARES['scrapy_splash.SplashCookiesMiddleware'] = 723
# DOWNLOADER_MIDDLEWARES['scrapy_splash.SplashMiddleware'] = 725
# SPIDER_MIDDLEWARES['scrapy_splash.SplashDeduplicateArgsMiddleware'] = 100

# Optional: Proxies Configuration
# PROXIES = [
#     'http://user:pass@ip:port',
#     'http://another_proxy_ip:port'
# ]

# Close Spider Settings
CLOSESPIDER_PAGECOUNT = 1000  # Limit total pages
CLOSESPIDER_ITEMCOUNT = 10000  # Limit total items
CLOSESPIDER_TIMEOUT = 3600  # 1 hour timeout

# Telnet Console (for debugging)
TELNETCONSOLE_ENABLED = False
TELNETCONSOLE_PORT = 6023
