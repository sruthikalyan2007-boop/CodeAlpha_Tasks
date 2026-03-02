import re
import random
import datetime

class SimpleChatbot:
    def __init__(self):
        self.memory = {}
        print("Bot: Hi! I'm PyBot. I can do math, tell time, and chat. Type 'bye' to exit.")

    def get_response(self, text):
        text = text.lower()
        
        # Feature 1: Greeting & Farewell
        if re.search(r'\b(hi|hello|hey)\b', text):
            return random.choice(["Hello!", "Hi there!", "Greetings human!"])
        if re.search(r'\b(bye|quit|exit)\b', text):
            return "QUIT"

        # Feature 2: Time & Date Check
        if "time" in text:
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
        if "date" in text:
            return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}."

        # Feature 3: Simple Math Calculator (e.g., "calc 5 + 5")
        math_match = re.search(r'calc (.*)', text)
        if math_match:
            try:
                # Security note: eval is used for brevity in this simple 50-line example
                return f"Result: {eval(math_match.group(1))}"
            except:
                return "I couldn't calculate that. Try 'calc 2 + 2'."

        # Feature 4: Basic Memory (Remembering Name)
        name_match = re.search(r'my name is (\w+)', text)
        if name_match:
            self.memory['name'] = name_match.group(1)
            return f"Nice to meet you, {self.memory['name']}!"
        if "what is my name" and "tell my name" in text:
            return f"Your name is {self.memory.get('name', 'unknown to me')}."
        
        #Feature 5 : Sentiment Detection
        sad_words=["sad","upset","depressed","unhappy"]
        happy_words=["happy","excited","great","awesome"]
        stress_words=["stressed","tired","pressure","worried"]
        angry_words=["angry","mad","frustrated"]
        if any(word in text for word in sad_words):
            self.memory['mood']="sad"
            return "I'm sorry you're feeling sad.Remember , tough times dont last ."
        if any(word in text for word in happy_words):
            self.memory['mood']="happy"
            return "That's amazing!! Keep spreading the positivity!"
        if any(word in text for word in stress_words):
            self.memory['mood']="stressed"
            return "Take a deep breath you've handled tough things before you got this!"
        if any(word in text for word in angry_words):
            self.memory['mood']="angry"
            return "Its ok to feel angry . Try stepping away for a moment and relax"

        # Feature 5: Random Fallback Responses
        return random.choice([
            "That's interesting! Tell me more.",
            "I'm not sure I understand, but I'm learning.",
            "Can you rephrase that?",
            "I am just a simple Python script, be nice!"
        ])

if __name__ == "__main__":
    bot = SimpleChatbot()
    while True:
        try:
            user_input = input("You: ")
            if not user_input: continue
            response = bot.get_response(user_input)
            if response == "QUIT":
                print("Bot: Goodbye!")
                break
            print(f"Bot: {response}")
        except KeyboardInterrupt:
            break
