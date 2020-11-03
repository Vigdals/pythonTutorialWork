def function3(x, y):
    return x + y


a = function3(5, 5)
print(a)


def function4(x):
    print(x)
    print("Still in the funtion")
    return 3 * x


f = function4(4)
print(f)


def function5(some_argument):
    print(some_argument)
    print("Weee")


function5(4)

# BMI Calc
name1 = "Adiran"
height_m1 = 1.85
weight_kg1 = 90

name2 = "Anne"
height_m2 = 1.65
weight_kg2 = 60

name3 = "Johannes"
height_m3 = 0.40
weight_kg3 = 3.9

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"


result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)


def convert(miles):
    km = 1.6 * miles
    print(miles)
    print("miles are this much km")
    return km


converterResult = convert(10)
print(converterResult)
