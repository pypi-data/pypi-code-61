import re

def check_email(email):
    if re.match("[\.\w]{2,}[@]\w+[.]\w+",email,re.IGNORECASE):
    	 return "PASS"
    else:
         return "FAIL"

def contains_only_digits(StrValue):
    # Using regex() 
    if re.match('^[0-9]*$', StrValue): 
       return   'PASS' 
    else: 
       return   'FAIL'

def Format_Validator(FieldFormat, FieldValue): 
    Regex_Match = re.match(FieldFormat, FieldValue)
    if Regex_Match: 
       return    Regex_Match
    else: 
       return    'FAIL'

