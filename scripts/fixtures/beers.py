import json
import random

names = """Hommage
Intens Rood
70 Belgian Blonde Ale
4 est Lager
5 Oclock Shadow Pale Ale
Home Sweet Home
In Your Face Ipa
Home Sweet Home
8.6 Extreme
8.6 India Pale Lager
Abandoned At The Altar Raspberry Sour
Abbot Ale
Carb Free
Carb Free Lime
Mexican Lager
Mexican Style Lager
Pilsner
Radler Mix Pack
Vienna Lager
Pale Ale
Pale Ale 0.5%
Aecht Schlenkerla Rauchbier
Alexander Keiths Red
All-Out Effort American Amber
Pushin the Limits India Pale Lager
Take a Break Tropical Double IIPA
Hustle Over Hype Pale Wheat
Mead Braggot
Think Bigger Cream Ale
Allsopps IPA
Alpine Lager
Amber Of The North
Amstel Ultra
3speed Lager
Boneshaker
Fracture Hazy Imperial IPA
Fracture Imperial IPA
Fracture Juicy Imperial IPA
Fria Cerveza Especial
Natural Blonde
Neon Haze Hazy IPA
Space Invader Ipa
Winter Entertainer
Summer Pilsner
Amber Ale
Winter Dubbel
Autumn
Aussie IPA
Giving IPA
New Zealand Lager
Cream Ale
Gold Lager
Anderson Ipa
Hard Cider Crisp Apple
Another Hazy Beer
Ardiel Cider House Dry Apple Cider
Aria Ipa
Aria Lager
Aria Porter
Aria Safron
Arizona Hard Half N Half Iced Tea Lemonade (Malt)
Arizona Hard Lemon Ice Tea (Malt)
Arizona Hard M Green Tea (Malt)
Arizona Hard Peach Iced Tea (Malt)
Arizona Hard Variety Pack
Asahi Super Dry
Amber Ale
Blueberry Wheat
Company Blueberry Wheat
Company Cream Ale
Averbode Abbey Ale
Spinning Yarn Barrel Aged
Ayinger Ur-Weisse Bavarian Dunkel
Backpaddle Bonde Ale
Hawkwatch NEIPA
Prospector's Ale
Rusty Husky
Sawmill Lager
Bangarang Pink Lemonade Hard Seltzer (Malt)
Bangarang Retro Mixer Pack
Bavaria 8.6
Bavaria 8.6 Red
Bavaria Premium
Bronzeback Dark Ale
Co. Orchard Cherry Lager
Honey Cream Ale
Long Pond Lager
Beach Chair Lager
Beach Day Every Day Berry Beach (Malt)
Beach Day Every Day Iced Tea (Malt)
Beach Day Every Day Mixer Pack (Malt)
Beach Day Every Day Mixer Pack 2022
Beach Bound Lager
Bear Runner Blonde Ale
Bearded Prospector Cream Ale
Beau's Full Time IPA
Beau's Juiced Af Hazy Ipa
Beau's Local Organic
Beau's Lug Lite Lager
Beau's Lug Tread 2.5%
Beau's Lug Tread Collectible Glass Gift Pack
Beau's Lug Tread Lagered Ale
Beau's Nordic Pale Ale
Beaus Lug Tread Collectible Glass Gift Pack
Beaus Nordic Pale Ale
Becks
Becks Non Alcoholic 0.0
Beer Nerds California IPA
Belhaven Black Scot Stout
Bellwoods A Stout with Coffee
Bellwoods Acid House Sour IPA
Bellwoods Bellweiser Pilsner
Bellwoods Brewery Jelly King Dry Hopped Sour
Bellwoods Brewery Jelly King with Plum
Bellwoods Brewery Jutsu Pale Ale
Bellwoods Ghost Orchid IPA
Bellwoods Jelly King Pink Guava
Bellwoods Jelly King Sour
Bellwoods Jutsu Pale Ale
Bellwoods Monogamy Mosaic IPA
Bellwoods Roman Candle
Ball's Fall Session Ipa
Ball's Falls Session IPA
Berry Fields Sour Ale
Hopster DIPA
Hopsters IPA
Lincoln Lager
Mountainview Stout
Oaked Pilsner
Short Hills East Coast IPA
Short Hills Hazy Ipa
Benediktiner Hell
Berliner Pilsner
Berry Fields Tart & Juicy Sour Ale
Beyond The Pale Aromatherapy
Beyond The Pale Aromatherapy IPA
Co. Yummy!
Clean Cut
Cosmic Latte
Darkness
Pale Ale Project
Pink Fuzz
Tropicale Breeze
Yummy
Frequency APA
On the Lam IPA
Velocipede India Pale Ale
Velocipede IPA
Big Drop Paradiso IPA
Alpha Bomb Ipa
Brewery Shakedown APA
Busted Sled Gingerbread Stout
Gold
Premium
Premium Pilsner
Pumpkin Porter
Shakedown Apa
Bighead Amber - 100% Ontario Organic Hops
Bilboquet Series 72 Commemorative Blonde Beer
Birra Castello
Birra Moretti
Bitburger
Big Buck IPA
Crop Top
El 9 Wye
White Witbier
Black Ice
Black Label
20 Hazy Years
Nut Brown Ale
Pale Ale
Tropical Situation Pineapple APA
Lockstation Milk Stout
Navigator IPA
IPA
Blackburn Brewhouse Crick Water IPA
Blacklist Black German Lager
Blanche De Chambly
Blood Brothers Auto Pop Cherry Cola
Entheogen IPA
Shumei
Guilty Remnant
Paradise Lost Guava
Paradise Lost Spiced Cherry Sour
Blue
Belgian White (Formerly Belgian Moon)
Light Sky (Formerly Belgian Moon)
Mango Wheat (Formerly Belgian Moon)
White Mocha Coffee Chocolate Nitro Stout
Raspberry Sour
Strawberry Kiwi
Common Loon APA
Dockside
Northern Lights
Stargazer Black Rye IPA
Common Loon
Dockside Ale
Firefly Belgian White
Northern Lights
Petes Lager
Sweet Tooth Pumpkin Spice Latte
Bombardier Ale
Bombshell Blonde Ale
Bold
Iced Tea Mix Pack (Malt)
Slam
35 & 118 Cream Ale
Kungaroo Ipa
Boxer Ice
Boxer Lager Gluten Free
Gougounes Rousses
Tuque Doree
Brauwerk North German Pilsner
Brava
Brava Light
Aid Game Face Lager
Lime Beer
Maple Beer
Microbrewery Maple Beer
Revolution Kashmir Norwegian Pale Ale
Revolution Neipa - Walkin On Sunshine
Brewdog Hazy Jane
Batch: 1904
Mix Pack
Pina Colada Cider
Pineapple Agave Cider
Queen Street 501
Raspberry Peach Cider
Rose Cider
Stadium Island Peach Cider
Yuzu Lemon Cider
Sinister Minister IPA
Brimstone Hail Mary Session IPA
Lavender Peach (Malt)
Mango And Lychee (Malt)
Broad Reach Nor-Easter Ipa
Amber Ale
Blueberry Blonde
Pilsner
Neipa
Pilsner
Tangerine Ipa
Blonde
Bohemian Pilsner
Craft Light Lager
Strong Scotch Ale
Mango Tango Milkshake IPA
Milk Chocolate Stout
Traditional Irish Red
Tropical Thunder NEIPA
Brouczech Premium Lager
Brugse Zot Blond
Chelada
Chelada (Malt)
Flavour Faves
Lime
Lime (Malt)
Mango
Peach
Seltzer Black Cherry (Malt)
Seltzer Mango (Malt)
Seltzer Mix Pack (Malt)
Strawberry Lemonade
Shot
Zero
Mimosa (Malt)
Original (Malt)
Tuesday Saison
Vermont Blond
Ice
Ice 6.0
Light
Busl - Rubus - Hibiscus & Raspberry Cider
Buzz Hemp Beer
C'est What Durham Al's Cask Ale
Bogie
Brown Cow Milk Stout
Co Horizon NEIPA
Front Porch
Portage Pilsner
Bogie West Coast American Ipa
Brown Cow Nitro Stout
Bohemian Pils
Deadly Dark
Deadly Dark Lager
Vienna Lager
Cameron's Ambear Red Ale
Co. Bad Robot New England Double IPA
Crooked Nose Stout
I Love Craft Beer Mixed Pack
Captain's Log Lager
Coast to Coast Dry Hopped Lager
Cosmic Cream Ale
Cruising through the Galaxy NEIPA
Jungle of Love Volume II
Jurassic IPA
Crooked Nose Stout
Canuck Pale Ale
Bailout Blonde Craft Beer
Incipient IPA
Carib Lager
Carib Shandy Lime (Malt)
Ice
Lager
Light
Danish Pilsner Snap Pack
Lite
Brunch Line 2017
Caboose IPA
Franco Lager Artisanale
Kolsch Style Lagered Ale
Cerveza Revolucion
Chill Street Afternoon Delight Cider
Chimay 150
Chimay Blue Cap
Chimay Gold
Chimay Premiere
Chimay White Cap
Co Chimera
Holy Smoke Scotch Ale
Northumberland Ale
West Coast Pale Ale
Cigar City Frost Proof Belgian-Style White
Class V Ipa
Clausthaler Original
Clausthaler Premium Non Alcoholic
Clavie Smoked Porter
Clear Lake Session Ale
Company Dark Streets of London ESB
Porter
Clifford Porter
Clubtails Seltzer Mix Pack (Malt)
Clutch American Pale Ale
Coffin Ridge Forbidden Artisanal Cider
Krispy Cream Ale
Sublime Ipa
Cold Break Sublime IPA
12 Spakling Hard Teas (Malt)
Audio Visual Lager
Beyond Reason
Circling The Sun Applecherry Cider
Daily Forecast
Good Monster
Guava Gose
Hazy State
Hey Nelson
Jam Up The Mash
Lager
Life in the Clouds
Matter of Fact
Mosaic Four Ways IPA 23
Non-Alcoholic Pale Ale
Ransack The Universe IPA
Raspberry Peach Bellini Sour
Stranger Than Fiction with Coffee & Maple Syrup
Stranger Than Fiction, Porter
Collective Lager 6 Pack
Backcountry Black Lager
Downhill Pale Ale
Freestyle Apocalypso Pilsner
Sunset Point Lager
Freestyle Festbier
Happy Tails Session IPA
Colt 45 (Malt)
Common Good Beer Company Solace East Coast IPA
Blonde Lager
Lager
Edge 0.5
Light
Original
Black Cherry (Malt)
Mango (Malt)
Orange Cream Pop (Malt)
Variety Pack (Malt)
Slice Lime (Malt)
Slice Orange
Light
Sunbrew
Coronita
Coronita Extra
Hard Lemonade Mixed Pack (Malt)
Hard Seltzer Mixed Pack (Malt)
Hard Tea Mixed Pack (Malt)
County Apple Cider
County Pear Cider
Lumbersexual Session IPA
Covered Bridge Walk on the Mild Side
Cowbell Absent Landlord
Cowbell Bobcat
Cowbell Boxing Bruin Ipa
Summer Mixer
Absent Landlord
Blood Orange Summer Ale
Blood Orange Wheat Ale
Bobcat
Boxing Bruin IPA
Cencerro Cerveza Mexican Style Lager
Draught Nitro Stout
Grapefruit Radler
Hazy Days IPA
Hazy Days IPA Toasted Coconut
Light & Dark Oatmeal Vanilla Lager
Original Cider
Shindig Lager
Simply The Best Mix Pack
Smooth Sailing Light Lager
Hazy Days Ipa
Rose Cider
Shindig Lager
Smooth Sailing Light Lager
Crank Lite Lager
Collection Pack Featuring IPA
Crisp Pilsner
Helles Light Lager
Lot 9 Pilsner
Pale Ale
Premium Lager
Session Ipa
Springs Helles Light Lager
Springs Savour Summer Collection
Winter Collection Pack
Witbier
Crest Super
Crystal
Cup & Saucer English Ale
Dark Lager
Berry Cider
Cider
Dark Lager
Lemon Radler Unfiltered (Malt)
Maibock
Original Lager
Ultimate
Ultimate Low Carb, Low Cal Light Beer
Follow Your Nose Blackberry Sour IPA.
Julia Peach Sour
Viaduct IPA
Dark Streets Of London Esb
Dassai '45' Junmai Daiginjo Nigori
Daura Damm
Deadline Premium Blonde Lager
Decouverte - Non-Alcoholic Ipa
Delirium Tremens
Fresh Hazy IPA
Haze Tron Imperial Hazy IPA
Jubelale Winter Ale
King Crispy Pilsner
Wowza! Lo-Cal Hazy Pale Ale
Destihl Haze Of The Dead Hazy Double IPA
Devil's Pale Ale
Dieu Du Ciel - Peche Mortel
Divercity Helles Lager
War Dog Lagered Ale
Civic Pilsner
Sunsplit Ipa
Town & Country Blonde Ale
Two Flags Ipa
Doppel Hirsch Doppel Bock
Hops & Robbers IPA
Pecan Porter
Sucker Punch Red Raspberry Sour Ale
Garnet Azacca Citra Pale Ale
Dragon Stout
Dragon's Gold Cider
Fat Tug IPA
Duchesse De Bourgogne
Dunes Beach Beer
Empire Extra Dry Cider
Raindance Rhubarb Infused
Standing Rock
Houblon Chouffe Belgian IPA
N'ice Chouffe
Tripel Hop Cashmere
Duxbury Cider Co Heritage 1650 Dry Cider 473 Can
Banana Bread Beer
East Hamilton Lager German Style Pilsner
East Street Cider Co. Landmark Dry Cider
Electro Tonic Juniper Saison
Let's Go Exploring
Ebb & Flow Raspberry Lemon Yuzu
Hibiscus Blossom Cider
Perfect Pear
Eggenberg Brewery's Samichlaus
El Gringo Ipanema New World Ipa
El Gringo La Pachanga Cerveza
Borealis Pale Ale
Company Lady Friend IPA""".splitlines()
types = [
    "Ale",
    "Hybrid",
    "Lager",
]
styles = [
    "American Lager",
    "International Lager",
    "American Pale Ale",
    "India Pale Ale (IPA)",
    "Stout",
    "Wheat Beer",
    "Pilsner",
    "Porter",
    "American Brown Ale",
    "Sour Beer",
]

data = []
pk = 1
for i in range(1, 73):
    for _ in range(12):
        record = {
            "model": "beer.beer",
            "pk": pk,
            "fields": {
                "brewery": i,
                "name": random.choice(names).strip(),
                "type": random.choice(types),
                "style": random.choice(styles),
                "abv": max([random.randint(0, 500) / 100, 0]),
                "ibu": random.randint(5, 100),
                "created_at": "1970-01-01 12:00:00.0+00:00",
                "updated_at": "1970-01-01 12:00:00.0+00:00",
            },
        }
        data.append(record)
        pk += 1


with open("../../app/beer/fixtures/beers.json", "w") as f:
    json.dump(data, f)
