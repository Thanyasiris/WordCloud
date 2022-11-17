import eel

# name of folder where the html, css, js, image files are located
eel.init('templates')

@eel.expose
def demo(x):
    return x**2

# 1000 is width of window and 600 is the height
#,mode='firefox-app'
eel.start('index.html',mode='firefox-app',port=8080, size=(1000, 600))