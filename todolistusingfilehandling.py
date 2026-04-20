file = "todo.txt"

while True:
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    ch = input("Enter Choice: ")

    # Add Task
    if ch == "1":
        id = input("Enter Task ID: ")
        task = input("Enter Task Description: ")
        status = input("Enter Status (Pending/Completed): ")

        f = open(file, "a")
        f.write(id + "," + task + "," + status + "\n")
        f.close()

        print("Task Added")

    # View Task
    elif ch == "2":
        f = open(file, "r")
        data = f.readlines()
        f.close()

        print("\nTask List:")
        for i in data:
            x = i.strip().split(",")
            print("ID:", x[0], "Task:", x[1], "Status:", x[2])

    # Update Task
    elif ch == "3":
        uid = input("Enter Task ID to Update: ")

        f = open(file, "r")
        data = f.readlines()
        f.close()

        f = open(file, "w")

        for i in data:
            x = i.strip().split(",")

            if x[0] == uid:
                task = input("Enter New Task: ")
                status = input("Enter New Status: ")
                f.write(uid + "," + task + "," + status + "\n")
            else:
                f.write(i)

        f.close()
        print("Task Updated")

    # Delete Task
    elif ch == "4":
        did = input("Enter Task ID to Delete: ")

        f = open(file, "r")
        data = f.readlines()
        f.close()

        f = open(file, "w")

        for i in data:
            x = i.strip().split(",")

            if x[0] != did:
                f.write(i)

        f.close()
        print("Task Deleted")

    # Exit(end)
    elif ch == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")