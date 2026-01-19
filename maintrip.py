import json
from datetime import datetime
from tripdata import get_trip
trips = []
trip1 = get_trip("Kochi", "15-05-2023", "Beautiful backwaters")
trip2 = get_trip("Munnar", "20-06-2023", "Amazing hill views")

trips.append(trip1)
trips.append(trip2)

for trip in trips:
    
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    
    trip["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)
print(json_data)
