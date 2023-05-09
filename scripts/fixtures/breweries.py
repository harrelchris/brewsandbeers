import json

breweries = """
8th Wonder Brewery[1]	Houston	2013	Cans	Taproom
Alamo Beer Company[2]	San Antonio	2015	Bottles
Adelbert's Brewery[3]	Austin	2011	Cans	Taproom	They permanently closed 31 Oct 2022
Austin Beer Garden Brewing Company[4]	Austin	2013	Kegs	Brewpub
Austin Beerworks[5][6]	Austin	2011	Cans	Taproom
Austin Eastciders[7]	Austin	2013	Cans, Kegs	Taproom
Anheuser-Busch Brewery[8][9][10]	Houston	1966			Annual production of 12 million barrels as of 2013
B-52 Brewing Company[11]	Conroe	2014	Kegs, cans, bottles	Taproom	Barrel-aged beers. Ranked #5 in 2019 Texas Craft Beer Report
Bare Arms Brewing[12]	Waco	2015	Kegs	Taproom, crowlers, kegs
Barrow Brewing Company[13]	Salado	2016	Kegs, cans, growlers	Taproom
Big Bend Brewing Company[14]	Alpine	2012	Cans	tours	Defunct; closed at the end of 2018
Blackwater Draw Brewing Co.[15]	Bryan	2010	Kegs, Cans, Bottles	Taproom
Blue Owl Brewing[16]	Austin	2015	Cans
Bold Republic Brewing Company[17]	Belton	2018		Taproom
BrainDead Brewing[18]	Dallas	2015	Kegs, bottles	Brewpub	Scratch kitchen, barrel program, house and guest taps	Blind Boar	Buffalo Bayou Brewing Company[19][20]	Houston	2011	Cans
Cactus Land Brewing Company[21]	Adkins	2016	Bottles; cans	taproom
Cedar Creek Brewery[20][22]	Seven Points	2012	Cans	brewpub
Celis Brewery[23]	Austin	1992	Bottles; cans	taproom
Circle Brewing Company[24]	Austin	2010	Cans	Taproom
Community Beer Company[25]	Dallas	2013	Bottles, Cans, Kegs	Taproom
Cypress Creek Southern Ales[26]	Winnsboro	2018	Kegs	Taproom
Deep Ellum Brewing[27]	Dallas	2011	Bottles; cans	taproom
ETX Brewing Company[28]	Tyler	2017	Kegs	taproom
Eureka Heights Brewing Company[29]	Houston	2016	Kegs	Brewpub
Franconia Brewing Company[20]	McKinney	2008	Bottles, Kegs
Freetail Brewing Company[30]	San Antonio	2008	Bottles; cans	Brewpub; brewery with taproom
Friends & Allies Brewing[31][32]	Austin	2016	Cans	taproom
Four Corners Brewing[33]	Dallas	2012	Cans	taproom
Galveston Bay Brewing[34]	Dickinson	2014	Kegs, Cans	Taproom
Galveston Island Brewing[35]	Galveston	2014	Kegs, Cans	Taproom
Holler Brewing Company[36]	Houston	2016	Kegs	Taproom
Hops & Grain Brewery[37]	Austin	2011	Cans	taproom
HopFusion Ale Works[38]	Fort Worth	2016	Cans	taproom
Hopsquad Brewing Company[39]	Austin	2019	Cans	taproom
Independence Brewing Co.[40]	Austin	2004	Kegs, Cans, Bottles	Taproom	Distributes to Arkansas[41]
Intrinsic Smokehouse & Brewery[42]	Garland	2015		Brewpub
Jester King Brewery[20][43]	Austin	2010		Taproom
Karbach Brewing Company[20][44]	Houston	2011	Bottles; cans	brewpub
Krootz Brewing Company[45][46]	Gainesville	2019	Kegs; Cans	Brewpub	Scratch kitchen, live entertainment, regional distribution
Künstler Brewing[47]	San Antonio	2017		brewpub
Lakewood Brewing Company[48]	Garland	2011	Bottles; cans	taproom
Live Oak Brewing Company[20][49]	Austin	1997	Draft; cans	taproom
Lone Pint Brewing Company[20][50]	Magnolia	2012	Bottles
Martin House Brewing Company[51]	Fort Worth	2013	Cans	taproom
Meanwhile Brewing[52]	Austin	2020		Taproom
Middleton Brewing[53]	San Marcos	2011		Taproom
MillerCoors Brewery[9][54][55]	Fort Worth	1966			Lone Star is made by Miller at the Fort Worth brewery. The Lone Star brand is owned by Pabst Brewing Company.[56]
New Republic Brewing Company[15]	College Station	2011	Kegs, Cans, Bottles	Taproom, Beer Garden	Barrel-aged beers
No Label Brewing Company[20][57]	Katy	2010	Bottles	taproom
NLand Brewing Company[20]	Austin	2017	Kegs	taproom
On Rotation Brewery & Kitchen[58][59]	Dallas	2015	Kegs, Cans, Crowlers	Brewpub	Small batch craft beers brewed in-house with guest taps, scratch kitchen, trivia night, reverse happy hour, luxurious dog-friendly patio, located outside Love Field
Pegasus City Brewery[60][61]	Dallas	2017	Kegs, Cans	taproom
Peticolas Brewing Company[62][63]	Dallas	2011	Kegs, Cans	taproom	Grand National Champion at the 2018 U.S. Open Beer Championship.
Rahr and Sons Brewing Company[20][64]	Fort Worth	2004	Bottles
Ranger Creek Brewing & Distilling[65]	San Antonio	2010	Cans, bottles	Taproom, tours
Real Ale Brewing Company[20][66][67][68]	Blanco	1996	Cans, Bottles	taproom
Revolver Brewing[69]	Granbury	2012	Bottles
Rogness Brewing Company[70]	Austin	2012	Bottles	taproom
Saint Arnold Brewing Company[20][71]	Houston	1994	Cans; bottles	brewpub	First modern craft brewery in Texas
Saloon Door Brewing [72]	Webster	2015	Cans	taproom	"Best Draw in the West" makers of TASTY AF
Shannon Brewing Company[73]	Keller	2014	Cans	taproom
Southerleigh Fine Food & Brewery[74]	San Antonio	2015	Bottles	brewpub
Southern Star Brewing Company[20]	Conroe	2007	Cans	taproom
Spoetzl Brewery[20][75]	Shiner	1909	Bottles; cans	Tours	Makers of Shiner beer
Texas Beer Company [76]	Taylor	2016	Cans, Kegs	Taproom	In the historic McCrory-Timmerman building at 2nd and Main Street in Taylor.
Texas Beer Refinery[77]	Dickinson	2013	Bottles	taproom
Texian Brewing Company[20][78]	Richmond	2012	Kegs; bottles
Thirsty Planet Brewing Company[20][79]	Austin	2010	Bottles; Kegs		Makers of Thirsty Goat Amber & Buckethead IPA. Tasting Room coming in 2019.
True Vine Brewing Company[80]	Tyler	2014	cans	Taproom
TUPPS Brewery[81]	McKinney	2015	Kegs, Cans	Taproom
Twin Peaks Brewing Company[82]	Irving	2014	Cans		Produces kegs for the Twin Peaks restaurant chain.
Under the Radar Brewery[83]	Houston	2016	Kegs	Taproom
Westlake Brewing Company[84]	Dallas	2019	Kegs, Cans	Taproom	Located in Deep Ellum. 2021 GABF Gold-Medal Winner[85]
"""

data = []
for index, line in enumerate(breweries.strip().splitlines()):
    parts = line.split("\t")
    name = parts[0].split("[")[0]
    founded = parts[2]
    record = {
        "model": "brewery.brewery",
        "pk": index + 1,
        "fields": {
            "name": name,
            "founded": founded,
            "created_at": "1970-01-01 12:00:00.0+00:00",
            "updated_at": "1970-01-01 12:00:00.0+00:00"
        }
    }
    data.append(record)

print(json.dumps(data, indent=2))
