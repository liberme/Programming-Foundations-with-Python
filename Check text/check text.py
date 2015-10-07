import urllib

def read_text():
    text = open('C:\Udacity\movie_quotes.txt')
    contents = text.read()
    print (contents)
    text.close()
    return contents

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)


check_profanity(read_text())
