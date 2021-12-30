#Grokking Deep Learning 

'''
Vector Math Challenge

Create functions that can can manipulate vectors in the 
following ways
1) Elementwise multiplication
2) Elementwise addition
3) Vector Sum 
4) Vector Average 

'''

def elementwise_multiplication( vec_a, vec_b ):

    assert ( len ( vec_a ) == len( vec_b ) )
    output = []
    for i in range( len( vec_a ) ): 
        output.append( vec_a[ i ] * vec_b[ i ] )

    return output

def elemnetwise_addition( vec_a, vec_b ):

    assert ( len( vec_a ) == len( vec_b ) )

    output = []

    for i in range( len ( vec_a ) ): 
        output.append( vec_a[ i ] + vec_b[ i ] )
    
    return output

def vector_sum ( vec_a ):

    sum = 0 

    for i in range( len( vec_a ) ):
        sum += vec_a[ i ]

    return sum

def vector_avg( vec_a ):
    n = len ( vec_a )

    sum = vector_sum ( vec_a )
    avg = sum / n
    return avg 


# Sample points 
a = [ 0.1, 0.2, 0 ]
b = [ 8.5, 0.65, 1.2 ]



el_mult = elementwise_multiplication ( a, b)
el_add = elemnetwise_addition ( a, b)

a_sum = vector_sum ( a )
b_sum = vector_sum ( b )

a_avg = vector_avg ( a )
b_avg = vector_avg ( b )

print ( el_mult, el_add, a_sum, b_sum, a_avg, b_avg)

# Use two of the above functions to compute the dot product of the two vectos 
dot_prod =  vector_sum ( el_mult )
print ( dot_prod )