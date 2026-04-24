class Computer:
    def __init__(self, cpu, hd):
        print("init called")
        self.cpu = cpu
        self.hd = hd
        
    
    def config(self):
        print("Configurations:", self.cpu, self.hd)
        
com1 = Computer("i5", "512")
com2 = Computer("i9", "1080")

com1.config()
        
com2.config()