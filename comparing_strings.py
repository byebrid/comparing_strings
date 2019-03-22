"""comparing_strings.py"""


def are_similar(s1, s2, max_edit_dist=1):
    """
    Returns True if s1=s2 (case-insensitive) or if edit distance between s1 and
    s2 is smaller than max_edit_dist.

    Edit distance is the number of additions/subtractions of a character you
    would need to perform to get from one string to another. For example,
    'Abc' & 'abDc' have an edit distance of 1, since you just need to add 'D' to
    'Abc' or remove 'D' from 'abDc'.

    Parameters
    ----------
    s1 : str (or convertible to str)
    s2 : str (or convertible to str)
    max_edit_dist: int
        The maximum edit distance s1 can be away from s2.
    """
    def get_char(s, i):
        """Returns s[i] if it exists, otherwise returns None"""
        try:
            char = s[i].upper()
        except IndexError:
            char = None
        return char

    # Accounting for if ints or floats, etc. are passed as args
    if type(s1) != str:
        s1 = str(s1)
    if type(s2) != str:
        s2 = str(s2)

    # Making it so len(s1) >= len(s2)
    if len(s2) > len(s1):
        s1, s2 = s2, s1

    # If required edits obviously > max_edit_dist, return False
    if len(s1) - len(s2) > max_edit_dist:
        return False

    # Keep track of how many more edits we can make (useful for checking next
    # 'n' characters in s2/s1)
    remaining_edits = max_edit_dist
    for i, char1 in enumerate(s1):
        # If we've edited too much, return False
        if remaining_edits < 0:
            return False

        # char1.upper() is equivalent to get_char(s=s1, i=i) here
        char1 = char1.upper()
        char2 = get_char(s=s2, i=i)

        if char1 == char2:
            continue

        # Get the next chars in s1 and s2 if possible.  Use list because
        # max_edit_dist/remaining_edits does not always equal 1.
        next_chars1 = [get_char(s=s1, i=i+j) for j in range(1, remaining_edits+1)]
        next_chars2 = [get_char(s=s1, i=i+j) for j in range(1, remaining_edits+1)]

        if char1 in next_chars2:
            # Puts s2's next char in the 'middle' of s1
            print(f'Putting {char2} from {s2} into {s1}')
            s1 = s1[:i] + char2 + s1[i:]
            remaining_edits -= 1
            continue
        elif char2 in next_chars1:
            print(f'Putting {char1} from {s1} into {s2}')
            # Puts s1's next char in the 'middle' of ss
            s2 = s2[:i] + char1 + s2[i:]
            remaining_edits -= 1
            continue
        elif char2 is None:
            # Test at end of function if we could just add the rest of s1 to s2
            break
        else:
            # If there are too many chars for us to insert,
            return False

    last_required_edits = len(s2) - len(s1)
    return last_required_edits <= remaining_edits and remaining_edits >= 0
