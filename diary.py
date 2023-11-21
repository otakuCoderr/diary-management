from datetime import *

def add():    
    dat = datetime.now()
    path = f'entries/entry{str(dat.date())}.txt'
    with open(path,'a') as diary:
        nowDate =  dat.isoformat(' ','minutes')
        print('Date and time written. Continue writing your diary. If nothing written, this will be removed and program will stop')
        today = input("What interesting things happened today?: ")
        if today != '':
            diary.write(nowDate+'\n\t'+today+'\n---')
        else:
            print("No inputs given. Closing the program...")


