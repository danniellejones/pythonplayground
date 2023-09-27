"""
CP3404 | Assignment 1 | Dannielle Jones

"""
import string
import textwrap


def main():
    """
    Substitution Cipher
    """
    plain_word = "deterministically"
    cipher_word = "mtqtbahjhkqhgseer"

    alpha = {'a': '?', 'b': '?', 'c': '?', 'd': '?', 'e': '?',
             'f': '?', 'g': '?', 'h': '?', 'i': '?', 'j': '?',
             'k': '?', 'l': '?', 'm': '?', 'n': '?', 'o': '?',
             'p': '?', 'q': '?', 'r': '?', 's': '?', 't': '?',
             'u': '?', 'v': '?', 'w': '?', 'x': '?', 'y': '?',
             'z': '?'}

    # Convert the chosen word into the permute alphabet
    for plain_char, cipher_char in zip(cipher_word, plain_word):
        alpha[plain_char] = cipher_char

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
    print(alpha)
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
