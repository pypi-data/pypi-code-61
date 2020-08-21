import argparse
import copy
import os
import sys

# Quiet down matplotlib msgs (obspy must import matplotlib with logLevel=DEBUG)
import logging
logger = logging.getLogger('matplotlib')
logger.setLevel(logging.WARNING)

from obspy.core.event import Catalog
from obspy.core.event import read_events
from obspy.core.event.event import Event

from . import get_format_dir
from .lib.lib_y2k import *
from .lib.liblog import getLogger
from .lib.lib_hypo import y2k_to_origin, y2k_phase_to_arrival


def main():

    #logger = getLogger()

    arc_file = processCmdLine()

    print(arc_file)

    fname = os.path.basename(arc_file)
    print(fname)
    d = os.path.dirname(arc_file)
    qname = fname.replace('.y2k','.qml')
    print(qname)
    exit()

    formats_dir = get_format_dir()
    logger.info("formats_dir=%s" % formats_dir)

# 1. Read the Hypoinverse Y2000 archive format:
    #y2000_format_file = 'formats/format.Y2000_station_archive'
    #y2000_header_file = 'formats/format.Y2000_header_archive'
    y2000_format_file = os.path.join(formats_dir, 'format.Y2000_station_archive')
    y2000_header_file = os.path.join(formats_dir, 'format.Y2000_header_archive')
    y2k_format = read_format(y2000_format_file)
    hdr_format = read_format(y2000_header_file)

    # Read in the y2k arc file
    (y2k, y2k_origin)  = read_arc_shadow_file(arc_file, y2k_format, hdr_format)

    #write_y2000_phase(hdr_format, y2k_origin)
    # Convert y2k origin to quakeml origin
    origin = y2k_to_origin(y2k_origin)
    #print(origin)

    arrivals = []
    picks = []

    for sta, chans in y2k.items():
        #print("sta:%s" % (sta))
        for cha, arr in chans.items():
            #print("cha:%s" % (cha))
            if arr['Psec'] > 0 and arr['Ssec'] > 0:
                print("ERROR: This looks like both P and S arrivals in 1 y2k arrival!")
                exit()
            elif arr['Psec'] > 0 and arr['Prmk'] != "":
                phase = 'P'
            elif arr['Ssec'] > 0 and arr['Srmk'] != "":
                phase = 'S'

            arrival, pick = y2k_phase_to_arrival(arr, phase)
            arrivals.append(arrival)
            picks.append(pick)
            #print("arrival id:%s pick_id:%s == %s" % (arrival.resource_id, arrival.pick_id, pick.resource_id))

    logger.info("Outputting quakeml into file:test.xml --> Code needs to be updated to add output filename!")

    origin.arrivals = arrivals
    event = Event()
    event.origins = [origin]
    event.picks = picks
    event.preferred_origin_id = origin.resource_id.id

    catalog = Catalog(events=[event])
    catalog.write("test.xml", format="QUAKEML")

    # TODO:
    # add mag
    # set pref mag

    return

def processCmdLine():

    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")


    required.add_argument("--y2kfile", type=str, metavar='Path to y2k arc file', required=True)

    #parser._action_groups.append(optional) # 
    #optional.add_argument("--optional_arg")

    args, unknown = parser.parse_known_args()

    return args.y2kfile



if __name__ == "__main__":
    main()
