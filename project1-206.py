import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
    in_file = open(file, 'r')
    lines = in_file.readlines()[1:]
    in_file.close()
    student_names = []
    
    for line in lines:
        line = line.rstrip("\n")
        line = line.split(",")
        first = line[0]
        last = line[1]
        email = line[2]
        year = line[3]
        dob = line[4]
        
        data = {}
        data["First"] = first
        data["Last"] = last
        data["Email"] = email
        data["Class"] = year
        data["DOB"] = dob
        
        student_names.append(data)
    return student_names
	
    pass

def mySort(data,col):
    sorted_names = sorted(data, key=lambda x:x[col])
    return sorted_names[0]['First'] + " " + sorted_names[0]['Last']
	
    pass


def classSizes(data):
    tuples = []
    Senior= 0
    Junior = 0
    Sophomore = 0
    Freshman = 0
    
    for dict in data:
        if dict["Class"] == "Senior":
            Senior += 1
        elif dict["Class"] == "Junior":
            Junior += 1
        elif dict["Class"] == "Sophomore":
            Sophomore += 1
        elif dict["Class"] == "Freshman":
            Freshman += 1
      
    (a, b) = ("Senior", Senior)
    (c, d) = ("Junior", Junior)
    (e, f) = ("Sophomore", Sophomore)
    (g, h) = ("Freshman", Freshman)
    tuples.append((a,b))
    tuples.append((c, d))
    tuples.append((e, f))
    tuples.append((g, h))
    
    sorted_tuples = sorted(tuples, key=lambda x:x[1], reverse=True)
    return sorted_tuples

    pass


def findMonth(a):
    x = {}
    for obj in a:
        birthday = obj['DOB']
        birthday = birthday.split("/")
        month = birthday[0]
        if month not in x:
            x[month] = 0
        x[month] += 1
    
    sorted_x = sorted(x.items(), key=lambda x:x[1], reverse=True)
    return int(sorted_x[0][0])

    pass

def mySortPrint(a,col,fileName):
    sorted_name = sorted(a, key=lambda x:x[col])
    outfile = open(fileName,"w")
    for name in sorted_names:
        outfile.write("{},{},{}\n".format(name["First"],name["Last"],name["Email"]))
    outfile.close()

    pass

def findAge(a):
    total_age = 0
    today = date.today()
    
    for person in a: 
        dob = person['DOB']
        dob = dob.split("/")
        month = dob[0]
        day = dob[1]
        year= dob[2]

        age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
        total_age += age
        
    avg_age = int(round(total_age / len(a)))
    return avg_age

    pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
