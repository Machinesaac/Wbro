


dic = {
                    "1": ["北京","101010100"],
                    "2": ["成都","101270101"],
                    "3": ["广州","101280101"],
                    "4": ["韶关","101280201"],
                    "5": ["上海","101020100"]
        }

def getCode(loc):
    if (loc in dic) and dic[loc]:
        return dic[loc][0], dic[loc][1]
    else:
        return 0, 0

"""
   [-]City not found.
   [!]Now only support:
    1.北京
    2.成都
    3.广州
    4.韶关
    5.上海   
"""