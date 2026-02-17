import re
from humre import *

def regex_strip(str_to_strip: str, char_stripped=' ') -> str:
    """
    We will take in a string and strip the char_stripped from beginning and end.
    
    :param str_to_strip: Description
    :type str_to_strip: str
    :return: stripped string
    :rtype: str
    """
    char_stripped_group = rf'[{char_stripped}]'
    
    beginning_regex = re.compile(one_or_more(char_stripped_group) + BOUNDARY)
    ending_regex = re.compile(BOUNDARY + one_or_more(char_stripped_group))
    str_to_strip = beginning_regex.sub('', str_to_strip)
    str_to_strip = ending_regex.sub('', str_to_strip)
    return str_to_strip

print(regex_strip('-,--Hassaan,,-', '-,'))


