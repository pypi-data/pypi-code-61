from .objects import Group
from traceback import format_exc

class Command:
    """
    :param name: str
    :param description: str
    :param usage: str
    :param aliases: list
    :param permission: bool
    """
    description = None
    permission = False
    groupuse = True
    aliases = []
    target = None
    usage = None
    name = ""
    
    def __init__(self, name=None, description=None, usage=None, aliases=[], permission=False, groupuse=True):
        self.name = name
        self.description = description
        self.aliases = aliases
        self.permission = permission
        self.groupuse = groupuse
        self.usage = usage
        
    def exec(self, user, chat, args, obj):
        """
        :param user: Sender class
        :param chat: Chat class
        :param args: command arguments
        :param obj: lp event object
        
        :type args: list
        :type obj: dict
        """
        if callable(self.target):
            self.target(user, chat, args, obj)
            
class CommandManager:
    commands = {}
    
    def __init__(self, bot):
        self.bot = bot
     
    def exec(self, user, chat, obj, text):  
        args = text.lstrip().split( )
        try:
            cmd = args.pop(0)
        except:
            cmd = text.strip()
    
        if cmd not in self.commands:
            if bool(self.bot.get_settings("command_not_found", True)):
                chat.sendMessage(self.bot.get_messages("command_not_found", cmd=cmd))
            return
            
        cmd = self.commands[cmd]
        
        if isinstance(user, Group) and not cmd.groupuse: 
            if bool(self.bot.get_settings("group_not_use", True)):
                chat.sendMessage(self.bot.get_messages("group_not_use"))
            return
        
        if not user.isAdmin() and cmd.permission:
            if bool(self.bot.get_settings("no_permission", True)):
                chat.sendMessage(self.bot.get_messages("no_permission"))
            return
        
        try:
            cmd.exec(user, chat, args, obj)
        except:
            if cmd.usage and "IndexError" in format_exc() and "args[" in format_exc():
                chat.sendMessage(cmd.usage)
                return
            if bool(self.bot.get_settings("command_error", True)):
                chat.sendMessage(self.bot.get_messages("command_error", cmd=cmd.name))
            self.bot.logger.error(self.bot.get_messages("command_error", cmd=cmd.name))
            self.bot.log_exception()
            
    def get_commands(self):
        """ returns a list of commands without aliases
        
        :returns: dict
        """
        cmds = {}
        for k, cmd in self.commands.items():
            if cmd.name in cmds:
                continue
            cmds[cmd.name] = cmd
        return cmds
        
    def unregister(self, command):
        """
        :param command: Command class
        """
        if not isinstance(command, Command):
            if command in self.commands:
                command = self.commands[command]
            else:
                return
        self.commands.pop(command.name, None)
        for alias in command.aliases:
            if alias in self.commands and alias != self.commands.get(alias).name:
                self.commands.pop(alias)
        
    def register(self, command):
        """
        :param command: Command class
        """
        if not isinstance(command, Command):
            return
        self.commands[command.name] = command
        for alias in command.aliases:
            if alias not in self.commands:
                self.commands[alias] = command