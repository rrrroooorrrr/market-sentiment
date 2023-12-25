import feedparser

# Example list of RSS feed URLs
rss_feeds = [
    "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
    # "https://rss.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml"
    # "https://rss.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml"
    # "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml"
    # "https://rss.nytimes.com/services/xml/rss/nyt/MediaAdvertising.xml"
    # "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"
    # "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    # "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
    # "https://rss.nytimes.com/services/xml/rss/nyt/YourMoney.xml"
    # "https://rss.nytimes.com/services/xml/rss/nyt/DealBook.xml"
    # "https://www.federalreserve.gov/feeds/press_all.xml",
    # "https://rss.csmonitor.com/feeds/business",
    # "https://rss.csmonitor.com/feeds/world",
    # "https://rss.csmonitor.com/feeds/usa",
    # "https://rss.csmonitor.com/feeds/politics",
    # "https://www.reutersagency.com/feed/?best-topics=health&post_type=best"
    # "https://www.reutersagency.com/feed/?best-topics=tech&post_type=best"
    # "https://www.reutersagency.com/feed/?best-topics=environment&post_type=best"
    # "https://www.reutersagency.com/feed/?best-topics=deals&post_type=best"
    # "https://www.reutersagency.com/feed/?taxonomy=best-customer-impacts&post_type=best",
    # "https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best"
    # "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
    # "https://www.reutersagency.com/feed/?best-sectors=economy&post_type=best",
    # "https://www.reutersagency.com/feed/?best-topics=political-general&post_type=best",
    # "https://www.cbsnews.com/latest/rss/us"
    # "https://www.cbsnews.com/latest/rss/health"
    # "https://www.cbsnews.com/latest/rss/science"
    # "https://www.cbsnews.com/latest/rss/space"
    # "https://www.cbsnews.com/latest/rss/technology"
    # "https://www.cbsnews.com/latest/rss/world"
    # "https://www.cbsnews.com/latest/rss/moneywatch"

]

def fetch_news():
    print('Fetching RSS Feeds...')
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

