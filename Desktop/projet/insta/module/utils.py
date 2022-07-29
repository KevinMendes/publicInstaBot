import configparser
import csv

class Utils():
    def __init__(self, iniFile, passedPubFile):
        self.iniFile = iniFile
        self.passedPubFile = passedPubFile

    def parseIni(self):
        config = configparser.ConfigParser()
        config.read(self.iniFile)

        return config

    def getPassedPub(self):
         with open(self.passedPubFile, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                return list(reader)
                
    def updatePassedPub(self, pub: list) -> None:
        with open(self.passedPubFile, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(pub)
            csvfile.close()
            return None