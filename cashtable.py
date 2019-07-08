import time
import threading

dataArr=[]
timeArr=[]
boolArr=[]
class MyThread(threading.Thread):
    """this class inherit from threading.Thread class
    it's important for creating threads which will expire the values
    """
    def run(self):
        """In this fun we will overwrite the one in the super class
        """
        i= len(dataArr)-1
        time.sleep(timeArr[i])
        boolArr[i]=False

def addCash(v,t):
    """Add cash values to the table.
    Arguments:
        v {str} -- the value which will be stored
        t {int} -- the time after which the value will be expired
    """
    dataArr.append(v)
    timeArr.append(t)
    boolArr.append(True)
    thr = MyThread()
    thr.start()
def CheckCash(data):
    """Check for the value if it still exist or expired or doesn't exist att all
    Arguments:
        data {str} -- the value you want to check
    Returns:
        str -- returns a string which told us if it still exist or expired or doesn't exist att all
    """
    if data in dataArr:
        if boolArr[dataArr.index(data)]:
            return "item  exist "
        else:
            return "item expired"
    else:
        return "item not exist"
if __name__ == '__main__':
    while True:
        i = int(input("please choose one \n1. enter new val \n2. check for old val \n3. exit"))
        if i == 1:
            addCash(input("enter a value"), float(input("enter time")))
        elif i == 2:
            data = input("enter a value")
            print(CheckCash(data))

        elif i == 3:
            break
        else:
            print("pls try again")

