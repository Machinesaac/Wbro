class Info:
    def __init__(self):
        self.Cloudy = """
                    .--.
                 .-(    ).
                (___.__)__)
                """
        self.Sunny = """
                     \\   / 
                      .-.
                   ‒ (   ) ‒
                      `-᾿
	                 /   \\ 
                """
        self.HeavyRain = """
                        .-.
                       (   ).
                      (___(__)
                     ‚ʻ‚ʻ‚ʻ‚ʻ 
                    ‚ʻ‚ʻ‚ʻ‚ʻ
                    """
        self.HeavyThunderRain = """
                        .-.       . 
                       (   ).    .
               .      (___(__)    .
              .      ‚ʻ‚ʻ‚ʻ‚ʻ    .
               .    ‚ʻ‚ʻ‚ʻ‚ʻ   
              ."""
        self.oops = """
        :))))
        """
    def getInfo(self,sign):
        if "云" in sign:
            return self.Cloudy
        elif "晴" in sign:
            return self.Sunny
        elif "雷" in sign:
            return self.HeavyThunderRain
        elif "雨" in sign:
            return self.HeavyRain
        else:
            return self.oops
