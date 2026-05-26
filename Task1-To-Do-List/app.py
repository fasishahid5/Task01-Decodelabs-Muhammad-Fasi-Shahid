import json

try: 
    with open("tasks.json","r")as file:
     tasks=json.load(file)
except:
   tasks=[]

def save_tasks():
   with open("tasks.json","w")as file:
      json.dump(tasks,file)

def fix_ids():
   for i ,task in enumerate(tasks):
      task["id"]=i+1


while True:
   print("\n--- To-Do List---")
   print("1. Add Task")
   print("2. View Task")
   print("3. Update Task")
   print("4. Delete Task")
   print("5. Mark Completed")
   print("6. Search Task")
   print("7. Filter Tasks")
   print("8. Exit")

   choice=int(input("Entwer your Choice according to the given number:"))

   if choice==1:
      name=input("Enter task name:")

      task={
         "id":len(tasks)+1,
         "name":name,
         "status":"pending"
      }

      tasks.append(task)
      save_tasks()
      print("Task added Succesfully!")

   elif choice==2:
      if not tasks:
         print("No task found")

      else:
         print("\nYour tasks:")
         for task in tasks:
            print(task["id"],"-",task["name"],"--",task["status"])

   elif choice==3:
      id_to_update=int(input("Enter task Id :"))

      for task in tasks:
         if task["id"]==id_to_update:
            new_name=input("Enter new task:")
            task["name"]=new_name
            save_tasks()
            print("Task Updated!")
            break
      else:
            print("Task not found!")

   elif choice==4:
      id_to_deleted=int(input("Enter task Id :"))  
      for task in tasks:
         if task["id"]==id_to_deleted:
            tasks.remove(task)
            fix_ids()
            save_tasks()
            print("Task deleted succesfully!")
            break
      else:
            print("Task not found!")

   elif choice==5:
       id_to_complete = int(input("Enter task ID: "))

       for task in tasks:
          if task["id"]==id_to_complete:
             task["status"]="completed"
             save_tasks()
             print("Task marked as completed!")
             break
       else:
             print("Task not found")

   elif choice==6:
      keyword=input("Enter keyword to search: ")
     
      found=False
      for task in tasks:
         if keyword.lower() in task["name"].lower():
            print(task["id"],"-",task["name"],"--",task["status"])
            found =True

      if not found:
         print("No matching task found!")
   
   elif choice==7:
      status=input("Enter staus (pending/completed): ").lower()
      if status not in ["pending","completed"]:
         print("Invalid status!")
      else:    
          for task in tasks:
            if task["status"]==status:
              print(task["id"],"-",task["name"])

   elif choice==8:
      break
   
   else:
      print("Invalid choice!")

      
          
      
