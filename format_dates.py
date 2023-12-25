from datetime import datetime
formats = [
    "%d/%m/%Y", "%m/%d/%Y", "%Y-%m-%d", "%d-%b-%Y", "%b-%d-%Y", "%B %d, %Y",
    "%Y %B %d", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%SZ",
    "%d/%m/%Y %H:%M", "%m/%d/%Y %I:%M %p", "%Y-%m-%d %H:%M:%S",
    "%d-%m-%Y", "%m-%d-%Y", "%Y/%m/%d", "%d/%b/%Y", "%b/%d/%Y", "%d %B %Y",
    "%Y %d %B", "%d %b %Y %H:%M:%S", "%Y-%m-%d %I:%M %p", "%Y-%m-%dT%H:%M:%S",
    "%d/%m/%Y %I:%M %p", "%m/%d/%Y %H:%M:%S", "%Y%m%d", "%d%m%Y",
    "%m%d%Y", "%Y%d%m", "%d%b%Y", "%b%d%Y", "%d%B%Y", "%B%d%Y",
    "%Y%d%B", "%Y%b%d", "%d %B %Y %H:%M", "%Y %d %B %I:%M %p",
    "%Y-%b-%d", "%b-%Y-%d", "%d-%Y-%b", "%d-%m-%Y %H:%M:%S",
    "%m-%d-%Y %I:%M:%S %p", "%Y%m%d%H%M%S", "%d%m%Y%H%M%S",
    "%m%d%Y%H%M%S", "%Y%d%m%H%M%S", "%H:%M %d-%m-%Y", "%I:%M %p %m-%d-%Y",
    # More formats can be added here
     "%a, %d %b %Y %H:%M:%S %Z", "%d %b %Y %H:%M %Z", "%b %d, %Y %H:%M %Z"
]




def convert_to_standard_format(date_str):
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Date format of '{date_str}' is not recognized")


