from typing import Sequence, Any, Callable, Mapping

__version__ = "0.0.b2.post2"
__all__ = [
    "predict_tensor_item_count",
    "count_tensor_items",
    "is_proper_sized_tensor",
    "this_sequence_is_a_leaf",
    "DetectATreeLeaf",
    "this_item_is_a_leaf",
]


def predict_tensor_item_count(potential_tensor: Sequence) -> int:
    """
    Predicts the assumed tensor size on basis of the first element within
    a nested Sequence. It is assumed that the given potential tensor has a
    shape of (i, j, ...). The shape's product reflects the tensor's item
    count. It also implies that all sub tensors within each level of the
    tensor have the same item count, therefore the first item within each
    level defines the shape of this particular level.

    Examples:
        >>> from treenodedefinition import predict_tensor_item_count

        For 'clean' tensors the prediction is equal to the actual item count.

        >>> predict_tensor_item_count([])
        0
        >>> predict_tensor_item_count([[], []])
        0
        >>> predict_tensor_item_count([1, 2])
        2
        >>> predict_tensor_item_count([[1, 1], [2, 2]])
        4
        >>> predict_tensor_item_count(
        ...     [
        ...         [[1, 1], [2, 2]],
        ...         [[3, 3], [4, 4]]
        ...     ]
        ... )
        8

        In this case the tensor should had an item count of 6, while two
        items are lacking in their tensor size.

        >>> predict_tensor_item_count([[1, 2], 3, 4])
        6

    Args:
        potential_tensor(Sequence):
            A potential nested sequence being assumed to be a potential tensor.

    Returns:
        int:
            The item count
    """
    # if this sequence is not nested anymore return its length
    # for the recursion
    size_of_current_tensor_level = len(potential_tensor)
    if size_of_current_tensor_level == 0:
        return 0
    representative_of_next_tensor_level = potential_tensor[0]
    if not isinstance(representative_of_next_tensor_level, (list, tuple)):
        return size_of_current_tensor_level
    size_of_next_level = predict_tensor_item_count(representative_of_next_tensor_level)
    return size_of_current_tensor_level * size_of_next_level


def count_tensor_items(potential_tensor: Sequence) -> int:
    """
    Counts the actual item within a nested sequence.

    Examples:
        >>> from treenodedefinition import count_tensor_items
        >>> count_tensor_items([1, 2])
        2
        >>> count_tensor_items([[1, 1], [2, 2]])
        4
        >>> count_tensor_items(
        ...     [
        ...         [[1, 1], [2, 2]],
        ...         [[3, 3], [4, 4]]
        ...     ]
        ... )
        8
        >>> count_tensor_items([[1, 2], 3, 4])
        4

    Args:
        potential_tensor(Sequence):
            A potential nested sequence being assumed to be a potential tensor.

    Returns:
        int:
            The item count
    """
    sum_of_total_tensor_items = 0
    item_should_be_flat = False
    for tensor_column in potential_tensor:
        # the recursion hit the bottom of the nested sequence and sums up
        # all items, so this sequence should be flat
        if not isinstance(tensor_column, (list, tuple)):
            sum_of_total_tensor_items += 1
            item_should_be_flat = True
            continue
        # if there was a flat item before but now a sequence was found
        # this nested sequence is not correct --> returning 0 should fuck up
        # the sum and n x m x .... != sum
        if item_should_be_flat:
            return 0
        sum_of_total_tensor_items += count_tensor_items(tensor_column)
    return sum_of_total_tensor_items


