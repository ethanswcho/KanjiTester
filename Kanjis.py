
import json, os
#Holds dictionary-loaded version of jlpt.json. Uses singleton design pattern.

class Kanjis:
    __instance = None

    # Access method. Kanjis class is always accessed using this method.
    def get_instance(self, *args):
        if Kanjis.__instance == None:
            Kanjis()
        return Kanjis.__instance
    
    # Private constructor. Only called when access method is called first time.
    def __init__(self):
        if Kanjis.__instance != None:
            raise Exception("Violating singleton design of Kanjis")
        #Load Kanjis from /kanji_db/jlpt.json
        else:
            kanji_dir = 'kanjis_db/jlpt.json'
            f = open(kanji_dir, encoding="utf-8", errors="ignore")
            self = json.load(f)
            Kanjis.__instance = self
