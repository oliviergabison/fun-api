import json

class Project:
    def __init__(self, path) -> None:
        self.path = path
        self.manifest = json.load(path + '/manifest.json')
    
    def createChangeLog(self):
        pass

    def createChangeset(self):
        pass

    def getPackagesToChange(self):
        pass

    def getPackages(self):
        pass
    
    def getChangesets(self):
        pass