def is_proper_sized_tensor(potential_tensor: Sequence) -> bool:
    """
    Estimates whether the given potential tensor has a proper shape of all
    items, or is inadequately filled.

    Examples:
        >>> from treenodedefinition import is_proper_sized_tensor
        >>> is_proper_sized_tensor([])
        False
        >>> is_proper_sized_tensor([1, 2])
        True
        >>> is_proper_sized_tensor([[1, 1], [2, 2]])
        True
        >>> is_proper_sized_tensor(
        ...     [
        ...         [[1, 1], [2, 2]],
        ...         [[3, 3], [4, 4]]
        ...     ]
        ... )
        True
        >>> is_proper_sized_tensor([[1, 1], 2, 3])
        False
        >>> is_proper_sized_tensor("A string is a sequence, but not a tensor,")
        False
        >>> is_proper_sized_tensor(["while", "a", "sequence", "of", "strings", "is."])
        True

    Raises:
        TypeError:
            If given *potential_tensor* doesn't implement len, which means
            that *potential_tensor* is not a sequence.

    Args:
        potential_tensor:
            A potential nested sequence being assumed to be a potential tensor.

    Returns:
        bool
    """
    if not potential_tensor:
        return False
    if isinstance(potential_tensor, str):
        return False
    # this method checks whether this sequence is an matrix/tensor by using
    # sum of array lengths. n x m x ...
    try:
        target_sum = predict_tensor_item_count(potential_tensor)
    except TypeError:
        raise TypeError("`potential_tensor` needs to be a sequence.")
    summed_items = count_tensor_items(potential_tensor)
    return target_sum == summed_items


def this_sequence_is_a_leaf(potential_tensor: Sequence) -> bool:
    """
    States if the given sequence is a leaf or node.

    Notes:
        All sequences, which are *proper sized tensor*
        (`is_proper_sized_tensor(..)`) are considered as values.

        Sequences which contain mixed containers (Sequences and Mappings) are
        considered as nodes. Also if the sequence contains different sized
        sequences.

    Examples:
        >>> from treenodedefinition import this_sequence_is_a_leaf
        >>> this_sequence_is_a_leaf([])
        False
        >>> this_sequence_is_a_leaf([1, 2])
        True
        >>> this_sequence_is_a_leaf([[1, 1], [2, 2]])
        True
        >>> this_sequence_is_a_leaf([[1, 1], 2, 3])
        False
        >>> this_sequence_is_a_leaf("A single string is a leaf, ")
        True
        >>> this_sequence_is_a_leaf(["while", "a", "sequence", "of", "strings", "is."])
        True
        >>> this_sequence_is_a_leaf([["a", "good", "start"], {"ended": "wrong"}])
        False

    Args:
        potential_tensor(Sequence):
            Is treated to be a potential tensor.

    Returns:
        bool:
            States whether the sequence is a leaf, which in this context is
            an adequate filled tensor.

    """
    if isinstance(potential_tensor, str):
        return True
    if is_proper_sized_tensor(potential_tensor):
        for item in potential_tensor:
            if isinstance(item, dict):
                return False
        return True
    return False


DetectATreeLeaf = Callable[[Any], bool]


def this_item_is_a_leaf(tree_node_item: Any) -> bool:
    """
    Differentiates a `tree_node_item` being a tree leaf or not.

    Examples:
        >>> from treenodedefinition import this_item_is_a_leaf

    An empty sequence is treatend as a node, as a potential placeholder for
    a future nested sequence.

        >>> this_item_is_a_leaf([])
        False

    (Nested) sequences are treatend as leafs, as long the resemble a proper
    filled tensor. The item type doesn't matter.

        >>> this_item_is_a_leaf([1, 2])
        True
        >>> this_item_is_a_leaf([[1, 1], [2, 2]])
        True
        >>> this_item_is_a_leaf([[1, 1], 2, 3])
        False
        >>> this_item_is_a_leaf("A string is.")
        True
        >>> this_item_is_a_leaf(["As", "is", "also", "a", "sequence", "of", "strings"])
        True
        >>> this_item_is_a_leaf(1)
        True
        >>> this_item_is_a_leaf(object())
        True

    A nested sequence with different containers is a node, with leafs.

        >>> this_item_is_a_leaf([["a", "good", "start"], {"ended": "wrong"}])
        False

    A dictionary is always a node, not a leaf.

        >>> this_item_is_a_leaf({"ended": "wrong"})
        False

    Args:
        tree_node_item(Any):
            Is this tree node item a leaf or node?

    Returns:
        bool:
            States if the tree node item is a leaf.

    """
    mappings_are_no_leafs_therefore_leave = isinstance(tree_node_item, Mapping)
    if mappings_are_no_leafs_therefore_leave:
        return False
    this_sequence_needs_to_be_checked_further = isinstance(tree_node_item, Sequence)
    if this_sequence_needs_to_be_checked_further:
        return this_sequence_is_a_leaf(tree_node_item)
    return True
