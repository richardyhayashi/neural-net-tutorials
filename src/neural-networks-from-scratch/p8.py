'''
Classes:
0 - dog
1 - cat
2 - human
'''
import numpy as np

softmax_output = np.array([[0.0, 0.1, 0.2],
                           [0.1, 0.5, 0.4],
                           [0.02, 0.9, 0.08]])
class_targets = [0, 1, 1]

print(-np.log(softmax_output[[0, 1, 2], class_targets]))