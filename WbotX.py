from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import chatbot as ai


## Selenium web drivers
driver  = None
waiting = 20 


def wait(web_opening_time=3):
    time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
    global driver
    driver = webdriver.Firefox()

## quit web driver for selenium
def web_driver_quit():
    driver.quit()

## actual login in hockey app site
def whatsapp_login():
    driver.get('https://web.whatsapp.com/');
    wait(10)

def sendMessage(msg):
    web_obj = driver.find_element_by_css_selector('.input')
    web_obj.clear()
    web_obj.send_keys(msg)
    snd = driver.find_element_by_css_selector('.icon-send > svg:nth-child(1) > path:nth-child(1)')
    snd.click()

def chatlist():
    web_obj = driver.find_element_by_css_selector('.icon-chat')
    web_obj.click()
    
def search(item):
    srch = driver.find_element_by_css_selector('.drawer > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)')
    srch.click()
    data=driver.find_element_by_css_selector('.drawer > div:nth-child(2) > div:nth-child(1) > label:nth-child(4) > input:nth-child(1)')
    data.clear()
    data.send_keys(item)
    
def chatbox():
    xnt='.contact > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
    web_obj = driver.find_element_by_css_selector(xnt)
    web_obj.click()
    
def conversation():
    x='.pane-body'
    vb = driver.find_element_by_css_selector(x)
    vt=vb.text
    vx = vt.split('\n')
    ch=[]
    for i in range(len(vx)):
        tmp = vx[i].split(':')
        try:
            hold = tmp[1]
        except IndexError:
            ch.append(tmp[0])
    return ch[-1]


print("Training Done!")
print(" ")

web_driver_load()
whatsapp_login()
wait()


print("Is Whatsaap web loging Done? If yes then press Y and if no then wait for a moment! For Quit press Q ")
start=time.time()
st = input() 
if st=='Y':
	chatlist()
	print("Enter Friend name: ")
	name = input()
	search(name)
	chatbox()
	print("For start Chatting Press Y! Dont press ctrl+z during chatting! Otherwise session turnedoff! ")
	st=input()
	if st=='Y':
		flag= 'hola'
		start=time.time()
		sendMessage(flag)
		time.sleep(waiting)
		val = conversation()
		while(1):
    			if val==flag:
        			sendMessage("well ttylt! Bye!")
        			break
    			else:
        			tmp = val
        			posts=ai.test_ai(val)
        			#time.sleep(0.02)
        			sendMessage(posts)
        			#time.sleep(5)
        			try:
            				time.sleep(waiting)
            				val=conversation()
            				if val=='shutdown':
                				sendMessage("well ttylt! Bye!")
                				break
        			except:
            				flag=val

else:
	print("Better luck next time!")
print("Thank you!")
stop = time.time()
print("Total session time: "+str(stop-start))

