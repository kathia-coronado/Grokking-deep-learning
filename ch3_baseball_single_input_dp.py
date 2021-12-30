#Grokking Deep Learning Chapter 3: 1st neural network
'''
This is a simple neural network maps one data input point to the output or prediction
input := the number of toes in a baseball team
prediction := likelihood that the team has won or lost
'''
weight = 0.1 
def neural_network ( input, weight ):
    prediction = weight * input
    return prediction

num_toes = [ 8.5, 9.5, 10, 9 ]
#input = num_toes [0]
#predic = neural_network(input,weight)
#print(predic)

for i,toes in enumerate ( num_toes ):
    input = toes
    predic = neural_network ( input, weight )
    print ('number of toes: ', toes,' Prediction: ', predic )