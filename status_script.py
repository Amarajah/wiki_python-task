import csv
import requests

# Specify the CSV file name
csv_filename = "Task 2 - Intern.csv"

def fetch_url_status(url, request_func=requests.get):
    """Fetches the status code of the URL plus specific error handling."""
    try:
        response = requests.get(url, timeout=2)
        return response.status_code
    except requests.exceptions.Timeout:
        return "Timeout Error"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    except requests.exceptions.RequestException:
        return "General Error"

# Prevents the script from automatically running when imported into test file
if __name__ == "__main__":
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        for row in reader:
            url = row[0].strip()
            status_code = fetch_url_status(url)
            print(f"({status_code}) {url}")