#loads list of English words
class Dictionary(object):
    wordlist = open('readwrite/wordlist.txt')
    words = wordlist.read().splitlines()

