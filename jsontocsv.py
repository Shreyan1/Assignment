import json
import csv

def json_to_csv(json_file, csv_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Open the CSV file for writing
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        
        # Write the header
        writer.writerow(['db_id', 'question', 'evidence', 'SQL'])
        
        # Write the data
        for item in data:
            writer.writerow([
                item.get('db_id', ''),
                item.get('question', ''),
                item.get('evidence', ''),
                item.get('SQL', '').replace('\n', ' ')  # Replace newlines with spaces
            ])

# Usage
json_file = 'train.json'
csv_file = 'output.csv'

json_to_csv(json_file, csv_file)
print(f"CSV file '{csv_file}' has been created.")