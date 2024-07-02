import edepparser

parser = edepparser.EdepSimParser('/path/to/your/file.root')

this_event = parser[0] # get the 0th event
ev.plot_segments() # plot the event segments using matplotlib

for this_segment in ev.segments:
    print (this_segment.GetEnergyDeposit())
