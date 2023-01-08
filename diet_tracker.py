class Diet:
    def __init__(self, breakfast_calories, lunch_calories, dinner_calories, exercise, bmr):
        self.breakfast_calories = breakfast_calories
        self.lunch_calories = lunch_calories
        self.dinner_calories = dinner_calories
        self.exercise = exercise
        self.bmr = bmr

    def calorie_deficit(self):
        deficit = self.bmr + self.exercise - (self.breakfast_calories + self.lunch_calories + dinner_calories)
        return deficit

breakfast_calories = int(input("How many cals did you have for breakfast? "))    
lunch_calories = int(input("How many cals did you have for lunch? "))    
dinner_calories = int(input("How many cals did you have for dinner? "))    
exercise = int(input("How many cals did you exercise did you burn exercising? "))
# BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years)
bmr = int(input("What is you BMR? "))

fitness = Diet(breakfast_calories, lunch_calories, dinner_calories, exercise, bmr)
weekly_deficit = 7 * fitness.calorie_deficit()

if weekly_deficit > 0:
    print(f"You will lose {round(weekly_deficit / 3500, 2)} lbs per week.")
elif weekly_deficit == 0:
    print("Your weight will stay the same.")
else:
    print(f"You will gain {round(-1 * weekly_deficit / 3500, 2)} lbs per week.")