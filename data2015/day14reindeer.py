class Reindeer:
    
    def __init__(self, name, speed, maxflytime, maxresttime):
        self.name = name
        self.speed = speed
        self.flytime = 0
        self.maxflytime = maxflytime
        self.resttime = 0
        self.maxresttime = maxresttime
        self.flying = True
        self.distance = 0
        self.points = 0
        
        
    def do_second(self):
        if self.flying:
            self.distance += self.speed
            self.flytime += 1
            if self.flytime == self.maxflytime:
                self.flytime = 0
                self.flying = False
        else:
            self.resttime += 1
            if self.resttime == self.maxresttime:
                self.resttime = 0
                self.flying = True
    
    def get_point(self):
        self.points += 1
        
        