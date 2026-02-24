try:
    sentence=input("enter a sentence:").strip()

    if sentence=="":
        print("no text entered in here.")
    else:
        print("original text:",sentence)
        print("total charecter:",len(sentence))
        print("uppercase:",len(sentence.upper()))
        print("lowercase:",len(sentence.lower()))
        print("reversed:",sentence[:-1])
        print("total words:",len(sentence))

except Exception as error:
        print("sentence is wrong",error)

