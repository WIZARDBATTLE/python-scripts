sentence = "is2 Thi1s T4est 3a"

def order(sentence):
    check = 1
    position = 0
    newSentence = sentence.split(" ")
    final = ""
    if len(sentence) == 0:
        return final
    while check < len(newSentence)+1:
        print("checking for " + str(check))
        if str(check) not in newSentence[position]:
            print("not it " + newSentence[position])
            position+=1
        elif str(check) in newSentence[position]:
            print("Found match " + newSentence[position])
            if check == 1:
                final = final + newSentence[position]
            else:
                final = final + " " + newSentence[position]
            position = 0
            check+=1
    return final