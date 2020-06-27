"""
CIS 422 Project 2: User Interface File

Last Modified: 3/7/20

Authors: Olivia Pannell, Ben Verney,
Bethany Van Meter, and Mikayla Campbell
"""

# Imports
from tkinter import *
from tkinter import Text, messagebox

import compatibility as c
import database as d

# Specific font variables
SMALL_FONT = ("Helvetica", 14)
TITLE_FONT = ("Helvetica", 50, "bold")
TAB_FONT = ("Helvetica", 18, "bold italic")
MATCH_FONT = ("Helvetica", 22, "bold")
PERCENT_FONT = ("Helvetica", 12, "bold italic")
QUESTION_FONT = ("Roboto", 15, "bold")
BUTTON_FONT = ("Helvetica", 14)
INFO_FONT = ("Helvetica", 16, "bold")

# Flag set to bypass any error checking that occurs in login page, signup page, namepreference page, or questionnaires.
# This is just for testing.
DEBUG = FALSE

# List of Majors/Subjects
MAJORS = ["Accounting", "Anthropology", "Architecture", "Art", "Art and technology", "Art history", "Arts management",
		   "Asian studies", "Biochemistry", "Biology", "Business administration", "Chemistry", "Chinese", "Cinema studies",
		   "Classics", "Communication disorders and sciences", "Comparative literature", "Computer and information science",
		   "Dance", "Earth sciences", "Economics", "Educational foundations", "English", "Environmental science","Environmental studies",
		   "Ethnic studies", "Family and human services", "Folklore and public culture", "French", 'General science',
		   "General social science", "Geography", "German", "History", "Humanities", "Human physiology", "Interior architecture",
		   "International studies", "Italian", "Japanese", "Journalism", "Journalism: advertising", "Journalism: mediastudies",
		   "Journalism: public relations", "Judaic studies", "Landscape architecture", "Latin American studies", "Linguistics",
		   "Marine biology", "Mathematics", "Mathematics and computer science", "Medieval studies", "Music", "Music composition",
		   "Music education", "Music: jazz studies", "Music performance", "Philosophy", "Physics", "Planning, public policy and management",
		   "Political science", "Product design", "Psychology", "Religious studies", "Romance languages", "Russian, East European, and Eurasian studies",
		   "Sociology", "Spanish", "Spatial data science and technology", "Theater arts", "Women's, gender, and sexuality studies"]

# Users questionnaire answers will be saved to this list
questionnaireAnswers = [-1, -1, -1, -1, -1, -1, -1, -1, -1,  -1,  -1, -1,  -1,  -1, -1, -1, -1, -1]

#Creates new user as a user class
new_account = c.User(0, "", "", 0, "", [], "", "", "", "")

# Main class that controls which frame is on top (shown to the user)
# in any given instance
class start(Tk):
	# Initializes the tk original window
	def __init__(self, *args, **kwargs):
		global questionnaireAnswers
		# initializes container for frames
		Tk.__init__(self, *args, **kwargs)
		container = Frame(self, height=500, width=450, bg="medium sea green")
		container.pack(side="top", fill="both", expand=True)
		self.pages = {}

		# For every page initialize a frame for it
		for page in (MainMenu, LoginPage, SignUpPage, HomePage, QuestionPage, QuestionPage2, ProfilePage,
					OtherProfilePage, QuestionPage3, QuestionPage4, QuestionPage5, NamePreferencesPage):
			frame = page(container, self)
			self.pages[page] = frame
			frame.place(relx=0.0, rely=0.0, height=425, width=600)
			frame.config(bg='medium sea green')

		self.show_frame(MainMenu)

	#Bring chosen frame to the front
	def show_frame(self, controller):
		frame = self.pages[controller]
		frame.tkraise()

