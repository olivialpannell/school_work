"""
CIS 422 Project 2: Compatibility Algorithm File

Last Modified: 3/7/20

Authors: Mikayla Campbell
"""
import database as d

# All of the program's users
users = []

global current_user

percent_scale = [100/13, 75/13, 50/13, 25/13, 0]
# Divide percent by 14 for each question because there are 14 questions
	# # Max 4 off
	# # 4 = 0%
	# # 3 = 25%
	# # 2 = 50%
	# # 1 = 75%
	# # 0 = 100%

class User:
	"""Class that stores each user's information"""
	def __init__(self, user_type, first, last, age, gender, questionnaire, bio, email, username, password):
	 	self.user_type = user_type # int (Mentor = 1, mentee = 0)
	 	self.first = first # string
	 	self.last = last # string
	 	self.age = age # int
	 	self.gender = gender # string
	 	self.q = questionnaire # list of numbers (Starts at 1)
	 	self.bio = bio # string
	 	self.email = email # string
	 	self.user_matches = [["", 0],["", 0], ["", 0], ["", 0], ["", 0]] # User Matches (Sorted)
	 	self.username = username # string
	 	self.password = password # string

	def __str__(self):
		return self.first + ' ' + self.last

	def __repr__(self):
		return "User({} {} {} {} {} {} {} {} {})".format(self.first, self.last,
			self.age, self.gender, self.q, self.bio, self.email,
			self.username, self.password)

current_user = User(0, "", "", 0, "", [], "", "", "", "")

def login_check(username, password):
	"""Checks login credentials"""
	current_user = User(0, "", "", 0, "", [], "", "", "", "")
	if len(users) <= 1:
		users.extend(d.extract_mentees())
		users.extend(d.extract_mentors())

	for user in users:
		if user.username == username and user.password == password:
			current_user = user
			pref_check(current_user)
			compat(current_user)
			return 1, current_user

	return 0, User(0, "", "", 0, "", [], "", "", "", "")


def equal_q_answer(current_user, user, q_num, count):
	"""Mentor and mentee must have equal answers"""
	percent = abs(current_user.q[q_num] - user.q[q_num])
	real_percent = percent_scale[percent]
	current_user.user_matches[count][1] += real_percent


def equal_or_higher(current_user, user, q_num, count):
	"""Mentor needs to be 1 or higher than mentee or equal"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent >= 0:
		real_percent = percent_scale[percent]
		current_user.user_matches[count][1] += real_percent


def equal_or_lower(current_user, user, q_num, count):
	"""Mentee needs to be 1 or lowerer than mentor or equal"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent <= 0:
		real_percent = percent_scale[abs(percent)]
		current_user.user_matches[count][1] += real_percent


def higher(current_user, user, q_num, count):
	"""Mentor needs to be 1 or higher than mentee"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent > 0:
		real_percent = percent_scale[percent - 1]
		current_user.user_matches[count][1] += real_percent


def lower(current_user, user, q_num, count):
	"""Mentee needs to be 1 or lower than mentor"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent < 0:
		real_percent = percent_scale[abs(abs(percent) - 1)]
		current_user.user_matches[count][1] += real_percent


def pref_check(current_user):
	"""Remove users who do not fit the current user's preferenes

	0) Gender (Male, Female, Other)
	1) Who do you want to be matched with? (Male, Female, Other)
	2) Age range (1 - 5)
	3) What is your career field? (47)
	"""

	age_ranges = [[18, 25], [25, 30], [30, 40], [40, 60], [60, 130]]

	count = 0
	for user in users:
		if user.user_type != current_user.user_type: # Make sure mentors are assigned to mentees and vice versa
			if user.q[1] == 3 or user.q[1] == current_user.q[0]: # Make sure gender prefeerence match up
				if user.q[3] == current_user.q[3]:
					if user.age >= age_ranges[current_user.q[4] - 1][0] and user.age <= age_ranges[current_user.q[4] - 1][1]:
						if len(current_user.user_matches) <= 5 and count != 5:
							current_user.user_matches[count][1] = 0
							current_user.user_matches[count][0] = user
							count += 1
						else:
							match = []
							match.append(user)
							match.append(0)
							current_user.user_matches.append(match)

