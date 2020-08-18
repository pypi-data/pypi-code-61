# the following functions still need to be validated in the new Slot() code
# as we port more API examples, then this can be deleted.

def reset(parser, input):
    parser.pattern.reset()
    return input.copy()

def reverse(parser, input):
    parser.pattern.reverse()
    return input.copy()

def shuffle(parser, input):
    parser.pattern.shuffle()
    return input.copy()

def expr_invert_set(parser, input, how, extra_info):
    how = evaluate_params(parser, how, want_int=True)
    res = input.invert(how)
    return res

def expr_skip_set(parser, input, how, extra_info):

    from warpseq.model.chord import Chord
    from warpseq.model.note import Note

    how = evaluate_params(parser, how, want_int=True)
    pattern = parser.pattern
    note_parser = input.get_parser()

    res = input

    for _ in range(0, how):
        sym = pattern.get_next()
        octave_shift = pattern.get_octave_shift(parser.track)
        res = note_parser.do(sym, octave_shift)
        #print("RES=%s" % res)

    if type(res) == Note:
        res = [ res ]

    return Chord(notes=res, from_scale=input.from_scale)

def expr_length_mod_set(parser, input, how, extra_info):
    how = evaluate_params(parser, how, want_float=True)
    return input.with_length_mod(how)

def expr_delay_set(parser, input, how, extra_info):
    how = evaluate_params(parser, how, want_float=True)
    return input.with_delay(how)

def expr_rush_set(parser, input, how, extra_info):
    how = evaluate_params(parser, how, want_float=True)
    return input.with_delay(-how)

def expr_track_copy(parser, input, how, extra_info):
    how = evaluate_params(parser, how, want_string=True)
    pattern = parser.song.find_track_by_name(how)
    if pattern is None:
        raise InvalidExpression("no such track to move note to: %s" % how)
    res = input.with_track_copy(pattern)
    return res

