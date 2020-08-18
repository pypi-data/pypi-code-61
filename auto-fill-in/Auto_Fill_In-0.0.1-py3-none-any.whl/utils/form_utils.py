# coding: utf-8
import re

from .generic_utils import handleKeyError, str_strip

SUPPORTED_FORM_TYPES = ["radio", "checkbox", "text"]
DOMAIN2FORM = {
    "forms.office.com": "office",
}

def whichForms(url):
    url_domain = re.match(pattern=r"^https?:\/\/(.+?)\/", string=url).group(1)
    handleKeyError(lst=list(DOMAIN2FORM.keys()), url_domain=url_domain)
    return DOMAIN2FORM.get(url_domain)

def answer_forms(qno, ans_data={}, inputElements=[], need_check=True):
    ans = ans_data.get(str(qno))

    input_required = True
    if ans is not None:
        input_required = False
        no = ans.get("no", 1)
        val = ans.get("val", "")
        if need_check:
            print(f"Is your answer correct? [Y/n] :\n{no},{val}")
            input_required = input().lower().startswith("n")

    if input_required:
        print("Please input Your answer: ", end="")
        no,*val = input().split(",")

    try:
        no = int(no)
    except ValueError:
        val = [no]
        no = 1
    
    answer_according_to_type(targets=inputElements, no=no, val=val)
    return {"no": no, "val": val}
    
def answer_according_to_type(targets, no, val):
    """ NOTE: input no is 1-based index.
    @params targets:
    @params no     : [NOTE] 1-based index.
    @params val    : 
    """
    target = targets[no-1]
    type = target.get_attribute("type")
    handleKeyError(lst=SUPPORTED_FORM_TYPES, type=type)

    if type == "radio":
        target.click()
    elif type == "checkbox":
        for no in set(val + [no]):
            targets[int(no)-1].click()
    elif type == "text":
        if not isinstance(val, str):
            val = str_strip(",".join(val))
        target.send_keys(val)
