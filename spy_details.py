from datetime import datetime

class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


spy = Spy('manik','Mr.', 21,5.5 ,)


friend_one = Spy('Pranav','Mr', 20,6.5)
friend_two = Spy('Harsh','Mr', 20,7.5)
friend_three= Spy('Akshay','Mr', 20,9.5)
friend_four = Spy('Satyam','Mr', 19,5.9)



friends=[friend_one,friend_two,friend_three,friend_four]

class ChatMessage:
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time =datetime.now()
        self.sent_by_me = sent_by_me

cm = ChatMessage('message','sent_by_me')

chats_one =  ChatMessage('message','sent_by_me')
chats_two = ChatMessage('message ','sent_by_me')
chats_three = ChatMessage('message','sent_by_me')
chats_four= ChatMessage('message','sent_by_me')


chats = [chats_one,chats_two,chats_three,chats_four]