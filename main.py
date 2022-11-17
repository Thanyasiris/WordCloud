import eel
import sentiment 
#from sentiment import inputkeyword
# name of folder where the html, css, js, image files are located
eel.init('templates')

print("Start Server")

@eel.expose
def demo(x):
    sentiment.inputkeyword("apec", 10, 3)
    print("Call Sentimental Analysis")
    return x**2

@eel.expose
def input(keyword, noOfTweet, select):
    sentiment.inputkeyword(keyword, noOfTweet, select)
    return

@eel.expose
def say_hello_py(x):
    print('Hello from %s' % x)

say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

print("Run Server Successful")
# 1000 is width of window and 600 is the height
#mode='firefox-app'
eel.start('index.html', size=(1000, 600))