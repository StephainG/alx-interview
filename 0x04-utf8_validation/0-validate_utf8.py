#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """To determine if a given data set
    represents a valid utf-8 encoding
    """
    nb = 0

    m_1 = 1 << 7
    m_2 = 1 << 6

    for i in data:

        mb = 1 << 7

        if nb == 0:

            while mb & i:
                nb += 1
                mb = mb >> 1

            if nb == 0:
                continue

            if nb == 1 or nb > 4:
                return False

        else:
            if not (i & m_1 and not (i & m_2)):
                return False

        nb -= 1

    if nb == 0:
        return True

    return False