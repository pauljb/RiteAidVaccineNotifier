# RiteAidVaccineNotifier
Windows desktop notifier for Rite Aid COVID-19 vaccine appointment slots

Store numbers are stored as strings and leading zeros aren't necessary
ie. stores=['11144','11143','3768']

When it finds availability, it will beep the number of times specified by numBeeps (default 100)

Set enableOutput to False if you only want to see when a shot is found.
Set enableOutput to True (default) to see the results of each request

