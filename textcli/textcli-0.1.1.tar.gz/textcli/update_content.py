import os
import logging

import time

from textcli.spider import Spider
    
class Textcli:

    def __init__(self, url_key, token, live_update):

        self.url_key = url_key
        self.token = token
        self.domain = "https://api.rqn9.com/data/1.0/textvn/"
        self.spider = Spider(self.url_key, self.token)
        self.pad_key = self.spider.pad_key

        self.content = self.spider.content
        self.haspw = self.spider.hspass
        
        if live_update:
            self.current_hash = self.spider.detech_change()
            self.update_tab()
    

    def update_tab(self):
        while 1:
            if self.spider.detech_change() == self.current_hash:
                pass
            elif self.spider.detech_change() == False:
                print("Something wrong!")
                break
            else:
                break
            time.sleep(5)

    def get_file_content(self, file_path):

        content = ''

        with open(file_path) as f:
            content = f.read()

        return content


    def check_file_change(self):

        new_file_stamp = os.stat(self.filepath).st_mtime

        if(new_file_stamp != self.file_stamp):
            return True
        return False


    def save_to_file(self, filename, overwrite):

        with open(filename, 'w') as f:
            f.write(self.content)

        return


    def save_file(self, filepath, overwrite):

        file_content = self.get_file_content(filepath)

        self.filepath = filepath
        self.file_stamp = os.stat(filepath).st_mtime

        self.content = ''
        if overwrite and file_content is not None:
            self.content = file_content
        elif file_content is not None:
            self.content += file_content
        else:
            self.content = ''

        self.spider.save(self.content)

        return

    def view_file(self):
        return self.content
