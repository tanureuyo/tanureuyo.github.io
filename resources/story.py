def wakeUp():
    sleep = input('After enjoying a long slumber, do you wakeup early? (Yes or No) ')
    if sleep == 'Yes' or sleep == 'yes':
        print ('You have chosen to wakeup early.')
        goEarly()
    elif sleep == 'No' or sleep == 'no':
        print ('You have chosen to not wakeup early.')
        goLate()
    else:
        print ('Please type Yes or No.')
        wakeUp()
        
def goEarly():
    school = input('As you have awaken early, do you chose to also go to school early? (Yes or No) ')
    if school == 'Yes' or school == 'yes':
        print ('You did go to school early.')
        studyTest()
    elif school == 'No' or school == 'no':
        print ('You went to school on time.')
        sleepClass()
    else:
        print ('Please type Yes or No.')
        goEarly()

def studyTest():
    study = input('The bio final is today. Would you like to study? (Yes or No) ')
    if study == 'Yes' or study == 'yes':
        print ('You get a good grade.')
    elif study == 'No' or study =='no':
        print ('You fail the test.')
    else:
        print ('Please type Yes or No.')
        studyTest()

def sleepClass():
    sleepClass = input('You are tired. Do you want to take a nap in class? (Yes or No) ')
    if sleepClass == 'Yes' or sleepClass == 'yes':
        print ('You are getting sent to detention where you will eventually die.')
    elif sleepClass == 'No' or sleepClass == 'no':
        print ('You will understand and remember the lesson.')
    else:
        print ('Please type Yes or No')
        sleepClass()

def goLate():
    go = input('You arive at school a tad late. Do you try to get to class on time? (Yes or No) ')
    if go == 'Yes' or go == 'yes':
        print ('You made it to class still! But you are so tired that you might fall asleep.')
        sleepClass()
    elif go == 'No' or go == 'no':
        print ('You arrive at the office.')
        stayGo()
    else:
        print ('Please type Yes or No')
        goLate()
        
def stayGo():
    stayGo = input('Do you feel like attending class? (Yes or No) ')
    if stayGo == 'Yes' or stayGo == 'yes':
        print ('You make your way to class.')
    elif stayGo == 'No' or stayGo == 'no':
        print ('You will stay inside the office.')
    else:
        print ('Please type Yes or No')
        stayGo()
        
wakeUp()

    
    
    
    
    