# Tasks ko store karne ke liye list (Global scope mein)
tasks = []

# Infinite loop jo program ko tab tak chalata rahega jab tak user exit na kare
while True:
    # 1. Menu display karna
    print("\n" + "="*20)
    print("    TO-DO LIST")
    print("="*20)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("="*20)
    
    # User se choice input lena
    choice = input("\nApni choice select karein (1-4): ").strip()
    
    # ---- 2. CHOICE 1: VIEW TASKS ----
    if choice == "1":
        # Check karna ke list khali to nahi hai
        if len(tasks) == 0:
            print("\n ⚠️   Aapki list abhi khali hai!")
        else:
            print("\nAapke Tasks:")
            # enumerate() loop ke sath index (1, 2, 3...) bhi generate karta hai
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
                
    # ---- 3. CHOICE 2: ADD TASK ----
    elif choice == "2":
        new_task = input("\nNaya task enter karein: ").strip() # strip() faltu spaces khatam karta hai
        
        # Check karna ke input khali to nahi hai
        if new_task != "":
            tasks.append(new_task) # List ke end mein task add karna
            print(f"✔️ '{new_task}' list mein add ho gaya hai!")
        else:
            print("❌ Task khali nahi ho sakta!")
            
    # ---- 4. CHOICE 3: DELETE TASK ----
    elif choice == "3":
        # Pehle check karo ke delete karne ke liye kuch hai ya nahi
        if len(tasks) == 0:
            print("\n⚠️ Delete karne ke liye koi task nahi hai!")
        else:
            print("\nAapke Tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
                
            # try-except block taake agar user number ke bajaye text likhe to crash na ho
            try:
                task_num = int(input("\nKaun sa task delete karna hai? (Number likhein): "))
                
                # Check karna ke entered number tasks list ki limit ke andar hai
                if 1 <= task_num <= len(tasks):
                    # Python index 0 se shuru karta hai, isliye task_num - 1 kiya
                    removed = tasks.pop(task_num - 1)
                    print(f"🗑️ '{removed}' delete kar diya gaya hai.")
                else:
                    print("❌ Invalid task number!")
            except ValueError:
                print("❌ ERROR: Plz sirf number enter karein!")
                
    # ---- 5. CHOICE 4: EXIT ----
    elif choice == "4":
        print("\n👋 Alvida! Apna khayal rakhiyega.")
        break # Loop ko break karke program se exit kar dega
        
    # ---- INVALID INPUT HANDLING ----
    else:
        print("❌ Invalid Choice! Plz 1 se 4 ke darmiyan koi number choose karein.")