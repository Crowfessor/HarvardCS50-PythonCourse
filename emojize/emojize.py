import emoji

emo = input("Input: ")
emojindex=emo.find(":")

emoji_name= emo[emojindex:]
filler= emo[:emojindex]

create_emoji= emoji.emojize(emoji_name, language='alias')
print("Output:",filler+create_emoji)



