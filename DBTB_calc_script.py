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
            elif i == "Vitamins":
                wellness_activity += 1
            elif i == "Running 30 minutes":
                wellness_activity += 4
        return wellness_activity

activity_list_test = ["Bicep Curls","Vitamins","Running 30 minutes"]
OLD_MAN_TEST = OLD_MAN(activity_list_test)
#activity_list_test = ["Bicep Curls","Vitamins","Running 30 minutes"]
print(OLD_MAN_TEST.weekly_list(activity_list_test))
            
                
