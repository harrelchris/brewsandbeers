import json
import random

data = []
pk = 1
for i in range(1, 365):
    for _ in range(5):
        record = {
            "model": "location.locationimage",
            "pk": pk,
            "fields": {
                "location": i,
                "image": f"images/location/{random.randint(1,21)}.png",
                "created_at": "1970-01-01 12:00:00.0+00:00",
                "updated_at": "1970-01-01 12:00:00.0+00:00",
            },
        }
        data.append(record)
        pk += 1

with open("../../app/location/fixtures/location_images.json", "w") as f:
    json.dump(data, f)
