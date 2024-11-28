import re

def divide(s: str):
    
    match = re.match(r"^(.*?)in(.*)$", s)
    
    if match:
        string1 = match.group(1)
        string2 = match.group(2)
        return string1, string2
    else:
        return "",""
