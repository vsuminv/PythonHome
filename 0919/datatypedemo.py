# kor = 90
# address ="서울시 강남구 역삼동"
# weight = 62.4
# print(type(kor))
# print(type(address))
# print(type(weight))

# myValue =True
# print(myValue)

# print(type(myValue))

# print(str(myValue) + "is of the data type " + str(type(myValue)))

# myString = "Thist is a string"
# print(myString)
# print(type(myString))

# print(myString + "is of the data type" + str(type(myString)))

# first = 'water'
# secondeString = 'fall'
# thirdString = first+secondeString
# print(thirdString)


# name = input("What is your name? ")
# # print(name)

# color = input("What is your favorite color ?")
# animal = input ("What is your favorite animal? ")
# print("{}, you like a {} {} !".format(name, color, animal))

# myMixedTypeList=[45,290578,1.02, True, "My dog is on the bed", "45"]

# for item in myMixedTypeList:
#     print("{}is of the data type{}".format(item,type(item)))

import csv
import copy
myVehicle = {
    "vin" :"<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mlieage" : 0   
}

for key, value in myVehicle.items():
    print("{}: {}".format(key,value))

myInventoyList = []
with open('car_fleet_csv')as csvFile:
    csvReacer = csv.reader(csvFile,delimiter=',')

    lineCount = 0
    for row in csvReacer:
        if lineCount == 0:
            print(f'Column names are : {",".join(row)}')
            lineCount += 1
        else:
            print(f'vin:{row[0]} make = {row[1]}, mode={row[2]}, year:{row[3]}, range : {row[4]}, topSpeed : {row[5]}, zeroSixty : {row[6]}, mileage : {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoyList.append(currentVehicle)
            lineCount += 1
        print(f'Processed {lineCount} lines')

            
            
