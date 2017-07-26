from meeting_assigner import Meeting

# Test -1 Adding a comma and space separated
# list of attendees creates an instance of 
# attendees that's a list of names without spaces

def test_one():
	test_one = Meeting("Test One")
	test_one.add_attendee("John, Paul, George, Ringo")
	has_spaces = " " in test_one.attendees
	print "(Has no spaces) Test passes if this is False. Result: " \
	+ str(has_spaces)
	print "(List of names) Test passes if this is list type. Result: "\
	+ str(type(test_one.attendees))
	print "This should print ['John', 'Paul', 'George', 'Ringo']. Results: " \
	+ str(test_one.attendees)

test_one()

# Test -1 Adding a comma and no space separated
# list of attendees creates an instance of 
# attendees that's a list of names without spaces

def test_two():
	test_one = Meeting("Test One")
	test_one.add_attendee("John,Paul,George,Ringo")
	has_spaces = " " in test_one.attendees
	print "(Has no spaces) Test passes if this is False. Result: " \
	+ str(has_spaces)
	print "(List of names) Test passes if this is list type. Result: "\
	+ str(type(test_one.attendees))
	print "This should print ['John', 'Paul', 'George', 'Ringo']. Results " \
	+ str(test_one.attendees)

test_two()