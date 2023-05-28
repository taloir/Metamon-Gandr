#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
from discord.ext.commands import Bot
import pickle
import time
import random

secretcode = 'MTAxNjg1OTI4NDM0NjI1MzMyMg.GWfP-8.j0STeR_KfY7ihlk7QDkdm20btOHobs62zLeyA8' #Enter your secret code

async def declare_results(odds, message):
    # rolling XL odds
        if odds.upper() == "XL":
            number = random.randrange(1,11)
            if number > 1:
                if number > 2:
                    if number > 6:
                        await message.channel.send(odds + " odds- " + str(number) + ": **Yes, and**")
                    else:
                        await message.channel.send(odds + " odds- " + str(number) + ": **Yes**")
                else:
                    await message.channel.send(odds + " odds- " + str(number) + ": **Yes, but**")
            else:
                await message.channel.send(odds + " odds- " + str(number) + ": **No, but**")

    #rolling VL odss
        elif odds.upper() == "VL":
        #finding the highest of 3d10
            number_1 = random.randrange(1,11)
            number_2 = random.randrange(1,11)
            number_3 = random.randrange(1,11)
            if number_1 >= number_2:
                if number_1 >= number_3:
                    number = number_1
                else:
                    number = number_3
            else:
                if number_2 >= number_3:
                    number = number_2
                else:
                    number = number_3
        #declaring the result
            if number > 1:
                if number > 4:
                    if number > 5:
                        if number > 6:
                            if number > 9:
                                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **Yes, and**")
                            else:
                                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **Yes**")
                        else:
                            await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **Yes, but**")
                    else:
                        await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **No, but**")
                else:
                    await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **No**")
            else:
                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **No, and**")

    #rolling L odds
        elif odds.upper() == "L":
        #finding the highest of 2d10
            number_1 = random.randrange(1,11)
            number_2 = random.randrange(1,11)
            if number_1 >= number_2:
                number = number_1
            else:
                number = number_2
        #declaring the result
            if number > 1:
                if number > 4:
                    if number > 5:
                        if number > 6:
                            if number > 9:
                                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **Yes, and**")
                            else:
                                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **Yes**")
                        else:
                            await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **Yes, but**")
                    else:
                        await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **No, but**")
                else:
                    await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **No**")
            else:
                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **No, and**")

    #rolling SL odds
        elif odds.upper() == "SL":
            number = random.randrange(1,11)
            if number > 1:
                if number > 3:
                    if number > 4:
                        if number > 5:
                            if number > 9:
                                await message.channel.send(odds + " odds- " + str(number) + ": **yes, and**")
                            else:
                                await message.channel.send(odds + " odds- " + str(number) + ": **Yes**")
                        else:
                            await message.channel.send(odds + " odds- " + str(number) + ": **Yes, but**")
                    else:
                        await message.channel.send(odds + " odds- " + str(number) + ": **No, but**")
                else:
                    await message.channel.send(odds + " odds- " + str(number) + ": **No**")
            else:
                await message.channel.send(odds + " odds- " + str(number) + ": **No, and**")

    #rolling EW odds
        elif odds.upper() == "EW":
            number = random.randrange(1,11)
            if number > 1:
                if number > 4:
                    if number > 5:
                        if number > 6:
                            if number > 9:
                                await message.channel.send(odds + " odds- " + str(number) + ": **Yes, and**")
                            else: 
                                await message.channel.send(odds + " odds- " + str(number) + ": **Yes**")
                        else:
                            await message.channel.send(odds + " odds- " + str(number) + ": **Yes, but**")
                    else:
                        await message.channel.send(odds + " odds- " + str(number) + ": **No, but**")
                else:
                    await message.channel.send(odds + " odds- " + str(number) + ": **No**")
            else:
                await message.channel.send(odds + " odds- " + str(number) + ": **No, and**")

    #rolling SU odds
        elif odds.upper() == "SU":
            number = random.randrange(1,11)
            if number > 1:
                if number > 5:
                    if number > 6:
                        if number > 7:
                            if number > 9:
                                await message.channel.send(odds + " odds- " + str(number) + ": **Yes, and**")
                            else: 
                                await message.channel.send(odds + " odds- " + str(number) + ": **Yes**")
                        else:
                            await message.channel.send(odds + " odds- " + str(number) + ": **Yes, but**")
                    else:
                        await message.channel.send(odds + " odds- " + str(number) + ": **No, but**")
                else:
                    await message.channel.send(odds + " odds- " + str(number) + ": **No**")
            else:
                await message.channel.send(odds + " odds- " + str(number) + ": **No, and**")

    #rolling U odds
        elif odds.upper() == "U":
        #finding the lowest of 2d10
            number_1 = random.randrange(1,11)
            number_2 = random.randrange(1,11)
            if number_1 <= number_2:
                number = number_1
            else:
                number = number_2
        #declaring results
            if number > 1:
                if number > 4:
                    if number > 5:
                        if number > 6:
                            if number > 9:
                                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **Yes, and**")
                            else: 
                                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **Yes**")
                        else:
                            await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **Yes, but**")
                    else:
                        await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **No, but**")
                else:
                    await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **No**")
            else:
                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ": **No, and**")

    #rolling VU odds
        elif odds.upper() == "VU":
        #finding the lowest of 3d10
            number_1 = random.randrange(1,11)
            number_2 = random.randrange(1,11)
            number_3 = random.randrange(1,11)
            if number_1 <= number_2:
                if number_1 <= number_3:
                    number = number_1
                else:
                    number = number_3
            else:
                if number_2 <= number_3:
                    number = number_2
                else:
                    number = number_3
        #declaring results
            if number > 1:
                if number > 4:
                    if number > 5:
                        if number > 6:
                            if number > 9:
                                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **Yes, and**")
                            else: 
                                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **Yes**")
                        else:
                            await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **Yes, but**")
                    else:
                        await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **No, but**")
                else:
                    await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **No**")
            else:
                await message.channel.send(odds + " odds- " + str(number_1) + ", " + str(number_2) + ", " + str(number_3) + ": **No, and**")

    #rolling XU odds
        elif odds.upper() == "XU":
            number = random.randrange(1,11)
            if number > 4:
                if number > 8:
                    if number > 9:
                        await message.channel.send(odds + " odds- " + str(number) + ": **Yes, but**")
                    else:
                        await message.channel.send(odds + " odds- " + str(number) + ": **No, but**")
                else:
                    await message.channel.send(odds + " odds- " + str(number) + ": **No**")
            else:
                await message.channel.send(odds + " odds- " + str(number) + ": **No, and**")


