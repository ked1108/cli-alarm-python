from playsound import playsound
import datetime

def alarm():
    time = str(input("Enter The Time(hh:mm:ss):\t"))+".000000"


    stop = False

    while not stop:
        rn = str(datetime.datetime.now().time())

        if rn >= time:
            stop = True
            playsound('alarm.mp3')
            snooze(60)
    
def snooze(time):
    stop_time = str(datetime.datetime.now().time())
    
    while True:
        rn = str(datetime.datetime.now().time())

        if stop_time >= rn:
            quit()

    

def timer():
    time = str(input("Enter The Time(hh:mm:ss):\t"))+".000000"

    stop_time = str(datetime.datetime.now().time())

    stop = False

    while not stop:

        rn = str(datetime.datetime.now().time())

        if rn >= stop_time:
            stop = True
            playsound('alarm.mp3')
            snooze(60)
    

def main():
    print("***********************", end="\n\n\n")
    print("Welcome To Timer!")
    print("What Do You Want To Do:")
    print("\t1.)Set Alarm:")
    print("\t2.)Set Timer:")
    print("\n\n***********************")
    try:
        choice = int(input("Enter Your Choice:\t"))
    
    except ValueError:
        print("Illegal Input, Try Again")
        main()
    
    if choice == 1:
        alarm()

    elif choice == 2:
        timer()

    else:
        print("Illegal Input, Try Again")
        main()

if __name__ == '__main__':
    main()
