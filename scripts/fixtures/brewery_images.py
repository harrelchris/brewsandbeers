import json
import random

data = []
pk = 1
for i in range(1, 74):
    for _ in range(4):
        record = {
            "model": "brewery.image",
            "pk": pk,
            "fields": {
                "brewery": i,
                "image": f"images/brewery/{random.randint(1,11)}.png",
                "created_at": "1970-01-01 12:00:00.0+00:00",
                "updated_at": "1970-01-01 12:00:00.0+00:00",
            },
        }
        data.append(record)
        pk += 1

with open("../../app/brewery/fixtures/brewery_images.json", "w") as f:
    json.dump(data, f)
