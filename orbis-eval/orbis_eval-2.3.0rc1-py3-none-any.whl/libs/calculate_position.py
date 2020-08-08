import logging

from fuzzysearch import find_near_matches

logging.getLogger().setLevel(logging.INFO)


def _calculate_pos_from_list(words, index, sequence):
    start_pos = sum([len(word) + 1 for word in words[:index]])
    sequence_length = sum([len(word) + 1 for word in words[index:index + sequence]])
    return start_pos, start_pos + sequence_length


def _longest_common_subsequence(text, sub_text):
    text = text.split(' ')
    sub_text_original = sub_text
    sub_text = sub_text.split(' ')
    longest_sequence_index = 0
    longest_sequence = 0
    for index, text_word in enumerate(text):
        for index_sub_text, sub_text_word in enumerate(sub_text):
            if sub_text_word == text_word:
                sequence_length = 0
                for index_sequence, sequence in enumerate(sub_text[index_sub_text:]):
                    if index + sequence_length >= len(text) or sequence != text[index + sequence_length]:
                        break
                    sequence_length = sequence_length + 1
                if sequence_length > longest_sequence:
                    longest_sequence = sequence_length
                    longest_sequence_index = index
    if longest_sequence_index:
        return _calculate_pos_from_list(text, longest_sequence_index, longest_sequence)
    logging.warning(f'Not found in text:\n{sub_text_original}')
    return -1, -1


def _add_start_end_fuzzy_search(text, sub_text, start_index):
    result = find_near_matches(sub_text, text[start_index:], max_l_dist=5)
    if result:
        return result[0].start, result[0].end
    return -1, -1


def get_start_end_position(post_text, full_text, start_index):
    """
    @Todo good description of the algorithm
    """
    post_text = post_text.casefold()
    full_text = full_text.casefold()
    if isinstance(post_text, str):
        found_start_index = full_text.find(post_text, start_index)
        if found_start_index > -1:
            return found_start_index, found_start_index + len(post_text)
        elif len(post_text) > 50:
            start, end = _add_start_end_fuzzy_search(full_text, post_text, start_index)
            if end > 0:
                return start, end
        return _longest_common_subsequence(full_text, post_text)
    logging.warning(f'post_text is not a string:\n{post_text}')
    return -1, -1
