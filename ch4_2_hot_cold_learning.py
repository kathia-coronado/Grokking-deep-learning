# neural network demo with hot and cold learning optimization 

weight = 0.5 
input = 0.5

goal_prediction = 0.8
step_amount = 0.001 

for iteration in range (1101):
    prediction = input * weight 
    error = (goal_prediction - prediction) ** 2 

    print ("Error:" + str(error) + " Prediction:" + str(prediction))

    up_pred = input * (weight + step_amount) # up 
    up_error = ( goal_prediction - up_pred) ** 2 

    down_pred = input * (weight - step_amount) # down 
    down_error = ( goal_prediction - down_pred) ** 2 

    if (down_error < up_error):
        weight = weight - step_amount

    if (down_error > up_error):
        weight = weight + step_amount
    
