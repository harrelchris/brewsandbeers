import json
import random

streets = """Second
Third
First
Fourth
Park
Main
Sixth
Oak
Maple
Pine
Cedar
Elm
Washington
Sunset
Ridge
High
Hill
Lake
Forest
Cherry
Meadow
Franklin
Lincoln
Broadway
Vine
Chestnut
Ridgeview
Madison
Adams
Grant
Jackson
Market
College
Walnut
Jefferson
Sunset View
Jefferson""".splitlines()

street_types = """Avenue
Boulevard
Circle
Drive
Hill
Lane
Parkway
Road
Street
Trail
Way""".splitlines()

cities = """New York City
Los Angeles
Chicago
Houston
Phoenix
Philadelphia
San Antonio
San Diego
Dallas
San Jose
Austin
Jacksonville
Franklin
Springfield
Clinton
Madison
Georgetown
Arlington
Centerville
Greenville
Chester
Liberty
Washington
Marion
Salem
Fairview
Oxford
Auburn
Union
Burlington
Bedford
Plymouth
Kingston
Mansfield
Monroe
Pleasanton
Bristol
Trenton
Milton
Columbus
Windsor
Kingston
Milton""".splitlines()

states = """Alabama
Alaska
Arizona
Arkansas
California
Colorado
Connecticut
Delaware
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
New York
North Carolina
North Dakota
Ohio
Oklahoma
Oregon
Pennsylvania
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming""".splitlines()


brewery_types = [
    "Brewery Only",
    "Taproom",
    "Brewpub",
    "Beer Garden",
    "Other"
]

capacities = [
    "< 10",
    "10-25",
    "25-50",
    "50-100",
    "> 100",
]

distributions = [
    "Cans",
    "Bottles",
    "Kegs",
    "Growlers",
    "Draft",
    "Other",
]

data = []
pk = 1
for i in range(1, 74):
    for _ in range(5):
        record = {
            "model": "brewery.brewerylocation",
            "pk": pk,
            "fields": {
                "brewery":  i,
                "street": f"{random.randint(100, 10000)} {random.choice(streets)} {random.choice(street_types)}",
                "city":  random.choice(cities),
                "state": random.choice(states),
                "type":  random.choice(brewery_types),
                "tours": random.randrange(100) > 90,
                "capacity":  random.choice(capacities),
                "distribution": random.choice(distributions),
                "created_at": "1970-01-01 12:00:00.0+00:00",
                "updated_at": "1970-01-01 12:00:00.0+00:00"
            }
        }
        data.append(record)
        pk += 1

print(json.dumps(data, indent=2))
