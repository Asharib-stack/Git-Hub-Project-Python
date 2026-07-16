task = []
while True:
    print ("\n"  + "="*20)
    print ("    TO-DO LIST")
    print ("="*20)
    print ("1) VIEW TASK")
    print ("2) ADD TASK")
    print ("3) DELETE TASK")
    print ("4) EXIT")
    print ("="*20)
   

    Choose = (input("\n Koi Bhi Task Choose Krne ke liye number Enter krien (1 se 4 tk): ")).strip()
    
    if Choose == "1":
        if len (task) == 0:
            print ("\n ⚠️ Apki ki list khali hy koi Tasks nahi hy Show krne ke liye")

        else:
            print ("\n Apka Task ye hy")

            for index, tasks in enumerate (task, 1):
                print (f"{index}. {tasks}")
    
    elif Choose == "2":
        new_task = input("Please apna new task enter krien: ").strip()

        if new_task != "":
            task.append(new_task)
            print (f" Apka {new_task} new task enter krdiya hy task list mien")

        else:
            print ("\n Khali Task enter nahi hota please task btien add krne ke liye")
    
    elif Choose == "3":

        if len (task) == 0:
            print ("\n ⚠️ Apki ki list khali hy koi Tasks nahi hy delete krne ke liye")

        else:
            print ("\n Apka Task ye hy")

            for index, tasks in enumerate (task, 1):
                print (f"{index}. {tasks}")

            try:
                task_num = int(input("\n Please select krien ismien se konsa task ap delete krna chahte hy (Number Btien): ").strip())

                if 1 <= task_num <= len(task):
                   removed = task.pop (task_num -1)
                   print ("\n 🗑️   Apka task remove krdiya hy")
                else:
                    print("❌ Invalid number! Sahi Number enter krien")
            except ValueError:
                print ("\n ❌ Please Only Number Enter krien")
    

    elif Choose == "4":
        print ("👋 Alvida Dost Dobara Milte hy")
        break

    else:
     print("❌ Invalid Choice! Plz 1 se 4 ke darmiyan koi number choose karein.")