# wiki_python-task

The Python script in this repo reads a list of URLs from a CSV file and checks their HTTP status codes using the Python 'requests' library.<br>
If a URL is accessible, its status code will be printed out along with the URL, else, an error message is displayed in place of the HTTP status.<br>

Please note that while testing, it was observed that the URLs in the CSV file appear to be broken or outdated and this resulted in errors, so you would need to test out the script with URLs that are actually accessible (or a CSV containing the accessible URLs) to see how it works in real time :)
