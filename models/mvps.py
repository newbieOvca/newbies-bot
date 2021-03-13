# from pymongo import MongoClient

# class MVPsModel:

#     def __init__(self):
#         self.client = MongoClient('mongodb+srv://todoAppUser:afryKa96@cluster0.jrvdm.mongodb.net/DiscordNewbies?retryWrites=true&w=majority')
#         self.db = self.client.DiscordNewbies.mvps

#     def get(self, mvpName):
#         result = self.db.find_one({'mvpName': mvpName})
#         return result

#     def create(self, mvpName, mvpLocation, mvpMinResp, mvpMaxResp):
#         mvp = {
#             'mvpName': mvpName,
#             'mvpLocation': mvpLocation,
#             'mvpKilledAt': 0,
#             'mvpMinResp': mvpMinResp,
#             'mvpMaxResp': mvpMaxResp
#         }
#         self.db.insert_one(mvp)

#     def update(self, mvpID, mvpName, mvpLocation, mvpKilledAt, mvpMinResp, mvpMaxResp):
#         mvp = {
#             'mvpName': mvpName,
#             'mvpLocation': mvpLocation,
#             'mvpKilledAt': mvpKilledAt,
#             'mvpMinResp': mvpMinResp,
#             'mvpMaxResp': mvpMaxResp
#         }
#         self.db.update_one({'partyID': mvpID}, {'$set': mvp})

#     def time(self, mvpName, mvpKilledAt):
#         mvp = {
#             'mvpKilledAt': mvpKilledAt,
#         }
#         self.db.update_one({'mvpName': mvpName}, {'$set': mvp}) 

#     def delete(self, mvpID):
#         self.db.delete_one({'mvpID': mvpID})

#     def reset(self):
#         self.db.update_many({}, {'$set': {'mvpKilledAt': ''}})

#     def list_mvps(self):
#         result = self.db.find({})
#         return result