import csv
from turtledemo.penrose import start


def read_csv(path):
    csv_list = []
    with open(path) as file:
        csv_file = csv.reader(file)
        for lines in csv_file:
            if len(lines) > 2:
                lines[2:] = [' '.join(lines[2:])]
                csv_list.append(lines)

    csv_list.sort()
    return csv_list


def find_tags(path):
    # instantiate an empty set
    tags_set = set()
    csv_list = []
    with open(path) as file:
        csv_file = csv.reader(file)
        for lines in csv_file:
            csv_list.append(lines)

    csv_list.sort()

    # iterates over each element
    for item in csv_list:
        # if a term contains 1 or more tags, add to the set
        if len(item) > 2:
            tags_set.update(item[2:])

    return tags_set


if __name__ == '__main__':
    print(read_csv('glossary.csv'))