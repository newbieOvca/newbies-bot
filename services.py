from models.bot_msgs import BotMsgsModel
from models.parties import PartiesModel
from models.roles import RolesModel

class BotMsgsServices:
    def __init__(self):
        self.model = BotMsgsModel()

    def create(self, botMsgID, partyName):
        return self.model.create(botMsgID, partyName)

    def get(self, partyID):
        return self.model.get(partyID)

    def delete(self, partyID):
        return self.model.delete(partyID)

class RolesServices:
    def __init__(self):
        self.model = RolesModel()

    def create(self, partyID, roleName):
        return self.model.create(partyID, roleName)

    def update(self, partyID, roleName, roleUsername, roleIsTaken):
        return self.model.update(partyID, roleName, roleUsername, roleIsTaken)

    def delete(self, partyID, roleName):
        return self.model.delete(partyID, roleName)

    def deleteBulk(self, partyID):
        return self.model.deleteBulk(partyID)

    def reset(self, partyID):
        self.model.reset(partyID)

    def list(self, partyID):
        response = self.model.list_roles(partyID)
        return response

    def clean(self, partyID):
        self.model.clean(partyID)

class PartiesServices:
    def __init__(self):
        self.model = PartiesModel()

    def create(self, partyName, partySlots, partyDate, partyTime, partyLeader):
        return self.model.create(partyName, partySlots, partyDate, partyTime, partyLeader)

    def getParty(self, partyName):
        return self.model.get(partyName)

    def updateSlots(self, partyID, partySlots):
        return self.model.updateDate(partyID, partySlots)

    def updateDate(self, partyID, partyDate):
        return self.model.updateDate(partyID, partyDate)

    def updateTime(self, partyID, partyTime):
        return self.model.updateTime(partyID, partyTime)

    def updateDone(self, partyID, partyDone):
        return self.model.updateTime(partyID, partyDone)

    def delete(self, partyID):
        return self.model.delete(partyID)