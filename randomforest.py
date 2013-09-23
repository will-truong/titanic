from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn import cross_validation
import csv
import numpy

train_file = csv.reader(open('csv/train.csv'))
test_file = csv.reader(open('csv/test.csv'))
out_file = csv.writer(open('csv/out.csv','w',newline=''))


data = []
test_data = []
for row in train_file:
	data.append(row)

for row in test_file:
	test_data.append(row)

del test_data[0]
del data[0]

dataset = [data, test_data]
for i in range(0,2):
	for row in dataset[i]:
		row[11] = 0 if row[11] == 'S' else 1 if row[11] == 'C' else 2 if row[11] == 'Q' else 0
		del row[11]
		del row[10]
		row[9] = 7.8958 if row[9] == '' else row[9]
		del row[8]
		row[5] = 28 if row[5] == '' else row[5]
		row[4] = 1 if row[4] == 'female' else 0 if row[4] == 'male' else row[4]
		del row[3]	
		temp = row[0]
		row[0] = row[1]
		row[1] = temp
		row[4] = 28 if row[4] == '' else float(row[4])
		del row[1]
		if i == 1:
			del row[0]
		row = [float(j) for j in row]
#		print(row)

data = numpy.array(data)

forest = RandomForestClassifier(n_estimators = 20)
data2 = data[0::,1::]
target = data[0::,0]
forest = forest.fit(data2, target)
prediction = forest.predict(test_data)

out_file.writerow(('Survived', 'PassengerId'))
passengerid = 892
for entry in prediction:
	out_file.writerow((int(entry), passengerid))
	passengerid = passengerid + 1

clf = svm.SVC(kernel='linear', C = 1)
scores = cross_validation.cross_val_score(clf, data2, target, cv=2)
print(scores)