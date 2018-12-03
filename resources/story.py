#Install colorama
#This is a short story using definitions
from colorama import init, Fore, Back, Style
init(autoreset=True)

def wakeUp():
    sleep = input('After enjoying a long slumber, do you wakeup early? (Yes or No) ')
    if sleep == 'Yes' or sleep == 'yes':
        print (Fore.GREEN + 'You have chosen to wakeup early.')
        goEarly()
    elif sleep == 'No' or sleep == 'no':
        print (Fore.GREEN + 'You have chosen to not wakeup early.')
        goLate()
    else:
        print (Fore.RED + 'Please type Yes or No.')
        wakeUp()
        
def goEarly():
    school = input('As you have awaken early, do you choose to also go to school early? (Yes or No) ')
    if school == 'Yes' or school == 'yes':
        print (Fore.GREEN + 'You did go to school early.')
        studyTest()
    elif school == 'No' or school == 'no':
        print (Fore.GREEN + 'You went to school on time.')
        sleepClass()
    else:
        print (Fore.RED + 'Please type Yes or No.')
        goEarly()

def studyTest():
    study = input('The bio final is today. Would you like to study? (Yes or No) ')
    if study == 'Yes' or study == 'yes':
        print (Fore.GREEN + 'You get a good grade.')
    elif study == 'No' or study =='no':
        print (Fore.GREEN + 'You fail the test.')
    else:
        print (Fore.RED + 'Please type Yes or No.')
        studyTest()

def sleepClass():
    sleep2 = input('You are tired. Do you want to take a nap in class? (Yes or No) ')
    if sleep2 == 'Yes' or sleep2 == 'yes':
        print (Fore.GREEN + 'You are getting sent to detention where you will eventually die.')
    elif sleep2 == 'No' or sleep2 == 'no':
        print (Fore.GREEN + 'You will understand and remember the lesson.')
    else:
        print (Fore.RED + 'Please type Yes or No.')
        sleepClass()

def goLate():
    go = input('You arive at school a tad late. Do you try to get to class on time? (Yes or No) ')
    if go == 'Yes' or go == 'yes':
        print (Fore.GREEN + 'You made it to class still! But you are so tired that you might fall asleep.')
        sleepClass()
    elif go == 'No' or go == 'no':
        print (Fore.GREEN + 'You arrive at the office.')
        stayGo()
    else:
        print (Fore.RED + 'Please type Yes or No.')
        goLate()
        
def stayGo():
    stay = input('Do you feel like attending class? (Yes or No) ')
    if stay == 'Yes' or stay == 'yes':
        print (Fore.GREEN + 'You make your way to class.')
    elif stay == 'No' or stay == 'no':
        print (Fore.GREEN + 'You will stay inside the office.')
    else:
        print (Fore.RED + 'Please type Yes or No.')
        stayGo()

wakeUp()
input('')
    
    
    
    
    