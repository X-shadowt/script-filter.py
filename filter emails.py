def instruction():
                       print(" ############################################# ")
                       print(" #               instructions                # ")
                       print(" #    tap your name file of your mailist     # ")
                       print(" #    after tap domain want to filtred gmail # ")
                       print(" #           or outlook or live              # ")
                       print(" ############################################# ")
instruction()                       
def Main():      

    
 try:
              
  filemailist =input('Name of file:') 
  filemailist = open(filemailist,'r')
  domaine = input("choice which domain want you to filtred gmail or live or outlook:")
  for emails in filemailist :
   
    if "@gmail" in emails and domaine == "gmail" :
        print(emails,end='')
        
    elif "@live" in emails and domaine == "live" :
        print(emails,end='')
    elif "@outlook" in emails and domaine == "outlook":
        print(emails,end='')
    else:      
        ("sorry try again you didn't enter the right domaine")
        
        
        
 
     

 
           
 

 except:
     
    print("[!]the file you entred not found try again[!]")
    Main()

 finally:
     print("\n[+]mailist filtred [+]")
     input('')
     

Main()     

 




    

