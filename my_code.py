# my_code.py

import csv
from pytrends.request import TrendReq
from datetime import datetime
import time
import os
# Create a pytrends object
pytrends = TrendReq(hl='en-US', tz=360, geo='US')

# Define your search query and timeframe
keyword = 'recipe'
timeframe = 'now 4-H'  # Retrieves data for the last 4 hours

while True:
    try:
        # Get the current date and time
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Build the payload for the Google Trends API request
        pytrends.build_payload(kw_list=[keyword], timeframe=timeframe)

        # Get Google Trends data for the specified keyword and timeframe
        trends_data = pytrends.interest_over_time()

        # Get related queries
        related_queries = pytrends.related_queries()

        # Check if the keyword exists in the related_queries dictionary
        if keyword in related_queries:
            related_rising_queries = related_queries[keyword]['rising']

            # Print the rising related queries
            print("\nRising Related Queries:")
            print(related_rising_queries)

            # Save rising related queries to a CSV file with a date column
            with open('rising_related_queries_with_date.csv', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Date', 'Query', 'Value'])
                for query in related_rising_queries.iterrows():
                    csv_writer.writerow([current_date] + list(query[1]))

            print(f"\nRising Related Queries saved to 'rising_related_queries_with_date.csv' with date {current_date}.")
            os._exit(0)

        else:
            print(f"No related queries found for '{keyword}'.")

        # Wait for a minute (60 seconds) before running again
        time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # Wait for a minute (60 seconds) before retrying
        time.sleep(60)
