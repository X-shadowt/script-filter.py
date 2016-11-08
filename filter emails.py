def instruction():
                       print(" ############################################# ")
                       print(" #               instructions                # ")
                       print(" #    tap your name file of your mailist     # ")
                       print(" #    after tap domain want to filtred gmail # ")
                       print(" #          or outlook or live or hotmail    # ")
                       print(" ############################################# ")
instruction()                       
def Main():      

    
 try:
              
  filemailist =input('Name of file:') 
  filemailist = open(filemailist,'r')
  domaine = input("choice which domain want you to filtred gmail or live or outlook or hotmail :")
  if "gmail"== domaine:
      print("[+]Plz wait until the program start[+]")
  elif "live" == domaine:
      print("[+]Plz wait until the program start[+]")
  elif "outlook" == domaine :
      print("[+]Plz wait until the program start[+]")
  elif "hotmail" == domaine :
      print("[+]Plz wait until the program start[+]")
  
      
  for emails in filemailist :
   
    if "@gmail" in emails and domaine == "gmail" :
        print(emails,end='')
        
        
    elif "@live" in emails and domaine == "live" :
        print(emails,end='')
        
    elif "@outlook" in emails and domaine == "outlook":
        print(emails,end='')
    elif "@hotmail" in emails and domaine == "hotmail":
        print(emails,end='')
    
    

  if domaine == "live"  :
        print("\n[+]mailist filtred [+]")
  elif domaine == "outlook" :
        print("\n[+]mailist filtred [+]")
  elif domaine == "gmail":
        print("\n[+]mailist filtred [+]")
  elif domaine == "hotmail":
        print("\n[+]mailist filtred [+]")

 
  else :
    
        print ("[!] sorry domaine you entred wrong try again[!]")
        Main()       
        
        
    
            
        
        
 except:
     
    print("[!]the file you entred not found try again[!]")
    Main()

 finally:
     input('')

 

     
Main()     





    

