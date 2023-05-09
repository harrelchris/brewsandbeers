import json
import random

data = []
pk = 1
for i in range(1, 865):
    for _ in range(3):
        record = {
            "model": "beer.beerimage",
            "pk": pk,
            "fields": {
                "beer": i,
                "image": f"images/beer/{random.randint(1,13)}.png",
                "created_at": "1970-01-01 12:00:00.0+00:00",
                "updated_at": "1970-01-01 12:00:00.0+00:00",
            },
        }
        data.append(record)
        pk += 1

with open("../../app/beer/fixtures/beer_images.json", "w") as f:
    json.dump(data, f)
