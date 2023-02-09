from typing import List
# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []


def perm_gen_lex(str_in: str) -> List:
    if len(str_in) == 1:
        return[str_in]
    temp = []
    i = 0
    while i in range(len(str_in)):
        perm = perm_gen_lex(str_in[0:i] + str_in[i+1:])
        j = 0
        while j in range(len(perm)):
            temp.append(str_in[i:i+1] + perm[j])
            j += 1
        i += 1

    return temp
