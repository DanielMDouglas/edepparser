class Event:
    """
    Container for event-level information.
    Initialize from a G4Event, and add attributes
    as calculated by a ParametricSimulator object
    """
    def __init__(self, tg4event_instance):
        self.event = tg4event_instance
        self.segments = sum([[segment
                              for segment in hitSegments]
                             for containerName, hitSegments in self.event.SegmentDetectors],
                            start = [])
        self.trajectories = self.event.Trajectories

    def plot_segments(self, output_file):
        """
        produce a single 3D plot of the segments
        in the input TG4Event
        """
        
        import matplotlib.pyplot as plt

        def color_by_PID(pid):
            known_pids = {11: 'blue',
                          -11: 'green',
                          13: 'orange',
                          22: 'yellow',
                          2112: 'cyan',
                          }
            if pid in known_pids.keys():
                return known_pids[pid]
            else:
                return 'gray'

        seen_pids = []

        fig = plt.figure()
        ax = fig.add_subplot(111, projection = '3d')

        for segment in self.segments:
            segment_pid = self.event.Trajectories[segment.Contrib[0]].GetPDGCode()
            if segment_pid not in seen_pids:
                seen_pids.append(segment_pid)
            ax.plot((segment.GetStart().X(),
                     segment.GetStop().X()),
                    (segment.GetStart().Y(),
                     segment.GetStop().Y()),
                    (segment.GetStart().Z(),
                     segment.GetStop().Z()),
                    color = color_by_PID(segment_pid)
                    )
        plt.savefig(output_file)
