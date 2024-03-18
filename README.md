# urltotext
 A light weight library that takes in a url and extracts any readable text in it.

 Accepting any and all PRs!

## Installation

```
pip install urltotext
```

## Pre-requisites

1. `urltotext` uses `selenium` with the driver scope currently limited to `chrome` only. Please ensure that chromedriver is properly configured. Use this [link](https://www.swtestacademy.com/install-chrome-driver-on-mac/) for installation instructions.

## Usage

1. Import and initialize ContentFinder

```python
from urltotext import ContentFinder
cf = ContentFinder
```

2. Scrape a url

```python
# scrape a url
cs.scrape_url(url="your_url_here")

# print the article
cs.print_article(url="your_url_here")

# all urls passed will be stored in the class instance.
# use the flush_data method to free memory
cs.flush_data()
```

Enjoy!