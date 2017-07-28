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

    def create_or_assign_record(self, record):
        record_file = record
        if not os.path.exists(self.record_path):
            os.makedirs(self.record_path)
        if ".csv" not in record:
            record_file = record + '.csv'
        if not os.path.exists(os.path.join(self.record_path,
                                           self.record_file)):
            self.record_file = record_file
            with open(os.path.join(self.record_path,
                                   self.record_file), 'a') as record_open:
                record_open.write('facilitator, scribe' + "\n")
                record_open.close()
        else:
            self.record_file = record
            print "This record already exists!"

    def assign_roles(self):
        eligible_scribes = self.attendees
        eligible_facilitators = self.attendees
        if self.record_file != "" and len(
                list(open(os.path.join(self.record_path,self.record_file), 'r'))) > 1:
            last_meeting_info = list(open(os.path.join(self.record_path,self.record_file),
                                          'r'))[-1].strip().split(", ")
            eligible_facilitators.remove(last_meeting_info[0])
            eligible_scribes.remove(last_meeting_info[1])
        # assign roles
        random.shuffle(eligible_facilitators)
        self.facilitator = eligible_facilitators[0]
        eligible_scribes.remove(self.facilitator)
        random.shuffle(eligible_scribes)
        self.scribe = eligible_scribes[0]
        message = "The facilitator will be " + self.facilitator + \
            " and the scribe will be " + self.scribe
        print message


# If this is a recurring meeting, add to record
    def add_to_record(self):
        with open(os.path.join(self.record_path,self.record_file), 'a') as record_new_row:
            record_new_row.write(str(self.facilitator) + ", " +
                                 str(self.scribe) + "\n")
