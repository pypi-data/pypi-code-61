import ast
from collections import defaultdict

try:
    import astunparse
except ImportError:
    astunparse = None


def _is_matching_decorator(node, removal_expression):
    if not hasattr(node, "decorator_list"):
        return False
    else:
        calls_list = [
            call for call in node.decorator_list
            if type(call) is ast.Call
        ]
        private_tag_call = [
            call for call in calls_list
            if call.func.value.id == "private"
            and call.func.attr == "tag"
        ]

        if len(private_tag_call) == 0:
            return False
        elif len(private_tag_call) > 1:
            raise ValueError("More then one call to tag decorator")

        private_tag_call, = private_tag_call

        tags = {arg.s: True for arg in private_tag_call.args}
        expression_globals = defaultdict(lambda: False, **tags)
        return eval(removal_expression, expression_globals)


def remove_tagged_source(source, removal_expression):
    ast_tree = ast.parse(source)
    if hasattr(ast_tree, "body"):
        ast_tree.body = [
            sub_node for sub_node in ast_tree.body
            if not _is_matching_decorator(sub_node, removal_expression)
        ]
        for sub_node in ast_tree.body:
            remove_tagged_source(sub_node, removal_expression)
    return astunparse.unparse(ast_tree)
