print'helo'
print'let\'s get started'
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

    else:
        print 'your age is not vaild to be spy'
else:
    print 'plz enter a valid name'