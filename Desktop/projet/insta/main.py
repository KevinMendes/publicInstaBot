from module.utils import Utils
from bot.bot import Bot
import os

def path(file):
    return os.path.abspath(file)


#Get credentials from ini file
fileParser = Utils(path('config.ini'), path('data/passedPub.csv'))
login = fileParser.parseIni()["CREDENTIAL"]["login"]
password = fileParser.parseIni()["CREDENTIAL"]["password"]
passedPubUpdate = fileParser.updatePassedPub
#Recupération des fichiers de data
passedPub = fileParser.getPassedPub()

#Run du bot
launchBot = Bot(login, password)

launchBot.Connexion()
listOfHashtag = fileParser.parseIni()["HASHTAG"]["list"].split(",")
launchBot.doThing(listOfHashtag=listOfHashtag, passedPub=passedPub, passedPubUpdate=passedPubUpdate)
launchBot.teardown_method()

