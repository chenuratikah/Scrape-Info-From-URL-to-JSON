# ScrapeFromURL_JSON

The following real time streaming pipeline are written to scrape data from URL in JSON format to MongoDB. The data is scraped based on polygons, stored hourly, sectioned by polygons and refreshed every 2 minutes.

In order to run the scripts every 2 minutes, I used Jenkins using cron expression to achieve this.

The actual set of polygons are excluded due to data sensitivity and confidential. The polygons are written in dictionary named as polygonsDict.py .
