import feedparser

# Example list of RSS feed URLs
rss_feeds = [
    "https://www.federalreserve.gov/feeds/press_all.xml",
    "https://rss.csmonitor.com/feeds/business",
    "https://rss.csmonitor.com/feeds/world",
    "https://rss.csmonitor.com/feeds/usa",
    "https://rss.csmonitor.com/feeds/politics",
    "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
    "https://www.reutersagency.com/feed/?best-sectors=economy&post_type=best",
    "https://www.reutersagency.com/feed/?best-topics=political-general&post_type=best",

]

def fetch_news():
    news_articles = []

    for feed_url in rss_feeds:
        feed = feedparser.parse(feed_url)
        
        for entry in feed.entries:
            article = {
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'summary': entry.summary if 'summary' in entry else None
            }
            news_articles.append(article)

    return news_articles

# Example usage
news_data = fetch_news()
for article in news_data:
    print(article['title'])
    # Further processing can be done here
