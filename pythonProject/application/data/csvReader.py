import csv

def read_csv(path):
    csv_list = []
    with open(path) as file:
        csv_file = csv.reader(file)
        for lines in csv_file:
            csv_list.append(lines)

    return csv_list


if __name__ == '__main__':
    print(read_csv('glossary.csv'))