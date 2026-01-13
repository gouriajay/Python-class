from tracker import create_record
from datetime import datetime
import json

records = [
    create_record("Kochi", "Beautiful backwaters", "05-06-2022"),
    create_record("Munnar", "Amazing hill station", "15-12-2023"),
    create_record("Goa", "Enjoyed the beach", "20-01-2024")
]

for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)
print("JSON Output:\n")
print(json_data)


parsed_data = json.loads(json_data)

print("\nParsed Records:\n")
for record in parsed_data:
    print(f"City: {record['city']}, Date: {record['date']}, Comment: {record['comment']}")
