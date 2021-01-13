#select 4 main emojis: smiling, laughing, sad, angry
#smile: U+1F604, smile, happy, joy
#laughing: U+1F602, laugh, happy, joke
#sad: U+1F62D, sad, sorrow, depressed, cry
#angry: U+1F620, angry, mad, rage

dict = {"smile": '\U0001f604', "laugh":'\U0001f602', "sad":'\U0001f62d', "angry":'\U0001f620', "tired": '\U0001f602'}

emojidict = dict.fromkeys(dict.keys)
# emojidict = dict.fromkeys(["smile", "laugh", "sad", "angry", "tired"])

smile = ["smile", "happy", "joy"]
laugh = ["laugh", "happy", "joke"]
sad = ["sad", "sorrow", "cry"]
angry = ["angry", "mad", "rage"]
tired = ["tired"]

emojis = [smile, laugh, sad, angry, tired]

from PyDictionary import PyDictionary
dictionary=PyDictionary()

for key in emojjidict:
    emojidict[key] = dictionary.synonym(str(key))

# emojidict["smile"] = dictionary.synonym("smile")
# emojidict["laugh"] = dictionary.synonym("laugh")
# emojidict["sad"] = dictionary.synonym("sad")
# emojidict["angry"] = dictionary.synonym("angry")
# emojidict["tired"] = dictionary.synonym("tired")


# for emoji in emojis:
#     for i in range(3):
#         #print(emoji[i])
#         emoji.extend(dictionary.synonym(emoji[i]))

 