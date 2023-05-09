import json
import random

texts = """
I like this beer
I love this beer
This beer is awesome
This beer is great
This beer is good
This beer is okay
I liked this beer the first time I tried it
I didn't like this beer at first, but now I like it
This is my favorite beer
This is one of my favorite beers.
I like this beer more than Budweiser
Really good beer
Great beer
Love this beer
Pretty good
Decent
Not bad
Goes well with hot dogs
Goes well with steak
I can drink this all day
I only drink this on special occasions
My wife's favorite beer
My brother's favorite beer
My favorite beer
My dad's favorite beer
I love this beer. Hope they make more like it
More like this please!
All of the beers from this brewery are really good
Can't get enough of this one
I have a six pack of this in my fridge right now
I have a six pack of this in my fridge at all times
Tasty!
Super tasty
Great taste
This is a crisp, refreshing beer
Get some of this ASAP!
You won't regret giving this beer a try
I highly recommend this beer
This is seasonal, so get some while it's available
I stock up on this beer. I love it
""".strip().splitlines()

data = []
for i in range(1, 4000):
    record = {
        "model": "beer.beerreview",
        "pk": i,
        "fields": {
            "beer": random.randint(1, 864),
            "text": random.choice(texts),
            "rating": random.randint(3, 5),
            "bitter": random.randint(1, 10),
            "sweet": random.randint(1, 10),
            "sour": random.randint(1, 10),
            "carbonation": random.randint(1, 10),
            "head": random.randint(1, 10),
            "smell": random.randint(1, 10),
            "user": random.randint(1, 200),
            "created_at": "1970-01-01 12:00:00.0+00:00",
            "updated_at": "1970-01-01 12:00:00.0+00:00",
        }
    }
    data.append(record)

with open("../../app/beer/fixtures/beer_reviews.json", "w") as f:
    json.dump(data, f)
