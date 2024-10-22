# Neural Networks from Scratch

by `sentdex`

YouTube: `https://www.youtube.com/watch?v=tMrbN67U9d4&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=3`

Source:

1. Intro and Neuron Code
2. Coding a Layer
3. The Dot Product
4. Batches, Layers, and Objects
5. Hidden Layer Activation Functions
6. Softmax Activation
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

$$
\begin{aligned}
y = \text{1 }x \gt 0\\
    \text{0 } x \leq 0
\end{aligned}
$$

#### Sigmoid Function

$$
y = \frac{1}{1 + e^{-x}}
$$

#### Rectified Linear Function

$$
\begin{aligned}
y = x\text{ } x > 0\\
    \text{0 } x \leq 0
\end{aligned}
$$

#### Exponential Function

$$y = e^x$$

e ~ 2.718281828459045

#### Softmax Activation Function

Exponentiation + Normalization

$$
S_{i,j}=\frac{e^{z_{i,j}}}{\Sigma_{l=1}^Le^{z_{i,j}}}
$$
