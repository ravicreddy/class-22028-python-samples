# Print GPA of each Student 
    # Ram : 89
    # Sita : 98


# GPA Dictionary Build 
# gpa = {}
# gpa["ram"] = 89
# gpa["sita"] = 98



# Calculate GPA
# gpa = (Sum of all grades form the list)/len(grade list) for each person
# def calculateGpa(scores):
#   sum = 0
#   for score in scores:
#        sum = sum + int(score)
#   gpa = sum/len(scores)
#   return gpa




# List of grades
# Get list from CSV file

#def writeScoresToFile(gpa_dcict, filename):
#   file = open(filename, "w")
#    for item in gpa_dcit:
#        file.write(item.keY(), item.value())


#def printScores(gpa_dict):
#    for item in gpa_dcit:
#        print(item.keY(), item.value())



# def readScores(fileName)
#   gpa_dict = {}
#   file = open(filename, "r")
#       for line in file :
#            name, scores = readSingleStudentScores(line)
#            gpa = calculateGpa(scores)
#           gpa_dict[name] = gpa
#   file.close()
#   return gpa_dict


# def name, scores readSingleStudentScores(line)  
#   items = line.split(',')
#   name = items.pop(1)
#   return name, items