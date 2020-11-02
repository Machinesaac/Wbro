class Icon:
    def __init__(self):
        self.codeCloudy = """   
              .--.
           .-(    ). 
           (___.__)__)
        """
        self.codeRain = """
               .-.
             .(   ).
            (___(__)
            ‚ʻ‚ʻ‚ʻ‚ʻ
            ‚ʻ‚ʻ‚ʻ‚ʻ
        """

        self.codeSun = """
              \\   /
               .-.
            ‒ (   ) ‒
               `-᾿
              /   \\
        """

    def getCloud(self):
        return self.codeCloudy

    def getRain(self):
        return self.codeRain

    def getSun(self):
        return self.codeSun