# Contains everything for the Main Menu frame
# This Includes a help button, and sign-in/login buttons.
class MainMenu(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		lbl1 = Label(self, text='MENTOR MEETER', bg="medium sea green", fg="white", font=TITLE_FONT)
		lbl1.place(relx=0.5, rely=0.20, anchor=CENTER)

		lbl2 = Label(self, text='Find your mentor today!', bg="medium sea green", fg="white", font=SMALL_FONT)
		lbl2.place(relx=0.5, rely=0.30, anchor=CENTER)	
		# Button takes user to login page
		b0 = Button(self, text="Login", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(LoginPage))
		b0.place(relx=0.5, rely=0.40, width=150, anchor=CENTER)
		#button takes user to signup page.
		b1 = Button(self, text="Sign-Up", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(SignUpPage))
		b1.place(relx=0.5, rely=0.50, width=150, anchor=CENTER)

# Contains everything for the Login Page frame.
# This is for the user who already has an existing account.
class LoginPage(Frame):

	def __init__(self, parent, controller):
		global username1
		global userlbl
		global password1
		global passlbl

		Frame.__init__(self, parent)
		lbl1 = Label(self, text='MENTOR MEETER', bg="medium sea green", fg="white", font=TITLE_FONT)
		lbl1.place(relx=0.5, rely=0.20, anchor=CENTER)

		lbl2 = Label(self, text='Find your mentor today!', bg="medium sea green", fg="white", font=SMALL_FONT)
		lbl2.place(relx=0.5, rely=0.30, anchor=CENTER)
		# Button takes the user back to the Main Menu
		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

		# Saves users input as username in username1	
		userlbl = Label(self, text='Username:', bg="medium sea green", fg="white", font=SMALL_FONT)
		userlbl.place(relx=0.30, rely=0.40, anchor=CENTER)
		username1 = Entry(self)
		username1.place(relx=0.55, rely=0.40, anchor=CENTER)

		#Saves users input as password in password1
		passlbl = Label(self, text='Password:', bg="medium sea green", fg="white", font=SMALL_FONT)
		passlbl.place(relx=0.30, rely=0.50, anchor=CENTER)
		password1 = Entry(self, show='*')
		password1.place(relx=0.55, rely=0.50, anchor=CENTER)

		# Button that calls loginerror to potentially log a user in
		log = Button(self, text="Login", highlightbackground="medium sea green", padx=10,
					 command=lambda: self.loginerror(parent, controller))
		log.place(relx=0.62, rely=0.62, anchor=SW)

	# Checking if username and password entrys were filled out before
	# clicking login
	def loginerror(self, parent, controller):
		global username1
		global password1
		global userlbl
		global passlbl

		# Quick way for testing to go to homepage
		if(DEBUG):
			win.pages[HomePage].load(parent, controller)
			controller.show_frame(HomePage)
			return

		# Error message that displays if at least one of the Username/Password
		# entries are not filled out
		errorlbl = Label(self, text='        *Please fill out all sections.    ', bg="medium sea green", fg="red4", font=SMALL_FONT)
		errorlbl2 = Label(self, text='*Incorrect Password or Username.', bg="medium sea green", fg="red4", font=SMALL_FONT)

		# If the username entry is empty turn text red
		if not username1.get():
			userlbl.config(text='*Username:', fg='red4')
			errorlbl.place(relx=0.43, rely=0.59, anchor=CENTER)

		# If the password entry is empty turn text red
		if not password1.get():
			passlbl.config(text='*Password:', fg='red4')
			errorlbl.place(relx=0.43, rely=0.59, anchor=CENTER)

		# Resets previous username error text
		if username1.get():
			userlbl.config(text='Username:', fg='white')

		# Resets previous password error text
		if password1.get():
			passlbl.config(text='Password:', fg='white')

		# If both are filled out
		if username1.get() and password1.get():
			# Checks if the username and password are in the database
			valid, usr = c.login_check(username1.get(), password1.get())
			#c.current_user = usr
			if valid:
				c.current_user = usr
				# Clears password entry for security reasons
				password1.delete(0, 'end')
				# If they are get rid of error messages and call the homepage
				errorlbl = Label(self, text='*Incorrect Password or Username.', bg="medium sea green", fg="medium sea green",
							 font=SMALL_FONT)
				errorlbl.place(relx=0.43, rely=0.59, anchor=CENTER)
				# Check to see if current user is mentor or mentee
				# Guides them to corresponding page
				win.pages[HomePage].load(parent, controller)
				controller.show_frame(HomePage)
			else:
				errorlbl2.place(relx=0.43, rely=0.59, anchor=CENTER)

# Contains everything for the Sign Up Page frame.
# This is where the user can create a new account.
class NamePreferencesPage(Frame):

	def __init__(self, parent, controller):
		global firstname, lastname, mentormentee, firstnamelbl, lastnamelbl
		global mentormenteelbl, bio, biolbl
		Frame.__init__(self, parent)

		lbl2 = Label(self, text='Please fill out all fields:', bg="medium sea green", fg="white",
								 font=QUESTION_FONT)
		lbl2.place(relx=0.5, rely=0.10, anchor=CENTER)
		# Button that takes user back to the signup page.
		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
								command=lambda: controller.show_frame(SignUpPage))
		b0.place(relx=0.0, rely=1.0, anchor=SW)
		# Button that calls signuperror to potentially move onto the questionnaire 
		b2 = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
								command=lambda: self.signuperror(parent, controller))
		b2.place(relx=1.0, rely=1.0, anchor=SE)

		# Saves users input as their first name in firstname
		firstnamelbl = Label(self, text='First name:', bg="medium sea green", fg="white", font=SMALL_FONT)
		firstnamelbl.place(relx=0.272, rely=0.20, anchor=CENTER)
		firstname = Entry(self)
		firstname.place(relx=0.55, rely=0.20, anchor=CENTER)

		# Saves users input as their last name in lastname
		lastnamelbl = Label(self, text='Last name:', bg="medium sea green", fg="white", font=SMALL_FONT)
		lastnamelbl.place(relx=0.275, rely=0.30, anchor=CENTER)
		lastname = Entry(self)
		lastname.place(relx=0.55, rely=0.30, anchor=CENTER)

		# This is where the user enters their bio and its saved in bio
		biolbl = Label(self, text='Please enter a little about yourself (250 char max):', bg="medium sea green", fg="white", font=QUESTION_FONT)
		biolbl.place(relx=0.5, rely=0.60, anchor=CENTER)
		bio = Entry(self, width=60)
		bio.place(relx=0.5, rely=0.70, anchor=CENTER)

		mentormentee = StringVar()
		mentormenteelbl = Label(self, text='Are you looking to be a mentor or mentee?', bg="medium sea green", fg="white",
					font=QUESTION_FONT)
		mentormenteelbl.place(relx=0.5, rely=0.43, anchor=CENTER)

		mentorrb = Radiobutton(self, text="Mentor", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
						  activebackground="medium sea green", variable=mentormentee, value=1, tristatevalue=2)
		mentorrb.place(relx=0.3, rely=0.5, anchor=W)

		menteerb = Radiobutton(self, text="Mentee", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
							activebackground="medium sea green", variable=mentormentee, value=0, tristatevalue=2)
		menteerb.place(relx=0.6, rely=0.5, anchor=W)

		pagenum = Label(self, text='pg 1/6', bg="medium sea green", font=("Helvetica", 14))
		pagenum.place(relx=0.82, rely=0.99, anchor=SW)


	# Error checking on the signup page
	def signuperror(self, parent, controller):
		global firstname, lastname, mentormentee, firstnamelbl, lastnamelbl
		global mentormenteelbl, bio, biolbl

		#debug code so i dont have to enter a password every time i want to check the questionanaire
		#set debug = true to bypass the create account check.
		if(DEBUG):
				controller.show_frame(QuestionPage)
				return

		# Error message that displays if at least one of the entry fields is not
		# filled in.
		# Spaces are used here to fully cover larger error labels
		errorlbl = Label(self, text='                     *Please fill out red sections.                    ',
				bg="medium sea green", fg="red4", font=SMALL_FONT)

		# If the first name entry is empty turn text red, else white
		if not firstname.get():
				firstnamelbl.config(text='*First name:', fg='red4')
				errorlbl.place(relx=0.50, rely=0.80, anchor=CENTER)
		else:
				firstnamelbl.config(text='First name:', fg='white')

		# If the last name entry is empty turn text red, else white
		if not lastname.get():
				lastnamelbl.config(text='*Last name:', fg='red4')
				errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
		else:
				lastnamelbl.config(text='Last name:', fg='white')

		# If the mentor/mentee entry is empty turn text red, else white
		if not mentormentee.get():
				mentormenteelbl.config(text='*Are you looking to be a mentor or mentee?', fg='red4')
				mentormenteelbl.place(relx=0.5, rely=0.43, anchor=CENTER)
		else:
				mentormenteelbl.config(text='Are you looking to be a mentor or mentee?', fg='white')

		# If all entries are filled out
		if firstname.get() and lastname.get() and mentormentee.get():
				# add information to user class to be later added into database
				new_account.first = firstname.get()
				new_account.last = lastname.get()
				new_account.user_type = int(mentormentee.get())
				new_account.bio = (bio.get()[:250])

				controller.show_frame(QuestionPage)

