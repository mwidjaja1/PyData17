import matplotlib.pyplot as plt
import numpy as np

last_ev = None


def event_printer(event):
    """Helper function for exploring events.

    Prints all public attributes +
    """
    # capture the last event
    global last_ev
    last_ev = event
    for k, v in sorted(vars(event).items()):
        print(f'{k}: {v!r}')
    print('-'*25)


th = np.linspace(0, 2*np.pi, 64)
fig, ax = plt.subplots()
# the `picker=5` kwarg turn on pick-events for this artist
ax.plot(th, np.sin(th), 'o-', picker=5)

# Shows location when button is clicked
cid = fig.canvas.mpl_connect('button_press_event', event_printer)
plt.show()
# fig.canvas.mpl_disconnect(cid)

# Shows location when button is released
cid = fig.canvas.mpl_connect('button_press_event', event_printer)

# Shows location of static cursor, when mouse wheel scrolls
cid = fig.canvas.mpl_connect('scroll_event', event_printer)

# Shows location of static cursor, when key is pressed or released
cid = fig.canvas.mpl_connect('key_press_event', event_printer)
cid = fig.canvas.mpl_connect('key_release_event', event_printer)

# Shows what Matplotlib object was selected when clicked
cid = fig.canvas.mpl_connect('pick_event', event_printer)

# Something about drawing data as a 'delta' of changes
# ln.figure.canvas.draw_idle()




# EXERCISE (10 - 15 minutes)
#
# play around with events interactively
#
#   - Try all 'active' events
#     ['button_press_event', 'button_release_event', 'scroll_event',
#      'key_press_event', 'key_release_event', 'pick_event']
#   - tweak the print line
#   - remove a callback
#   - add more than one callback to the canvas
