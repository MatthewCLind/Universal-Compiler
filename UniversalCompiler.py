import sys
import urllib2


# Class from ANU's website
class ANURandom:
    BINARY = "BINARY"
    HEX = "HEX"
    CHAR = "CHAR"

    def getRandom(self,type):
        if type == self.BINARY:
            url = 'http://150.203.48.55/RawBin.php'
        elif type == self.HEX:
            url = 'http://150.203.48.55/RawHex.php'
        elif type == self.CHAR:
            url = 'http://150.203.48.55/RawChar.php'

        page = urllib2.urlopen(url, timeout=5)

        data = page.read()
        num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
        return num

    def getBin(self):
        return self.getRandom(self.BINARY)

    def getHex(self):
        return self.getRandom(self.HEX)

    def getChar(self):
        return self.getRandom(self.CHAR)


num_bytes = 0
if(sys.argv[1].isdigit()):
    num_bytes = int(sys.argv[1])
else:
    affirmation_filename = sys.argv[1]
    affirmation_text = ''
    with open(affirmation_filename, 'r') as affirmation_file:
        affirmation_text = affirmation_file.read()
    affirmation_len = len(affirmation_text)
    print("affirmation len: " + str(affirmation_len))
    num_bytes = affirmation_len

data = ''
generator = ANURandom()
while len(data) < num_bytes:
    data += generator.getChar()

data.encode()

output_filename = sys.argv[2]
with open(output_filename, 'wb') as output_file:
    output_file.write(data)

# Note: not recommended for unlucky people
if "-e" in sys.argv:
    eval(data)
