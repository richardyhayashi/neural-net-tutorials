# Neural Networks from Scratch
by `sentdex`

YouTube: `https://www.youtube.com/watch?v=tMrbN67U9d4&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=3`

Source:

1. Intro and Neuron Code
2. Coding a Layer
3. The Dot Product
4. Batches, Layers, and Objects
5. Hidden Layer Activation Functions
6.
7.
8.
9.


## Notes

### Start Python Environment

`$ cd neural-networks-from-scratch`
`$ pipenv shell`

### Install

`$ pipenv install numpy matplotlib nnfs`

### Websites

`https://cs231n.github.io/neural-networks-case-study`

### Activation Functions

#### Step Function

y = 1  x > 0
    0  x <= 0
    
#### Sigmoid Function

         1
y =  --------
           -x
      1 + e
#### Rectified Linear Function

y = x  x > 0
    0  x <= 0