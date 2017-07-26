import random
import os

# Define the path where your leaderboard directory will be created
path = 
class Meeting:

    def __init__(self, name):
        self.name = name
        self.attendees = list()
        self.facilitator = ""
        self.scribe = ""
        self.leaderboard_file = ""
        self.meeting_id = 1
        self.leaderboard_path = os.path.join(path, 'leaderboards')

    def add_attendee(self, attendee):
        self.attendees = [name.strip() for name in attendee.split(",")]  

    def remove_attendee(self, attendee):
        # FIXME - this will throw an error if there's a typo in attendee name
        self.attendees.remove(attendee)

    # If this is a new recurring meeting, we should create a new leaderboard
    # so that we can track past facilitators and scribes
    def create_leaderboard(self, leaderboard):
        # TODO - Check that the leaderboard actually doesn't exist
        # TODO2 - check if .csv is included, otherwise add it
        if not os.path.exists('leaderboards'):
            os.makedirs(os.path.join(path, 'leaderboards'))
        self.leaderboard_file = leaderboard + '.csv'
        with open(os.path.join(self.leaderboard_path,self.leaderboard_file), 'a') as leaderboard_open:
            leaderboard_open.write('meeting_id, facilitator, scribe' + "\n")
            leaderboard_open.close()

    # If this is a new meeting, just assign the leaderboard file
    # update its meeting id if there's a record
    def assign_leaderboard(self, leaderboard):
        # TODO - Expect that .csv will be omitted, check if it exists
        self.leaderboard_file = leaderboard
        if len(list(open(self.leaderboard_file, 'r'))) > 1:
            last_meeting_info = list(open(self.leaderboard_file, 'r'))[-1]
            self.meeting_id = int(last_meeting_info[0])+1

    # if there was a meeting, to be fair, we remove its previous
    # scribe and facilitator from being eligible for this role again
    def assign_roles(self):
        eligible_scribes = self.attendees
        eligible_facilitators = self.attendees
        # TODO - add message as a default string
        if self.leaderboard_file != "":
            last_meeting_info = list(open(self.leaderboard_file,
                                          'r'))[-1].strip().split(", ")
            if len(list(open(self.leaderboard_file, 'r'))) > 1:
                # we need to bump the past facilitator and scribe
                eligible_facilitators.remove(last_meeting_info[1])
                eligible_scribes.remove(last_meeting_info[2])
                # TODO - refactor by only cleaning lists in that if statement.
                # Make role assignment a common method

                random.shuffle(eligible_scribes)
                self.scribe = eligible_scribes[0]

                # a scribe cannot be a facilitator,
                # bump scribe then shuffle facilitators and pick one
                eligible_facilitators.remove(self.scribe)
                random.shuffle(eligible_facilitators)
                self.facilitator = eligible_facilitators[0]
            else:
                random.shuffle(eligible_facilitators)
                self.facilitator = eligible_facilitators[0]
                eligible_scribes.remove(self.facilitator)
                random.shuffle(eligible_scribes)
                self.scribe = eligible_scribes[0]
            print "The facilitator will be " + self.facilitator + \
                " and the scribe will be " + self.scribe
        else:
            random.shuffle(eligible_facilitators)
            self.facilitator = eligible_facilitators[0]
            eligible_scribes.remove(self.facilitator)
            random.shuffle(eligible_scribes)
            self.scribe = eligible_scribes[0]
            print "You're creating an ad hoc meeting, the scribe will be " \
                  + self.scribe + " and the facilitator will be " \
                  + self.facilitator

# If this is a recurring meeting, add to leaderboard
    def add_to_leaderboard(self):
        with open(self.leaderboard_file, 'a') as leaderboard_new_row:
            leaderboard_new_row.write(str(self.meeting_id) + ", " +
                                      str(self.facilitator) + ", " +
                                      str(self.scribe) + "\n")

