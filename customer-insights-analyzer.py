# customer-insights-analyzer.py
# Description: Analyzes customer data from a CSV file to provide insights on demographics and
# purchase behavior, including average age, most common name, average purchase amount, and total sales.
# Reports invalid data entries.


import csv
import re
from collections import Counter
from statistics import mean

# Function to validate email addresses using a regular expression
def is_valid_email(email):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

# Path to the CSV file containing customer data
csv_file_path = ""  # Replace with your actual file path

customer_data = []  # List to store valid customer data
invalid_data = []  # List to store errors related to invalid data entries

try:
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Validate and convert data, catching any discrepancies
            try:
                row['Age'] = int(row['Age'])
                if not is_valid_email(row['Email']):
                    raise ValueError(f"Invalid email format for customer {row['CustomerID']}.")
                customer_data.append(row)  # Add valid data to the list
            except ValueError as e:
                invalid_data.append(str(e))  # Collect error messages for invalid entries
except FileNotFoundError:
    print(f"Error: File {csv_file_path} not found.")
    exit()

# Analyze the data only if valid entries are present
if customer_data:
    # Calculate demographic insights
    average_age = mean(customer['Age'] for customer in customer_data)
    name_counter = Counter(customer['Name'] for customer in customer_data)
    most_common_name, most_common_name_count = name_counter.most_common(1)[0]

    # Calculate purchase behavior insights
    average_purchase_amount = mean(float(customer['PurchaseAmount']) for customer in customer_data)
    total_sales = sum(float(customer['PurchaseAmount']) for customer in customer_data)

    # Display insights
    print(f"Average Age: {average_age}")
    print(f"Most Common Name: {most_common_name} ({most_common_name_count} occurrences)")
    print(f"Average Purchase Amount: {average_purchase_amount}")
    print(f"Total Sales: {total_sales}")

# Report any invalid data entries
for error in invalid_data:
    print(error)
