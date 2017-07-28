import random
import os


class Meeting:

    def __init__(self, name, path):
        self.name = name
        self.attendees = list()
        self.facilitator = ""
        self.scribe = ""
        self.record_file = ""
        self.meeting_id = 1
        self.path = path
        self.record_path = os.path.join(self.path, 'records')

    def add_attendee(self, attendee):
        self.attendees = [name.strip() for name in attendee.split(",")]

    def remove_attendee(self, attendee):
        if attendee in self.attendees:
            self.attendees.remove(attendee)
        else:
            print "I can't find this attendee in the list." \
                + " Please check spelling"

    def create_record(self, record):
        record_file = record
        if not os.path.exists(self.record_path):
            os.makedirs(self.record_path)
        if ".csv" not in record:
            record_file = record + '.csv'
        if not os.path.exists(os.path.join(self.record_path,
                                           record_file)):
            self.record_file = record_file
            with open(os.path.join(self.record_path,
                                   self.record_file), 'a') as record_open:
                record_open.write('facilitator, scribe' + "\n")
                record_open.close()
        else:
            print "This record already exists!"

    def assign_record(self, record):
        # TODO - Expect that .csv will be omitted, check if it exists
        if ".csv" not in record:
            self.record_file = record + ".csv"
        else:
            self.record_file = record
        if len(list(open(self.record_file, 'r'))) > 1:
            last_meeting_info = list(open(self.record_file, 'r'))[-1]

    # if there was a meeting, to be fair, we remove its previous
    # scribe and facilitator from being eligible for this role again
    def assign_roles(self):
        eligible_scribes = self.attendees
        eligible_facilitators = self.attendees
        # TODO - add message as a default string
        if self.record_file != "":
            last_meeting_info = list(open(self.record_file,
                                          'r'))[-1].strip().split(", ")
            if len(list(open(self.record_file, 'r'))) > 1:
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

# If this is a recurring meeting, add to record
    def add_to_record(self):
        with open(self.record_file, 'a') as record_new_row:
            record_new_row.write(str(self.meeting_id) + ", " +
                                 str(self.facilitator) + ", " +
                                 str(self.scribe) + "\n")
