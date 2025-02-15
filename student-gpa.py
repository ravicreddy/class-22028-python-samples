

# function to read grades of a student into a an arry
# this fucntion return student name and array of grades
#
#input - String, Single line from CSV file. Each line supposed to have 
#eleven comma seprated values, a name followed by scores from 10 tests
def readSingleStudentScores(csvRecord):
  values = csvRecord.split(',')
  return values.pop(0), values


#This function opens a file that contains scores and reads scores for each student 
# from file and copies them to a dictionary.
#
#Input - name of the file to open
#output - Dictionary of student scores in the following format
#         {'name', [22, 44, 45, 67, 56, 67, 78, 89, 98 17]}
def loadScoresFromFile(fileName):
    csvFileHanlde = open(fileName, 'r')
    studentScores = dict()
    for record in csvFileHanlde:
        name, values = readSingleStudentScores(record)
        studentScores[name] = values
    csvFileHanlde.close()
    return studentScores


#this finction takes dictionary of student scores and calculate grade for each 
#student. Grade is average of scores from 10 tests

#Input - Dictionary of scores, Key is student name abd value, an arry for 10 
#scores
#output - New dictionary with student name and single grade
#         ['name', 56] format
def computeGradesFromScores(scores):
  for name, values in scores.items():
    #values = scores[name];
    grade = sum(values/len(values))
    #grades[name] = grade
  return grades

#finally the starting point for the programs
#calls the main funtion for py passing math scores csv file name
scores = loadScoresFromFile('student-scores-math.csv')
grades = computeGradesFromScores(scores)
print(grades)