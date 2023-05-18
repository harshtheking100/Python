a=int(input("Enter No1 : "))
b=int(input("Enter No2 : "))
print(a/b)


try:
    a=int(input("Enter No1 : "))
    b=int(input("Enter No2 : "))
    print(a/b)
except:
    print("Error occured")






try:
    a=int(input("Enter No1 : "))
    b=int(input("Enter No2 : "))
    try:
        print(a/b)
    except:
        print("Zero Division")
except:
    print(" Wrong input ")
    
    

try:
    a=int(input("Enter No1 : "))
    b=int(input("Enter No2 : "))
    print(a/b)
except ValueError:
    print("Enter valid Input")
except ZeroDivisionError:
    print("Zero Division")
    
    
    
try:
    a=int(input("Enter No1 : "))
    b=int(input("Enter No2 : "))
    print(a/b)
except Exception as e:
    print("Error occured " ,e)
 
    
try:
    a=int(input("Enter No1 : "))
    b=int(input("Enter No2 : "))
    print(a/b)
except (ValueError, ZeroDivisionError,TypeError) as e:
    print("Error : ",e)
except Exception as e:
    print("Generic: ",e)
    
    
    
try:
    a=int(input("Enter No1 : "))
    b=int(input("Enter No2 : "))
    print(a/b)
except (ValueError, ZeroDivisionError,TypeError) as e:
    print("Error : ",e)
except Exception as e:
    print("Generic: ",e)
else:
    print("Done without error")



while(1):
    try:
        age=int(input("Enter Age"))
        if age <18:
            print("You can not vote")
        else:
            print("You can vote")
            
    except:
        print("Wrong input. Enter valid age Value. ")
    else:
        break


lst=[1,2,3,4,5,6]
while(1):
    try:
        index=int(input("Enter index"))
        print(lst[index])
            
    except:
        print("Wrong input. Enter valid index Value. ")
    else:
        break
    
    
lst=[1,2,3,4,5,6]
while(1):
    try:
        index=int(input("Enter index"))
        print(lst[index])
            
    except:
        print("Wrong input. Enter valid index Value. ")
    else:
        print("Else Executed")
        break
    
    finally:
        print("I will be always executed")
        print(lst)
        
        
        
try:
    print("in try")
except Exception as e:
    print(e)
else:
    print("No Error")
finally:
    print(" I am always executed")  
    




age=int(input("Enter Age"))
if age <18:
    raise Exception ("You can not vote")
else:
    print("You can vote")
print("Done with Task")
    



try:
    age=int(input("Enter Age"))
    if age <18:
        raise Exception ("You can not vote")
    else:
        print("You can vote")
      
except:
    print("Wrong input. Enter valid age Value. ")
print("Done ")




try:
    age=int(input("Enter Age"))
    if age <18:
        raise Exception ("You can not vote")
    else:
        print("You can vote")
      
except Exception as e:
    print("Wrong input. Enter valid age Value. ", e)
print("Done ")


class InvalidAge(Exception):
    pass

try:
    age=int(input("Enter Age"))
    if age <18:
        raise InvalidAge("You can not vote")
    else:
        print("You can vote")
      
except Exception as e:
    print("Wrong input. Enter valid age Value. ", e)
print("Done ")
      

    
class InvalidAge(Exception):
    def __init__(self,no=0,name="Error occured"):
        self.erno=no
        self.msg= name
    
    def __str__(self):
        return f"error code{self.erno} and msg:{self.msg}"

try:
    age=int(input("Enter Age"))
    if age <18:
        raise InvalidAge(789,"You can not vote")
    else:
        print("You can vote")
      
except InvalidAge as e:
    print("Wrong input.", e)
print("Done ")