class BeastBot:
    def __init__(self, cS, intents):
        self.client = Bot(command_prefix="!", intents=discord.Intents.all())
        self.clientSecret = cS
        self.metaDataFilePath = r"C:\\Users\\Landon\\Desktop\\BetaBeasts database\\Memory.pickle" #Replace with your own location for the file with allbeast data
        self.defaultMetaData = {'Beasts': {}}
        self.metaData = self.loadMetaDataFile()
        self.memoryMetadata = {
            'Roles': {}
        }
        print(self.metaData)
        self.update = False
        self.EmptyBeastDictionary = {
                    'Beast Name': '',
                    'Creator': '',
                    'Owner': '',
                    'ATK': '',
                    'DEF': '',
                    'Rarity': '',
                    'Type': '',
                    'Size': '',
                    'Personality': '',
                    'Beast Description': '',
                    'Basic Attack Name': '',
                    'Passive Skill': '',
                    'Wound': 0,
                    'XP': 0,
                    'Location': '',
                    'Abilities': {}
                    }
        self.OddsDictionary = {
            'XL': 9,
            'VL': 8,
            'L': 7,
            'SL': 6,
            'EW': 5,
            'SU': 4,
            'U': 3,
            'VU': 2,
            'XU': 1
        }
        self.CreatorIDRole = (616677867471896621) #need to be changed to beast server creator role
        self.EmptyAbilityDictionary = {
            'Ability Name': '',
            'Ability Description': ''
        }


    # Start Discord Bot
    def run(self):
        self.client.run(self.clientSecret)

    def saveMetaDataFile(self):
        with open(self.metaDataFilePath,'wb') as outfile:
            pickle.dump(self.metaData,outfile)

    def loadMetaDataFile(self):
        try:
            with open(self.metaDataFilePath,"rb") as pickle_in:
                metaData = pickle.load(pickle_in)
        except:
            metaData = self.defaultMetaData
        for dataName,data in self.defaultMetaData.items():
            if dataName not in metaData:
                metaData[dataName] = data
        return metaData

