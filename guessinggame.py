def init():
    library = [
    {
        "answer": "elephant",
        "attributes": ['alive', 'animal', 'large', 'grey']
    },
    {
        "answer": 'basketball',
        "attributes": ['basketball', 'object', 'toy', 'small', 'orange']
    },
    {
        "answer": 'dog',
        "attributes": ['dog', 'alive', 'animal', 'small', 'brown']
    },
    {
        "answer": 'plant',
        "attributes": ['plant', 'alive', 'plant', 'small', 'green']
    },
    {
        "answer": 'chair',
        "attributes": ['chair', 'object', 'large', 'black']
    }
    ]

    def start_round(item, index, array):
        answer = item["answer"]
        attributes = item["attributes"]


        def ask_question():
            input_string = input("Ask a question (e.g.: is it ... ?)\n")

            def input_string_has_attribute(attribute):
                return attribute in input_string

            if answer in input_string:
                if index == len(library) - 1:
                    print("You guessed it! You win the game!")
                else:
                    print("You guessed it! Onto the next round...\n")
            elif any(map(input_string_has_attribute, attributes)):
                print("Yes, have another guess...\n")
                ask_question()
            else:
                print("No, have another guess...\n")
                ask_question()
        ask_question()

    for index, item in enumerate(library):
        start_round(item, index, library)


init()


