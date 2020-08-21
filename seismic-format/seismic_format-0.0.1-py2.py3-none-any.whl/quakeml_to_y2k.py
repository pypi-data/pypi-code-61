import argparse
import os
import sys
from obspy.core.event import read_events

from . import get_format_dir
from .lib.lib_y2k import *
from .lib.liblog import getLogger
from .lib.lib_hypo import origin_to_y2k, arrival_to_y2k

import copy

def main():

    logger = getLogger()

    quakemlfile = processCmdLine()

    formats_dir = get_format_dir()

    y2000_format_file = os.path.join(formats_dir, 'format.Y2000_station_archive')
    y2000_header_file = os.path.join(formats_dir, 'format.Y2000_header_archive')

# 1. Read the Hypoinverse Y2000 archive format:
    y2k_format = read_format(y2000_format_file)
    hdr_format = read_format(y2000_header_file)

    event = None
    mag = None
    origin = None
    preferred_origin = False

    try:
        cat = read_events(quakemlfile, format="quakeml")
        event = cat[0]
        mag = event.preferred_magnitude() or event.magnitudes[0]
        origin = event.preferred_origin() or event.origins[0]

        if not origin:
            print("****** There is NO origin in this quakeml!")
    except:
        print("ERROR reading quakeml file=[%s]" % quakemlfile)
        raise

    #print("quakeml: norigins=%d nmags=%d narrivals=%d npicks=%d namplitudes=%d" % \
        #(len(event.origins),len(event.magnitudes),len(origin.arrivals), len(event.picks), len(event.amplitudes)))

    # Note that we can also write out the origin line with this func:
    write_y2000_phase(hdr_format, origin_to_y2k(origin, hdr_format))

    for arrival in origin.arrivals:
        y2k_phase = arrival_to_y2k(arrival, y2k_format)
        write_y2000_phase(y2k_format, y2k_phase)

    return

def processCmdLine():

    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")


    required.add_argument("--quakeml", type=str, metavar='Path to quakeml.xml file', required=True)

    #parser._action_groups.append(optional) # 
    #optional.add_argument("--optional_arg")

    args, unknown = parser.parse_known_args()

    return args.quakeml



if __name__ == "__main__":
    main()
