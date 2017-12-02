import matplotlib.pyplot as plt
from w_helpers import load_data, aggregate_by_day, extract_day_of_hourly, label_date

import uuid

datasource = 'central_park'

temperature = load_data(datasource)
temperature = temperature[temperature['year'] >= 2017]
temperature_daily = aggregate_by_day(temperature)


class RowPrinter:
    def __init__(self, ln, df, picker=10):
        ln.set_picker(picker)
        # we can use this to ID our line!
        self.uid = str(uuid.uuid4())
        ln.set_gid(self.uid)
        self.ln = ln  # Line object
        self.df = df  # Data frame object
        self.cid = None
        self.connect()

    def connect(self):
        self.remove()
        self.cid = ln.figure.canvas.mpl_connect('pick_event',
                                                self)

    def __call__(self, event):
        # ignore picks on not-our-artist
        if event.artist is not self.ln:
            return
        # for each hit index, print out the row
        for i in event.ind:
            print(self.df.iloc[i])

    def remove(self):
        if self.cid is not None:
            self.ln.figure.canvas.mpl_disconnect(self.cid)
            self.cid = None


fig, ax = plt.subplots(2, 1)
ln, = ax[0].plot('mean', '-o', data=temperature_daily)  # Will plot DF temperature_daily['mean']
ax[0].set_xlabel('Date [UTC]')
ax[0].set_ylabel('Air Temperature [℃]')
ax[0].set_title(f'{datasource} temperature')

rp = RowPrinter(ln, temperature_daily)

# Plots the day's values below
one_day = extract_day_of_hourly(temperature, 2017, 10, 27)
ln, = ax[1].plot('mean', '-o', data=one_day)

plt.show()

# EXERCISE
# - make the print out nicer looking

# - open a new window with plot of day temperature
#   - fig, ax = plt.subplots()
#   - one_day = extract_day_of_hourly(temperature, 2015, 10, 18)
# - make picking add a label with `label_date`

# - use `get_gid` to filter artists instead of `is not`
