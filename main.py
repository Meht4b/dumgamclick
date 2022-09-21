import pytesseract as tess
from PIL import Image
import pyautogui
import time

userSellPrice=0
userBuyPrice=0
sellbuy = input('sell/buy, s/b')
if sellbuy =='s':
    userSellPrice = float(input('price'))
if sellbuy =='b':
    userBuyPrice = float(input('price'))
userProfitmargin=float(input('desired profit margin?'))

imageMyoffers=Image.open('myoffers.png')
imageParts=Image.open('parts.png')
imageChange=Image.open('change.png')
imageOk=Image.open('ok.png')

print('switch to game window')

time.sleep(2)

while True:

    screenshotRaw=pyautogui.screenshot(region=((788,356,1200,73)))
    rawData=tess.image_to_string(screenshotRaw)
    rawNums=''
    for x in rawData:
        if x.isdigit() or x == ' ' or x =='.' or x == '-':
            rawNums = rawNums + x
    numData=rawNums.split()
    currentSellprice=float(numData[0])
    currentBuyprice=float(numData[2])
    currentProfitMargin=float(numData[4])

    if userSellPrice != currentSellprice and sellbuy=='s' and currentProfitMargin > userProfitmargin:
        # move to my offers tab
        pyautogui.moveTo(573, 107)
        time.sleep(0.2)
        pyautogui.click()
        #       #move to change order
        pyautogui.moveTo(983, 415)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(0.5)
        # change order
        newSellprice = str(currentSellprice - 0.001)
        pyautogui.write(newSellprice)
        # click change
        pyautogui.moveTo(773, 760)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(2)
        # click ok
        pyautogui.moveTo(964, 600)
        time.sleep(0.4)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(255, 108)
        time.sleep(0.2)
        pyautogui.click()

        userSellPrice = newSellprice


    if userBuyPrice != currentBuyprice and sellbuy=='b' and currentProfitMargin > userProfitmargin:
        #move to my offers tab
        pyautogui.moveTo(573,107)
        time.sleep(0.2)
        pyautogui.click()
#       #move to change order
        pyautogui.moveTo(983,415)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(0.5)
        #change order
        newBuyprice=str(currentBuyprice+0.01)
        pyautogui.write(newBuyprice)
        #click change
        pyautogui.moveTo(773,760)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(2)
        #click ok
        pyautogui.moveTo(964,600)
        time.sleep(0.4)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(255,108)
        time.sleep(0.2)
        pyautogui.click()

        userBuyPrice=newBuyprice
        print(userBuyPrice,newBuyprice,currentBuyprice)


    time.sleep(4)


