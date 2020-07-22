import requests
import asciify

key = "key=5ce5cb6b817f4661ba8d292679a546f1"
#loc = "location=101010100"
#url = "https://devapi.heweather.net/v7/weather/now?"+key+'&'+loc
#url2 = "https://devapi.heweather.net/v7/weather/3d?"+key+'&'+loc
#print(url2)
#board = requests.get(url2).json()
#print(board)

class WeatherNow:
    def __init__(self,location):
        self.loc = location
        self.board = requests.get(url).json()
        self.nowInf = self.board['now']

    def getTime(self):
        text = "现在时间是:" + self.nowInf['obsTime']
        return text

    def getTemp(self):
        text = "现在的温度是:" + self.nowInf['temp']
        return text

    def getIcon(self):
        return self.nowInf['icon']

    def getWind(self):
        winddir = self.nowInf['windDir']
        windScale = self.nowInf['windScale']
        windSpeed = self.nowInf['windSpeed']
        text = "现在的风是" + winddir + " 风力" + windScale + "级" + " 风速" + windSpeed + "km/s."
        return text

class Day:
    def __init__(self,board):
        self.bo = board

    def getTime(self):
        time = self.bo['fxDate']
        return str(time)

    def getTemp(self):
        tmpmax = self.bo['tempMax']
        tmpmin = self.bo['tempMin']
        return (tmpmin,tmpmax)

    def getIcon(self):
        return self.bo['iconDay']

    def getText(self):
        text = self.bo['textDay']
        return str(text)

    def getWind(self):
        winddir = self.bo['windDirDay']
        windScale = self.bo['windScaleDay']
        windSpeed = self.bo['windSpeedDay']
        return [winddir,windScale,windSpeed]

class Printer:
    def __init__(self,day):
        self.d = day

    def printDate(self):
        return "日期: " + self.d.getTime()

    def printTemp(self):
        return "最低温" + self.d.getTemp()[0] + " 最高温:"+self.d.getTemp()[1]

    def printText(self):
        return "今天天气:" + self.d.getText()

    def printWind(self):
        wind = self.d.getWind()
        return "今天的风是" + wind[0] + ",风力" + wind[1] + "级" + ",风速" + wind[2] + "km/s."

def printWeather(Printer):
    print(Printer.printDate())
    print(Printer.printTemp())
    print(Printer.printText())
    print(Printer.printWind())

def getFutWeather(location,num):
    d = str(num)+"d?"
    loc = "location=" + location
    url = "https://devapi.heweather.net/v7/weather/" + d + key + '&' + loc
    print(url)
    board = requests.get(url).json()
    days = [Day(i) for i in board['daily']]

    for day in days:
        printWeather(Printer(day))
        print()


getFutWeather("101010100",3)

#r.encoding = 'utf-8'
#print(r.json()['forecast']['12h']['101280201'])