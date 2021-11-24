#How to run more code in unity
#How to achieve a better state of consciunsness by improving how our details create in the world more composition of intellectual capabilities
#When i sense how to achieve a new concept of life, how to experience a new way to detial the realities we create each moment.
#How our minds make us believe in the movement of the world, how to relate the whole movement to a new degree, how to maximize the opinion of the self.

#Como yo puedo emplear el componente que se mueve en mi vida, como yo puedo emprender el saber que se mueve en mi conciencia, como yo puedo detallar como mi 
#Realidad se vive en mi vida como mi conciencia hace que todo sea mas preciso como mi realidad.
#Maximiza como mi saber busac el concepto
#The kind of detail capable to build in us motion and improvement, motion and idea, motion and interaction with the world, the ability to maxmize
#THe conception of the whole movement
#How to produce more movement in the self
#How to create more quality
#Comprendiendo como la coherencia del saber determina como la totalidad se vive, como la totalidad se experimenta, como yo puedo hacer para aprender
#A ser mas nuevo, como yo puedo ser mas magico en el saber.
#Produciendo mejores formas de aprender a sentir las verdades que se mueven en mi mente, como las verdades de mi saber producen el camino que yo quiero vivir.
#Como yo puedo motivar la vida al grado mas alto como yo puedo sintetizar el saber que se vive en mi realidad, el saber que me hace mas claro como el comportamiento de mi psoicoligia
#Produce las interacciones qeu yo quiero apreciar.
#Como yo puedo activar en la mente las funciones que producen realidad.
#
# os for file management



# selenium for web driving
import selenium
from selenium import webdriver

# time for pausing between navigation
import time

# Datetime for recording time of submission
import datetime

# os for file management
import os


def submit_assignment(file_tup):
	# Using Chrome to access web
	driver = webdriver.Chrome()

	time.sleep(5)

	# Open the website
	driver.get('https://canvas.case.edu')

	# Password for Canvas
	with open('C:/Users/Will Koehrsen/Desktop/cp.txt', 'r') as f:
	    cp = f.read()


	# Locate id and password
	id_box = driver.find_element_by_name('username')
	pass_box = driver.find_element_by_name('password')

	# Send login information
	id_box.send_keys('wjk68')
	pass_box.send_keys(cp)

	# Click login
	login_button = driver.find_element_by_name('submit')
	login_button.click()

	# Find and click on list of courses
	courses_button = driver.find_element_by_id('global_nav_courses_link')
	courses_button.click()


	# Wait for the page to load
	time.sleep(2)

	# Get the name of the folder
	folder = file_tup[0]
	    
	# Class to select depends on folder
	if folder == 'DSCI451':
	    class_select = driver.find_element_by_link_text('Applied Data Science Research (100/5047)')
	elif folder == 'DCSI453':
	    class_select = driver.find_element_by_link_text('Data Science: Statistical Learning, Modeling and Prediction (100/5046)')
	elif folder == 'EECS491':
	    class_select = driver.find_element_by_link_text('Artificial Intelligence: Probabilistic Graphical Models (100/10039)')
	elif folder == 'EECS531':
	    class_select = driver.find_element_by_link_text('Computer Vision (100/10040)')

	# Click on the specific class
	class_select.click()

	assignment_button = driver.find_element_by_link_text('Assignments')
	assignment_button.click()

	# Wait for the page to load 
	time.sleep(2)

	# Locate the specific assignment
	file_name = file_tup[1]
	file_locator = file_name.split('.')[0]
	 
	specific_assigment = driver.find_element_by_link_text(file_locator)
	specific_assigment.click()

	# Click on the button to submit an assignment
	try:
	    submit_assignment_button = driver.find_element_by_link_text('Submit Assignment')
	# If assignment has already been submitted
	except:
	    print('Assignment already submitted, re-submitting')
	    submit_assignment_button = driver.find_element_by_link_text('Re-submit Assignment')

	submit_assignment_button.click()

	# Wait for the page to load
	time.sleep(2)

	# Choose file button
	choose_file = driver.find_element_by_name('attachments[0][uploaded_data]')

	# Send the name of the file to the button
	file_location = os.path.join(submission_dir, folder, file_name)
	choose_file.send_keys(file_location)

	submit_assignment = driver.find_element_by_id('submit_file_button')
	submit_assignment.click()

	# Wait for the page
	time.sleep(2)

	# Move the file to the submitted folder
	submitted_dir = 'C:/Users/Will Koehrsen/Desktop/submitted_assignments'
	submitted_dir = os.path.join(submitted_dir, folder)
	submitted_file_name = 'Submitted ' + file_name

	submitted_file_location = os.path.join(submitted_dir, submitted_file_name)
	# os.rename(file_location, submitted_file_location)

	print('{} Assignment for Class {} successfully submitted at {}.'.format(
		file_name, folder, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

	print('Submitted assignment available at {}.'.format(submitted_file_location))

	return

if __name__ == "__main__":

	# Build tuple of (folder, file) to turn in
	submission_dir = 'C:/Users/Will Koehrsen/Desktop/completed_assignments'
	dir_list = list(os.listdir(submission_dir))

	for directory in dir_list:
	    file_list = list(os.listdir(os.path.join(submission_dir, directory)))
	    if len(file_list) != 0:
	        file_tup = (directory, file_list[0])

	if len(file_tup) == 0:
		print('No files to submit')

	else:
		print('Assignment "{}" for "{}" found.'.format(file_tup[1], file_tup[0]))
		input('Press enter to proceed: ')
		submit_assignment(file_tup)





