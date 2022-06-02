import random

history = []

hedges = ()

qualifiers = ()

replacements = {}

    def reply(sentence):
        probability = random.randint(1, 5)

        if probability in (1, 2)
            answer = random.choice(hedges)

        elif probability == 3 and len(history) > 3:

            answer = "Earlier you said that " + \ changePerson(random.choice(history))
        else:

            answer = random.choice(qualifiers) + changePerson(sentence)
        history.append(sentence)
        return answer

    def changePerson(sentence):

        words = sentence.split()
        replyWords = []
        for word in words:
        replyWords.append(replacements.get(word, word))
        return " ".join(replyWords)

    def main():

        print("Good morning, I hope you are well today.")
        print("What can I do for you?")
            while True:
        sentence = input("\n>> ")
    if sentence.upper() == "QUIT":
        print("Have a nice day!")
            break

        print(reply(sentence))


if __name__ == "__main__":
main()
