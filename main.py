# Defining the base class for the Chatbot
class Chatbot:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def introduce(self):
        return f"Hello! I am {self.name}, a chatbot powered by version {self.version}. How can I assist you today?"

# Inheriting the base Chatbot class to add more specific functionalities
class CustomChatbot(Chatbot):
    def __init__(self, name, version, developer_name, purpose):
        super().__init__(name, version)
        self.developer_name = developer_name
        self.purpose = purpose

    def additional_info(self):
        return (f"I was developed by {self.developer_name}. "
                f"My main purpose is to {self.purpose}.")

# Instantiating the chatbot object
def main():
    # You can replace the attributes as per your requirement
    bot = CustomChatbot("Breezy", "1.0", "Thando", "assist with restaurant queries")
    print(bot.introduce())
    print(bot.additional_info())

# Running the program
if __name__ == "__main__":
    main()
