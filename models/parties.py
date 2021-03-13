from pymongo import MongoClient

class PartiesModel:

    def __init__(self):
        self.client = MongoClient('mongodb+srv://todoAppUser:afryKa96@cluster0.jrvdm.mongodb.net/DiscordNewbies?retryWrites=true&w=majority')
        self.db = self.client.DiscordNewbies.parties

    # Get Party
    def get(self, partyName):
        result = self.db.find_one({'partyName': partyName})
        return result

    # Create Party
    def create(self, partyName, partySlots, partyDate, partyTime, partyLeader):
        party = {
            'partyName': partyName,
            'partySlots': partySlots,
            'partyDate': partyDate,
            'partyTime': partyTime,
            'partyLeader': partyLeader,
            'partyIsDone': 0
        }
        result = self.db.insert_one(party)
        return result.inserted_id

    # Update Slots
    def updateSlots(self, partyID, partySlots):
        party = {
            'partySlots': partySlots
        }
        self.db.update_one({'_id': partyID}, {'$set': party})

    # Update Date
    def updateDate(self, partyID, partyDate):
        party = {
            'partyDate': partyDate
        }
        self.db.update_one({'_id': partyID}, {'$set': party})

    # Update Time
    def updateTime(self, partyID, partyTime):
        party = {
            'partyTime': partyTime
        }
        self.db.update_one({'_id': partyID}, {'$set': party})

    # Update Done
    def updateDone(self, partyID, partyDone):
        party = {
            'partyIsDone': partyDone
        }
        self.db.update_one({'_id': partyID}, {'$set': party})

    # Delete Party
    def delete(self, partyID):
        self.db.delete_many({'_id': partyID})