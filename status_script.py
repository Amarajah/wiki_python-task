import csv
import requests

# Specify the CSV file name
csv_filename = "Task 2 - Intern.csv"


# Open and read the CSV file
with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # This line skips the header row

    for row in reader:
        url = row[0].strip()  # Get the URL from the row and remove extra spaces
        
        try:
            response = requests.get(url, timeout=2)  # Send a request with a timeout
            status_code = response.status_code  # Get the status code
        except requests.exceptions.RequestException:
            status_code = "Error"  # If request fails, set status code as Error
        
        print(f"({status_code}) {url}")  # Print the output
