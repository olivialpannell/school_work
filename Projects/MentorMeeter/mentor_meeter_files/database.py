"""
CIS 422 Project 2 File I/O

Description: putting in information for mentors and mentees

Date Last Modified: 3/2/20

Authors: James Kang

Note: All comments on top of functions
1. Describes what the function does
2. Describes its arguments
3. Describes its outputs
"""

#import compatibility
import mysql.connector
import compatibility as c

# this function checks if the the email address and the username is already taken in our database
# given the email(string), username(string), the mentor/mentee state (1:mentor, 0:mentee)
# returns 1 if email is not value, 2 if username is not valid, 3 if both are not valid, 0 if they are all valid
def valid(email, username, status):
	if(status):
		query = "SELECT * FROM mentor"
	else:
		query = "SELECT * FROM mentee"

	# connecting to our database
	mydb = mysql.connector.connect(host="ix.cs.uoregon.edu", user="guest", passwd="guest", database="mentor",
								   port="3141")
	# using a cursor to add into the databse
	mycursor = mydb.cursor()

	# fetching all
	mycursor.execute(query)
	myresult = mycursor.fetchall()

	# checking for duplicate email addresses and username
	i = 0
	for row in myresult:
		if(row[6] == email):
			i = i + 1
		if(row[7] == username):
			i+=2

	return i

# the function is to create a mentor in our system
# Given the data as a User class type
# return 1 if the email is already registered
# 2 if the username is already registered
# 3 if both is already registered
# 0 if all is good and the account was created
def create_mentor(User):
	# checks if the user name and the email is already registered or not
	error = valid(User.email, User.username, User.user_type)
	if error:
		return error
	# connecting to our database
	mydb = mysql.connector.connect(host="ix.cs.uoregon.edu", user="guest", passwd="guest", database="mentor",
								   port="3141")
	# using a cursor to add into the databse
	mycursor = mydb.cursor()

	insert_s = (
		"INSERT INTO mentor(first, last, age, gender, q, bio, email, username, password) "
		"VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")

	q = ""
	for i in User.q:
		q += str(i)
		q += ','
	qs = q[:-1]

	data = (
	str(User.first), str(User.last), str(User.age), str(User.gender), qs, str(User.bio), str(User.email),
	str(User.username), str(User.password))

	mycursor.execute(insert_s, data)

	mydb.commit()
	return error

# the function is to create a mentee in our system
# Given the data as a User class type
# return 1 if the email is already registered
# 2 if the username is already registered
# 3 if both is already registered
# 0 if all is good and the account was created
def create_mentee(User):
	# checks if the user name and the email is already registered or not
	error = valid(User.email, User.username, User.user_type)
	if error:
		return error
	# connecting to our database
	mydb = mysql.connector.connect(host="ix.cs.uoregon.edu", user="guest", passwd="guest", database="mentor",
								   port="3141")
	# using a cursor to add into the databse
	mycursor = mydb.cursor()

	insert_s = ("INSERT INTO mentee(first, last, age, gender, q, bio, email, username, password) "
				"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

	q = ""
	for i in User.q:
		q += str(i)
		q += ','
	qs = q[:-1]

	data = (str(User.first), str(User.last), str(User.age), str(User.gender), qs, str(User.bio),
			str(User.email), str(User.username), str(User.password))

	mycursor.execute(insert_s, data)

	mydb.commit()
	return error

# given the username
# obtain the information of the following mentor
# returns result as a User class type
# if no such information exists then return User with userype = -1
def mentor_info(username):
	# connecting to our database
	mydb = mysql.connector.connect(host="ix.cs.uoregon.edu", user="guest", passwd="guest", database="mentor",
								   port="3141")
	# using a cursor to add into the databse
	mycursor = mydb.cursor()
	# fetching all
	query = "SELECT * FROM mentor"
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	for row in myresult:
		if (row[7] == username):
			age = int(row[2])
			qs = row[4].split(",")
			for i in range(len(qs)):
				qs[i] = int(qs[i])
			result = c.User(1, row[0], row[1], age, row[3], qs, row[5], row[6], row[7], row[8])
	try:
		return result
	except:
		return c.User(-1, None, None, 0, None, {}, None, None, None, None)

# given the username of the mentee
# obtain the information of the following mentee
# returns result as a User class type
def mentee_info(username):
	# connecting to our database
	mydb = mysql.connector.connect(host="ix.cs.uoregon.edu", user="guest", passwd="guest", database="mentor",
								   port="3141")
	# using a cursor to add into the databse
	mycursor = mydb.cursor()
	#fetching all
	query = "SELECT * FROM mentee"
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	for row in myresult:
		if (row[8] == username):
			age = int(row[2])
			qs = row[4].split(",")
			for i in range(len(qs)):
				qs[i] = int(qs[i])
			result = c.User(1, row[0], row[1], age, row[3], qs, row[5], row[6], row[7], row[8])

	try:
		return result
	except:
		return c.User(-1, None, None, 0, None, {}, None, None, None, None)

# extract all of the information of the mentors
# returns a list of mentors with User class type
def extract_mentors():
	# connecting to our database
	mydb = mysql.connector.connect(host="ix.cs.uoregon.edu", user="guest", passwd="guest", database="mentor",
								   port="3141")
	# using a cursor to add into the databse
	mycursor = mydb.cursor()
	# fetching all
	query = "SELECT * FROM mentor"
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	result = []
	for row in myresult:
		age = int(row[2])
		qs = row[4].split(",")
		for i in range(len(qs)):
			qs[i] = int(qs[i])

		result.append(c.User(1, row[0], row[1], age, row[3], qs, row[5], row[6], row[7], row[8]))
	return result

# extract all of the information of the mentees
# returns a list of mentors with User class type
def extract_mentees():
	# connecting to our database
	mydb = mysql.connector.connect(host="ix.cs.uoregon.edu", user="guest", passwd="guest", database="mentor",
								   port="3141")
	# using a cursor to add into the databse
	mycursor = mydb.cursor()
	# fetching all
	query = "SELECT * FROM mentee"
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	result = []
	for row in myresult:
		age = int(row[2])
		qs = row[4].split(",")
		for i in range(len(qs)):
			qs[i] = int(qs[i])

		result.append(c.User(0, row[0], row[1], age, row[3], qs, row[5], row[6], row[7], row[8]))
	return result

# creates an account in our database
def create_account(User):
	# Checks if mentor of mentee
	if User.user_type:
		create_mentor(User)
	else:
		create_mentee(User)
	# Initializes current user
	c.current_user = c.User(0, "", "", 0, "", [], "", "", "", "")
	# Adds users to users[] if havent already.
	if len(c.users) <= 1:
		c.users.extend(extract_mentees())
		c.users.extend(extract_mentors())
	# initialize current user to this user
	c.current_user = User
	c.users.append(c.current_user)
	# Gets current users matches.
	c.pref_check(c.current_user)
	c.compat(c.current_user)

	return c.current_user