# Contains everything for the Sign Up Page frame.
# This is where the user can create a new account.
class SignUpPage(Frame):

	def __init__(self, parent, controller):
		global newusername, newpassword, newemail, passcheck, newuserlbl, newpasslbl, newemaillbl, pclbl

		Frame.__init__(self, parent)
		lbl1 = Label(self, text='MENTOR MEETER', bg="medium sea green", fg="white", font=TITLE_FONT)
		lbl1.place(relx=0.5, rely=0.20, anchor=CENTER)
		lbl2 = Label(self, text='Welcome! Create your new account now!', bg="medium sea green", fg="white",
					 font=SMALL_FONT)
		lbl2.place(relx=0.5, rely=0.30, anchor=CENTER)

		# Button that takes user back to the main menu page.
		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

		# Button that calls signuperror to potentially move onto the namepreferencepage 
		b2 = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
					command=lambda: self.signuperror(parent, controller))
		b2.place(relx=1.0, rely=1.0, anchor=SE)

		# Saves users input as their new username in newusername
		newuserlbl = Label(self, text='New Username:', bg="medium sea green", fg="white", font=SMALL_FONT)
		newuserlbl.place(relx=0.272, rely=0.40, anchor=CENTER)
		newusername = Entry(self)
		newusername.place(relx=0.55, rely=0.40, anchor=CENTER)

		# Saves users input as their new password in newpassword
		newpasslbl = Label(self, text='New Password:', bg="medium sea green", fg="white", font=SMALL_FONT)
		newpasslbl.place(relx=0.275, rely=0.50, anchor=CENTER)
		newpassword = Entry(self, show='*') #"show='*'" hides the password to the user for security 
		newpassword.place(relx=0.55, rely=0.50, anchor=CENTER)

		# Saves users input as for their password verification in passcheck
		pclbl = Label(self, text='Re-Enter Password:', bg="medium sea green", fg="white", font=SMALL_FONT)
		pclbl.place(relx=0.25, rely=0.60, anchor=CENTER)
		passcheck = Entry(self, show = '*')
		passcheck.place(relx=0.55, rely=0.60, anchor=CENTER)

		# Saves users input as their new email in newemail
		newemaillbl = Label(self, text='Email:', bg="medium sea green", fg="white", font=SMALL_FONT)
		newemaillbl.place(relx=0.325, rely=0.70, anchor=CENTER)
		newemail = Entry(self)
		newemail.place(relx=0.55, rely=0.70, anchor=CENTER)

	# Error checking on the signup page
	def signuperror(self, parent, controller):
		global newusername, newpassword, newemail, passcheck, newuserlbl, newpasslbl, newemaillbl, pclbl

		#debug code so i dont have to enter a password every time i want to check the questionanaire
		#set debug = true to bypass the create account check.
		if(DEBUG):
			controller.show_frame(NamePreferencesPage)
			return

		# Error message that displays if at least one of the entry fields is not
		# filled in.
		# Spaces are used here to fully cover larger error labels
		errorlbl = Label(self, text='              *Please fill out all sections.              ',
			bg="medium sea green", fg="red4", font=SMALL_FONT)
 
		# Error message that displays if password and password check dont match.
		errorlbl2 = Label(self, text='*Passwords did not match. Please try again.',
			bg="medium sea green", fg="red4", font=SMALL_FONT)

		# Error message that displays if email check doesn't pass.
		errorlbl3 = Label(self, text='           *Invalid email. Please try again.         ',
			bg="medium sea green", fg="red4", font=SMALL_FONT)

		# If the username entry is empty turn text red, else white
		if not newusername.get():
			newuserlbl.config(text='*New Username:', fg='red4')
			errorlbl.place(relx=0.50, rely=0.80, anchor=CENTER)
		else:
			newuserlbl.config(text='Username:', fg='white')

		# If the password entry is empty turn text red, else white
		if not newpassword.get():
			newpasslbl.config(text='*New Password:', fg='red4')
			errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
		else:
			newpasslbl.config(text='New Password:', fg='white')

		# If the user does not enter the password twice it turns red, else white
		if not passcheck.get():
			pclbl.config(text='*Re-Enter Password:', fg='red4')
			errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
		else:
			pclbl.config(text='Re-Enter Password:', fg='white')

		# If the email entry is empty turn text red, else white
		if not newemail.get():
			newemaillbl.config(text='*Email:', fg='red4')
			errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
		else:
			newemaillbl.config(text='Email:', fg='white')

		# If all entries are filled out
		if newusername.get() and newpassword.get() and passcheck.get() and newemail.get():
			# Check for password and password check to match
			if newpassword.get() == passcheck.get():
				#Check for valid email with @ -> newemail.get().count(at)
				if check_email(newemail.get()):
					# Check to ensure the username is not taken
					if check_username(newusername.get()):
						# add information to user class to be later added into database
						#c.current_user = c.User(0, None, None, 0, None, {}, None, None, None, None)
						#c.current_user.username = newusername.get()
						new_account.username = newusername.get()
						new_account.password = newpassword.get()
						new_account.email = newemail.get()

						# Clears password entry for security reasons
						newpassword.delete(0, 'end')
						passcheck.delete(0, 'end')
						errorlbl = Label(self, text='*Passwords did not match. Please try again.', bg="medium sea green", fg="medium sea green",
									 font=SMALL_FONT)
						errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
						controller.show_frame(NamePreferencesPage)
					else:
						errorlbl.config(text='*Username is taken, please enter a new username', fg='red4')
						errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
				else:
					newemaillbl.config(text='*Email:', fg='red4')
					errorlbl3.place(relx=0.50, rely=0.8, anchor=CENTER)
			else:
				newpasslbl.config(text='*New Password:', fg='red4')
				pclbl.config(text='*Re-Enter Password:', fg='red4')
				errorlbl2.place(relx=0.50, rely=0.8, anchor=CENTER)

