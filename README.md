# RiteAidVaccineNotifier
Windows desktop notifier for Rite Aid COVID-19 vaccine appointment slots

Store numbers are stored as strings and leading zeros aren't necessary
ie. stores=['11144','11143','3768']

When it finds availability, it will beep the number of times specified by numBeeps (default 10)

Set enableOutput to False if you only want to see when a shot is found.

Set enableOutput to True (default) to see the results of each request

HOT TIP: The slots seem to get refreshed near midnight. The program alerted me at 11:54PM ET and I was immediately able to get one. Not sure if it refreshes for all timezones near midnight, or midnight in each timezone.
I recommend signing up for first slot you get, you can always cancel it if you get another at a closer store later on.