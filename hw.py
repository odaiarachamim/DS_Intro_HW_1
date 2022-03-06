#203660709
############## TASKS A ############
def my_func(x1, x2, x3):
#arr is list of parameters and another varieble is the calculte of denominator 
#chack all parameters should be float numbers, otherwise – print 
        arr=[x1,x2,x3]
        for i in range (0,len(arr)):
           if isinstance(arr[i],float)==False:
               print( "Error: parameters should be float")
               return""
        denominator= x1+x2+x3
#chack if the denominator is zero the function return text
        if denominator==0:
            return "Not a number – denominator equals zero"
#the function return a float number 
        return(((denominator)*(x2+x3)*x3)/(denominator))
############## TASKS B ############
import math 
def convert(hours,minutes):
#The function can accept float or int
    if not(isinstance(hours,int) or isinstance(hours,float)) and (isinstance(minutes,int) or isinstance(minutes,float)):
        print("hours and minutes should be integer or float")
        return ""
    #validate that the input is not positive and printing arror.
    if hours<0 or minutes<0:
        print("Input error!")
        return ""
    return (hours*60*60+minutes*60) 
#The function can accept float and split to minutes and hours
    if isinstance(hours, float)==True:
         r= math.modf(hours)
         hours=float(r[1])
         minutes+=float(r[0])*60
    hours=hours*3600.0
    minutes= minutes*60.0
    return(hours+minutes)
