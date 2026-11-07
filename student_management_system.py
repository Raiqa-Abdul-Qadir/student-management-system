# Initialize variable
students = []
attendance = []

# Function to display main menu and get user choice
def main_menu():
    while True:
        print("\nIIT Campus")
        print("\nMain Menu")
        print("1) Enroll a new student")
        print("2) View details of a student")
        print("3) View details of all the students according to the branch")
        print("4) Update student details")
        print("5) Mark attendance")
        print("6) View attendance")
        print("7) Exit")
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            enroll_student()
        elif choice == "2":
            view_student_details()
        elif choice == "3":
            view_students_by_branch()
        elif choice == "4":
            update_student_details()
        elif choice == "5":
            mark_attendance()
        elif choice == "6":
            view_attendance()
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to enroll a new student
def enroll_student():
    print("\nIIT Campus")
    print("\nEnroll a new student")
    

    while True:
        student_id = input("Student ID (9-digit number): ")
        if not (student_id.isdigit() and len(student_id) == 9):
            print("Invalid Student ID. It must be a 9-digit number.")
        else:
            break
        
    while True:
        nic = input("NIC (National Identity Card number - 10 characters): ").strip()
        if len(nic) != 10:
            print("Invalid NIC. It must be exactly 10 characters.")
        else:
            break

    while True:
        first_name = input("First Name (max 10 characters): ").strip()
        if len(first_name) > 10:
            print("Invalid First Name. It must not exceed 10 characters.")
        else:
            break

    while True:
        last_name = input("Last Name (max 15 characters): ").strip()
        if len(last_name) > 15:
            print("Invalid Last Name. It must not exceed 15 characters.")
        else:
            break
        
    birth_date = input("Birth Date (DD-MM-YYYY): ").strip()

    while True:
        permanent_address = input("Permanent Address (max 15 characters): ").strip()
        if len(permanent_address) > 15:
            print("Invalid Permanent Address. It must not exceed 15 characters.")
        else:
            break

    while True:
        phone_number = input("Phone Number (10 characters): ").strip()
        if not (phone_number.isdigit() and len(phone_number) == 10):
            print("Invalid Phone Number. It must be exactly 10 digits.")
        else:
            break
        
    tutorial_group = input("Tutorial Group: ").strip()
    
    centre = input("Centre: ").strip()
    
    # Store the student details in the database
    student = {
        'Student_ID': student_id,
        'NIC': nic,
        'First_Name': first_name,
        'Last_Name': last_name,
        'Birth_Date': birth_date,
        'Permanent_Address': permanent_address,
        'Phone_Number': phone_number,
        'Tutorial_Group': tutorial_group,
        'Centre': centre
    }
    
    # Save the student to the database (list)
    students.append(student)
    
    save_response = input("Do you want to save the details? (Yes/No): ").strip().lower()
    if save_response == "yes":
        print("Student enrolled successfully.")
    elif save_response == "no":
        print("Student details not saved.")
    else:
        print("Invalid response. Please enter Yes or No.")

# Function to view details of a student by ID
def view_student_details():
    print("\nIIT Campus")
    print("\nView details of a student")
    student_id = input("\nStudent ID: ").strip()
    
    # Search for the student in the database
    student = next((s for s in students if s['Student_ID'] == student_id), None)
    
    if student:
        print(f"NIC: {student['NIC']}")
        print(f"Phone Number: {student['Phone_Number']}")
        print(f"First Name: {student['First_Name']}")
        print(f"Last Name: {student['Last_Name']}")
        print(f"Tutorial Group: {student['Tutorial_Group']}")
        print(f"Centre: {student['Centre']}")
    else:
        print("Student not found.")
    
    view_another = input("Do you want to view another student’s details? (Yes/No): ").strip().lower()
    if view_another == "yes":
        view_student_details()
    elif view_another == "no":
        print("Exiting student details view.")
    else:
        print("Invalid response. Please enter Yes or No.")

