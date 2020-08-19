from fim.graph.labels import Label, LabelException

if __name__ == "__main__":

    l = Label(ltype="mac", lval="something")
    print(l)
    print(l.get_label_as_json())
    l1 = Label(ltype="mac", lval="something else")
    l2 = Label(ltype="bdf", lval="other")
    assert l1.check_label_type(l2) is False
    assert l.check_label_type(l1) is True