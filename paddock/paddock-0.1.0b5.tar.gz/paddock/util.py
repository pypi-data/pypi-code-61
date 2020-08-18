__all__ = [
    "format_results",
]


def format_results(results, header):
    newres = []
    for row in results:
        newr = {}
        for k, v in row.items():
            newr[header[k]] = v
        newres.append(newr)
    return newres
