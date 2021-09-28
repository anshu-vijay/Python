class Solution:
    def __init__(self,length):
        self.length = length
        
    def outputData(self):
        print(self.length)
        print(self.length+10)


obj = Solution(3)
obj.outputData()