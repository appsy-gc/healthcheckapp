from colored import Fore, Back, Style
import json
from rich import print_json
import os
from prettytable import PrettyTable
import pandas as pd
from classes.person import Female, Male
from classes.subjective_measures import APSSLevel1
from classes.objective_measures import BodyMassIndex, WaistToHip, HeartRate

# Set up colors
color1: str = f"{Style.BOLD}{Back.GREEN}"
color2: str = f"{Style.BOLD}{Fore.RED}"
color3: str = f"{Style.BOLD}{Fore.YELLOW}"


def menu():
    # Create Menu
    print(f" {color1}>>> MAIN MENU <<<{Style.reset}\n")
    # - 1. Complete the Questionnaire
    print("1. Complete the Questionnaire")
    # - 2. Import measurements from csv
    print("2. Import from CSV")
    # - 3. Print results
    print("3. Print Results")
    # - 4. Update measurements
    print("4. Update Measurements")
    # - 5. Quit
    print("5. Quit\n")

    choice = ""
    while choice != "5":
        choice = input(f"{color3}Choose an option from the menu above:{Style.reset} ").strip()

        match choice:
            case "1":
                execute_and_save()
                break
            case "2":
                import_csv()
                break
            case "3":
                print_results()
                break
            case "4":
                update_measures()
                break
            case "5":
                print(f"You have chosen Quit. Goodbye {color2}Meat bag...{Style.reset}\n")
            case _:
                print(f"{color2}Invalid choice:{Style.reset} Please select a number between 1 and 5 (inclusive).\n")
    

