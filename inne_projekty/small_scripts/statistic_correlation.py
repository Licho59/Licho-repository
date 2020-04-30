import math

x_data = [65, 72, 78, 65, 72, 70, 65, 68]
y_data = [72, 69, 79, 69, 84, 75, 60, 73]

mean_x = sum(x_data) / len(x_data)
mean_y = sum(y_data) / len(y_data)
print('mean(x) =', mean_x, '\t', 'mean(y) =', mean_y)

var_x = 0
for x in x_data:
    m = math.pow((x - mean_x), 2)
    var_x += m
var_x = var_x / len(x_data)

var_y = 0
for y in y_data:
    m = math.pow((y - mean_y), 2)
    var_y += m
var_y = var_y / len(y_data)

print('variance(x) =', round(var_x, 2), '\t',
      'variance(y) =', round(var_y, 2), '\n')

covar = 0
for i in range(len(x_data)):
    k = x_data[i] * y_data[i]
    covar += k
covar = covar / len(x_data) - (mean_x * mean_y)
print('Covariance(x,y) =', round(covar, 2))

x_y_correlance = round(covar / math.sqrt(var_x * var_y), 2)
print('Correlation between x and y is', x_y_correlance)
