# Webshop Scraper

### Author: Imaduddin A Majid

This is Scrapy's spider to scrape product information from a webshop site.

## Setup

### Installation Requirements

pyOpenSSL>=19.0.0
Scrapy>=1.6.0

Install required Python packages by the following command:

```
$ pip install -r requirements.txt
```

## Usage

To run the spider, we can use Scrapy's `runspider` command:

```
$ scrapy runspider sandal.py
```

To produce the csv file as output we can add this option:

```
scrapy runspider sandal.py -o sandals_info.csv
```