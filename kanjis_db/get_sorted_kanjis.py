import json, os

# Sort Kanji database by JLPT levels.

def get_sorted_kanjis():
    
    kanji_dir = os.path.join(os.getcwd(), "kanji-data-master/kanji.json")
    f = open(kanji_dir, encoding="utf-8", errors="ignore")

    data = json.load(f)

    sorted_kanjis = {1: [],
                     2: [],
                     3: [],
                     4: [],
                     5: []}
    for kanji, info in data.items():
        if info["jlpt_new"] is not None:
            sorted_kanjis[int(info["jlpt_new"])].append({kanji: info})
    
    print(sorted_kanjis)

    #, encoding="utf-8"
    with open("jlpt.json", "w", encoding="utf-8") as fp:
        json.dump(sorted_kanjis, fp, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    get_sorted_kanjis()