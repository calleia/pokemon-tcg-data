import json

def run():
    with open("sets/en.json") as sets_file, open("images/images.tsv", "w") as images_file, open("images/images-large.tsv", "w") as images_large_file:
        sets = json.load(sets_file)

        for card_set in sets:
            set_path = "cards/en/" + card_set["id"] + ".json"

            with open(set_path) as set_file:
                set_data = json.load(set_file)

                for card in set_data:
                    print(card["name"])
                    images_file.write(card["id"] + "\t" + card["images"]["small"] + "\n")
                    images_large_file.write(card["id"] + "\t" + card["images"]["large"] + "\n")

if __name__ == "__main__":
    run()
