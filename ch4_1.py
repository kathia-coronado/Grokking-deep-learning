#Hot and cold learning demonstration 

weight = 0.1 
lr = 0.01 
def neural_network(input, weight):
    prediction = input * weight
    return prediction

number_of_toes = [8.5]
win_or_loose_binary = [1] # won!! 
input = number_of_toes[0]
true = win_or_loose_binary[0]
lr = 0.01

pred = neural_network(input, weight)
error = (pred - true) ** 2

p_up = neural_network(input, weight + lr)
e_up = (p_up - true) ** 2

p_dn = neural_network(input, weight - lr)
e_dn = (p_dn - true) ** 2

if (error > e_dn or error > e_up):
    if (e_dn < e_up):
        weight -= lr
    
    if (e_up < e_dn):
        weight += lr
print(error, e_up, e_dn)
print(weight)