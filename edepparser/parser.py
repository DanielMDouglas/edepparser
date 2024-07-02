from .event import Event
from ROOT import TG4Event, TFile
import numpy as np

class EdepSimParser:
    """
    Parser class for generating event spill
    images (a set of vertices, segments, and trajectories)
    corresponding to a single logical event
    """
    def __init__(self, edepsim_path, shuffle = False):
        self._edepsim_path = edepsim_path
        self._inputFile = TFile(self._edepsim_path)
        
        self._inputTree = self._inputFile.Get("EDepSimEvents")

        self.event = TG4Event()
        self._inputTree.SetBranchAddress("Event", self.event)

        self._entries = self._inputTree.GetEntriesFast()

        if shuffle:
            self._sample_order = np.random.choice(self._entries,
                                                  self._entries,
                                                  replace = False)
        else:
            self._sample_order = np.arange(self._entries)
        
    def __getitem__(self, idx):
        """
        return the event/interaction corresponding to the provided index
        """
        nb = self._inputTree.GetEntry(idx)

        return Event(self.event)

    # def __repr__(self):
    #     print (self.event.Primaries)
    #     for primaryVertex in self.event.Primaries:
    #         print (self.event.EventId)
    #         print (primaryVertex.GetPosition().X())
    #         print (primaryVertex.GetPosition().Y())
    #         print (primaryVertex.GetPosition().Z())
        
    #     for iTraj, trajectory in enumerate(self.event.Trajectories):
    #         start_pt, end_pt = trajectory.Points[0], trajectory.Points[-1]
    #         print ("track ID", trajectory.GetTrackId())
    #         print ("Parent ID", trajectory.GetParentId())
    #         print (start_pt.GetPosition().X(), start_pt.GetPosition().Y(), start_pt.GetPosition().Z())
    #         print (end_pt.GetPosition().X(), end_pt.GetPosition().Y(), end_pt.GetPosition().Z())
    #         print ("PDG Code", trajectory.GetPDGCode())

    def __iter__(self):
        for idx in self._sample_order:
            yield self.__getitem__(idx)
