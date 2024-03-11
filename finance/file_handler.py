import pandas

def read_file(path: str):
    try:
        data = pandas.read_csv(path)
    except:
        print("Could not read data from given file.")
        return None

    data = data[["Date", "Time", "Name", "Category", "Amount"]]
    return data

def store_file(data: pandas.DataFrame, label: str, path: str):
    path = path + label + ".csv"

    try:
        data.to_csv(path)
    except:
        print("Could not write file.")
        return False

    return True

data = read_file("test.csv")
print(data)
if data is not None:
    store_file(data, "test_store", "")