#By Default marking everyone as unauthorized, returning authorized when the UserID is a creator role ID
    def isCreator(self, UserID):
        authorized = False
        for creatorMember in self.memoryMetadata['Roles']['Creator'].members:
            if UserID == creatorMember.id:
                authorized = True
        return authorized

    async def shutdown(self):
        self.saveMetaDataFile()
        time.sleep(1)
        print("BeastBot shutting down.")
        await self.client.close()

    async def ShowStats(self,BeastData):

        OwnerUser = await self.beastServer.fetch_member(BeastData['Owner'])
        CreatorUser = await self.beastServer.fetch_member(BeastData['Creator'])
        OwnerName = OwnerUser.display_name
        CreatorName = CreatorUser.display_name
        StatBlockList = []

        StatBlockText = '**Beast Name:** '+BeastData['Beast Name']+'\n'+\
        '**Owner:** '+OwnerName+'\n'+\
        '**Creator:** ' + CreatorName + '\n' +'\n'+\
        '**ATK:** '+BeastData['ATK']+'\n'+\
        '**DEF:** '+BeastData['DEF']+'\n'+'\n'+\
        '**Rarity:** '+BeastData['Rarity']+'\n'+\
        '**Type:** '+BeastData['Type'] + '\n' +\
        '**Size:** '+BeastData['Size']+'\n'+\
        '**Personality:** '+BeastData['Personality']+'\n'+\
        '**Beast Description:** '+BeastData['Beast Description']+'\n'+'\n'+\
        '**Basic Attack Name:** '+BeastData['Basic Attack Name']+'\n'+\
        '**Passive Skill:** '+BeastData['Passive Skill'] + '\n' +'\n'+\
        '**Current Wounds:** '+str(BeastData['Wound'])+'\n'+\
        '**Current XP:** '+str(BeastData['XP'])+'\n'+\
        '**Location:** ' + str(BeastData['Location']) + '\n'+'\n'

        for AbilityName, AbilityDictionary in BeastData['Abilities'].items():
            newline = '**Ability Name:** '+AbilityName+'\n'+\
                            '**Ability Description:** '+AbilityDictionary['Ability Description']+'\n'
            if len(StatBlockText)+len(newline) > 1800:
                StatBlockList.append(StatBlockText)
                StatBlockText = newline
            StatBlockText += '**Ability Name:** '+AbilityName+'\n'+\
                            '**Ability Description:** '+AbilityDictionary['Ability Description']+'\n'
        StatBlockList.append(StatBlockText)
        return StatBlockList

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    intents = discord.Intents.default()
    intents.message_content = True


    SuperClient = BeastBot(secretcode,intents)


    @SuperClient.client.event
    async def on_ready():
        SuperClient.beastServer = SuperClient.client.get_guild(614210470571933748) #need to replace with beast server ID
        print(f'We have logged in as {SuperClient.client.user}')
        SuperClient.memoryMetadata["Roles"]["Creator"] = SuperClient.beastServer.get_role(SuperClient.CreatorIDRole)

    @SuperClient.client.event
    async def on_message(message):
        if SuperClient.update == True:  # Keep after every other function
            SuperClient.saveMetaDataFile()
            SuperClient.update = False
        if message.author == SuperClient.client.user:
            return

        if message.author.id == "Taloir#3941":
            if message.content.lower() == 'shut off':
                print(SuperClient.metaData)
                await SuperClient.shutdown()

        #Put all the commands in here
        if message.content.startswith('!'):
            commandWord = message.content.split()[0].lower()

            #All of the dice commands
            if commandWord == "!xl":
                await declare_results("XL",message)
            
            if commandWord =="!vl":
                await declare_results("VL",message)
            
            if commandWord =="!l":
                await declare_results("L",message)
            
            if commandWord =="!sl":
                await declare_results("SL",message)
            
            if commandWord =="!ew":
                await declare_results("EW",message)
            
            if commandWord =="!su":
                await declare_results("SU",message)
            
            if commandWord =="!u":
                await declare_results("U",message)

            if commandWord =="!vu":
                await declare_results("VU",message)

            if commandWord =="!xu":
                await declare_results("XU",message)
                #end dice commands


            if commandWord == '!check':
                SuperClient.update = True
                CheckData = message.content[7:].split('\n')
                BeastName = CheckData[0]

                #checking a users owned beasts
