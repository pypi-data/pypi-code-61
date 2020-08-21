# ------------------------------------------------------------------
# Warp Sequencer
# (C) 2020 Michael DeHaan <michael@michaeldehaan.net> & contributors
# Apache2 Licensed
# ------------------------------------------------------------------

# a Pattern is a list of symbols/expressions that will eventually
# evaluate into Chords/Notes.

from .base import NewReferenceObject
from warpseq.api.exceptions import *
from warpseq.model.directions import *
from warpseq.utils.serialization import Serializer
from warpseq.model.slot import Slot, DataSlot

class DataPool(NewReferenceObject, Directionable):

    __slots__ = [ 'name', 'slots', 'current_slots', 'direction', 'current_direction', 'length',
                  '_iterator', 'obj_id' ]

    SERIALIZER = Serializer(
        values = ( 'name', 'direction', 'length'),
        objects = ( ),
        object_lists = (),
        objects_2d = (),
        custom = ( 'slots' ),
    )

    def __init__(self, name=None, slots=None, direction=FORWARD, length=None, obj_id=None):

        self.name = name
        self.slots = slots

        for x in slots:
            assert isinstance(x, DataSlot)

        if not direction in DIRECTIONS:
            raise InvalidInput("direction must be one of: %s" % DIRECTIONS)

        self.direction = direction
        self.current_direction = direction
        self.obj_id = obj_id

        if length is None:
            length = len(slots)
        self.length = length


        super(DataPool, self).__init__()
        self.reset()

    #def get_length(self):
    #    return self.length

    #def get_iterator(self):
    #    #for _ in range(0, self.get_length()):
    #    yield next(self._iterator)
