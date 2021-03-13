from pymongo import MongoClient

class BotMsgsModel:

    def __init__(self):
        self.client = MongoClient(sometokenfromenv)
        self.db = self.client.DiscordNewbies.bot_msgs

    def get(self, partyID):
        result = self.db.find_one({'partyID': partyID})
        return result

    def create(self, botMsgID, partyID):
        bot_msg = {
            'botMsgID': botMsgID,
            'partyID': partyID
        }
        self.db.insert_one(bot_msg)

    def delete(self, partyID):
        self.db.delete_many({'partyID': partyID})
