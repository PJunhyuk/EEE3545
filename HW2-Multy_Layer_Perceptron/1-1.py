import math
import random
random.seed(10300)


# Generate a random number x that is a <= x < b
def rand(a, b):
    return (b - a) * random.random() + a

# Create a matrix and initialize with 'value'
def createMatrix(I, J, value=0.0):
    matrix = []
    for i in range(I):
        matrix.append([value] * J)
    return matrix

# Sigmoid function
def sigmoid(x):
    return math.tanh(x)

# Derivative of sigmoid function
def d_sigmoid(y):
    return 1.0 - y ** 2



class MLP:
    def __init__(self, n_input, n_hidden, n_output):
        self.n_input = n_input + 1
        self.n_hidden = n_hidden
        self.n_output = n_output

        self.activ_input = [1.0] * self.n_input
        self.activ_hidden = [1.0] * self.n_hidden
        self.activ_output = [1.0] * self.n_output

        self.weight_input = createMatrix(self.n_input, self.n_hidden)
        self.weight_output = createMatrix(self.n_hidden, self.n_output)

        for i in range(self.n_input):
            for j in range(self.n_hidden):
                self.weight_input[i][j] = rand(-0.2, 0.2)
        for j in range(self.n_hidden):
            for k in range(self.n_output):
                self.weight_output[j][k] = rand(-2.0, 2.0)

        self.change_input = createMatrix(self.n_input, self.n_hidden)
        self.change_output = createMatrix(self.n_hidden, self.n_output)


    def update(self, inputs):
        ############################ 1-1 ##################################
        #input layer activation
        # input으로 받은 데이터를 sigmoid함수를 통하여 activ_input에 반복하여 입력한다.
        for i in range(self.n_input - 1):


        ###################################################################
            

        ############################ 1-2 ##################################
        # hidden layer activation
        # hidden layer를 만들어서 input 데이터에 가중치를 주어서 sigmoid함수를 통하여 activ_hidden에 입력한다.
        for i in range(self.n_hidden):
            sum = 0.0
            for j in range(self.n_input):
        

        ###################################################################            

        ############################ 1-3 ##################################
        # output layer activation
        # output layer를 만들어서 hidden layer 데이터에 가중치를 주어서 sigmoid함수를 통하여 active_output에 입력한다.
        # 입력한 값을 반환한다
        for i in range(self.n_output):
            sum = 0.0
            for j in range(self.n_hidden):

        return self.activ_output[:]



        ###################################################################


    def backpropagation(self, target, L, M):
        
        ############################ 1-4 ##################################
        # calculate output layer error
        # d_sigmoid 함수를 이용하여 output_delta값을 구한다.
        output_delta = [0.0] * self.n_output
        for k in range(self.n_output):



        ###################################################################
            
        ############################ 1-5 ##################################
        # calculate hidden layer error
        # d_sigmoid 함수를 이용하여 hidden_delta값을 구한다.
        hidden_delta = [0.0] * self.n_hidden
        for j in range(self.n_hidden):
            error = 0.0
            for k in range(self.n_output):


        ###################################################################            

        ############################ 1-6 ##################################
        # update output layer weights
        # weight_output과 change_output값을 업데이트 한다.
        for j in range(self.n_hidden):
            for k in range(self.n_output):


        
        ###################################################################

        ############################ 1-7 ##################################
        # update input layer weights
        for i in range(self.n_input):
            for j in range(self.n_hidden):
        

        
        ###################################################################

        ############################ 1-8 ##################################
        # calculate error
        # target data값과 output 값의 차이를 error에 입력하여 error값을 반환한다.
        error = 0.0
        for k in range(len(target)):

        return error        
        ###################################################################



    ############################ 1-9 ##################################
    # train for given iteration 
    def train(self, pattern, iterations=1000):

        L = 0.5      #learning rate
        M = 0.1      #momentum factor
        
    # input 으로 pattern을 받아, 1000회에 걸쳐 training을 수행함
    
        
    ###################################################################


    ############################ 1-10 ##################################
    #input으로 pattern을 받아 test를 수행하고, 콘솔에 결과를 출력한다.
    def test(self, pattern):
    
        
    ###################################################################


def Network():
    # Our goal is  XOR function
    pat = [
        [[0, 0], [0]],
        [[0, 1], [1]],
        [[1, 0], [1]],
        [[1, 1], [0]]
    ]
    # MLP with two input nodes, three hidden nodes, and one output node
    n = MLP(2, 3, 1)

    # training
    n.train(pat)

    # testing
    n.test(pat)


if __name__ == '__main__':
    Network()