#                if BeastName.mentions != []:
#                    UserID = BeastName.mentions[0].id
#                    if UserID in SuperClient.metaData['Beasts'][SuperClient.client.user.id]:  
#                        StatBlockList = await SuperClient.ShowStats(SuperClient.metaData['Beasts'][SuperClient.client.user.id][BeastName])
#                        for StatBlock in StatBlockList:
#                            await message.channel.send(StatBlock['Description'])
#                        return                 

                #checking a specific beast
                if message.mentions != []:
                    UserID = message.mentions[0].id
                    if UserID == SuperClient.client.user.id: #If the Person is mentioning a person
                        if BeastName in SuperClient.metaData['Beasts'][SuperClient.client.user.id]:
                            if SuperClient.metaData['Beasts'][SuperClient.client.user.id][BeastName]['Location'] == 'Wilds' and SuperClient.isCreator(message.author.id) == True:
                                StatBlockList = await SuperClient.ShowStats(SuperClient.metaData['Beasts'][SuperClient.client.user.id][BeastName])
                                for StatBlock in StatBlockList:
                                    await message.channel.send(StatBlock)
                                return
                            else:
                                await message.channel.send('The Beast does not exist')
                                return
                        else:
                            await message.channel.send('The Beast does not exist')
                            return
                else:
                    UserID = message.author.id #If the person doesn't mention a person
                if UserID in SuperClient.metaData['Beasts'].keys() and BeastName in SuperClient.metaData['Beasts'][UserID].keys():
                    StatBlockList = await SuperClient.ShowStats(SuperClient.metaData['Beasts'][UserID][BeastName])
                    for StatBlock in StatBlockList:
                        await message.channel.send(StatBlock)
                    return
                else:
                    OwnerList = []
                    for Owner, Beasts in SuperClient.metaData['Beasts'].items():
                        for OwnedBeast in Beasts.keys():
                            if OwnedBeast == BeastName:
                                OwnerList.append(Owner)
                    if len(OwnerList) > 1:
                        await message.channel.send('Multiple Beasts with that name exist. Please @Mention owner')
                        return
                    elif OwnerList == []:
                        await message.channel.send('Beast '+BeastName+' does not exist')
                        return
                    else:
                        OwnerID = OwnerList[0]
                        if SuperClient.metaData['Beasts'][OwnerID][BeastName]['Location'] == 'Wilds' and SuperClient.isCreator(message.author.id) == True:
                            StatBlockList = await SuperClient.ShowStats(SuperClient.metaData['Beasts'][OwnerID][BeastName])
                            for StatBlock in StatBlockList:
                                await message.channel.send(StatBlock)
                            return
                        elif SuperClient.metaData['Beasts'][OwnerID][BeastName]['Location'] != 'Wilds':
                            StatBlockList = await SuperClient.ShowStats(SuperClient.metaData['Beasts'][OwnerID][BeastName])
                            for StatBlock in StatBlockList:
                                await message.channel.send(StatBlock)
                            return
                        else:
                            await message.channel.send('Beast ' + BeastName + ' does not exist')
                            return



            if commandWord == '!setup':
                SuperClient.update = True
                BeastData = message.content[7:].split('\n')
                if SuperClient.isCreator(message.author.id) == False:
                    await message.channel.send('You do not have permissions to Create Beasts. Only @Creator Role can use this function')
                    return
                if len(BeastData) != 11:
                    await message.channel.send('You have not specified Enough Parameters for the Beast')
                    return
                BeastName = BeastData[0]
                CreatorID = message.author.id
                OwnerID = SuperClient.client.user.id #gives the BotID
                if OwnerID in SuperClient.metaData['Beasts'].keys():
                    if BeastName in SuperClient.metaData['Beasts'][OwnerID].keys():
                        await message.channel.send('Owner cannot have Duplicate Beast Names. Rename Beast.')
                        return
                ATK = BeastData[1].split(":", 1)
                ATK = ATK[1].upper().strip()
                if ATK not in SuperClient.OddsDictionary.keys():
                    await message.channel.send('ATK Odds are invalid')
                    return
                DEF = BeastData[2].split(":", 1)
                DEF = DEF[1].upper().strip()
                if DEF not in SuperClient.OddsDictionary.keys():
                    await message.channel.send('DEF Odds are invalid')
                    return
                Rarity = BeastData[3].split(":", 1)
                Rarity = Rarity[1]
                BeastType = BeastData[4].split(":", 1)
                BeastType = BeastType[1]
                Size = BeastData[5].split(":", 1)
                Size = Size[1]
                Personality = BeastData[6].split(":", 1)
                Personality = Personality[1]
                BeastDescription = BeastData[7].split(":", 1)
                BeastDescription = BeastDescription[1]
                BasicAttackName = BeastData[8].split(":", 1)
                BasicAttackName = BasicAttackName[1]
                PassiveSkill = BeastData[9].split(":", 1)
                PassiveSkill = PassiveSkill[1]
                Location = BeastData[10].split(":", 1)
                Location = Location[1].strip().lower()
                if Location not in ('event', 'wilds','owned'):
                    await message.channel.send('You need to Specify if the Beast is Event or Wilds')
                    return


                BeastDictionary = {
                    'Beast Name': BeastName,
                    'Creator': CreatorID,
                    'Owner': OwnerID,
                    'ATK': ATK,
                    'DEF': DEF,
                    'Rarity': Rarity,
                    'Type': BeastType,
                    'Size': Size,
                    'Personality': Personality,
                    'Beast Description': BeastDescription,
                    'Basic Attack Name': BasicAttackName,
                    'Passive Skill': PassiveSkill,
                    'Wound': 0,
                    'XP': 0,
                    'Location': Location,
                    'Abilities': {}
                    }
                SuperClient.metaData['Beasts'].setdefault(OwnerID, {})
                SuperClient.metaData['Beasts'][OwnerID][BeastName] = BeastDictionary
                await message.channel.send('The Beast '+BeastName+' was Successfully Created! :D')
                StatBlockList = await SuperClient.ShowStats(BeastDictionary)
                for StatBlock in StatBlockList:
                    await message.channel.send(StatBlock)
                return


            if commandWord == '!update':
                SuperClient.update = True
                if SuperClient.isCreator(message.author.id) == False:
                    await message.channel.send(
                        'You do not have permissions to Update Beasts. Only @Creator Role can use this function')
                    return
                BeastOwners = []
                UpdateData = message.content[8:].split('\n')
                BeastName = UpdateData[0]
                StatName = UpdateData[1]
                NewValue = UpdateData[2]

                #Checking for errors
                if StatName in ('Owner', 'Creator'):
                    await message.channel.send('Use the !Transfer function to move beasts to new Owners or Creators')
                    return
                elif StatName not in SuperClient.EmptyBeastDictionary.keys():
                    await message.channel.send('Stat does not exist')
                    return
                elif StatName in ('Wound','XP'):
                    if set(NewValue).issubset(set('1234567890')):
                        NewValue = int(NewValue)
                    else:
                        await message.channel.send('Wound and XP can only be changed to a number')
                        return
                elif StatName in ('ATK','DEF') and NewValue not in SuperClient.OddsDictionary.keys():
                    await message.channel.send('ATK or DEF not given valid odds')
                    return
                #Checks for Beast Owner
                if message.mentions != []:
                    MentionID = message.mentions[0].id

                else:
                    MentionID = message.author.id
                if MentionID in SuperClient.metaData['Beasts'].keys() and BeastName in SuperClient.metaData['Beasts'][MentionID]:
                    NewBeastDictionary = SuperClient.metaData['Beasts'][MentionID][BeastName]
                    NewBeastDictionary[StatName] = NewValue
                    if StatName == 'Beast Name':
                        if NewValue in SuperClient.metaData['Beasts'][MentionID].keys():
                            await message.channel.send('You already have a beast named '+NewValue)
                            return
                        else:
                            del SuperClient.metaData['Beasts'][MentionID][BeastName]
                            SuperClient.metaData['Beasts'][MentionID][NewValue] = NewBeastDictionary
                    else:
                        SuperClient.metaData['Beasts'][MentionID][BeastName] = NewBeastDictionary
                        await message.channel.send(StatName+' was successfully updated to '+NewValue)
                        return
                else:
                    for OwnerID,Beasts in SuperClient.metaData['Beasts'].items():
                        for OwnedBeastName in Beasts.keys():
                            if BeastName == OwnedBeastName:
                                BeastOwners.append(OwnerID)
                    if len(BeastOwners) > 1:
                        await message.channel.send('There are multiple Beasts with this name. Please @Mention Owner when updating')
                        return
                    elif len(BeastOwners) == 1:
                        NewBeastDictionary = SuperClient.metaData['Beasts'][BeastOwners[0]][BeastName]
                        NewBeastDictionary[StatName] = NewValue
                        if StatName == 'Beast Name':
                            if NewValue in SuperClient.metaData['Beasts'][BeastOwners[0]].keys():
                                await message.channel.send('You already have a beast named ' + NewValue)
                                return
                            else:
                                del SuperClient.metaData['Beasts'][BeastOwners[0]][BeastName]
                                SuperClient.metaData['Beasts'][BeastOwners[0]][NewValue] = NewBeastDictionary
                        else:
                            SuperClient.metaData['Beasts'][BeastOwners[0]][BeastName] = NewBeastDictionary
                            await message.channel.send(StatName + ' was successfully updated to ' + NewValue)
                            return
                    else:
                        await message.channel.send('Unable to find beast')
                        return

            if commandWord == '!delete':
                SuperClient.update = True
                if SuperClient.isCreator(message.author.id) == False:
                    await message.channel.send('You do not have permissions to Update Beasts. Only @Creator Role can use this function')
                    return
                else:
                    UpdateData = message.content[8:].split('\n')
                    BeastName = UpdateData[0]
                    if message.mentions != []:
                        MentionID = message.mentions[0].id
                    else:
                        await message.channel.send(
                            'You need to mention a user to Delete a Monster')
                        return

                    if MentionID not in SuperClient.metaData['Beasts'].keys():
                        await message.channel.send('Mentioned User does not have a beast')
                        return
                    elif BeastName not in SuperClient.metaData['Beasts'][MentionID].keys():
                        await message.channel.send('Mentioned User does not have a beast named '+BeastName)
                        return
                    else:
                        del SuperClient.metaData['Beasts'][MentionID][BeastName]
                        await message.channel.send(BeastName+' has been deleted from user')
                        return

            if commandWord == '!ability':
                SuperClient.update = True
                if SuperClient.isCreator(message.author.id) == False:
                    await message.channel.send('You do not have permissions to Update Beasts. Only @Creator Role can use this function')
                    return
                else:
                    UpdateData = message.content[9:].split('\n')
                    BeastName = UpdateData[0]
                    UpdateType = UpdateData[1].lower()
                    AbilityName = UpdateData[2]
                    AbilityDescription = UpdateData[3]
                    if message.mentions != []:
                        MentionID = message.mentions[0].id
                    else:
                        await message.channel.send('Mention ID of beast must be added to arguments')
                        return
                    if MentionID not in SuperClient.metaData['Beasts'].keys() or BeastName not in SuperClient.metaData['Beasts'][MentionID].keys():
                        await message.channel.send('Unable to find Beast')
                        return
                    if UpdateType not in ('add','update','delete'):
                        await message.channel.send('No argument given for if the ability is being added, updated, or deleted')
                        return
                    else:
                        if UpdateType in ('add','update'):
                            AbilityDictionary = {
                                'Ability Description': AbilityDescription
                            }
                            SuperClient.metaData['Beasts'][MentionID][BeastName]['Abilities'][AbilityName] = AbilityDictionary
                            await message.channel.send('The Beast ' + BeastName + ' now has the '+AbilityName+' ability! :D')
                            return

                        elif UpdateType == 'delete':
                            if AbilityName not in SuperClient.metaData['Beasts'][MentionID][BeastName]['Abilities'].keys():
                                await message.channel.send('The ability name does not exist')
                                return
                            else:
                                del SuperClient.metaData['Beasts'][MentionID][BeastName]['Abilities'][AbilityName]
                                await message.channel.send('The Beast ' + BeastName + ' has removed the ' + AbilityName + ' ability! :O')
                                return

            if commandWord == '!transfer':
                SuperClient.update = True
                if SuperClient.isCreator(message.author.id) == False:
                    await message.channel.send('You do not have permissions to Update Beasts. Only @Creator Role can use this function')
                    return
                else:
                    if len(message.mentions) == 2:
                        UpdateData = message.content[10:].split('\n')
                        BeastName = UpdateData[0]
                        Mention1 = message.mentions[0].id
                        Mention2 = message.mentions[1].id

                        if Mention1 != Mention2:
                            Beastgiver = None
                            Beastrec = None
                            for mentionID in [Mention1, Mention2]:
                                if mentionID in SuperClient.metaData['Beasts'].keys():
                                    if BeastName in SuperClient.metaData['Beasts'][mentionID].keys():
                                        Beastgiver = mentionID
                                    else:
                                        Beastrec = mentionID
                                else:
                                    Beastrec = mentionID

                            if Beastgiver != None and Beastrec != None:
                                SuperClient.metaData['Beasts'].setdefault(Beastrec, {})
                                BeastDictionary = SuperClient.metaData['Beasts'][Beastgiver][BeastName]
                                if BeastDictionary['Location'] == 'Wilds':
                                    BeastDictionary['Location'] = 'Owned'
                                if BeastDictionary['Location'] == 'Event':
                                    await message.channel.send('Event Beast cannot be transferred')
                                    return
                                if Beastrec == SuperClient.client.user.id:
                                    BeastDictionary['Location'] = 'Wilds'
                                BeastDictionary['Owner'] = Beastrec
                                SuperClient.metaData['Beasts'][Beastrec][BeastName] = BeastDictionary
                                del SuperClient.metaData['Beasts'][Beastgiver][BeastName]
                                await message.channel.send(BeastName+' was transferred successfully')
                                return
                            else:
                                await message.channel.send('There are errors transferring this beast. Please check both owners do not have the same beast name')
                                return
                        else:
                            await message.channel.send('Two DIFFERENT Users must be @Mentioned to use this function')
                            return
                    else:
                        await message.channel.send('Two Users must be @Mentioned to use this function')
                        return

            if commandWord == '!help':
                HelpMessage = ''
                UpdateData = message.content[6:].split('\n')
                KeyWord = UpdateData[0].lower()

                if KeyWord == 'roll':
                    HelpMessage = 'Formatting for Roll is "![odds code] flavor text". See below for the list of valid odds codes.' + '\n' + \
                    'XL, VL, L, SL, EW, SU, U, VU, XU'
                    
                
                elif KeyWord == 'setup':
                    HelpMessage = 'Formatting for Setup is Like Below, ignore []. Newlines are important to load correctly'+ '\n' + '\n'+ \
                    '!Setup [BeastName] - Beast Name must be unique per Owner.'+ '\n' + \
                    'ATK - Must be in correct Odds format'+ '\n' + \
                    'DEF - Must be in correct Odds format'+ '\n' + \
                    'Rarity'+ '\n' + \
                    'Type'+ '\n' + \
                    'Size'+ '\n' + \
                    'Personality'+ '\n' + \
                    'Beast Description'+ '\n' + \
                    'Basic Attack Name'+ '\n' + \
                    'Passive Skill'+ '\n' + \
                    'Location - Must be Wilds, Event, or Owned'+ '\n'

                elif KeyWord == 'ability':
                    HelpMessage = 'Formatting for Ability is Like Below, ignore []. Newlines are important to load correctly' + '\n' + '\n'+ \
                        '!ability [BeastName]'+ '\n' + \
                        'Type - This needs to be add/update/delete'+ '\n' + \
                        'Ability Name' + '\n' + \
                        'Ability Description'+ '\n'+ \
                        'Owner @Mention' + '\n'

                elif KeyWord == 'delete':
                    HelpMessage = 'Formatting for delete is Like Below, ignore []. Newlines are important to load correctly' + '\n' + '\n'+ \
                        '!delete [BeastName]'+ '\n' + \
                        'Owner @Mention' + '\n'

                elif KeyWord == 'update':
                    HelpMessage = 'Formatting for Update is Like Below, ignore []. Newlines are important to load correctly' + '\n' + '\n'+ \
                        '!update [BeastName]'+ '\n' + \
                        'Stat to be change - must be spelled exactly. Case sensitive. Spelling in !help setup. Wound and XP can also be adjusted'+ '\n' + \
                        'New Value of Stat' + '\n' + \
                        'Owner @Mention - optional' + '\n'

                elif KeyWord == 'transfer':
                    HelpMessage = 'Formatting for transfer is Like Below, ignore []. Newlines are important to load correctly. @ mentions can be done in any order' + '\n' + '\n'+ \
                        '!transfer [BeastName]'+ '\n' + \
                        'Current owner @Mention'+ '\n' + \
                        'New Owner @Mention' + '\n'

                elif KeyWord == 'check':
                    HelpMessage = 'Formatting for check is Like Below, ignore []. Newlines are important to load correctly. Only @Creators can see Beasts in the Wilds' + '\n' +  '\n'+\
                        '!check [BeastName]'+ '\n' + \
                        'Owner @Mention - optional' + '\n'

                else:
                    HelpMessage = 'Commands listed below. You could use !help commandname for additional information' + '\n' + '\n'+ \
                    '!EW - Usable by anyone. Rolls the dice.' + '\n' + \
                    '!Setup -Only usable by @creator. Used to Create New Beasts.'+ '\n' + \
                    '!Ability - Only usable by @creator. Used to add/update/delete beast abilities.'+ '\n' + \
                    '!Delete - Only usable by @creator. Deletes a Beast' '\n' + \
                    '!Transfer - Only usable by @creator. Moves ownership of a Beast.' + '\n' + \
                    '!Update - Only usable by @creator. Change Stat for a Beast' + '\n' + \
                    '!Check - Usable for Anyone. Check the statblock for a Beast.' + '\n'

                await message.channel.send(HelpMessage)
                return






    SuperClient.run()



