# from datetime import datetime, date
import discord

class MsgTemplate:

    def getTemplate(self, roleList, date, time, name, leader):
        string = f'''
```css
[Party]
Leader: {leader}
Name: {name}
Date: {date}
Time: {time} server time - gear up 15 minutes earlier!

[Team] \n'''
        if roleList.count() == 0:
            string = string + "No roles specified"
        else:
            for role in roleList:
                charName = ''
                if role['roleUsername'] == '' or role['roleUsername'] is None:
                    charName = ''
                else:
                    charName = f">> {role['roleUsername']}"
                string = string + f"{role['roleName']}: {charName}\n"
        string = string + f'''```'''
        return string

    def getNoTemplate(self):
        string = f'''```css
Party has not been scheduled yet.

Hint: use $setDate and $setTime in order to proceed.```'''
        return string