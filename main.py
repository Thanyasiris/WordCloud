import eel
import sentiment 
#from sentiment import inputkeyword
# name of folder where the html, css, js, image files are located
eel.init('templates')

print("Start Server")

@eel.expose
def input(keyword, noOfTweet, select):
    print("keyword : "+keyword)
    sentiment.inputkeyword(keyword, noOfTweet, select)
    return

print("Run Server Successful")

# 1000 is width of window and 600 is the height
# mode='firefox-app'
# port=8000
# default path http://localhost:8000/index.html
eel.start('index.html', size=(1000, 600))