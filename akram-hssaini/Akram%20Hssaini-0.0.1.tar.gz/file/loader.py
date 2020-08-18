import pathlib as pl

global_path = str(pl.Path(__file__).parents[2])


def load_td_file(path):
    file = open(global_path + '\\'+path, 'r')
    train_data = []
    for x in file:
        line = x.strip()
        line_data = []
        for item in line.split(';'):
            if 'str:' in item:
                line_data.append(str(item.replace('str:', '')))
            if 'b:' in item:
                val = item.replace('b:','')
                if val == 'True' or val == '1':
                    line_data.append(True)
                if val == 'False' or val == '0':
                    line_data.append(False)
        train_data.append(line_data)
    return train_data