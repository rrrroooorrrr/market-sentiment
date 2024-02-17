import requests
import datetime
from db_init import init_db
from time import sleep
from format_dates import convert_to_standard_format
start_date = "1993-05-29"
end_date = "2001-01-31"

# Convert start and end date strings to datetime objects
start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")

api_key = ''


def fetch_archives(year, month):
    """
    Fetches news archive for a specific year and month from the New York Times Archive API.

    Args:
    year (int): Year of the archive.
    month (int): Month of the archive.
    api_key (str): API key for authenticating with the New York Times API.

    Returns:
    dict: JSON response containing the archive data.
    """
    url = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json"
    params = {'api-key': api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        response = response.json()
        docs = response['response']['docs']
        return docs
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

db_connected = False
i=0
try:
    db = init_db('article_archive')
    collection = db['nyt']
    articles = collection.find({})
    for article in articles:
        pub_date = article['pub_date']
        date = convert_to_standard_format(pub_date)
        article['pub_date'] = date
        year = datetime.datetime.strptime(date,"%Y-%m-%d").strftime('%Y')
        if db[year] == None:
            db.create_collection(year)
        db[year].insert_one(article)
        print(f'insert article #{i}')
        i+=1
        

    
    # db_connected = True



    # if db_connected:
    #     current_date = start_date_obj
    #     while current_date <= end_date_obj:
    #         # Extract year and month as strings
    #         year = str(current_date.year)
    #         month = str(current_date.month).zfill(1)

    #         if current_date.month > 9:
    #             month = str(current_date.month).zfill(2)  # Ensure double-digit month format
    #         archive_data = fetch_archives(year, month)
    #         db['nyt'].insert_many(archive_data)
    #         # Process the API response as needed
    #         # (e.g., parse JSON, store data, etc.)

    #         # Move to the next month
    #         current_date += datetime.timedelta(days=30)
    #         print(f'Fetched and saved archive {month}/{year} on {datetime.datetime.now().strftime("%c")}')
    #         sleep(30)
except Exception as e:
    print(f'db connect failed {e}')