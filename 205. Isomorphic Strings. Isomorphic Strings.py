def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    pairs = {}

    # if string length is not the same
    # then they can't be isomorphic
    if (not len(s) == len(t)):
        return False

    for i in range(len(s)):
        print(pairs)
        # for each index, check if the pair exists
        if (check_for_pair(pairs, s[i], t[i])):
            # pair already in there and is identical
            continue
        else:
            # try adding a the new pair
            if (not add_pair(pairs, s[i], t[i])):
                # there was already a record of one of the chars, return false
                return False

    return True


def add_pair(pairs, a, b):
    if (a in pairs or b in pairs.values()):
        return False

    # else add pair to list
    pairs.update({a:b})
    return True

# order matters
def check_for_pair(pairs, a, b):
    if (a in pairs):
        x = pairs[a]
        if (x == b):
            return True

    return False

example = {
    'a' :  'b',
    'c' : 'd'
}


s = "paper"
t = "title"
print(isIsomorphic(s, t))