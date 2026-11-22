import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "I am" : "You are",
    "I was" : "You were",
    "I" : "You",
    "I'm" : "You are",
    "I'd" : "You would",
    "I've" : "You have",
    "I'll" : "You will",
    "My" : "Your",
    "You are" : "I am",
    "You were" : "I was",
    "You" : "I",
    "You are" : "I'm",
    "You would" : "I'd",
    "You have" : "I've",
    "You will" : "I'll",
    "Your" : "My",
    "Yours" : "Mine",
    "You" : "Me",
    "Me" : "You"
}

pairs = [
    [
        r"My name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"Hi|Hey|Hello",
        ["Hello", "Hey",]
    ],
    [
        r"What is your name?",
        ["I am a bot created by Codingal Edu. You can call me Jarvis",]
    ],
    [
        r"How are you?",
        ["I am doing good, how about you?",]
    ],
    [
        r"I am fine.",
        ["That's great to hear. How can I help you today?",]
    ],
    [
        r"I'm doing good.",
        ["That's great to hear. How can I help you today?",]
    ],
    [
        r"Who (.*) (moviestar|actor)?",
        ["Benedict Cumberbatch"]
    ],
    [
        r"I am looking for online guides and courses to learn data science, can you suggest?",
        ["Jarvis_Tech has many great articles with step explanations along with code, you can explore."]
    ],
    [
        r"quit",
        ["Bye, take care, see you soon", "It was great talking to you, see you soon"]
    ],
]

def chat():
    print("Hi! I am a chatbot created by Codingal Edu")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chat()