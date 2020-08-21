from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotEvent
from .objects import User, Chat, Group, Sender
from configparser import ConfigParser
from traceback import format_exc
from .task import Task, TaskManager
from .command import CommandManager, Command
from vk_api import ApiError
from vk_api import VkApi
from time import time as utime
#####################
import logging.config
import threading
import logging
import sys
import os

class VkBot:
    """ Main class
    :param config: Configuration file path
    :type config: str
    
    :param logger: Logging config file path
    :type logger: str
    """
    MESSAGES = {}
    RUNNING = True
    admins = []
    prefix = None
    events = {}
    config = None
    logger = None
    lang = "rus"
    time = 0
    vk = None
    lp = None
    
    def __init__(self, config, logger):
        self.__load_configs(config, logger)
        self.logger = logging.getLogger(self.get_settings("logger", "vkbot"))
        self.vk = VkApi(token=self.get_settings("access_token"), api_version=self.get_settings("version", 5.120))
        self.admins = self.get_settings("admins", "").split(",")
        self.prefix = self.get_settings("prefix", None)
        self.lp = VkBotLongPoll(self.vk, self.get_settings("group_id"), int(self.get_settings("lp_wait", 5)))
        self.register(VkBotEventType.MESSAGE_NEW, self.cmd_event)
        self.cmd = CommandManager(self)
        self.tasks = TaskManager(self)
        th = threading.Thread(target=self.__exit)
        th.daemon = True
        th.start()
        
        self.logger.info(self.get_messages("start", id=self.get_settings("group_id")))
        self.time = utime()
        
    def task(self, time, repeating=0):
        """ Add task with decorator
        
        :param time: complete time
        :param repeating: repeating count
        """
        def tsk(func):
            tsk = Task(time, repeating)
            tsk.target = func
            tsk.name = func.__name__
            self.tasks.add_task(tsk)
            return func
        return tsk
        
    def command(self, name, **kwargs):
        """ Register command with decorator
        
        :param kwargs: Command constructor args
        """
        def cmd(func):
            cmd = Command(name=name, **kwargs)
            cmd.target = func
            self.cmd.register(cmd)
            return func
        return cmd
        
    def event(self, event):
        """ Register event with decorator
        
        :param event: Event type
        :type event: str
        """
        def register(func):
            self.register(event, func)
            return func
        return register
        
    def cmd_event(self, obj):
        user = self.get_object(obj.from_id)
        chat = self.get_chat(obj.peer_id)
        if self.prefix:
            if obj.text[:1] == self.prefix[:1]:
                self.cmd.exec(user, chat, obj, obj.text[1:])
        else:
            self.cmd.exec(user, chat, obj, obj.text)
    
    def get_id(self, id):
        """
        :param id: Id|domain|link
        :returns: available id
        """
        if not isinstance(id, str):
            return id
        
        try:    
            for r in ("@", "*", "[", "]", "id", "club", "https://vk.com/"):
                id = id.replace(r, "")
            id = id.split("|")
            id = id[0]
            if not id.isnumeric():
                type = self.method("messages.getConversationsById", peer_ids=id)["items"][0]["peer"]["type"]
                if type == "group":
                    id = -self.method("groups.getById", group_ids=id)[0]["id"]
                elif type == "user":
                    id = self.method("users.get", user_ids=id)[0]["id"]
        except:
            pass
        return id
    
    def get_object(self, id):
        """
        :param id: id|domain|link
        :returns: User|Sender|Chat|Group
        """
        id = self.get_id(id)
        type = self.method("messages.getConversationsById", peer_ids=id)
        type = type["items"][0]["peer"]["type"]
        if type == "chat":
            return self.get_chat(id)
        elif type == "user":
            return self.get_user(id)
        elif type == "group":
            return self.get_group(id)
        return Sender(self, id)
    
    def get_group(self, id):
        return Group(self, self.get_id(id))
        
    def get_chat(self, id):
        return Chat(self, id)
        
    def get_user(self, id):
        return User(self, self.get_id(id))
        
    def method(self, method, **kwargs):
        """ Call the api method
        
        :param method: str
        :param kwargs: method params
        """
        try:
            response = self.vk.method(method, kwargs)
        except ApiError as e:
            self.logger.error(self.get_messages("method_error", method=method, message=e))
            seld.log_exception()
            response = []
        return response
            
    def register(self, event, consumer):
        """ Register event
        
        :param event: str
        :param consumer: func
        """
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(consumer)
        
    def __handle(self, event, obj):
        if event not in self.events:
            return
        
        for e in self.events[event]:
            if callable(e):
                try:
                    e(obj)
                except:
                    self.logger.error(self.get_messages("event_error", event=event))
                    self.log_exception()
        
    def start(self):
        while self.RUNNING:
            try:
                for event in self.lp.check():
                    thread = threading.Thread(target=self.__handle, args=(event.type, event.obj))
                    thread.daemon = True
                    thread.start()
            except:
                self.log_exception()
        else:
            self.logger.info(self.get_messages("stop_listen"))
            self.logger.info(self.get_messages("stop", ut=self.uptime()))
        
    def log_exception(self):
        self.logger.debug(format_exc())
        
    def get_messages(self, key, **args):
        """
        :param key: Messages key
        :type key: str
        
        :param args: kwargs
        :returns: str
        """
        if not self.config:
            return key
        else: 
            try:
                msg = self.config.get("messages", key)
            except:
                msg = self.MESSAGES[self.lang].get(key)
            if msg:
                return msg.format(**args)
            else:
                return key
            
    def get_settings(self, key, default=None):
        """
        :param key: Settings key
        :type key: str
        
        :param default: if the key is not found in the config, it will return the default value
        :type default: mixed
        
        :returns: mixed
        """
        if not self.config:
            return default
        else:
            try:
                res = self.config.get("settings", key)
                return res
            except:
                return default
    
    def uptime(self):
        time = utime() - self.time
        fmt = self.get_messages("time_format").split(",")
        
        months = round(time / 2592000 % 999)
        weeks = round(time / 604800 % 4)
        days = round(time / 86400 % 7)
        hours = round(time / 3600 % 24)
        minutes = round(round(time / 60) % 60)
        
        if months > 0:
            return "{}{} {}{}".format(months, fmt[0], weeks, fmt[1])
            
        format = ""
        
        if days > 0:
            format += "{}{} ".format(days, fmt[2])
        if hours > 0:
            format += "{}{} ".format(hours, fmt[3])
        if minutes > 0:
            format += "{}{} ".format(minutes, fmt[4])
        format += "{}{}".format(round(time % 60), fmt[5])
        return format
     
    def __exit(self):
        input()
        self.stop() 
        
    def stop(self):
        self.RUNNING = False
        
    def __load_configs(self, config, logger):
        logging.config.fileConfig(logger)
        self.config = ConfigParser()
        self.config.sections()
        self.config.read(config)
        
        self.MESSAGES["rus"] = {
            "start": "Бот запущен. ID:{id}",
            "stop": "Бот остановлен. Время работы: {ut}",
            "time_format": "мес.,нед.,дн.,чс.,мн.,сек.",
            "stop_listen": "Остановка прослушивания..",
            "event_error": "Не удалось обработать событие '{event}'",
            "method_error": "ApiError: не удалось вызвать метод '{method}' - {message}",
            "task_error": "Не удалось выполнить задачу '{task}'",
            "no_permission": "У вас недостаточно прав!",
            "command_not_found": "Комада {cmd} не найдена",
            "command_error": "При выполнении команды {cmd} произошла ошибка.",
            "group_not_use": "Эту команду могут использовать только пользователи!"
        }
        self.MESSAGES["eng"] = {
            "start": "Bot started. ID:{id}",
            "stop": "Bot stopped. Uptime: {ut}",
            "time_format": "mh.,w.,d.,h.,m.,s.",
            "stop_listen": "Stop listening..",
            "event_error": "Failed to execute method '{event}'",
            "method_error": "ApiError: Failed to call method '{method}' - {message}",
            "task_error": "failed to complete the task '{task}'",
            "no_permission": "You do not have sufficient permissions!",
            "command_not_found": "Command {cmd} not found",
            "command_error": "An error occurred while executing the {cmd} command.",
            "group_not_use": "This command can only be used by users!"
        }
        
        if not self.get_settings("access_token"):
            raise Exception("specify the access token in the config file!")
        if not self.get_settings("group_id"):
            raise Exception("specify the group id in the config file!")