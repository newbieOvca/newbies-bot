from pymongo import MongoClient

class RolesModel:

    def __init__(self):
        self.client = MongoClient(sometokenfromenv)
        self.db = self.client.DiscordNewbies.roles

    def get(self, partyID, roleName):
        result = self.db.find_one({'partyID': partyID, 'roleName': roleName})
        return result

    def create(self, partyID, roleName):
        role = {
            'partyID': partyID,
            'roleName': roleName,
            'roleUsername': '',
            'roleIsTaken': 0
        }
        self.db.insert_one(role)

    def update(self, partyID, roleName, roleUsername, roleIsTaken):
        print(partyID)
        print("Inserting " + roleUsername + " for " + roleName)
        role = {
            'roleUsername': roleUsername,
            'roleIsTaken': roleIsTaken,
        }
        self.db.update_one({'partyID': partyID, 'roleName': roleName}, {'$set': role})

    def delete(self, partyID, roleName):
        self.db.delete_one({'partyID': partyID, 'roleName': roleName})

    def deleteBulk(self, partyID):
        self.db.delete_many({'partyID': partyID})

    def clean(self, partyID):
        self.db.delete_many({'partyID': partyID})

    def reset(self, partyID):
        self.db.update_many({'partyID': partyID}, {'$set': {'roleUsername': ''}})

    def list_roles(self, partyID):
        result = self.db.find({'partyID': partyID})
        return result
