import requests
import Dic
import time
import sys
from draw import Icon


def bar():
    print("[*]正在查询......")
    for i in range(11):
        if i != 10:
            sys.stdout.write("==")
        else:
            sys.stdout.write("== " + str(i * 10) + "%/100%")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n" + "[+]查询完成")


key = "key=5ce5cb6b817f4661ba8d292679a546f1"


# loc = "location=101010100"
# url = "https://devapi.heweather.net/v7/weather/now?"+key+'&'+loc
# url2 = "https://devapi.heweather.net/v7/weather/3d?"+key+'&'+loc
# print(url2)
# board = requests.get(url2).json()
# print(board)

class WeatherNow:
    def __init__(self, location):
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
    def __init__(self, board, pm2):
        self.bo = board
        self.pm = pm2

    def getTime(self):
        time = self.bo['fxDate']
        return str(time)

    def getTemp(self):
        tmpmax = self.bo['tempMax']
        tmpmin = self.bo['tempMin']
        return (tmpmin, tmpmax)

    def getIcon(self):
        return self.bo['iconDay']

    def getText(self):
        text = self.bo['textDay']
        return str(text)

    def getWind(self):
        winddir = self.bo['windDirDay']
        windScale = self.bo['windScaleDay']
        windSpeed = self.bo['windSpeedDay']
        return [winddir, windScale, windSpeed]


class Printer:
    def __init__(self, day):
        self.d = day

    def printDate(self):
        return "日期: " + self.d.getTime()

    def printTemp(self):
        return "温度:" + self.d.getTemp()[0] + "~" + self.d.getTemp()[1] + "℃"

    def printText(self):
        return "今天天气:" + self.d.getText()

    def printWind(self):
        wind = self.d.getWind()
        return "今天的风是 " + wind[0] + " ,风力 " + wind[1] + " 级" + ",风速 " + wind[2] + "km/s."

    def printIcon(self):
        image = Icon()
        if "云" in self.d.getText():
            icon = image.getCloud()
        elif "晴" in self.d.getText():
            icon = image.getSun()
        elif "雨" in self.d.getText():
            icon = image.getRain()
        else:
            return "What"
        return icon


def printWeather(Printer):
    print(Printer.printDate())
    print(Printer.printText())
    print(Printer.printIcon())
    print(Printer.printTemp())
    print(Printer.printWind())


def getFutWeather(location, name, num):
    d = str(num) + "d?"
    loc = "location=" + location
    url = "https://devapi.heweather.net/v7/weather/" + d + key + '&' + loc
    urlpm = "https://devapi.heweather.net/v7/air/now?" + key + '&' + loc
    print(url)
    board = requests.get(url).json()
    pm = requests.get(urlpm).json()
    days = [Day(i, pm) for i in board['daily']]
    bar()
    for _ in range(2):
        print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("你当前所在地的PM2.5为:", pm['now']['pm2p5'])
    print("空气质量", pm['now']['category'])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for _ in range(2):
        print()
    print("[+]以下是" + name + "近三天天气: ")
    print("——————————————————————————————")
    for day in days:
        printWeather(Printer(day))
        print()
        print("——————————————————————————————")


def main():
    print("""[*]现在可查询城市有：
                        1.北京
                        2.上海
                        3.广州
                        4.成都
                        5.韶关   """)

    print("__________________")
    while True:
        loc = input("[*]请选择你要查询的城市序号:")
        dic = Dic.Dictionary(loc)
        city = dic.getCity()
        for key in city:
            print(key + '.' + city[key][0])
        area = input("[*]请选择你要查询的区域序号:")
        dic.setArea(area)
        name, code = dic.getArea()
        if not code:
            print("[-]City not found.")
            continue
        break
    getFutWeather(code, name, 3)


if __name__ == "__main__":
    main()
# r.encoding = 'utf-8'
# print(r.json()['forecast']['12h']['101280201'])
