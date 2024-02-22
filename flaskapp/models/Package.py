import json

class Package:
    def __init__(self, path):
        self.path = path
        self.manifest = json.load(path + "/manifest.json")
    
    def hasChanged(self):
        pass