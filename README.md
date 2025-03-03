# Scrapy Rumah123 Crawler

This repository contains a web scraper built using Scrapy to extract data from Rumah123.

## Installation & Setup

Before running the scraper, follow these steps to set up your environment.

### 1. Create a Virtual Environment
Python virtual environments help isolate dependencies for different projects.

```sh
python -m venv .venv
```

Alternatively, if you are using **conda**, you can create an environment with:

```sh
conda create --name rumah123-crawler python=3.10
```

### 2. Activate the Virtual Environment

Activate the virtual environment based on your shell:

- **Linux/macOS (bash/zsh/fish)**:
  ```sh
  source .venv/bin/activate
  ```
- **Windows (cmd/PowerShell)**:
  ```sh
  .venv\Scripts\activate
  ```
- **Windows (Git Bash)**:
  ```sh
  source .venv/Scripts/activate
  ```

### 3. Install Dependencies

Install Scrapy and additional user-agent middleware:

```sh
pip install scrapy scrapy-user-agents
```

#### Optional: Install Additional Dependencies
- If dealing with **CAPTCHAs**, consider installing `scrapy-selenium` or `scrapy-splash`:
  ```sh
  pip install scrapy-selenium scrapy-splash
  ```
- To store results in **MongoDB or PostgreSQL**:
  ```sh
  pip install pymongo psycopg2
  ```

### 4. Run the Scraper

Execute the crawler with the following command:

```sh
scrapy crawl rumah123 -s JOBDIR=crawls/rumah123
```

#### Explanation:
- `scrapy crawl rumah123` → Runs the spider named `rumah123`.
- `-s JOBDIR=crawls/rumah123` → Enables job persistence, allowing the scraper to resume from where it left off in case of interruptions.

#### Optional: Export Data
You can save scraped data in various formats:
- JSON:
  ```sh
  scrapy crawl rumah123 -o output.json
  ```
- CSV:
  ```sh
  scrapy crawl rumah123 -o output.csv
  ```
- XML:
  ```sh
  scrapy crawl rumah123 -o output.xml
  ```

## Troubleshooting

- **Command Not Found**: Ensure the virtual environment is activated.
- **Permission Issues**: Try running commands with `python3` instead of `python`.
- **Scrapy Not Found**: Run `pip show scrapy` to confirm installation.

## Contributing
Feel free to submit issues or pull requests to improve this project!

