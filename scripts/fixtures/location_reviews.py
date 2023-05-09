import json
import random

texts = [
    "My wife and I really like this place.",
    "The beer here is awesome.",
    "They have live music every weekend, you should check it out!",
    "I like to take my dog here. They are super pet friendly.",
    "One of the best hidden gems in the city.",
    "Superb!",
    "It's a bar, I guess.",
    "I didn't like their beer lineup last summer, but this year's lineup is a banger!",
    "I went here once.",
    "Great staff!",
    "Good beer",
    "Nice music",
    "I love the atmosphere here. Super friendly",
    "This place is great, definitely recommend.",
    "Too many out of towners here.",
    "Their bathrooms are always clean",
    "Their flights are a great value",
    "I come here a couple times per week for happy hour with my friends.",
    "This is the place where my dad told me he cheated on my mom, so not the greatest memories tbh",
    "They have a friendly bar cat",
    "Not a fan of sour beers usually, but the sour beers here are so tasty",
    "They allow you to bring outside food and have a food truck on site",
    "We love that this establishment is kid friendly. We can being our family here and enjoy some beers.",
    "They donate to good charities.",
    "Trivia night is really fun",
    "One of my top 5 most visited places in this city for sure",
    "Definitely worth going out of your way to visit this place. Really good beer!",
]

data = []
pk = 1
for location in range(1, 365):
    for _ in range(5):
        record = {
            "model": "brewery.brewerylocationreview",
            "pk": pk,
            "fields": {
                "brewery_location": location,
                "user": random.randint(1, 200),
                "text": random.choice(texts),
                "rating": random.randint(3, 6),
                "created_at": "1970-01-01 12:00:00.0+00:00",
                "updated_at": "1970-01-01 12:00:00.0+00:00",
            },
        }
        data.append(record)
        pk += 1

with open("../../app/brewery/fixtures/location_reviews.json", "w") as f:
    json.dump(data, f)
