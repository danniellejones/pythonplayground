"""
CP3404 | Assignment 1 | Dannielle Jones

"""
import string
import textwrap


def main():
    """
    Substitution Cipher
    """
    alpha = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
             'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
             'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o',
             'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',
             'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y',
             'z': 'z'}
    keyword = ""
    cipher_text = "qyt ovtbsqhojse mhksmisjqsptk oz qyt ojt-qhat vsm ysit etm qo qyt mtiteovatjq oz gojmhqhojseer " \
                  "ktgwbt kqbtsa ghvytbk dyhgy sbt sfet qo btqshj qyt vokhqhit gysbsgqtbhkqhgk oz ojt-qhat vsmk dyhet " \
                  "siohmhjp aokq oz qythb jtpsqhit skvtgqk. qyt veshjqtlq hk tjgbrvqtm hj awgy qyt ksat dsr sk qyt " \
                  "ojt-qhat vsm, fwq dhqy mtqtbahjhkqhgseer ptjtbsqtm vktwmo-bsjmoa ktcwtjgtk."
    display_plaintext(cipher_text, alpha)
    determine_key(keyword)


def display_plaintext(cipher_text, alpha):
    """
    Display Plaintext
    :param cipher_text: String to decipher
    :param alpha: Permute alphabet dictionary
    """
    plaintext = ""
    for char in cipher_text:
        if char in alpha:
            plaintext += alpha[char]
        else:
            plaintext += char

    width = 60
    wrap_text = textwrap.wrap(plaintext, width=width)
    print("Plaintext:")
    for line in wrap_text:
        print(line)
    print()


def determine_key(keyword):
    """
    Determine keyword
    :param keyword: The keyword of the table
    """
    alphabet = list(string.ascii_uppercase)
    # Remove repeated characters from keyword
    unique_chars = []
    for char in keyword:
        if char not in unique_chars:
            unique_chars.append(char)
    compare_chars = list(unique_chars)

    # Create keyword table 6x5
    table = []
    # Rows
    for i in range(6):
        row = []
        # Columns
        for j in range(5):
            if unique_chars:
                row.append(unique_chars.pop(0))
            else:
                item = alphabet.pop(0) if alphabet else ''
                while item in compare_chars:
                    item = alphabet.pop(0) if alphabet else ''
                row.append(item)
        table.append(row)

    print("Key:")
    for row in table:
        print(' '.join(row))


main()
