# main.py

import os
import csv
import json
from flask import Flask, request, jsonify, render_template
from my_code import my_function  # Import my_function from my_code.py

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Execute my_function from my_code.py
        my_function()

        # Read the CSV file and convert it to JSON
        data = []
        with open('rising_related_queries_with_date.csv', 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)

        # Render an HTML template and pass the data to it
        return render_template('index.html', data=data)

    except Exception as e:
        return f'An error occurred: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
