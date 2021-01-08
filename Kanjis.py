
import json, os
#Holds dictionary-loaded version of jlpt.json. Uses singleton design pattern.

class Kanjis:
    __instance = None

    # Access method. Kanjis class is always accessed using this method.
    def get_kanjis(self, levels):
        if Kanjis.__instance == None:
            Kanjis()

        else:
            # Error handling. Wrap non-list with a list and convert ints as string.
            if type(levels) is not list:
                levels = [levels]
                
            levels = [str(level) for level in levels]

            return {level:self.__instance[level] for level in levels}
    
    # Private constructor. Only called when access method is called first time.
    def __init__(self):
        if Kanjis.__instance != None:
            raise Exception("Kanjis already exists.")
        #Load Kanjis from /kanji_db/jlpt.json
        else:
            kanji_dir = 'kanjis_db/jlpt.json'
            f = open(kanji_dir, encoding="utf-8", errors="ignore")
            Kanjis.__instance = json.load(f)
