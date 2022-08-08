import configparser
import csv
import uuid
import os
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
                reader = csv.reader(csvfile, delimiter=';')
                return list(reader)
                
    def updatePassedPub(self, pub: list) -> None:
        with open(self.passedPubFile, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(pub)
            csvfile.close()
            return None

    def modifyPassedPub(self, uuidStr: str) -> None:
        with open(self.passedPubFile, 'r', newline='') as oldFile, open('data/passedPub_temp.csv', 'w', newline='') as newFile:
            reader = csv.reader(oldFile, delimiter=';')
            writer = csv.writer(newFile, delimiter=';')
            for row in reader:
                if row[5] == uuidStr:
                    writer.writerow([row[0],row[1],row[2],row[3],'Oui',row[5]])
                else:
                    writer.writerow(row)
        os.remove('data/passedPub.csv')
        os.rename('data/passedPub_temp.csv', 'data/passedPub.csv')