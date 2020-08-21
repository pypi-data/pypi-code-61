class Sender:
    """
    :param bot: Bot Main
    :param id: int
    """
    id = None
    bot = None
    
    def __init__(self, bot, id):
        self.bot = bot
        self.id = id
      
    def isAdmin(self):
        return str(self.id) in self.bot.admins
        
    def getId(self):
        """ Возвращает айди
        
        :returns: int
        """
        return self.id
        
    def send(self, **kwargs):
        return self.bot.method("messages.send", **kwargs)
        
    def sendMessage(self, message, mentions=True):
        mentions = 0 if mentions else 1
        self.send(
            random_id=0,
            message=message,
            peer_id=self.id,
            disable_mentions=mentions
            )
    
    def sendAttachment(self, attachment):
        self.send(
            random_id=0,
            peer_id=self.id,
            attachment=attachment
            )
            
    def sendKeyboard(self, message, keyboard, mentions=False):
        mentions = 0 if mentions else 1
        self.send(
            random_id=0,
            peer_id=self.id,
            message=message,
            keyboard=keyboard,
            disable_mentions=mentions
            )
    
    def sendSticker(self, id):
        self.send(
            random_id=0,
            sticker_id=id,
            peer_id=self.id
            )
    
class User(Sender):
    
    info = {}
    def __init__(self, bot, id):
        super().__init__(bot, id)
        self.setInfo(["domain", "sex", "status"])
        
    def __getitem__(self, key):
        return self.info.get(key)
        
    def setInfo(self, fields=[]):
        self.info = self.bot.method("users.get", user_ids=self.id, fields=",".join(fields))[0]
     
    def getDomain(self):
        return self.info.get("domain")
     
    def getStatus(self):
        return self.info.get("status")
        
    def getSex(self):
        return self.info.get("sex")
        
    def isBoy(self):
        return self.getSex() == 2
        
    def isGirl(self):
        return self.getSex() == 1
        
    def getName(self, link=False):
        name = self.info.get("first_name")
        if link:
            return "[id{}|{}]".format(self.id, name)
        return name
        
    def getLast(self, link=False):
        last = self.info.get("last_name")
        if link:
            return "[id{}|{}]".format(self.id, last)
        return last   
        
    def getFullName(self, link=False):
        return "{} {}".format(self.getName(link), self.getLast(link))

class Group(Sender):
    
    info = {}
    def __init__(self, bot, id):
        super().__init__(bot, id)
        self.setInfo(["description", "members_count", "status"])
        
    def setInfo(self, fields=[]):
        self.info = self.bot.method("messages.getConversationsById", peer_ids=self.id, extended=1,
                                    fields=",".join(fields))
     
    def getDomain(self):
        return self.info["groups"][0]["screen_name"]
    
    def getDescription(self):
        return self.info["groups"][0]["description"]
        
    def getStatus(self):
        return self.info["groups"][0]["status"]
        
    def getMembers(self):
        return self.info["groups"][0]["members_count"]
        
    def getName(self, link=False):
        name = self.info["groups"][0]["name"]
        if link:
            return "[{}|{}]".format(self.getDomain(), name)
        return name

class Chat(Sender):
    
    info = {}
    def __init__(self, bot, id):
        super().__init__(bot, id)
        self.info = bot.method("messages.getConversationsById", peer_ids=id, 
                               extended=1)["items"][0]
       
    def get(self, key):
        if "chat_settings" in self.info:
            return self.info["chat_settings"].get(key)
        else:
            return
        
    def getOwner(self):
        id = self.get("owner_id")
        if id:
            return self.bot.get_object(id)
        return id
        
    def getTitle(self):
        return self.get("title")
        
    def getMembersCount(self):
        return self.get("members_count")
        
    def getAdmins(self):
        return self.get("admin_ids")
        
    def getActives(self):
        return self.get("active_ids")
        
    def getMembers(self, items=False):
        if not self.getTitle():
            return []
            
        resp = self.bot.method("messages.getConversationMembers", peer_id=self.id)
        if items:
            return resp["items"]
            
        members = []
        
        for member in resp["profiles"]:
            user = User(self.bot, member["id"])
            members.append(user)
        for group in resp["groups"]:
            members.append(Group(self.bot, group["id"]))
            
        return members