# Contains everything for the Home Page frame.
# This is where the user can see pontential matches.
class HomePage(Frame):
	#Initalizes frame
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

	#Seperate load function so the the homepage is reloaded with the current users matches
	def load(self, parent, controller):
		#Top tab navigation buttons
		b0 = Button(self, text="Potential Matches", width=30, font=TAB_FONT)
		b0.place(relx=0.25, rely=0.02, anchor=CENTER)
		b1 = Button(self, text="Profile", padx=50, font=TAB_FONT, command=lambda: [win.pages[ProfilePage].load(parent, controller), controller.show_frame(ProfilePage)])
		b1.place(relx=0.65, rely=0.02, anchor=CENTER)
		b2 = Button(self, text="Logout", padx=40, font=TAB_FONT, command=lambda: controller.show_frame(MainMenu))
		b2.place(relx=0.90, rely=0.02, anchor=CENTER)

		# First given match
		# check to make sure a user has any matches
		if c.current_user.user_matches[0][0] == "":
			fr1 = Frame(self, width=570, height=70, bg='medium sea green')
			fr1.place(relx=0.50, rely=0.17, anchor=CENTER)
			userlbl = Label(self, text='No available matches at this time...', fg="white", font=MATCH_FONT, bg = 'medium sea green')
			userlbl.place(relx=0.5, rely=0.15, anchor=CENTER)
		else:
			#Displays first match
			fr1 = Frame(self, width=570, height=70, bg='white')
			fr1.place(relx=0.50, rely=0.17, anchor=CENTER)

			userlbl = Label(fr1, text=c.current_user.user_matches[0][0], fg="black", font=MATCH_FONT)
			userlbl.place(relx=0.05, rely=0.3, anchor=W)

			userlbl = Label(fr1, text='Compatibility: ' + str(c.current_user.user_matches[0][1]) + '%', fg="grey40", font=PERCENT_FONT)
			userlbl.place(relx=0.05, rely=0.7, anchor=W)

			b2 = Button(fr1, text="Learn More...", padx=10, font=SMALL_FONT, command=lambda: [win.pages[OtherProfilePage].loadd(parent, controller, c.current_user.user_matches[0][0]), controller.show_frame(OtherProfilePage)])
			b2.place(relx=0.90, rely=0.75, anchor=CENTER)

			b2 = Button(fr1, text="Contact", padx=30, font=SMALL_FONT,
				command=lambda: connect(str(c.current_user.user_matches[0][0].first), c.current_user.user_matches[0][0].last, c.current_user.user_matches[0][0].email))
			b2.place(relx=0.90, rely=0.25, anchor=CENTER)

		#Second given match
		# Checks to see if the user has at least a second match
		# If not returns and doesnt display anything
		if c.current_user.user_matches[1][0] == "":
			fr2 = Frame(self, width = 570, height = 70, bg = 'medium sea green')
			fr2.place(relx=0.50, rely=0.35, anchor=CENTER)
		else:
			#Displays second match
			fr2 = Frame(self, width = 570, height = 70, bg = 'white')
			fr2.place(relx=0.50, rely=0.35, anchor=CENTER)

			userlbl = Label(fr2, text=c.current_user.user_matches[1][0], fg="black", font=MATCH_FONT)
			userlbl.place(relx=0.05, rely=0.3, anchor=W)

			userlbl = Label(fr2, text='Compatibility: ' + str(c.current_user.user_matches[1][1]) + '%', fg="grey40", font=PERCENT_FONT)
			userlbl.place(relx=0.05, rely=0.7, anchor=W)

			b2 = Button(fr2, text="Learn More...", padx=10, font=SMALL_FONT, command=lambda: [win.pages[OtherProfilePage].loadd(parent, controller, c.current_user.user_matches[1][0]), controller.show_frame(OtherProfilePage)])
			b2.place(relx=0.90, rely=0.75, anchor=CENTER)

			b2 = Button(fr2, text="Contact", padx=30, font=SMALL_FONT,
				command=lambda: connect(str(c.current_user.user_matches[1][0].first), c.current_user.user_matches[1][0].last, c.current_user.user_matches[1][0].email))
			b2.place(relx=0.90, rely=0.25, anchor=CENTER)


		#Third given match
		# Checks to see if the user has at least a third match
		# If not returns and doesnt display anything
		if c.current_user.user_matches[2][0] == "":
			fr3 = Frame(self, width = 570, height = 70, bg = 'medium sea green')
			fr3.place(relx=0.50, rely=0.53, anchor=CENTER)
		else:
			#Displays third match
			fr3 = Frame(self, width = 570, height = 70, bg = 'white')
			fr3.place(relx=0.50, rely=0.53, anchor=CENTER)

			userlbl = Label(fr3, text=c.current_user.user_matches[2][0], fg="black", font=MATCH_FONT)
			userlbl.place(relx=0.05, rely=0.3, anchor=W)

			userlbl = Label(fr3, text='Compatibility: ' + str(c.current_user.user_matches[2][1]) + '%', fg="grey40", font=PERCENT_FONT)
			userlbl.place(relx=0.05, rely=0.7, anchor=W)

			b2 = Button(fr3, text="Learn More...", padx=10, font=SMALL_FONT, command=lambda: [win.pages[OtherProfilePage].loadd(parent, controller, c.current_user.user_matches[2][0]), controller.show_frame(OtherProfilePage)])
			b2.place(relx=0.90, rely=0.75, anchor=CENTER)

			b2 = Button(fr3, text="Contact", padx=30, font=SMALL_FONT,
				command=lambda: connect(str(c.current_user.user_matches[2][0].first), c.current_user.user_matches[2][0].last, c.current_user.user_matches[2][0].email))
			b2.place(relx=0.90, rely=0.25, anchor=CENTER)


		#Fourth given match
		# Checks to see if the user has at least a fourth match
		# If not returns and doesnt display anything
		if c.current_user.user_matches[3][0] == "":
			fr4 = Frame(self, width = 570, height = 70, bg = 'medium sea green')
			fr4.place(relx=0.50, rely=0.71, anchor=CENTER)
		else:
			#Displays fourth match
			fr4 = Frame(self, width = 570, height = 70, bg = 'white')
			fr4.place(relx=0.50, rely=0.71, anchor=CENTER)

			userlbl = Label(fr4, text=c.current_user.user_matches[3][0], fg="black", font=MATCH_FONT)
			userlbl.place(relx=0.05, rely=0.3, anchor=W)

			userlbl = Label(fr4, text='Compatibility: ' + str(c.current_user.user_matches[3][1]) + '%', fg="grey40", font=PERCENT_FONT)
			userlbl.place(relx=0.05, rely=0.7, anchor=W)

			b2 = Button(fr4, text="Learn More...", padx=10, font=SMALL_FONT, command=lambda: [win.pages[OtherProfilePage].loadd(parent, controller, c.current_user.user_matches[3][0]), controller.show_frame(OtherProfilePage)])
			b2.place(relx=0.90, rely=0.75, anchor=CENTER)

			b2 = Button(fr4, text="Contact", padx=30, font=SMALL_FONT,
				command=lambda: connect(str(c.current_user.user_matches[3][0].first), c.current_user.user_matches[3][0].last, c.current_user.user_matches[3][0].email))
			b2.place(relx=0.90, rely=0.25, anchor=CENTER)


		#Fifth given match
		# Checks to see if the user has a fifth match
		# If not returns and doesnt display anything
		if c.current_user.user_matches[4][0] == "":
			fr5 = Frame(self, width = 570, height = 70, bg = 'medium sea green')
			fr5.place(relx=0.50, rely=0.89, anchor=CENTER)
		else:
			#Displays fifth match
			fr5 = Frame(self, width = 570, height = 70, bg = 'white')
			fr5.place(relx=0.50, rely=0.89, anchor=CENTER)

			userlbl = Label(fr5, text=c.current_user.user_matches[4][0], fg="black", font=MATCH_FONT)
			userlbl.place(relx=0.05, rely=0.3, anchor=W)

			userlbl = Label(fr5, text='Compatibility: ' + str(c.current_user.user_matches[4][1]) + '%', fg="grey40", font=PERCENT_FONT)
			userlbl.place(relx=0.05, rely=0.7, anchor=W)

			b2 = Button(fr5, text="Learn More...", padx=10, font=SMALL_FONT, command=lambda: [win.pages[OtherProfilePage].loadd(parent, controller, c.current_user.user_matches[4][0]), controller.show_frame(OtherProfilePage)])
			b2.place(relx=0.90, rely=0.75, anchor=CENTER)

			b2 = Button(fr5, text="Contact", padx=30, font=SMALL_FONT, 
				command=lambda: connect(str(c.current_user.user_matches[4][0].first), c.current_user.user_matches[4][0].last, c.current_user.user_matches[4][0].email))
			b2.place(relx=0.90, rely=0.25, anchor=CENTER)

# Contains the current users profile page.
# The user can see their name as well as some of their information.
class ProfilePage(Frame):
	# Initializes the profilepage frame
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
	#Function that reloads information based on the current user once they login or signup
	def load(self, parent, controller):
		# Top tab navigation buttons 
		b0 = Button(self, text = "Potential Matches", width = 30, font = TAB_FONT, command=lambda: controller.show_frame(HomePage))
		b0.place(relx=0.25, rely=0.02, anchor=CENTER)
		b1 = Button(self, text="Profile", padx = 50, font = TAB_FONT)
		b1.place(relx=0.65, rely=0.02, anchor=CENTER)
		b2 = Button(self, text="Logout", padx = 40, font = TAB_FONT, command=lambda: controller.show_frame(MainMenu))
		b2.place(relx=0.90, rely=0.02, anchor=CENTER)
		fr1 = Frame(self, width = 570, height = 380, bg = 'white')
		fr1.place(relx=0.50, rely=0.52, anchor=CENTER)

		#Displays users name
		lbl1 = Label(fr1, text=c.current_user.first + " " + c.current_user.last, bg="white", fg="sea green", font=(
			"Helvetica", 46, "bold"))
		lbl1.place(relx=0.5, rely=0.15, anchor=CENTER)

		# Random line for looks
		fr2 = Frame(fr1, width = 500, height = 5, bg = 'grey70')
		fr2.place(relx=0.5, rely=0.3, anchor=CENTER)
		Label(fr1, text="     Biography:     ", bg="white", fg="black", font=TAB_FONT).place(relx=0.5, rely=0.3, anchor=CENTER)

		# Random line for looks
		fr3 = Frame(fr1, width = 500, height = 5, bg = 'grey70')
		fr3.place(relx=0.5, rely=0.60, anchor=CENTER)

		# Displays the users bio
		lbl2 = Label(fr1, text=c.current_user.bio, bg="white", fg="gray20", 
			font=INFO_FONT, wraplength = 510, justify = CENTER)
		lbl2.place(relx=0.5, rely=0.45, anchor=CENTER)

		# More about me sections 
		Label(fr1, text="     A little more about me...     ", bg="white", fg="black", font=TAB_FONT).place(relx=0.5, rely=0.60, anchor=CENTER)

		Label(fr1, text="Age:", bg="white", fg="black", font=INFO_FONT).place(relx=0.1, rely=0.70, anchor=W)
		Label(fr1, text=c.current_user.age, bg="white", fg="gray20", font=INFO_FONT).place(relx=0.17, rely=0.70, anchor=W)
		# Gender label and answer from current user
		Label(fr1, text="Gender: ", bg="white", fg="black", font=INFO_FONT).place(relx=0.1, rely=0.80, anchor=W)
		Label(fr1, text=c.current_user.gender, bg="white", fg="gray20", font=INFO_FONT).place(relx=0.21, rely=0.80, anchor=W)

		# Career Field and answer from current user
		Label(fr1, text="Career Field:", bg="white", fg="black", font=INFO_FONT).place(relx=0.1, rely=0.90, anchor=W)
		Label(fr1, text= MAJORS[c.current_user.q[3]], bg="white", fg="gray20", font=INFO_FONT).place(relx=0.27, rely=0.90, anchor=W)

