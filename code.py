def get_data(path):
    """Read the file and return a list of lists of integers."""
    with open(path) as p:
        num = []
        for lines in p:
            lines = lines.split()
            lines = list(map(int, lines))
            num.append(lines)
    return num


def analyze_data(int_list, option):
    """Do the math work indicated by the option on a list of lists of integers."""
    if option == "average":
        num = 0
        length = 0
        for i in range(0, len(int_list)):
            length = length + len(int_list[i])
            for numbers in int_list[i]:
                num = num + numbers
        print(round(num / length, 1))
    if option == "standard deviation":
        num = 0
        length = 0
        for i in range(0, len(int_list)):
            length = length + len(int_list[i])
            for numbers in int_list[i]:
                num = num + numbers
        average = num / length
        squared_diff = 0
        for i in range(0, len(int_list)):
            for numbers in int_list[i]:
                squared_diff = squared_diff + (numbers - average) ** 2
        print(round((squared_diff / length) ** 0.5, 1))
    if option == "covariance":
        list1 = int_list[0]
        list2 = int_list[1]
        sum1 = 0
        sum2 = 0
        for numbers in list1:
            sum1 = sum1 + numbers
        for numbers in list2:
            sum2 = sum2 + numbers
        mean1 = sum1 / len(list1)
        mean2 = sum2 / len(list2)
        numerator = 0
        for i in range(0, len(list1)):
            numerator = numerator + (list1[i] - mean1) * (list2[i] - mean2)
        print(int(numerator / (len(list1))))
    if option == "correlation":
        list1 = int_list[0]
        list2 = int_list[1]
        sum1 = 0
        sum2 = 0
        for numbers in list1:
            sum1 = sum1 + numbers
        for numbers in list2:
            sum2 = sum2 + numbers
        mean1 = sum1 / len(list1)
        mean2 = sum2 / len(list2)
        numerator = 0
        squared_diff1 = 0
        squared_diff2 = 0
        for i in range(0, len(list1)):
            numerator = numerator + (list1[i] - mean1) * (list2[i] - mean2)
            squared_diff1 = squared_diff1 + (list1[i] - mean1) ** 2
            squared_diff2 = squared_diff2 + (list2[i] - mean2) ** 2
        print(round(numerator / (squared_diff1 * squared_diff2) ** 0.5, 3))
