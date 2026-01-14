#DAD BOD TO OLD THOR BOD

#Create data plot of overall health
#start with a point system for activities,
#brushing teeth +1, bicep curls .25 for each bicep curl
#one beer -2 points
#running 30 minutes 5 points
#flossing 1 point
#Showering .5 point
#CPAP 1 point per hour
#multivitamin .5 point
import csv
#create CSV with weekly score and judgement
class OLD_MAN(object):
    #tracks old man activities
    def __init__(self,name):
        self.name = name
        self.activity_list = []
        self.data = {} # Initialize an empty dictionary as an instance attribute
    def add_item(self, key, value):
        '''Method to add items to the dictinoary.'''
        self.data[key] = value
    def get_data(self):
        '''Method to retrieve the entire dicionary.'''
        return self.data
        
    def weekly_list(self, activity_list):
        wellness_activity = 0
        for i in activity_list:
            if i == "CPAP":
                wellness_activity += 5
            elif i == "Bicep Curls":
                wellness_activity += 3
            elif i == "Shoulder Press":
                wellness_activity += 1
            elif i == "Seated Row":
                wellness_activity += 1
            elif i == "Vitamins":
                wellness_activity += 1
            elif i == "Running 30 minutes":
                wellness_activity += 4
            elif i == "Running 15 minutes":
                wellness_activity += 2
            elif i == "Beer":
                wellness_activity -= 3
            elif i == "Doctor":
                wellness_activity += 4
            elif i == "Bench Press":
                wellness_activity += 1
            elif i == "Leg Press":
                wellness_activity += 2
            elif i == "Squats":
                wellness_activity += 2
            elif i == "Topo Chico":
                wellness_activity += .5
            elif i == "Salad":
                wellness_activity += 2
        if wellness_activity <= 2:
            print("You are not going for that Old Thor Life, my friend.")
        elif wellness_activity >= 3 and wellness_activity <= 5:
            print("Tis fair, you are maintaining, you can do beter.")
        elif wellness_activity > 5 and wellness_activity <= 8:
            print("This is alright you are giving some effort.But you will not defeat Frost Giants.")
        elif wellness_activity >8:
            print("You are on your way to obtaining Thor's Hammer if worthy!")
        return wellness_activity
    def weekly_dict(self, data):
        wellness_activity = 0
        for i in data:
            if i == 3:
                wellness_activity += 5
            elif i == "Bicep Curls":
                wellness_activity += 3
            elif i == "Shoulder Press":
                wellness_activity += 1
            elif i == "Seated Row":
                wellness_activity += 1
            elif i == "Vitamins":
                wellness_activity += 1
            elif i == "Running 30 minutes":
                wellness_activity += 4
            elif i == 15:
                wellness_activity += 2
            elif i == 2:
                wellness_activity -= 3
            elif i == 4:
                wellness_activity += 4
            elif i == "Bench Press":
                wellness_activity += 1
            elif i == "Leg Press":
                wellness_activity += 2
            elif i == "Squats":
                wellness_activity += 2
            elif i == 2015:
                wellness_activity += .5
            elif i == 19:
                wellness_activity += 2
        if wellness_activity <= 2:
            print("You are not going for that Old Thor Life, my friend.")
        elif wellness_activity >= 3 and wellness_activity <= 5:
            print("Tis fair, you are maintaining, you can do beter.")
        elif wellness_activity > 5 and wellness_activity <= 8:
            print("This is alright you are giving some effort.But you will not defeat Frost Giants.")
        elif wellness_activity >8:
            print("You are on your way to obtaining Thor's Hammer if worthy!")
        return wellness_activity
    def output_csv(self, wellness_activity,csv_file, week, comment):
        fieldnames = ['Wellness Score','Week','Comment']
        data = [{'Wellness Score': str(wellness_activity),'Week': week,'Comment': comment}]
        with open (csv_file, "a", newline = '') as f:
        #    fieldnames = ['Wellness Score','Date','Commnt']
        
         #   f.write("You're score for this week: %d." % wellness_activity)
            writer = csv.DictWriter(f, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(data) #Write the data rows
        
  

activity_list_test = ["Bicep Curls","Vitamins","Running 30 minutes"]
activity_list_test_week_zed = ["CPAP","Vitamins","Beer","Beer","Beer","Beer","Beer","Bicep Curls","Shoulder Press","Seated Row","Beer","CPAP","Running 15 minutes","Vitamins"]
activity_list_test_week_one = ["CPAP","CPAP","Doctor","Vitamins","Beer","Beer","Beer","Beer","Beer","Beer","Seated Row","Shoulder Press","Bicep Curls"]
activity_list_test_week_two = ["CPAP","CPAP","Beer","Beer","Beer","Bicep Curls","Bench Press","Leg Press","Squats"]
activity_list_new_year = ["CPAP","CPAP","Running 15 minutes","Vitamins","Topo Chico","Topo Chico", "Topo Chico", "Salad"] 
#OLD_MAN_TEST = OLD_MAN(activity_list_test)
#activity_list_test = ["Bicep Curls","Vitamins","Running 30 minutes"]
#print(OLD_MAN_TEST.weekly_list(activity_list_test))
#print(OLD_MAN_TEST.weekly_list(activity_list_test_week_zed))
#wellness_test = OLD_MAN_TEST.weekly_list(activity_list_test_week_zed)
new_year_week_one = OLD_MAN("New Year")
new_year_week_one_list = new_year_week_one.weekly_list(activity_list_new_year)
print(new_year_week_one_list)
#OLD_MAN_TEST.output_csv(wellness_test, "test.csv",'10.21-25.2025','Celebration')
#print(OLD_MAN_TEST.assess(activity_list_test_week_zed))
#wellness_test_two = OLD_MAN_TEST.weekly_list(activity_list_test_week_one)
#OLD_MAN_TEST.output_csv(wellness_test_two,"test.csv",'10-27-11-1.2025','Halloween')
new_year_week_one.output_csv(new_year_week_one_list,"test.csv",'01-05-2026-01-10-2026','Week One Fast')                
new_year_week_two = OLD_MAN('Week Two')
new_year_week_two.add_item(15,"Running 15 minutes")
new_year_week_two.add_item(19, "Salad")
new_year_week_two.add_item(2015, "Topo Chico")
new_year_week_two.add_item(4, "Doctor")
new_year_week_two.add_item(3,"CPAP")
new_year_week_two.add_item(2,"Beer")
data2 = (15,19,2,2)
new_year_week_two.weekly_dict(data2)