def compat(current_user):
	"""Compute compatibility amongst users"""
	# If the current user is a mentor
	if current_user.user_type:
		count = 0
		for user in current_user.user_matches:
			if user[0] != current_user and user[0] != '':
				# 5) How much time would you like to invest in your mentor-mentee relationship?
				equal_q_answer(current_user, user[0], 5, count)

				# 6) What is your experience level in your field?
				higher(current_user, user[0], 6, count)
				# 7) How good are your networking skills?
				higher(current_user, user[0], 7, count)

				# 17) What kind of work do you want to do?
				equal_q_answer(current_user, user[0], 17, count)
				# 8) How much do you value integrity?
				#equal_q_answer(current_user, user[0], 8, count)

				# 8) How good are you organizational skills?
				higher(current_user, user[0], 8, count)

				# 9) How good are your communication skills?
				equal_or_higher(current_user, user[0], 9, count)

				# 16) What is your primary career goal?
				equal_q_answer(current_user, user[0], 16, count)

				# 10) How good are your time management skills?
				# 11) How would you rate your work ethic?
				# 12) How flexible/adaptable are you?
				for i in range(10, 13):
					equal_or_higher(current_user, user[0], i, count)

				# 15) What kind of learner are you?
				equal_q_answer(current_user, user[0], 15, count)

				# 13) How would you rate your ability to work with others?
				equal_or_higher(current_user, user[0], 13, count)

				# 14) How introverted/extroverted are you?
				equal_q_answer(current_user, user[0], 17, count)

				# No one is 100% compatible -- account for that
				if current_user.user_matches[count][1] >= 100:
					current_user.user_matches[count][1] = 99.0
				else:
					current_user.user_matches[count][1] = round(current_user.user_matches[count][1], 1)

				if current_user.user_matches[count][0] == '':
					current_user.user_matches[count][1] = 0

				count += 1
	else:
		count = 0
		for user in current_user.user_matches:
			if user[0] != current_user and user[0] != '':
				# 5) How much time would you like to invest in your mentor-mentee relationship?
				equal_q_answer(current_user, user[0], 5, count)

				# 6) What is your experience level in your field?
				lower(current_user, user[0], 6, count)
				# 7) How good are your networking skills?
				lower(current_user, user[0], 7, count)

				# 17) What kind of work do you want to do?
				equal_q_answer(current_user, user[0], 17, count)
				# 8) How much do you value integrity?
				#equal_q_answer(current_user, user[0], 8, count)

				# 8) How good are you organizational skills?
				lower(current_user, user[0], 8, count)

				# 9) How good are your communication skills?
				equal_or_lower(current_user, user[0], 9, count)

				# 16) What is your primary career goal?
				equal_q_answer(current_user, user[0], 16, count)

				# 10) How good are your time management skills?
				# 11) How would you rate your work ethic?
				# 12) How flexible/adaptable are you?
				for i in range(10, 13):
					equal_or_lower(current_user, user[0], i, count)

				# 15) What kind of learner are you?
				equal_q_answer(current_user, user[0], 15, count)

				# 13) How would you rate your ability to work with others?
				equal_or_lower(current_user, user[0], 13, count)

				# 14) How introverted/extroverted are you?
				equal_q_answer(current_user, user[0], 14, count)

				# No one is 100% compatible -- account for that
				if current_user.user_matches[count][1] >= 100:
					current_user.user_matches[count][1] = 99.0
				else:
					current_user.user_matches[count][1] = round(current_user.user_matches[count][1], 1)

				if current_user.user_matches[count][0] == '':
					current_user.user_matches[count][1] = 0

				count += 1
	sort_matches(current_user)


def sort_matches(current_user):
	"""Sort matches by % compatibility"""
	for i in range(len(current_user.user_matches)):
		for j in range(len(current_user.user_matches) - i - 1):
			if current_user.user_matches[j][1] < current_user.user_matches[j + 1][1]:
				current_user.user_matches[j], current_user.user_matches[j + 1] = current_user.user_matches[j + 1], current_user.user_matches[j]