def check_name(name):
    try:
        with open("files/health_records.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    for list in data:
        if list["name"] == name:
            found = True
            break
    else:
        found = False

    return found

# Ensure input is a number and is not zero to avoid a division error
def get_measure_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(f"\n{color2}Input cannot be zero or negative.{Style.reset}\n")
            else:
                return value
        except ValueError:
            print(f"\n{color2}Please only enter numbers greater than zero.{Style.reset}\n")

# Ensure age is a number and greater than zero
def check_age(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print(f"\n{color2}Age cannot be zero or negative.{Style.reset}\n")
            else:
                return value
        except ValueError:
            print(f"\n{color2}Please only enter numbers greater than zero.{Style.reset}\n")



def get_user_input(prompt, validation_fn):
    while True:
        user_input = input(prompt)
        if validation_fn(user_input):
            return user_input
        else:
            print(f"\n{color2}Invalid input. Please try again.{Style.reset}\n")



def get_name():
    return get_user_input("Enter your full name: ", lambda x: len(x.split()) == 2)



def get_sex():
    return get_user_input("Enter your biological sex (m/f): ", lambda x: x.lower() in ["m", "f"]).lower()



def new_user():
    print("\nPlease provide some basic information below\n")
    name = get_name()
    age = check_age("Enter your age: ")
    sex = get_sex()

    if sex == "m":
        sex = "male"
        new_person = Male(name, age, sex)
    else:
        sex = "female"
        new_person = Female(name, age, sex)

    # Assign risk category based on age and sex
    health_risk = new_person.risk_cat()
    # Set up list for json
    user_data = {
        "name": name, 
        "age": age, 
        "sex": sex, 
        "chronic_risk": health_risk
        }

    return user_data



def questionnaire():
    print(f"\n {color1}>>> HEALTH QUESTIONNAIRE <<<{Style.reset} \n")
    print(f"Please answer the following questions {color2}'Y'{Style.reset} or {color2}'N'{Style.reset}: ")
    
    def get_yes_no_input(prompt):
        while True:
            answer = input(prompt).lower()
            if answer in ['y', 'n']:
                return answer
            else:
                print(f"{color2}\nInvalid entry.{Style.reset} Please enter 'y' for yes or 'n' for no.\n")

    # Apply validation to each question
    question1 = get_yes_no_input("1. Has your medical practitioner ever told you that you have a heart condition or have you ever suffered a stroke? (Y/N): ")
    question2 = get_yes_no_input("2. Do you ever experience unexplained pains or discomfort in your chest at rest or during physical activity/exercise? (Y/N): ")
    question3 = get_yes_no_input("3. Do you ever feel faint, dizzy or lose balance during physical activity/exercise? (Y/N): ")
    question4 = get_yes_no_input("4. Have you had an asthma attack requiring immediate medical attention at any time over the last 12 months? (Y/N): ")
    question5 = get_yes_no_input("5. If you have diabetes (type 1 or 2) have you had trouble controlling your blood sugar (glucose) in the last 3 months? (Y/N): ")
    question6 = get_yes_no_input("6. Do you have any other conditions that may require special consideration for you to exercise? (Y/N): ")

    risk_level = APSSLevel1(question1, question2, question3, question4, question5, question6)
    health_risk = risk_level.assess_questions()

    return health_risk



def measurements(user_data):
    print(f"\n {color1}>>> BODY MEASUREMENTS <<<{Style.reset} \n")
    print("Please provide the required measurements below.\n")
    

    # Get input from user for body measurements + error handling
    weight = get_measure_input("Please enter your weight in kg: ")
    height = get_measure_input("Please enter your height in cm: ")
    hip = get_measure_input("Please enter your hip circumference in cm: ")
    waist = get_measure_input("Please enter your waist circumference in cm: ")
    heart_rate = get_measure_input("Please enter your resting heart rate in beats per min: ")

    new_bmi = BodyMassIndex(weight, height)
    bmi_data = new_bmi.calculate()
    new_whr = WaistToHip(hip, waist, user_data["sex"])
    whr_data = new_whr.calculate()
    new_hr_rating = HeartRate(heart_rate)
    hr_rating_data = new_hr_rating.calculate()

    merged_measure_data = bmi_data.copy()
    merged_measure_data.update(whr_data)
    merged_measure_data.update(hr_rating_data)

    return merged_measure_data
    


def execute_and_save():
    # Add data to new json
    try:
    #     # Load json and assign data to data
        with open("files/health_records.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        # Create new file if one does not exist
        data = []
    # Collect user data
    user_data = new_user()
    if check_name(user_data["name"]):
        return print(f"\n{color2}ERROR: {Style.reset}Name already exists.\n")
    else:
        questionnaire_data = questionnaire()
        measurement_data = measurements(user_data)
        # Merge data into a single dictionary
        merged_data = user_data.copy()
        merged_data.update(questionnaire_data)
        merged_data.update(measurement_data)
        # Add new dictionary to json file
        data.append(merged_data)
        with open("files/health_records.json", "w") as file:
            json.dump(data, file, indent=4)
        # Print results to user
        print("\nHere are your results: ")
        print_json(json.dumps(merged_data, indent=4))


def import_csv():
    # Create a table instance for an example for user
    table = PrettyTable()

    # Add headers (first row)
    table.field_names = ["Name", "Age", "Sex (m or f)", "Weight (kg)", "Height (cm)", "Hip (cm)", "Waist (cm)", "Heart Rate (bpm)"]

    # Add the data (second row)
    table.add_row(["Justin Case", 99, "m", 90, 190, 90, 70, 80])

    # Instruct user how to create the csv
    print("\nTo add your information via a csv file, follow these steps: ")
    print(f"{color2}\nStep 1 -{Style.reset} Create a spreadsheet using MS Excel or Google Sheets, which must have the following headings (ignore the first 0) :")
    print(table)
    input("\nPress any key to continue to the next step...")
    print(f"{color2}\nStep 2 -{Style.reset} Download as a csv file.")
    input("\nPress any key to continue to the next step...")
    # Ask user for filepath to csv
    print(f"{color2}\nStep 3 -{Style.reset} Paste the filepath below (Use Google to find out how to get the filepath for your file)")
    print(f"{color2}\nImportant:{Style.reset} If you do not create the csv file correctly or use the correct path, this will not work and you will need to manually enter the information by selecting option 1 at the main menu.")
    # Exception handling for this later on when the app tries to access it
    file_path = input(f"\n{color3}Filepath: {Style.reset}")
    # Validate the file path
    if not os.path.exists(file_path):
        print(f"\n{color2}Invalid file path.{Style.reset} Please start again and provide a correct file path.")
        return
    # Load csv
    # Exception for incorrect filepath or no file.
    try:
        user_file = pd.read_csv(file_path)
        csv_data = user_file.to_dict(orient="records")
        print("Here is the information you provided: ")
        print_json(json.dumps(csv_data, indent=4))
        # Have them complete the questionnaire
        print("\nPlease complete a short questionnaire: \n")
        questionnaire_data = questionnaire()
        # Use data from csv and run through classes
        if csv_data[0]["sex (m or f)"] == "m":
            sex = "male"
            new_person = Male(csv_data[0]["name"], csv_data[0]["age"], sex)
        else:
            csv_data[0]["sex (m or f)"] = "female"
            new_person = Female(csv_data[0]["name"], csv_data[0]["age"], sex)
        # Get health risk from basic information
        health_risk = new_person.risk_cat()
        # Set up list for json
        user_data = {
            "name": csv_data[0]["name"], 
            "age": csv_data[0]["age"], 
            "sex": sex, 
            "chronic_risk": health_risk
            }
        # Use csv data to create instances of measurements child classes
        new_bmi = BodyMassIndex(csv_data[0]["weight (kg)"], csv_data[0]["height (cm)"])
        bmi_data = new_bmi.calculate()
        new_whr = WaistToHip(csv_data[0]["hip (cm)"], csv_data[0]["waist (cm)"], user_data["sex"])
        whr_data = new_whr.calculate()     
        new_hr_rating = HeartRate(csv_data[0]["heart_rate (bpm)"])
        hr_rating_data = new_hr_rating.calculate()
        # Merge all data into one list
        merged_measure_data = user_data.copy()
        merged_measure_data.update(questionnaire_data)
        merged_measure_data.update(bmi_data)
        merged_measure_data.update(whr_data)
        merged_measure_data.update(hr_rating_data)
        # Append to json file
        with open("files/health_records.json") as file:
            data = json.load(file)
        data.append(merged_measure_data)
        with open("files/health_records.json", "w") as file:
            json.dump(data, file, indent=4)
        # Print results for user
        print(f"\n{color2}Here are your results: {Style.reset}")
        print_json(json.dumps(merged_measure_data, indent=4))
    except FileNotFoundError:
        print(f"\n{color2}Error: {Style.reset} the file {file_path} was not found. Enter data manually or try again.\n")
    except TypeError:
            print(f"\n{color2}ERROR:{Style.reset} Incorrect data in file. Check values and try again.\n")
    except ValueError:
        print(f"\n{color2}ERROR:{Style.reset} Incorrect data in file. Check values and try again.\n")


def print_results():
    name = input("Enter your account name to see your record: ").lower()
    try:
        with open("files/health_records.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    found = False
    i = 0

    for list in data:
        if list["name"].lower() == name:
            print("File located. Here are your results: ")
            print_json(json.dumps(data[i]))
            # rprint(json.dumps(data[i], indent=4))
            found = True
        i += 1
    
    if not found:
        print(f"\n{color2}Record Not Found.{Style.reset}\n")


# def update_field(health_record, field, new_value, data):
#     health_record[field] = new_value
#     data.append(health_record)
#     with open("files/health_records.json", "w") as file:
#         json.dump(data, file, indent=4)


def update_measures():
    print(f"\n{color1}Time to update your measurements?{Style.reset}\n")
    print("You can only do this for one measurement at a time\n")
    
    # Must enter their name to locate the correct record in json
    name = input("Please enter your name so we can locate your file: ").lower()
    with open("files/health_records.json") as file:
        data = json.load(file)
        
    for record in data:
        if record["name"].lower() == name:
            health_record = record
            # Remove the old record to avoid duplication
            data.remove(record)  
            break
    else:
        print(f"{color2}Record Not Found.{Style.reset}\n")
        return

    # Print the found record
    print(f"\n{color2}Here is your record: {Style.reset}")
    print_json(json.dumps(health_record, indent=4))

    # User chooses what to update
    print("What would you like to update?")
    print("Choose from the list below\n")
    print(f"{color2}1 - {Style.reset}Age")
    print(f"{color2}2 - {Style.reset}Weight (kg)")
    print(f"{color2}3 - {Style.reset}Hip Circumference (cm)")
    print(f"{color2}4 - {Style.reset}Waist Circumference (cm)")
    print(f"{color2}5 - {Style.reset}Resting Heart Rate (bpm)")
    print(f"{color2}6 - {Style.reset}CANCEL\n")

    choice = int(input(f"{color3}Enter your choice: {Style.reset}"))

    # Process user choice
    match choice:
        case 1:
            # Update Age
            new_age = check_age("Enter your new age: ")
            health_record["age"] = new_age
            if health_record["sex"] == "male":
                updated_user = Male(health_record["name"], new_age, health_record["sex"])
            else:
                updated_user = Female(health_record["name"], new_age, health_record["sex"])
            health_record["chronic_risk"] = updated_user.risk_cat()

        case 2:
            # Update Weight and BMI
            new_weight = get_measure_input("Enter your new weight in kg: ")
            health_record["weight"] = new_weight
            updated_measure = BodyMassIndex(health_record["weight"], health_record["height"])
            new_bmi = updated_measure.calculate()
            health_record["bmi"] = new_bmi["bmi"]
            health_record["bmi_rating"] = new_bmi["bmi_rating"]

        case 3:
            # Update Hip Circumference and WHR
            new_hip = get_measure_input("Enter your new hip circumference in cm: ")
            health_record["hip"] = new_hip
            updated_measure = WaistToHip(health_record["hip"], health_record["waist"], health_record["sex"])
            new_whr = updated_measure.calculate()
            health_record["whr"] = new_whr["whr"]
            health_record["whr_rating"] = new_whr["whr_rating"]

        case 4:
            # Update Waist Circumference and WHR
            new_waist = get_measure_input("Enter your new waist circumference in cm: ")
            health_record["waist"] = new_waist
            updated_measure = WaistToHip(health_record["hip"], health_record["waist"], health_record["sex"])
            new_whr = updated_measure.calculate()
            health_record["whr"] = new_whr["whr"]
            health_record["whr_rating"] = new_whr["whr_rating"]

        case 5:
            # Update Resting Heart Rate
            new_rhr = get_measure_input("Enter your new resting heart rate in bpm: ")
            health_record["heart_rate"] = new_rhr
            updated_measure = HeartRate(health_record["heart_rate"])
            new_hr_rating = updated_measure.calculate()
            health_record["hr_rating"] = new_hr_rating["hr_rating"]

        case 6:
            print("\nSuccessfully Cancelled\n")
            return

        case _:
            print(f"{color2}An Error has Occurred.{Style.reset} Try running the program again.")
            return

    # After all updates, append the record once and write back to JSON
    data.append(health_record)
    with open("files/health_records.json", "w") as file:
        json.dump(data, file, indent=4)

    # Print updated record
    print(f"\nHere is your {color2}UPDATED{Style.reset} record: ")
    print_json(json.dumps(health_record, indent=4))