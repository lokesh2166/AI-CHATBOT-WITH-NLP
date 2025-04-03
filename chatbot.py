import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r"hello|hi|hey", ["Hello!", "Hi there!", "Hey! How can I help?"]),
    (r"what is anime?", ["Anime is a style of animation that originated in Japan. It includes a wide range of genres and is enjoyed worldwide!"]),
    (r"recommend an anime", ["Sure! Some popular anime are Attack on Titan, Naruto, One Piece, and Death Note."]),
    (r"(.*) best anime?", ["The best anime depends on your taste! Action fans might love One Punch Man, while mystery lovers might enjoy Steins;Gate."]),
    (r"(.*) anime genres?", ["Anime comes in many genres such as Shonen (action-packed), Shojo (romantic), Mecha (robot-focused), and Slice of Life (realistic)."]),
    (r"quit", ["Goodbye!", "See you later!", "Happy watching!"])
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm your anime chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(response)

chat()
