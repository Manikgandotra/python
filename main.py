from spy_details import spy, friends, chats
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import Spy, ChatMessage, friend
import csv
from termcolor import colored

print( colored('Helo \nlet\'s get started','cyan', attrs=['dark','bold']))


def load_friends():
    with open('friends.csv','rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            spy = Spy(row[0],row[1],row[2],row[3])

            friends.append(spy)


load_friends()

def load_chats():
    with open('chats.csv','rb') as chats_data:
        reader = csv.reader(chats_data)

        for row in reader:
            cm = ChatMessage(row[0],row[1])
            chats.append(cm)

load_chats()

def load_history():
    with open('history.csv','rb') as history_data:
        reader = csv.reader(history_data)
        for row in reader:

            history.append(load_chats())

load_history()

STATUS_MESSAGES = ['URGENT CALL ONLY','CAN\'T TALK SC ONLY','SLEEPING','BUSY']

def add_status(c_s_m):
    if c_s_m != None:
        print 'your current status is: ' + c_s_m
    else:
        print'You don\'t have any status currently'
        user_choice = raw_input('DO YOU WANT TO SELECT FROM OLD STATUS? Y or N: ')

    if user_choice.upper() == 'Y':
        serial_no = 1
        for old_status in STATUS_MESSAGES:
            print str(serial_no) + '.' + old_status
            serial_no =serial_no +1
        user_status_selection = input('WHICH ONE DO YOY WANT TO SET THIS TIME?')
        new_status = STATUS_MESSAGES[user_status_selection-1]

    elif user_choice.upper() == 'N':
      new_status = raw_input('WRITE YOUR STATUS: ')
      STATUS_MESSAGES.append(new_status)
    else:
        print "INVALID ENTRY"
    return new_status

def add_friends():

    frnd = Spy(' ',' ',0,0.0)
    frnd.name = raw_input('WRITE YOUR FRND\'S NAME :')
    frnd_sal = raw_input('Mr. or Ms. :')
    frnd.name = frnd_sal + ' ' +frnd.name
    frnd.age = input('WRITE THE AGE OF FRND:')
    frnd.rating = input('write the rating of frnd:')
    frnd.is_online = True

    if len(frnd.name)>2 and 50>frnd.age>12 and  frnd.rating >= spy.rating:
        friends.append(frnd)
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([frnd.name,frnd.age,frnd.rating,frnd.is_online])


    else:
        print 'frnd with these values can not be a0dded'


    return len(friends)
def select_frnd():
    serial_no = 1
    for frnd in friends:
        print  str(serial_no) +' '+ frnd.name
        serial_no = serial_no + 1
    user_selected_frnd = input("WHICH ONE YOU WANT TO SEND OR READ MESSAGE FROM ? ")
    user_index = friends[user_selected_frnd - 1]
    return user_index

def send_message():
    selected_frnd = select_frnd()
    message =raw_input('WHAT IS YOUR SECRET MESSAGE ?')
    original_image = raw_input('WHAT IS THE NAME OF YOUR IMG ?')
    output_path = 'output.jpg'
    Steganography.encode(original_image,output_path,message)
    new_chat = ChatMessage('message','sent_by_me')
    friends.append(new_chat)
    print 'MESSAGE ENCRYPTED'
    with open('chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow(message)

def read_message():
    chosen_frnd = select_frnd()
    output_path = raw_input('NAME OF IMAGE TO BE DECOTED:')
    secret_text = Steganography.decode(output_path)
    print 'THE SECRET MESSAGE IS :- '
    print ( colored(secret_text,'red'))
    new_chat = (secret_text.upper()).split()
    with open('chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow(secret_text)

def Chat_History():
    Chat = select_frnd()
    print '\n'
    for chat in friend.chat:
        if chat.sent_by_me:
            print '[%s]  %s' %('you said:', chat.message)
        else:
            print '[%s]  %s' %(friend.name,chat.message)

def start_chat(spy_name,spy_age,spy_rating):

    current_status_message = None
    show_menu = True
    while show_menu:
         menu_choice = input('WHAT DO YOU WANT TO DO ? \n 1.Add a Status \n 2.Add a friend \n 3. Send a message \n 4. Read A Message \n 5. Your talks \n 0. Exit \n')
         if menu_choice == 1:
              user_status_message = add_status(current_status_message)
              print 'YOUR NEW STATUS IS UPDATED TO' + str(user_status_message)
         elif menu_choice ==2:
             no_of_frnds = add_friends()
             print 'I have ' + str(no_of_frnds) +' friends'
         elif menu_choice == 3:
             send_message()
         elif menu_choice == 4:
             read_message()
         elif menu_choice ==5:
             Chat_History()
         elif menu_choice ==0:
             show_menu = False
         else:
             print 'Invalid choice'

def question():
    Question = raw_input('ARE YOU A NEW USER? Y or N:')
    if Question.upper()== 'N':

        login = raw_input('FOR SPYCHAT YOU MUST LOGIN \nUSERNAME PLZ:')
        print 'HELLO'+' '+ login +' Lets talk secretly'

        start_chat(spy.name, spy.age, spy.rating)


    elif Question.upper()=='Y':

        spy.name = raw_input('What should i call you')
        if len(spy.name)>3:
            print'Welcome'+ spy.name +' Glad to meet you'
            spy_salutation = raw_input('what shoula i call you ? Mr. or Ms.')
            spy.name = spy_salutation + spy.name
            print 'Alright' + spy.name + ' I\'d like to know more about you'
            spy.age = input('What is your age')
            if spy.age>12 and spy.age<55:
                print 'Spy, your age is prefect'
                spy.rating=input('what is your rating')
                if spy.rating>=5.0:
                    print 'Great Spy'
                elif spy.rating<5.0 and spy.rating>=4.5:
                    print 'Nice Spy'
                elif spy.rating<4.5 and spy.rating>=3.5:
                    print 'Fine Spy'
                else:
                    print 'Useless Spy'
                spy_is_online=True
                print 'Authentication completed. Welcome ' + spy.name + 'Age:-' + str(spy.age) + ' and Rating :- ' + str(spy.rating) + ' Proud to have you onboard '+ 'Your Username is :-' + spy.name

                start_chat(spy.name,spy.age,spy.rating)

            else:
                print 'your age is not vaild to be spy'

        else:
            print 'plz enter a valid name'
    else:
        print'Invalid entry'
        question()





Question = raw_input('ARE YOU A NEW USER? Y or N:')
if Question.upper()== 'N':
    login = raw_input('FOR SPYCHAT YOU MUST LOGIN \nUSERNAME PLZ:')
    print 'HELLO '+ login +' Lets talk secretly'
    start_chat(spy.name,spy.age,spy.rating)
elif Question.upper()=='Y':
  spy.name = raw_input('What should i call you')
  if len(spy.name)>3:
      print 'Welcome'+ spy.name +' Glad to meet you'
      spy_salutation = raw_input('what shoula i call you ? Mr. or Ms. ')
      spy.name = spy_salutation + spy.name
      print 'Alright ' + spy.name + ' I\'d like to know more about you'
      spy.age = input('What is your age')
      if spy.age>12 and spy.age<55:
          print 'Spy, your age is prefect'
          spy.rating=input('what is your rating')
          if spy.rating>=5.0:
              print 'Great Spy'
          elif spy.rating<5.0 and spy.rating>=4.5:
              print 'Nice Spy'
          elif spy.rating<4.5 and spy.rating>=3.5:
              print 'Fine Spy'
          else:
              print 'Useless Spy'
          spy_is_online=True
          print 'Authentication completed. Welcome '+ spy.name +' Age:-' + str(spy.age) + ' and Rating :- ' + str(spy.rating) + ' Proud to have you onboard '+' Your Username is:- '+ spy.name
          start_chat(spy.name,spy.age,spy.rating)

      else:
          print 'your age is not vaild to be spy'

  else:
      print 'plz enter a valid name'
else:
    print'Invalid entry'
    question()




