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
    def __init__(self,activity_list):
        self.activity_list = activity_list
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
OLD_MAN_TEST = OLD_MAN(activity_list_test)
#activity_list_test = ["Bicep Curls","Vitamins","Running 30 minutes"]
print(OLD_MAN_TEST.weekly_list(activity_list_test))
print(OLD_MAN_TEST.weekly_list(activity_list_test_week_zed))
wellness_test = OLD_MAN_TEST.weekly_list(activity_list_test_week_zed)
OLD_MAN_TEST.output_csv(wellness_test, "test.csv",'10.21-25.2025','Celebration')
#print(OLD_MAN_TEST.assess(activity_list_test_week_zed))
            
                