# Contains the other users profile page.
# The user can see potential matches name as well as some of their information.
class OtherProfilePage(Frame):
	#Initializes the other profile page frame
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

	# Loads the given matches information for their profile page
	# NOTE: even though the variable name is mentor this can be either a mentee or mentor.
	def loadd(self, parent, controller, mentor):
		# b0, b1, and b2 are top tabs for navigation 
		b0 = Button(self, text = "Potential Matches", width = 30, font = TAB_FONT, command=lambda: controller.show_frame(HomePage))
		b0.place(relx=0.25, rely=0.02, anchor=CENTER)
		b1 = Button(self, text="Profile", padx = 50, font = TAB_FONT, command=lambda: controller.show_frame(ProfilePage))
		b1.place(relx=0.65, rely=0.02, anchor=CENTER)
		b2 = Button(self, text="Logout", padx = 40, font = TAB_FONT, command=lambda: controller.show_frame(MainMenu))
		b2.place(relx=0.90, rely=0.02, anchor=CENTER)
		fr1 = Frame(self, width = 570, height = 340, bg = 'white')
		fr1.place(relx=0.50, rely=0.48, anchor=CENTER)

		#Back button that takes user back to the homepage
		b3 = Button(self, text="Back", padx = 30, font = TAB_FONT, highlightbackground = 'medium sea green', command=lambda: controller.show_frame(HomePage))
		b3.place(relx=0.12, rely=0.93, anchor=CENTER)

		# Random line for looks
		fr4 = Frame(fr1, width = 500, height = 5, bg = 'grey70')
		fr4.place(relx=0.5, rely=0.08, anchor=CENTER)
		Label(fr1, text="     Match's Profile:     ", bg="white", fg="black", font=TAB_FONT).place(relx=0.5, rely=0.08, anchor=CENTER)
		# Displays mentors/mentees name
		lbl1 = Label(fr1, text=mentor.first + " " + mentor.last, bg="white", fg="sea green", font=("Helvetica", 46, "bold"))
		lbl1.place(relx=0.5, rely=0.22, anchor=CENTER)

		# Random line for looks
		fr2 = Frame(fr1, width = 500, height = 5, bg = 'grey70')
		fr2.place(relx=0.5, rely=0.35, anchor=CENTER)
		Label(fr1, text="     Biography:     ", bg="white", fg="black", font=TAB_FONT).place(relx=0.5, rely=0.35, anchor=CENTER)

		# Random line for looks
		fr3 = Frame(fr1, width = 500, height = 5, bg = 'grey70')
		fr3.place(relx=0.5, rely=0.67, anchor=CENTER)

		# Displays the users bio
		lbl2 = Label(fr1, text=mentor.bio, bg="white", fg="gray20", 
			font=INFO_FONT, wraplength = 510, justify = CENTER)
		lbl2.place(relx=0.5, rely=0.5, anchor=CENTER)

		# More about me sections 
		Label(fr1, text="    A little more about me...    ", bg="white", fg="black", font=TAB_FONT).place(relx=0.5, rely=0.67, anchor=CENTER)
		# Age label and answer from current user
		Label(fr1, text="Age:", bg="white", fg="black", font=INFO_FONT).place(relx=0.1, rely=0.74, anchor=W)
		Label(fr1, text=mentor.age, bg="white", fg="gray20", font=INFO_FONT).place(relx=0.17, rely=0.74, anchor=W)
		# Gender label and answer from current user
		Label(fr1, text="Gender: ", bg="white", fg="black", font=INFO_FONT).place(relx=0.1, rely=0.82, anchor=W)
		Label(fr1, text=mentor.gender, bg="white", fg="gray20", font=INFO_FONT).place(relx=0.21, rely=0.82, anchor=W)
		# Career Field and answer from current user
		Label(fr1, text="Career Field:", bg="white", fg="black", font=INFO_FONT).place(relx=0.1, rely=0.9, anchor=W)
		Label(fr1, text= MAJORS[mentor.q[3]], bg="white", fg="gray20", font=INFO_FONT).place(relx=0.27, rely=0.9, anchor=W)

