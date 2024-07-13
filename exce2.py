import sys
randomlist=['a',0,2]
for entry in randomlist:
    try:
        print("entry = ",entry)
        r=1/entry
       
    except ZeroDivisionError:
       # print("error = ",sys.exc_info()[0])
        print("zero entry")
        print()
    except ValueError:
        #print("error = ",sys.exc_info()[0])
        print("value entry")
        print()
    except:
        print("error occured")
    else:
        print("No error")
    finally:
        print("This code is cumplsory")

print("bye")