# Function to view students by branch
def view_students_by_branch():
    print("\nIIT Campus")
    print("\nView details of all the students")
    branch_name = input("\nBranch Name: ").strip()
    
    # Filter students based on branch (Here we assume 'Centre' is the branch)
    students_in_branch = [s for s in students if s['Centre'] == branch_name]
    
    if students_in_branch:
        for student in students_in_branch:
            print(f"NIC: {student['NIC']} | Student ID: {student['Student_ID']} | First Name: {student['First_Name']} | Last Name: {student['Last_Name']} | Tutorial Group: {student['Tutorial_Group']}")
    else:
        print("No students found in this branch.")
    
    update_response = input("Do you want to update any student’s details? (Yes/No): ").strip().lower()
    if update_response == "yes":
        update_student_details()
    elif update_response == "no":
        print("Exiting student details view.")
    else:
        print("Invalid response. Please enter Yes or No.")

# Function to update student details
def update_student_details():
    print("\nIIT Campus")
    print("\nUpdate Student Details")
    student_id = input("\nStudent ID: ").strip()
    
    # Search for the student in the database
    student = next((s for s in students if s['Student_ID'] == student_id), None)
    
    if student:
        # Ask for new details, but allow blank to keep current data
        nic = input(f"New NIC (current: {student['NIC']}): ").strip() or student['NIC']
        first_name = input(f"New First Name (current: {student['First_Name']}): ").strip() or student['First_Name']
        last_name = input(f"New Last Name (current: {student['Last_Name']}): ").strip() or student['Last_Name']
        birth_date = input(f"New Birth Date (current: {student['Birth_Date']}): ").strip() or student['Birth_Date']
        permanent_address = input(f"New Permanent Address (current: {student['Permanent_Address']}): ").strip() or student['Permanent_Address']
        phone_number = input(f"New Phone Number (current: {student['Phone_Number']}): ").strip() or student['Phone_Number']
        
        # Update the student data
        student['NIC'] = nic
        student['First_Name'] = first_name
        student['Last_Name'] = last_name
        student['Birth_Date'] = birth_date
        student['Permanent_Address'] = permanent_address
        student['Phone_Number'] = phone_number
        # Ask if the user wants to save the new details after successful update
        update_response = input("Do you want to save the new details? (Yes/No): ").strip().lower()

        if update_response == "yes":
            update_student_details()  # Call the function to save the updated details
        elif update_response == "no":
            print("Existing student details view.")
        else:
            print("Invalid response. Please enter Yes or No.")
    else:
        print("Student not found.")
        
# Function to mark attendance
def mark_attendance():
    print("\nIIT Campus")
    print("\nMark Attendance")
    centre = input("\nCentre: ").strip()
    tutorial_group = input("Tutorial Group: ").strip()
    date = input("Date (DD-MM-YYYY): ").strip()
    
    print("\nMark Attendance for the Student ID:")
    # Ideally, filter students based on centre and tutorial group for attendance marking 
    student_ids = [s['Student_ID'] for s in students if s['Centre'] == centre and s['Tutorial_Group'] == tutorial_group]
    
    if student_ids:
        for student_id in student_ids:
            status = input(f"student_id Present or Absent? (Enter 'Present' or 'Absent'): ").strip().lower()
            if status not in ['present', 'absent']:
                print("Invalid status. Please enter 'Present' or 'Absent'.")
                continue
            
            # Store attendance record
            attendance.append({
                'Student_ID': student_id,
                'Date': date,
                'Status': status
            })
        
        save_response = input("Do you want to save the attendance details? (Yes/No): ").strip().lower()
        if save_response == "yes":
            print("Attendance saved successfully.")
        else:
            print("Attendance details not saved.")
    else:
        print("No students found in this tutorial group.")

# Function to view attendance records
def view_attendance():
    print("\nIIT Campus")
    print("\nView Attendance")
    student_id = input("\nStudent ID: ").strip()
    start_date = input("Enter the start date (From) in DD-MM-YYYY format: ").strip()
    end_date = input("Enter the end date (To) in DD-MM-YYYY format: ").strip()
    
    # Search attendance records
    records = [r for r in attendance if r['Student_ID'] == student_id and start_date <= r['Date'] <= end_date]
    
    if records:
        for record in records:
            print(f"Date: {record['Date']} - Status: {record['Status']}")
    else:
        print("No attendance records found.")
    
    main_menu_response = input("Do you want to direct to the main menu? (Yes/No): ").strip().lower()
    if main_menu_response == "yes":
        main_menu()
    else:
        print("Exiting attendance view.")

# Start the program by displaying the main menu
main_menu()
