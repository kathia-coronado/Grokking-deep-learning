#Grokking Deep Learning 

'''
Single weight neural network uses one input in order to produce multiple
outputs or predictions. 

Input(s): wlrec := win loss records of the team 

Outputs: hur_pred := percentage of the team members that are hurt
         win_pred := likelihood that the team won
         sad_pred := likelihood that the players are sad
'''

def elementwise_multiplication( vec_a, vec_b ):

    '''
    Computes the elementwise multiplication a scalor and a vector
    
    inputs: vec_a := scalor 
            vec_b := vector

    Outputs: output: predicitons on how many players are hurt, 
                     if the the team won, 
                     and the likelihood that the players are sad.
    
    '''

    output = [ None ] * len( vec_b )

    # multiply the input scalor by each of the element in the vector
    for i in range( len( vec_b ) ): 
        output[i] = ( vec_a * vec_b [ i ] )

    return output



def neural_network (input, weights): 
    
    pred = elementwise_multiplication( input, weights)

    return pred

weights = [ 0.3, 0.2, 0.9 ]
wrlec = [ 0.65, 0.8, 0.8, 0.9 ] 


for i in range( len( wrlec) ):
    input = wrlec [ i ] 
    predic = neural_network( input, weights )
    print ( 'Input: ', input, ' Prediction: ', predic )


