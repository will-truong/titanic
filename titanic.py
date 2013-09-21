import csv
import numpy

csv_file = csv.reader(open('train.csv', 'r'))
header = next(csv_file)

data = []
for row in csv_file:
	data.append(row)
data = numpy.array(data)

print(header)

num_passengers = numpy.size(data[0::,1])
num_survivors = numpy.sum(data[0::,1].astype(numpy.float))
print(num_survivors/num_passengers)

women_only = data[0::,4] == "female"
women_onboard = data[women_only, 1].astype(numpy.float)
women_survival_rate = numpy.sum(women_onboard) / numpy.size(women_onboard)
print("%s%% of women survived" % women_survival_rate)

men_only = data[0::,4] != "female"
men_onboard = data[men_only, 1].astype(numpy.float)
men_survival_rate = numpy.sum(men_onboard) / numpy.size(men_onboard)
print("%s%% of men survived" % men_survival_rate)