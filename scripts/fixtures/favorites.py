import json
import random

data = []
pk = 1
for user in range(1, 201):
    for _ in range(10):
        record = {
            "model": "beer.favorite",
            "pk": pk,
            "fields": {
                "beer": random.randint(1, 864),
                "user": user,
                "created_at": "1970-01-01 12:00:00.0+00:00",
                "updated_at": "1970-01-01 12:00:00.0+00:00",
            },
        }
        data.append(record)
        pk += 1

with open("../../app/beer/fixtures/favorites.json", "w") as f:
    json.dump(data, f)
