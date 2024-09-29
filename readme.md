# Health Check App
This app is designed to take objective and subjective health information and provide health outputs and rating before starting and picking back up an exercise journey.

To use it you must use terminal and load the libraries in requirements.txt. 

You may optionally import certain metrics via a csv file on your computer. More instructions will be provided further on.

## The Main Menu
You have five options at the main menu:

1. Complete the Questionnaire
2. Import from CSV
3. Print Results
4. Update Measurements
5. Quit

### 1. The Questionnaire
This is a great option for new users to the app. You are stepped through all of the information required:

**Basic Personal Details**
- Name (format must be firstname lastname, e.g., "Jusin Case")
- Age (age in numbers only)
- Biological sex (m or f only)

**Adult Pre-Exercise Screen System Level 1**
There are 6 important questions you must answer to acertain your level of risk when starting exercise. This needs to be done once per year or whenever there are significant changes to your health status. You answer with either yes or no. If you answer 'yes' to any question, you are consider a high risk exercise participant and should seek medical clearance before attempting to exercise. If all responses are 'no' then you are considered low risk. Here are the questions:

1. Has your medical practitioner ever told you that you have a heart condition or have you ever suffered a stroke? 
2. Do you ever experience unexplained pains or discomfort in your chest at rest or during physical activity/exercise? 
3. Do you ever feel faint, dizzy or lose balance during physical activity/exercise?
4. Have you had an asthma attack requiring immediate medical attention at any time over the last 12 months? 
5. If you have diabetes (type 1 or 2) have you had trouble controlling your blood sugar (glucose) in the last 3 months? 
6. Do you have any other conditions that may require special consideration for you to exercise? 

If you're unsure, respond with 'y' and speak with your general practitioner.

**Body Measurements**
Finally, you will need to take some basic measurements of yourself:
- Height in centimeters (sometimes on your drivers license)
- Weight in kilograms
- Hip circumference in centimeters*
- Waist circumference in centimeters*
- Resting Heart Rate in beats per minute*

*Look up how to do these things on YouTube

If for some reason you cannot provide one or more of these measurements, have a guess. You can't not answer it or put zero. When you get the results you can ignore the rating. When you are able to take the measurement, you can use the Update Measurement option in the main menu.

### 2. Import from CSV
This option will require more technical knowledge using spreadsheets. This option is good if you already track your measurements in a spreadsheet. You can input the following measurements using this option, and the formatting must be the same as detailed in the questionnaire section above:

- Name
- Age
- Sex
- Weight
- Height
- Hip circumference
- Waist circumference
- Resting heart rate

Set up your spreadsheet in the following way. These are the column headings where a comma denotes the next column:

**name,age,sex (m or f),weight (kg),height (cm),hip (cm),waist (cm),heart_rate (bpm)**

Enter your data in the next row down, then once complete, download the file as a csv. You will need to capture the file address to where your file is. This will different depending on your operating system. If you aren't sure, Google how to copy the file location of a file. You can paste it into the terminal once prompted.

If the file location, formatting or heading spelling is incorrect, the file will not work.

**NOTE:** You cannot update existing records with the import method at this stage. You must use the update measurements option at the main menu.

### 3. Print Results
This is a simple option to print your record should you ever choose to. If you do not enter your name correctly, or you haven't create a record yet, you will get an error.

### 4. Update Measurements
When it's time to update certain measurements, you can choose this option from the main menu. You can only update one measurement at a time. Here are the measurements you can update:

- Age
- Weight
- Hip circumference
- Waist circumference
- Resting heart rate

Your results will be printed once they are updated so you can view any changes to health rating, if applicable. Formatting continues to be important here.

### 5. Quit
Ends the current session

**Note**: At any time you can press ctrl + c (cmd + c on mac) to force quit the program.

## Understanding Your Results
Here is an example of a record:
```
{
        "name": "Jane Doe",
        "age": 56,
        "sex": "female",
        "chronic_risk": "Your age group has a higher risk of chronic health conditions.",
        "heart_condition": "n",
        "chest_pains": "y",
        "dizzy": "n",
        "asthma": "n",
        "diabetes": "n",
        "other_conditions": "n",
        "health_risk": "Exercise presents a high risk to you. Please seek guidance from a general practitioner",
        "weight": 90.0,
        "height": 150.0,
        "bmi": 40.00,
        "bmi_rating": "Obese I",
        "hip": 120.0,
        "waist": 120.0,
        "whr": 1.0,
        "whr_rating": "High Health Risk",
        "heart_rate": 90.0,
        "hr_rating": "High Heart Rate"
    }
```
You will notice a few extra items here in addition to the responses and data you provided.

### chronic_risk
Males over 45 and females over 55 are more susceptible to chronic health conditions such as cardiovascular disease. This isn't a cause for concern, but something to consider. If you are concerned, you can speak to your GP, especially if you have a family history.

### health_risk
If you answered 'n' to all health question, you will be in the low risk category. Otherwise you will be high risk and should not begin exercising without medical clearance.

### bmi and bmi_rating
Body Mass Index (BMI) is a very general measurement with the following ratings:
- Underweight = bmi < 18.5
- Healthy weight = bmi between 18.5 and 24.9
- Overweight = bmi between 25 and 29.9
- Obese class I = bmi between 30 and 34.9
- Obese class II = bmi between 35 and 39.9
- Obese class III = bmi > 40

The rating is not considered very accurate as it doesn't account for muscle mass. However, it provides a base measurement for which you can track over time. For example, as your weight decreases, your BMI will drop. So, it's something you can use to track progress.

### whr and whr_rating
Using your waist and hip circumference measurements, we can determine your Waist to Hip ratio (WHR). The higher the WHR, the higher your risk is of heart disease. Here are the ratings for men and women

**WOMEN**
- Low <= 0.8
- Moderate = between 0.81 and 0.85
- High >= 0.86

**MEN**
- Low <= 0.95
- Moderate = between 0.96 and 1.0
- High > 1.0

The results aren't a cause for alarm, it is simply a base measurement to track. For example, if you lose fat from around your waist, it will reduce your WHR and your risk of heart disease.

### heart_rate and hr_rating
Our resting heart rate can also help us identify an issue with our body. Heart rates between 60 and 90 are considered health. Below 60 is 'low' and above 90 is 'high'. Generally, the fitter we are, the lower our resting heart rate.

It is best to measure this first thing in the morning before coffee, exercise or any other stimulants. Depressants (e.g., alcohol) can also affect our resting heart rate.

## Overall Moderate Risk
If you responded to all the health questions with 'n', but you have received a few other high-risk results such as high BMI and WHR, it is recommended that you speak to your GP. Although starting exercise at a low to moderate intensity would be beneficial.

## Troubleshooting
If you encounter any issues with this terminal app, please send as much information as possible through to help@healthcheckapp.com. Any feedback which helps to improve this app is much appreciated.


