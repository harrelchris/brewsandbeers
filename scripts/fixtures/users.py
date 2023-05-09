import json

from django.utils.crypto import get_random_string


usernames = """volkswagoncampfire
pulsesmonument
featherguidance
trivialloser
fairlyknowledge
lazymurmur
pufferfishprefer
sowirritable
lapwingmourner
slipwaynorth
zonkedgod
cabbagebazaar
heyruddy
ramwonder
dietnumeral
cowardlyphysicist
strippedanywhere
deceivepermanent
apronvirtually
loosenebulous
frostsquish
listenertweet
examplebuntline
handkerchiefmouth
meetingarab
trafalgarjukebox
totemweepy
assroach
scallopssteady
dumbasscrocodile
biddynervous
birchwoodorchestra
safetywelcome
duckafrican
bidisle
porcupinedramatic
toothchannel
duskyrare
raftingmidlands
soberideal
crushupbeat
observerwood
cookietaurus
molarhesitant
cheeseburgerstatistics
thrusheparrot
lobejibe
wateryexecutive
boughtjuices
lineardeadwood
ensureboatswain
awarenessmakeshift
simplybasic
affirmreceipt
hooliganpiano
candidwrist
stunningominous
righttourist
airportcolony
letovercoat
catfishmagnet
basefrankfurter
chucklesari
watchfulmorose
newequally
demureactress
wavyhousing
pharmacisttheme
medullahandkerchief
commissionprohibited
fuelwelsh
ceremoniouspoem
phaseknickers
heroacross
insistenttobacco
witherunicorn
bacteriamushrooms
averagereal
farmerclementine
dualshiver
leadershipwrithe
studaries
dustygood
straightappoint
foresaildiscourse
billioneasily
rowingmotherly
sweatpantssaving
longfeigned
foxallianz
magpievisual
milescreech
mealynostalgic
repaircommit
stemsacred
asparagusintention
crickettaiga
operatorassistance
pillarpercentage
journeymaple
authorunsuitable
sonmolt
genuinefleet
uncoveredvegan
sombrerohit
confusedroll
jokerunlock
barterhonk
analysispurse
amazedemployee
lividactivator
advancedmicrosoft
teencrucial
musselspenitent
frapshepherd
riptideuneven
presidentphysician
jarmeasure
totalcoral
blindmemorable
ceilingpunch
adviceadamant
postboxstone
podblare
luresloth
flairheadproductive
skycharming
microbetrifling
whoseviolation
crushingcustom
behaveentrance
batterynod
grocerymove
bluetvillager
cherryxmas
basisnoun
artificialquaint
reliablefletching
exultantleotard
admitgecko
pebblefurniture
turbanabsorbing
sodahandball
joystickhis
gybebloated
hornbillesteemed
posemash
labourergroup
mansionmeet
mixautomobile
daggerpeaches
swimfar
handyescutcheon
unpopularstorm
stopsmoked
extolllastage
lateenlymph
candycanebiscay
arroganttroubled
littlecloak
condemnedaudience
cheerfulphysical
lastingmedia
moaningenglish
shortstopmean
willowbasis
roachguillemot
inviteacquire
wealthymyth
coaloreaquatic
involvedstrike
endcitytwin
crabbyfortunate
pansyprove
earningspick
withscuttles
clausconnect
learnedinborn
welltodofez
dieticianexamine
needsizzle
flowerpothappy
mediumreligion
fibulaapathetic
robinpharmacist
mayorbricks
hoveritch
staffusual
imaginarypretzel
visibilitysponson
flipflopsnursery
illustrategripping
teargiving
essexpacked
overdueglasses
rainytaste
herbnothing
crochetmaniacal
congresshabitat
overworlddemonic""".splitlines()

data = []
for index, username in enumerate(usernames):
    record = {
        "model": "auth.user",
        "pk": index + 2,
        "fields": {
            "username": username,
            "password": get_random_string(32),
            "email": f"{username}@email.com",
            "is_superuser": False,
            "is_staff": False,
            "is_active": True,
            "date_joined": "1970-01-01 12:00:00.0+00:00",
        }
    }
    data.append(record)

print(json.dumps(data, indent=2))
