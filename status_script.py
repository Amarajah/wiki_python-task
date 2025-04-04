import csv
import requests

# Specify the CSV file name
csv_filename = "Task 2 - Intern.csv"

def fetch_url_status(url):
    """Fetch the status code of a given URL with error handling."""
    try:
        response = requests.get(url, timeout=2)
        return response.status_code
    except requests.exceptions.Timeout:
        return "Timeout Error"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    except requests.exceptions.RequestException:
        return "General Error"

# Prevent the script from running when imported
if __name__ == "__main__":
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        for row in reader:
            url = row[0].strip()
            status_code = fetch_url_status(url)
            print(f"({status_code}) {url}")
