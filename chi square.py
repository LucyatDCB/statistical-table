#combined t test and z test
ttable1 = [
    [6.314,12.706,31.821,63.657,318.309,636.619],
    [2.920,4.303,6.965,9.925,22.327,31.599],
    [2.353,3.182,4.541,5.841,10.215,12.924],
    [2.132,2.776,3.747,4.604,7.173,8.610],
    [2.015,2.571,3.365,4.032,5.893,6.869],
    [1.943,2.447,3.143,3.707,5.208,5.959],
    [1.894,2.365,2.998,3.499,4.785,5.408],
    [1.860,2.306,2.896,3.355,4.501,5.041],
    [1.833,2.262,2.821,3.250,4.297,4.781],
    [1.812,2.228,2.764,3.169,4.144,4.587],
    [1.796,2.201,2.718,3.106,4.025,4.437],
    [1.782,2.179,2.681,3.055,3.930,4.318],
    [1.771,2.160,2.650,3.012,3.852,4.221],
    [1.761,2.145,2.624,2.977,3.787,4.140],
    [1.753,2.131,2.602,2.947,3.733,4.073],
    [1.746,2.120,2.583,2.921,3.686,4.015],
    [1.740,2.110,2.567,2.898,3.646,3.965],
    [1.734,2.101,2.552,2.878,3.610,3.922],
    [1.729,2.093,2.539,2.861,3.579,3.883],
    [1.725,2.086,2.528,2.845,3.552,3.850],
    [1.721,2.080,2.518,2.831,3.527,3.819],
    [1.717,2.074,2.508,2.819,3.505,3.792],
    [1.714,2.069,2.500,2.807,3.485,3.768],
    [1.711,2.064,2.492,2.797,3.467,3.745],
    [1.708,2.060,2.485,2.787,3.450,3.725],
    [1.706,2.056,2.479,2.779,3.435,3.707],
    [1.703,2.052,2.473,2.771,3.421,3.690],
    [1.701,2.048,2.467,2.763,3.408,3.674],
    [1.699,2.045,2.462,2.756,3.396,3.659],
    [1.697,2.042,2.457,2.750,3.385,3.646],
    [1.694,2.037,2.449,2.738,3.365,3.622],
    [1.691,2.032,2.441,2.728,3.348,3.601],
    [1.688,2.028,2.434,2.719,3.333,3.582],
    [1.686,2.024,2.429,2.712,3.319,3.566],
    [1.684,2.021,2.423,2.704,3.307,3.551],
    [1.682,2.018,2.418,2.698,3.296,3.538],
    [1.680,2.015,2.414,2.692,3.286,3.526],
    [1.679,2.013,2.410,2.687,3.277,3.515],
    [1.677,2.011,2.407,2.682,3.269,3.505],
    [1.676,2.009,2.403,2.678,3.261,3.496],
    [1.671,2.000,2.390,2.660,3.232,3.460],
    [1.667,1.994,2.381,2.648,3.211,3.435],
    [1.664,1.990,2.374,2.639,3.195,3.416],
    [1.662,1.987,2.368,2.632,3.183,3.402],
    [1.660,1.984,2.364,2.626,3.174,3.390],
    [1.658,1.980,2.358,2.617,3.160,3.373],
    [1.655,1.976,2.351,2.609,3.145,3.357],
    [1.653,1.972,2.345,2.601,3.131,3.340],
    [1.650,1.968,2.339,2.592,3.118,3.323],
    [1.649,1.966,2.336,2.588,3.111,3.315],
    [1.648,1.965,2.334,2.586,3.107,3.310],
    [1.647,1.964,2.333,2.584,3.104,3.307],
    [1.645,1.960,2.326,2.576,3.090,3.291]
  ]

dof = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 60, 70, 80, 90, 100, 120, 150, 200, 300, 400, 500, 600, 'inf']
α1 = [5, 2.5, 1, 0.5, 0.1, 0.05]
α2 = [10, 5, 2, 1, 0.2, 0.1]

print("Statistics")
print("\n 1. t-test\n 2. z-test\n 3. chi-square test\n 4. f-test")
option1 = int(input("Choose your option: "))

# t-test
if option1 == 1:
    print("\n 1. one-tailed\n 2. two-tailed test")
    option2 = int(input("Choose your option: "))
    α_list = α1 if option2 == 1 else α2

# z-test
elif option1 == 2:
    print("\n 1. one-tailed\n 2. two-tailed test")
    option2 = int(input("Choose your option: "))
    α_list = α1 if option2 == 1 else α2
else:
    α_list = α1 #need correction in the code here

while True:
    try:
        n1 = int(input("Enter the degree of freedom: (ex. 1, 2, 3, ...) "))
        n2 = float(input(f"Enter level of significance (α) in %: (ex. {', '.join(map(str, α_list))}) "))

        if n1 in dof and n2 in α_list:
            break
        else:
            print("Invalid values. Please enter valid dof and α values.")
    except ValueError:
        print("Invalid input.")

print("The value in the statistical table of dof (", n1, ") and α (", n2, ") is ", ttable1[dof.index(n1)][α_list.index(n2)])
