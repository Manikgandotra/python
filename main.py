from spy_details import spy_name,spy_age,spy_rating
print'helo'
print'let\'s get started'

STATUS_MESSAGES = ['URGENT CALL ONLY','CAN\'T TALK SC ONLY']

def add_status(c_s_m):
    if c_s_m != None:
        print 'your current status is: ' + c_s_m
    else:
        print'You don\'t have any status currently'
        user_choice = raw_input('DO YOY WANT TO SELECT FROM OLD STATUS? Y or N: ')

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

def start_chat(spy_name,spy_age,spy_rating) :
    current_status_message = None
    show_menu = True
    while show_menu:
         menu_choice = input('WHAT DO YOU WANT TO DO ? \n 1.Add a Status \n 2.Add a friend \n 0. Exit \n')
         if menu_choice == 1:
              updated_status_message = add_status(current_status_message)
              print 'YOUR NEW STATUS IS UPDATED TO' + updated_status_message
         elif menu_choice ==2:
             print 'will add a friend'
         elif menu_choice ==0:
             show_menu = False
         else:
             print 'Invalid choice'


question = raw_input('ARE YOU A NEW USER? Y or N:')
if question.upper()== 'N':
    print'we al ready have your detail'
    start_chat(spy_name,spy_age,spy_rating)

elif question.upper()=='Y':
    spy_name = raw_input('What should i call you')
    if len(spy_name)>3:
        print'Welcome'+ spy_name +' Glad to meet you'
        spy_salutation = raw_input('what shoula i call you ? Mr. or Ms.')
        spy_name = spy_salutation + spy_name
        print 'Alright' + spy_name + ' I\'d like to know more about you'
        spy_age=0
        spy_rating=0.0
        spy_is_online=False
        spy_age = input('What is your age')
        if spy_age>12 and spy_age<55:
            print 'Spy, your age is prefect'
            spy_rating=input('what is your rating')
            if spy_rating>=5.0:
                print 'Great Spy'
            elif spy_rating<5.0 and spy_rating>=4.5:
                print 'Nice Spy'
            elif spy_rating<4.5 and spy_rating>=3.5:
                print 'Fine Spy'
            else:
                print 'Useless Spy'
            spy_is_online=True
            print 'Authentication complete. Welcome '+ spy_name + 'age:' + str(spy_age) + ' and rating of:' + str(spy_rating) + ' Proud to have you onboard'

            start_chat(spy_name,spy_age,spy_rating)

        else:
            print 'your age is not vaild to be spy'
    else:
        print 'plz enter a valid name'
else:
    print'Invalid entry'