from subprocess import call

class Task(object):

    """Docstring for Task. """

    def __init__(self, calendar, title, location, date, time, duration,
            description, reminder):
        """TODO: to be defined1.

        :calendar: TODO
        :title: TODO
        :location: TODO
        :date: TODO
        :time: TODO
        :duration: TODO
        :descriptdescription: TODO
        :reminder: TODO

        """
        self._calendar = calendar
        self._title = title
        self._location = location
        self._date = date
        self._time = time
        self._duration = duration
        self._description = description
        self._reminder = reminder


    def add_to_calendar(self):
        call (["gcalcli", "--calendar", self._calendar, "add", "--title",
            self._title, "--where", self._location, "--when",self._date,
            self._time,  "--description", self._description, "--duration",
            self._duration, "--reminder", self._reminder])
