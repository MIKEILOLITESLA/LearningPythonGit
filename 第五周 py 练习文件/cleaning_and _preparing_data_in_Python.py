#
num_rows = len(moma)

#
# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)


opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

#
age1 = "I am thirty-one years old"
age2 = age1.replace("one","two")

#
for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(","")
    nationality = nationality.replace(")","")
    row[2] = nationality

    gender = row[5]
    gender = gender.replace("(","")
    gender = gender.replace(")","")

#
for row in moma:
   
    gender = row[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender

    
    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality

#
def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    birth_date = row[3]
    death_date = row[4]
    
    birth_date = clean_and_convert(birth_date)
    death_date = clean_and_convert(death_date)
    
    row[3] = birth_date
    row[4] = death_date

#
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = []
for d in test_data:
    date = strip_characters(d)
    stripped_test_data.append(date)

#
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']
def process_date(date):
    if "-" in date:
        split_date = date.split("-")
        date_one = split_date[0]
        date_two = split_date[1]       
        date = (int(date_one) + int(date_two)) / 2
        date = round(date)
    else:
        date = int(date)