# Contains everything for the First page of the questionaire page.
# After creating a new account the user answers questions from these
# pages to help match them up with similar mentors
class QuestionPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		global gender
		global matchgender
		global careerfield
		global userage
		gender = IntVar()
		matchgender = IntVar()
		careerfield = StringVar()

		lbl1 = Label(self, text='Please answer the following questions so we can match you with a mentor:',
					 bg="medium sea green", fg="white", font=("Roboto", 18, "bold"), wraplength = 400, justify= LEFT)
		lbl1.place(relx=0.05, rely=0.1, anchor=W)

		lbl1 = Label(self, text='What is your gender?', bg="medium sea green", fg="white", font=QUESTION_FONT)
		lbl1.place(relx=0.05, rely=0.25, anchor=W)

		maleRB = Radiobutton(self, text="Male", bg="medium sea green", selectcolor="medium sea green",
							 activebackground="medium sea green", variable=gender, value=1, font=BUTTON_FONT, tristatevalue=6,
							 command=lambda: self.removeinputgender())
		maleRB.place(relx=0.1, rely=0.36, anchor=W)

		femaleRB = Radiobutton(self, text="Female", bg="medium sea green", selectcolor="medium sea green",
							   activebackground="medium sea green", variable=gender, value=2, font=BUTTON_FONT, tristatevalue=6,
							   command=lambda: self.removeinputgender())
		femaleRB.place(relx=0.1, rely=0.43, anchor=W)

		selfidentifyRB = Radiobutton(self, text="Self Identify:", bg="medium sea green", selectcolor="medium sea green",
									 activebackground="medium sea green", variable=gender, value=3, font=BUTTON_FONT, tristatevalue=6,
									 command=lambda: self.placeinputgender())
		selfidentifyRB.place(relx=0.1, rely=0.50, anchor=W)

		matchgenderLB = Label(self, text='Who do you want to be matched with?', bg="medium sea green", fg="white",
							font=QUESTION_FONT, wraplength = 200, justify = LEFT)
		matchgenderLB.place(relx=0.53, rely=0.27, anchor=W)


		malematchRB = Radiobutton(self, text="Male", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
								  activebackground="medium sea green", variable=matchgender, value=1, tristatevalue=6)
		malematchRB.place(relx=0.58, rely=0.36, anchor=W)

		femalematchRB = Radiobutton(self, text="Female", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
									activebackground="medium sea green", variable=matchgender, value=2, tristatevalue=6)
		femalematchRB.place(relx=0.58, rely=0.43, anchor=W)

		everyonematchRB = Radiobutton(self, text="Everyone", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
									  activebackground="medium sea green", variable=matchgender, value=3,
									  tristatevalue=6)
		everyonematchRB.place(relx=0.58, rely=0.50, anchor=W)

		majorLabel = Label(self, text='What is your career field?', bg="medium sea green", fg="white",
							font=QUESTION_FONT)
		majorLabel.place(relx=0.05, rely=0.62, anchor=W)

		# Sets initial drop down option to say "Choose one"
		# This does not show in the list of options.
		careerfield.set("Choose One...")
		majoroptions = OptionMenu(self, careerfield, *MAJORS)

		#Changes the colors of the background to match our theme
		majoroptions.config(bg = 'medium sea green')

		# Changes the drop down font color to be green,
		# we can change this if you dont like it!
		majoroptions["menu"].config(bg = 'medium sea green')
		majoroptions.place(relx=0.1, rely=0.70, anchor=W)



		enterage = Label(self, text='How old are you?', bg="medium sea green", fg="white",
							font=QUESTION_FONT)
		enterage.place(relx=0.53, rely=0.62, anchor=W)
		userage = Entry(self)
		userage.place(relx=0.58, rely=0.69, anchor=W)


		pagenum = Label(self, text='pg 2/6', bg="medium sea green", font=("Helvetica", 14))
		pagenum.place(relx=0.82, rely=0.99, anchor=SW)


		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
					  command=lambda: self.checkfilledout(parent, controller))
		next.place(relx=1.0, rely=1.0, anchor=SE)

		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					  command=lambda: controller.show_frame(NamePreferencesPage))
		back.place(relx=0.0, rely=1.0, anchor=SW)


		global inputgender
		inputgender = Entry(self)



	def checkfilledout(self,parent,controller):
		global userage
		global gender
		global matchgender
		global careerfield
		global inputgender
		errorlbl = Label(self, text='              *Please fill out all sections.              ',
					 bg="medium sea green", fg="red4", font=SMALL_FONT)

		ageerror = Label(self, text='              *Please enter an integer in the age field              ',
					 bg="medium sea green", fg="red4", font=SMALL_FONT)

		gendererror = Label(self, text='                 *Please enter your gender                 ',
						 bg="medium sea green", fg="red4", font=SMALL_FONT)

		if(DEBUG):
			controller.show_frame(QuestionPage2)
			return

		if (gender.get() == 0) or (not userage.get()) or (matchgender.get() == 0) or (
				careerfield.get() == "Choose One..."):
			errorlbl.place(relx=0.5, rely=0.85, anchor=S)
			return


		if not (userage.get().isdigit()):
			ageerror.place(relx=0.5, rely=0.85, anchor=S)
			return

		if(gender.get() == 3) and (not inputgender.get()):

			gendererror.place(relx=0.5, rely=0.85, anchor=S)
			return

		self.save()
		Label(self, text='                 *Please enter your gender                 ',
			  bg="medium sea green", fg="medium sea green", font=SMALL_FONT).place(relx=0.5, rely=0.85, anchor=S)
		controller.show_frame(QuestionPage2)

	def save(self):
		global questionnaireAnswers
		global gender
		global matchgender
		global careerfield
		global userage
		global inputgender
		questionnaireAnswers[0] = gender.get()
		questionnaireAnswers[1] = matchgender.get()
		questionnaireAnswers[3] = MAJORS.index(careerfield.get())
		questionnaireAnswers[2] = int(userage.get())

		if(gender.get() == 1):
			new_account.gender = "Male"
		elif(gender.get() == 2):
			new_account.gender = "Female"
		elif (gender.get() == 3):
			new_account.gender = inputgender.get()
		else :
			print("gender error")

	def placeinputgender(self):
		global inputgender
		inputgender.place(relx=0.13, rely=0.56, anchor=W)

	def removeinputgender(self):
		global inputgender
		inputgender.place_forget()

