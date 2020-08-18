# coding: utf-8
import os
import re
import copy
import time
import subprocess
from imgcat import imgcat
from abc import ABCMeta, abstractmethod
from gummy.utils import (get_driver,
                         try_find_element_click, try_find_element_send_keys)

from .utils.coloring_utils import toBLUE
from .utils.environ_utils import load_envfile, save_envfile
from .utils.form_utils import answer_forms
from .utils.generic_utils import now_str, mk_class_get

SUPPORTED_FORMS = ["office"]

class AutoFillInAbstForms(metaclass=ABCMeta):
    def __init__(self, path, verbose=True, **kwargs):
        self.name  = self.__class__.__name__
        self.name_ = re.sub(r"([a-z])([A-Z])", r"\1_\2", self.name).lower()
        self.verbose = verbose
        self.path, self.envdata = load_envfile(path, ret_path=True)
        self.__dict__.update(kwargs)

    def login(self, driver, url, login_data={}):
        if self.verbose: print(f"\nLogin\n{'='*30}\nGet {toBLUE(url)}")
        driver.get(url)
        prefix = "try_find_element"
        login_data = copy.deepcopy(sorted(login_data.items(), key=lambda x:x[0]))
        for no,values in login_data:
            method = values.pop("func", None)
            globals().get(f"{prefix}_{method}")(driver=driver, verbose=self.verbose, **values)

    def save_envdata(self, indent=2, update=True):
        save_envfile(path=self.path, data=self.envdata, indent=indent, update=update)

    def run(self, browser=False, **kwargs):
        with get_driver(browser=browser) as driver:
            self.login(driver=driver, url=self.envdata.get("URL"), login_data=self.envdata.get("login", {}))
            self.answer_form(driver=driver, **kwargs)

    def _dev_run(self, browser=True, **kwargs):
        driver = get_driver(browser=browser)
        self.login(driver=driver, url=self.envdata.get("URL"), login_data=self.envdata.get("login", {}))
        self.answer_form(driver=driver, **kwargs)
        return driver
    
    @staticmethod
    def show_curt_browser(driver):
        fn = "tmp.png"
        driver.save_screenshot(fn)
        try:
            imgcat(open(fn))
        except:
            subprocess.run(["imgcat", fn])
        os.remove(fn)

    @abstractmethod
    def answer_form(self, driver, **kwargs):
        if "answer" not in self.envdata:
            self.envdata["answer"] = {}
        if self.verbose: print(f"\nAnswer Form\n{'='*30}")

class OfficeForms(AutoFillInAbstForms):
    def __init__(self, path, verbose=True, **kwargs):
        super().__init__(path=path, verbose=verbose, **kwargs)

    def answer_form(self, driver, need_check=True, update=True, show_result=True, **kwargs):
        super().answer_form(driver=driver, **kwargs)
        envdata = self.envdata["answer"]
        answered_qnos = []
        not_found_count=0
        while True:
            visible_questions = driver.find_elements_by_class_name(name="office-form-question")
            if len(answered_qnos) == 0:
                if not_found_count>5: break
                time.sleep(1)
                not_found_count += 1
            elif len(answered_qnos) == len(visible_questions): 
                break
            for question in visible_questions:
                # NOTE: question number depends on forms.
                qno = int(question.find_element_by_css_selector("span.ordinal-number").text.rstrip("."))
                if qno not in answered_qnos:
                    print(question.find_element_by_css_selector("div.question-title-box").text+"\n")
                    inputElements = question.find_elements_by_tag_name(name="input")
                    num_inputElements = len(inputElements)
                    for j,inputTag in enumerate(inputElements):
                        type_ = inputTag.get_attribute("type")
                        value = inputTag.get_attribute("value")
                        # NOTE: input no is 1-based index.
                        print(f"\t{j+1:>0{len(str(num_inputElements))}} [{type_}] {value}")
                    answer = answer_forms(qno=qno, ans_data=envdata, inputElements=inputElements, need_check=need_check)
                    self.envdata["answer"][str(qno)] = answer
                    answered_qnos.append(qno)
                    print("-"*30)
        try_find_element_click(driver=driver, by="css selector", identifier="button.__submit-button__")        
        if update:
            self.save_envdata()
        if show_result:
            time.sleep(3)
            self.show_curt_browser(driver=driver)
        
all = AutoFillInForms = {
    "office" : OfficeForms,
}

get = mk_class_get(
    all_classes=AutoFillInForms,
    gummy_abst_class=[AutoFillInAbstForms],
    genre="forms"
)