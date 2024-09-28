from colored import Fore, Back, Style
import json
from rich import print_json
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
                # new_user()
                # questionnaire()
                # measurements()
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
    


def new_user():
    print("\nPlease provide some basic information below\n")
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    sex = input("Enter your biological sex (M/F): ").lower()

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
    print(f"{color1}\n>>> HEALTH QUESTIONNAIRE <<<{Style.reset}\n")
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
    print(f"{color1}\n>>> BODY MEASUREMENTS <<<{Style.reset}\n")
    print("Please provide the required measurements below.\n")

    def get_measure_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print(f"\n{color2}Please only enter numbers.{Style.reset}\n")

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
    # Instruct user how to create the csv
    print("\nTo add your information via a csv file, follow these steps: ")
    print(f"{color2}\nStep 1 -{Style.reset} Create a spreadsheet using MS Excel or Google Sheets, which must have the following headings (ignore the first 0) :")
    csv_file = pd.read_csv("files/example.csv")
    print(csv_file)
    pause = input("\nPress any key to continue to the next step...")
    print(f"{color2}\nStep 2 -{Style.reset} Download as a csv file.")
    pause = input("\nPress any key to continue to the next step...")
    # Ask user for filepath to csv
    print(f"{color2}\nStep 3 -{Style.reset} Paste the filepath below (Use Google to find out how to get the filepath for your file)")
    # Exception handling for this later on when the app tries to access it
    file_path = input("\nFilepath: ")
    pause = input("\nPress any key to continue to the next step...")
    print(f"{color2}\nImportant:{Style.reset} If you do not create the csv file correctly or use the correct path, this will not work and you will need to manually enter the information by selecting option 1 at the main menu.")
    # Load csv
    # Exception for incorrect filepath or no file.
    try:
        user_file = pd.read_csv(file_path)
        csv_data = user_file.to_dict(orient="records")
        print("Here is the information you provided: ")
        print_json(json.dumps(csv_data, indent=4))
    except FileNotFoundError:
        print(f"{color2}Error: {Style.reset} the file {file_path} was not found.")

    # Use data from csv and run through classes

    # Return merged data and append to json file

    # Print results - similar to end of execuse_and_save()



def print_results():
    name = input("Enter your account name to see your record: ").lower()

    with open("files/health_records.json") as file:
        data = json.load(file)

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
        print("File Not Found")



def update_measures():
    print("\nTime to update your measurements\n")

    # User chooses what they want to update (weight, height or waist)

    # json file loaded and measurement overwritten

    # new results displayed to user