class QuestionPage2(Frame):

	def __init__(self, parent, controller):
		global agerange
		global timeinvestment
		global experiencelevel
		global networkingskills
		agerange = IntVar()
		timeinvestment = IntVar()
		experiencelevel = IntVar()
		networkingskills = IntVar()


		Frame.__init__(self, parent)


		Label(self, text='What age range do you want to be matched with?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.1, anchor=W)

		Radiobutton(self, text="18-25", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=agerange, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.1, rely=0.17, anchor=W)

		Radiobutton(self, text="25-30", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=agerange, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.25, rely=0.17, anchor=W)

		Radiobutton(self, text="30-40", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=agerange, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.4, rely=0.17, anchor=W)

		Radiobutton(self, text="40-60", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=agerange, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.55, rely=0.17, anchor=W)

		Radiobutton(self, text="60+", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=agerange, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.7, rely=0.17, anchor=W)



		Label(self, text='How much time would you like to invest in your mentor-mentee relationship? (1 = low, 5 = high)', bg="medium sea green", fg="white",
							  font=QUESTION_FONT, wraplength = 400, justify = LEFT).place(relx=0.05, rely=0.3, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=timeinvestment, value=1, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.1, rely=0.4, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timeinvestment, value=2, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.25, rely=0.4, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timeinvestment, value=3, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.4, rely=0.4, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timeinvestment, value=4, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.55, rely=0.4, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timeinvestment, value=5, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.7, rely=0.4, anchor=W)



		Label(self, text='What is your experience level in your field?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.5, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=experiencelevel, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.1, rely=0.6, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=experiencelevel, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.25, rely=0.6, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=experiencelevel, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.4, rely=0.6, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=experiencelevel, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.55, rely=0.6, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=experiencelevel, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.7, rely=0.6, anchor=W)



		Label(self, text='How good are your networking skills?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.7, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=networkingskills, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.1, rely=0.8, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.25, rely=0.8, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.4, rely=0.8, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.55, rely=0.8, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.7, rely=0.8, anchor=W)

		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(QuestionPage))
		back.place(relx=0.0, rely=1.0, anchor=SW)

		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
					  command=lambda: self.checkfilledout(parent,controller))
		next.place(relx=1.0, rely=1.0, anchor=SE)

		pagenum = Label(self, text='pg 3/6', bg="medium sea green", font=("Helvetica", 14))
		pagenum.place(relx=0.82, rely=0.99, anchor=SW)

	def save(self):
		global agerange
		global timeinvestment
		global experiencelevel
		global networkingskills
		questionnaireAnswers[4] = agerange.get()
		questionnaireAnswers[5] = timeinvestment.get()
		questionnaireAnswers[6] = experiencelevel.get()
		questionnaireAnswers[7] = networkingskills.get()

	def checkfilledout(self, parent, controller):
		global agerange
		global timeinvestment
		global experiencelevel
		global networkingskills

		errorlbl = Label(self, text='              *Please fill out all sections.              ',
						 bg="medium sea green", fg="red4", font=SMALL_FONT)

		if (DEBUG):
			controller.show_frame(QuestionPage3)
			return

		if (agerange.get() == 0) or (timeinvestment.get() == 0) or (experiencelevel.get() == 0) or (networkingskills.get() == 0):
			errorlbl.place(relx=0.5, rely=0.9, anchor=S)
			return

		self.save()
		Label(self, text='                 *Please fill out all sections                 ',
			  bg="medium sea green", fg="medium sea green", font=SMALL_FONT).place(relx=0.5, rely=0.9, anchor=S)
		controller.show_frame(QuestionPage3)

class QuestionPage3(Frame):

	def __init__(self, parent, controller):
		global kindofwork
		global integrity
		global orginizationalskills
		global communicationskills
		kindofwork = IntVar()
		integrity = IntVar()
		orginizationalskills = IntVar()
		communicationskills = IntVar()

		Frame.__init__(self, parent)


		Label(self, text='What kind of work do you want to do?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.1, anchor=W)

		Radiobutton(self, text="Large corporate company", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.05, rely=0.17, anchor=W)

		Radiobutton(self, text="Startup/small business", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.47, rely=0.17, anchor=W)

		Radiobutton(self, text="Own your own business", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.05, rely=0.24, anchor=W)

		Radiobutton(self, text="Freelancer/contractor", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.43, rely=0.24, anchor=W)

		Radiobutton(self, text="Non-Profit", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.78, rely=0.24, anchor=W)



		Label(self, text='How much do you value integrity? (1 = low, 5 = high)', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.3, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=integrity, value=1, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.1, rely=0.4, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=integrity, value=2, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.25, rely=0.4, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=integrity, value=3, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.4, rely=0.4, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=integrity, value=4, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.55, rely=0.4, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=integrity, value=5, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.7, rely=0.4, anchor=W)



		Label(self, text='How good are your organizational skills?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.5, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=orginizationalskills, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.1, rely=0.6, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=orginizationalskills, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.25, rely=0.6, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=orginizationalskills, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.4, rely=0.6, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=orginizationalskills, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.55, rely=0.6, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=orginizationalskills, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.7, rely=0.6, anchor=W)



		Label(self, text='How good are your communication skills?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.7, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=communicationskills, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.1, rely=0.8, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=communicationskills, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.25, rely=0.8, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=communicationskills, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.4, rely=0.8, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=communicationskills, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.55, rely=0.8, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=communicationskills, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.7, rely=0.8, anchor=W)



		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
				  command=lambda: controller.show_frame(QuestionPage2))
		back.place(relx=0.0, rely=1.0, anchor=SW)

		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
				  command=lambda: self.checkfilledout(parent, controller))
		next.place(relx=1.0, rely=1.0, anchor=SE)

		pagenum = Label(self, text='pg 4/6', bg="medium sea green", font=("Helvetica", 14))
		pagenum.place(relx=0.82, rely=0.99, anchor=SW)


	def save(self):
		global kindofwork

		global orginizationalskills
		global communicationskills
		questionnaireAnswers[17] = kindofwork.get()
		#questionnaireAnswers["networkingskills"] = networkingskills.get()
		questionnaireAnswers[8] = orginizationalskills.get()
		questionnaireAnswers[9] = communicationskills.get()

	def checkfilledout(self, parent, controller):
		global kindofwork
		global integrity
		global orginizationalskills
		global communicationskills

		errorlbl = Label(self, text='              *Please fill out all sections.              ',
						 bg="medium sea green", fg="red4", font=SMALL_FONT)

		if (DEBUG):
			controller.show_frame(QuestionPage4)
			return

		if (kindofwork.get() == 0) or (orginizationalskills.get() == 0) or (integrity.get() == 0) or (communicationskills.get() == 0):
			errorlbl.place(relx=0.5, rely=0.9, anchor=S)
			return

		self.save()
		Label(self, text='                 *Please fill out all sections                 ',
			  bg="medium sea green", fg="medium sea green", font=SMALL_FONT).place(relx=0.5, rely=0.9, anchor=S)
		controller.show_frame(QuestionPage4)

class QuestionPage4(Frame):

	def __init__(self, parent, controller):
		global careergoals
		global timemanagementskills
		global workethic
		global flexiblility
		careergoals = IntVar()
		timemanagementskills = IntVar()
		workethic = IntVar()
		flexiblility = IntVar()

		Frame.__init__(self, parent)


		Label(self, text='What is your primary career goal?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.1, anchor=W)

		Radiobutton(self, text="Money", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=careergoals, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.1, rely=0.17, anchor=W)

		Radiobutton(self, text="Happiness", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=careergoals, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.24, rely=0.17, anchor=W)

		Radiobutton(self, text="Community", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=careergoals, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.44, rely=0.17, anchor=W)

		Radiobutton(self, text="Stability", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=careergoals, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.65, rely=0.17, anchor=W)

		Radiobutton(self, text="Influence", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=careergoals, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.81, rely=0.17, anchor=W)



		Label(self, text='How good are your time management skills?\n(1 = low, 5 = high)', bg="medium sea green", fg="white",
							  font=QUESTION_FONT, wraplength = 400, justify = LEFT).place(relx=0.05, rely=0.28, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=timemanagementskills, value=1, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.1, rely=0.4, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timemanagementskills, value=2, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.25, rely=0.4, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timemanagementskills, value=3, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.4, rely=0.4, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timemanagementskills, value=4, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.55, rely=0.4, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timemanagementskills, value=5, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.7, rely=0.4, anchor=W)



		Label(self, text='How would you rate your work ethic?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.5, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=workethic, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.1, rely=0.6, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workethic, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.25, rely=0.6, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workethic, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.4, rely=0.6, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workethic, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.55, rely=0.6, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workethic, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.7, rely=0.6, anchor=W)



		Label(self, text='How flexible/adaptable are you?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.7, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=flexiblility, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.1, rely=0.8, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=flexiblility, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.25, rely=0.8, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=flexiblility, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.4, rely=0.8, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=flexiblility, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.55, rely=0.8, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=flexiblility, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.7, rely=0.8, anchor=W)




		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
				  command=lambda: controller.show_frame(QuestionPage3))
		back.place(relx=0.0, rely=1.0, anchor=SW)

		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
				  command=lambda: self.checkfilledout(parent, controller))
		next.place(relx=1.0, rely=1.0, anchor=SE)

		pagenum = Label(self, text='pg 5/6', bg="medium sea green", font=("Helvetica", 14))
		pagenum.place(relx=0.82, rely=0.99, anchor=SW)


	def save(self):
		global careergoals
		global timemanagementskills
		global workethic
		global flexiblility
		questionnaireAnswers[16] = careergoals.get()
		questionnaireAnswers[10] = timemanagementskills.get()
		questionnaireAnswers[11] = workethic.get()
		questionnaireAnswers[12] = flexiblility.get()


	def checkfilledout(self, parent, controller):
		global careergoals
		global timemanagementskills
		global workethic
		global flexiblility



		errorlbl = Label(self, text='              *Please fill out all sections.              ',
						 bg="medium sea green", fg="red4", font=SMALL_FONT)

		if (DEBUG):
			controller.show_frame(QuestionPage5)
			return

		if (careergoals.get() == 0) or (timemanagementskills.get() == 0) or (workethic.get() == 0) or (flexiblility.get() == 0):
			errorlbl.place(relx=0.5, rely=0.9, anchor=S)
			return

		self.save()
		Label(self, text='                 *Please fill out all sections                 ',
			  bg="medium sea green", fg="medium sea green", font=SMALL_FONT).place(relx=0.5, rely=0.9, anchor=S)
		controller.show_frame(QuestionPage5)

class QuestionPage5(Frame):

	def __init__(self, parent, controller):
		global learningstyle
		global workwithothers
		global introvertextrovert
		learningstyle = IntVar()
		workwithothers = IntVar()
		introvertextrovert = IntVar()

		Frame.__init__(self, parent)



		Label(self, text='What kind of learner are you?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.08, anchor=W)

		Radiobutton(self, text="Visual (Spatial): You prefer using pictures, images, and spatial understanding.", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=1, font=("Helvetica", 12), tristatevalue=6).place(relx=0.05, rely=0.15, anchor=W)

		Radiobutton(self, text="Aural (Auditory-Musical): You prefer using sound and music.", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=2, font=("Helvetica", 12), tristatevalue=6).place(relx=0.05, rely=0.22, anchor=W)

		Radiobutton(self, text="Verbal (Linguistic): You prefer using words, both in speech and writing", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=3, font=("Helvetica", 12), tristatevalue=6).place(relx=0.05, rely=0.29, anchor=W)

		Radiobutton(self, text="Physical (Kinesthetic): You prefer using our body, hands, and sense of touch.", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=4, font=("Helvetica", 12), tristatevalue=6).place(relx=0.05, rely=0.36, anchor=W)

		Radiobutton(self, text="Logical (Mathematical): You prefer using logic, reasoning, and systems.", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=5, font=("Helvetica", 12), tristatevalue=6).place(relx=0.05, rely=0.43, anchor=W)



		Label(self, text='How would you rate your ablility to work with others?\n(1 = low, 5 = high)', bg="medium sea green", fg="white",
							  font=QUESTION_FONT, justify = LEFT).place(relx=0.05, rely=0.55, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=workwithothers, value=1, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.1, rely=0.65, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workwithothers, value=2, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.25, rely=0.65, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workwithothers, value=3, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.4, rely=0.65, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workwithothers, value=4, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.55, rely=0.65, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workwithothers, value=5, font=BUTTON_FONT,  tristatevalue=6).place(relx=0.7, rely=0.65, anchor=W)



		Label(self, text='How introverted/extroverted are you?\n(1 = introverted, 5 = extroverted)', bg="medium sea green", fg="white",
							  font=QUESTION_FONT, justify = LEFT).place(relx=0.05, rely=0.75, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=introvertextrovert, value=1, font=BUTTON_FONT, tristatevalue=6).place(relx=0.1, rely=0.85, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=introvertextrovert, value=2, font=BUTTON_FONT, tristatevalue=6).place(relx=0.25, rely=0.85, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=introvertextrovert, value=3, font=BUTTON_FONT, tristatevalue=6).place(relx=0.4, rely=0.85, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=introvertextrovert, value=4, font=BUTTON_FONT, tristatevalue=6).place(relx=0.55, rely=0.85, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=introvertextrovert, value=5, font=BUTTON_FONT, tristatevalue=6).place(relx=0.7, rely=0.85, anchor=W)




		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
				  command=lambda: controller.show_frame(QuestionPage4))
		back.place(relx=0.0, rely=1.0, anchor=SW)

		finish = Button(self, text="Finish!", highlightbackground="medium sea green", padx=10,
				  command=lambda: self.checkfilledout(parent, controller))
		finish.place(relx=1.0, rely=1.0, anchor=SE)

		pagenum = Label(self, text='pg 6/6', bg="medium sea green", font=("Helvetica", 14))
		pagenum.place(relx=0.81, rely=0.99, anchor=SW)


	def finishaccount(self):
		global learningstyle
		global workwithothers
		global introvertextrovert
		questionnaireAnswers[15] = learningstyle.get()
		questionnaireAnswers[13] = workwithothers.get()
		questionnaireAnswers[14] = introvertextrovert.get()


		new_account.q = questionnaireAnswers
		new_account.age = questionnaireAnswers[2]
		d.create_account(new_account)
		c.current_user = new_account

	def checkfilledout(self, parent, controller):
		global learningstyle
		global workwithothers
		global introvertextrovert

		errorlbl = Label(self, text='            *Please fill out all sections.            ',
						 bg="medium sea green", fg="red4", font=SMALL_FONT)



		if (learningstyle.get() == 0) or (workwithothers.get() == 0) or (introvertextrovert.get() == 0):
			errorlbl.place(relx=0.5, rely=0.95, anchor=S)
			return

		self.finishaccount()
		Label(self, text='               *Please fill out all sections               ',
			  bg="medium sea green", fg="medium sea green", font=SMALL_FONT).place(relx=0.5, rely=0.95, anchor=S)
		win.pages[HomePage].load(parent, controller)
		controller.show_frame(HomePage)

# this function is checking to make sure the email entered is the correct format
# returns True if email is in the correct format
def check_email(address):
		# check for the @ sign
		if ("@" in address):
				# split the string at the @ to be able to check the second part of the email
				address_split = address.split("@")
				# check if a . exists in the part of the email after the @
				if "." in address_split[1]:
						# split again at the . to ensure there are characters behind and after the .
						address_split_second = address_split[1].split(".")
						if len(address_split_second[0]) >= 1 and len(address_split_second[1]) >= 1:
								return True
		return False

# this checks if a username already exists in the database. Returns True if username is not taken
def check_username(username):
		for user in c.users:
				if username == user.username:
						return False
		return True

# Function used to show mentors/mentees information after the connect
# button from the HomePage is clicked.
def connect(first, last, email):
	#Create new smaller window
	top = Toplevel()
	top.geometry('310x170')
	top.resizable(False, False)
	top.title("Match Information")
	top.config(bg='medium sea green')

	#Combine first and last name
	name = first + " " + last
	l = Label(top, text=name, fg="White", bg = 'medium sea green', font=INFO_FONT)
	l.place(relx=0.05, rely=0.13, anchor=W)
	fr1 = Frame(top, width=600, height=5, bg='white')
	fr1.place(relx=0.05, rely=0.25, anchor=CENTER)

	#Add "Contact By" with email to new string
	em = "Contact By: " + email
	l2 = Label(top, text=em, fg="White", bg = 'medium sea green', font=SMALL_FONT)
	l2.place(relx=0.05, rely=0.4, anchor=W)

	#Button that will exit out of this small window
	b = Button(top, text="Back", padx=50, highlightbackground='medium sea green', command=lambda: exit(top))
	b.place(relx=0.5, rely=0.7, anchor=CENTER)

# Helper function for connect that will close the window after a button
# is clicked
def exit(top):
	top.destroy()

#Initializes the window, sets size, title, and background color.
win = start()
win.geometry('600x425')
win.resizable(False, False)
win.title("Mentor Meeter")
win.config(bg='medium sea green')
win.mainloop()

'''
RESOURCES:
https://pythonprogramming.net/change-show-new-frame-tkinter/

'''
