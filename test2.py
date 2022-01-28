

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import re
import json


def preprocesstweets():
    df1 = pd.read_csv('tests/covidvaccine.csv', usecols=['text'])
    df1.info(verbose=False, memory_usage="deep")

    list1 = df1.values.tolist()

    hashtags = []
    for i in range(10000):
        hashtags.append(re.findall(r"#(\w+)", json.dumps(list1[i])))

    list2 = [x for x in hashtags if x != []]
    print(len(list2))
    str1 = ""
    for ele in list2:
        for elem in ele:
            str1 += elem
            str1 += " -1 "
        str1 += "-2\n"
    covidvaccinedata  = open("tests/covidvaccinedata.text" ,"w")
    covidvaccinedata.write(str1)
    covidvaccinedata.close()
