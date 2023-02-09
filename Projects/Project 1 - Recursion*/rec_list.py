from __future__ import annotations
from typing import Optional, Any, Tuple

# NodeList is
# None or
# Node(value, rest), where rest is the rest of the NodeList
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value
        self.rest = rest

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value
            and self.rest == other.rest
            )
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist: Optional[Node]) -> Optional[str]:
    if strlist == None:
        raise ValueError
    if strlist.rest == None:
        return strlist.value
    tempStr = first_string(strlist.rest)
    if strlist.value < tempStr:
        return strlist.value
    return tempStr

# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist: Optional[Node]) -> Tuple[Optional[Node], Optional[Node], Optional[Node]]:
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    if strlist == None:
        raise ValueError
    if strlist.value == None and strlist.rest == None:
        print ("hi")
        return None

    if strlist.rest == None:
        if strlist.value[0].lower() in vowels:
            return (Node(strlist.value, None), None, None)
        elif strlist.value[0].lower() in consonants:
            return (None, Node(strlist.value, None), None)
        else:
            return (None, None, Node(strlist.value, None))

    tempTup = split_list(strlist.rest)

    if strlist.value[0].lower() in vowels:
        if tempTup[0] == None:
            return (Node(strlist.value, None), tempTup[1], tempTup[2])
        else:
            if tempTup[0].value < strlist.value:
                return (Node(strlist.value, tempTup[0]), tempTup[1], tempTup[2])
    elif strlist.value[0].lower() in consonants:
        if tempTup[1] == None:
            return (tempTup[0], Node(strlist.value, None), tempTup[2])
        else:
            return (tempTup[0], Node(strlist.value, tempTup[1]), tempTup[2])
    else:
        if tempTup[2] == None:
            return (tempTup[0], tempTup[1], Node(strlist.value, None))
        else:
            return (tempTup[0], tempTup[1], Node(strlist.value, tempTup[2]))
