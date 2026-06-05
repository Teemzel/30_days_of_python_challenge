# 100 numpy exercises

''' This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow
and in the numpy documentation. The goal of this collection is to offer a quick reference for both old
and new users but also to provide a set of exercises for those who teach.'''


''' If you find an error or think you've a better way to solve some of them, feel
free to open an issue at <https://github.com/rougier/numpy-100>.
File automatically generated. See the documentation to update questions/answers/hints programmatically. '''

# 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

# 2. Print the numpy version and the configuration (★☆☆)
print(np.__version__)
print(np.show_config())

# 3. Create a null vector of size 10 (★☆☆)
Z = np.zeros(10, dtype=int)
print(Z)

# 4. How to find the memory size of any array (★☆☆)
print(Z.nbytes)

# 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
np.info(np.add)

# 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
Z = np.zeros(10)
Z[4] = 1
print(Z)

# 7. Create a vector with values ranging from 10 to 49 (★☆☆)
Z = np.arange(10, 50)
print(Z)

# 8. Reverse a vector (first element becomes last) (★☆☆)
Z = Z[::-1]
print(Z)

# 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
Z = np.arange(9).reshape(3, 3)
print(Z)

# 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
Z = np.array([1, 2, 0, 0, 4, 0])
indices = np.nonzero(Z)
print(indices)

# 11. Create a 3x3 identity matrix (★☆☆)
Z = np.eye(3)
print(Z)

# 12. Create a 3x3x3 array with random values (★☆☆)
Z = np.random.random((3, 3, 3))
print(Z)

# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
Z = np.random.random((10, 10))
print("Minimum value:", Z.min())
print("Maximum value:", Z.max())
print(Z)
# 14. Create a random vector of size 30 and find the mean value (★☆☆)
Z = np.random.random(30)
print("Mean value:", Z.mean())

# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
Z = np.ones((5, 5))
Z[1:4, 1:4] = 0
print(Z)

# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
Z = np.ones((5, 5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)

# 17. What is the result of the following expression? (★☆☆)
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1 

# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
Z = np.diag(1 + np.arange(4), k=-1) 

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
Z = np.zeros((8, 8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1

# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
Z = np.arange(6*7*8).reshape(6, 7, 8)
index = np.unravel_index(100, Z.shape)

# 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
Z = np.tile([[0, 1], [1, 0]], (4, 4))

# 22. Normalize a 5x5 random matrix (★☆☆)
Z = np.random.random((5, 5))
Z = (Z - Z.min()) / (Z.max() - Z.min())

# 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
dt = np.dtype([('r', np.uint8), ('g', np.uint8), ('b', np.uint8), ('a', np.uint8)])

# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
A = np.random.random((5, 3))
B = np.random.random((3, 2))
Z = np.dot(A, B)
print(Z)

# 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
Z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Z[(Z > 3) & (Z < 8)] *= -1

# 26. What is the output of the following script? (★☆☆)
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))


# 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
'''Z**Z
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
Z<Z>Z'''


# 28. What are the result of the following expressions? (★☆☆)
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]).astype(int).astype(float)

# 29. How to round away from zero a float array ? (★☆☆)
Z = np.array([-1.5, -0.5, 0.5, 1.5])
rounded = np.where(Z > 0, np.ceil(Z), np.floor(Z)) 

# 30. How to find common values between two arrays? (★☆☆)
Z1 = np.array([1, 2, 3, 4, 5])
Z2 = np.array([4, 5, 6, 7, 8])
common_values = np.intersect1d(Z1, Z2)
print(common_values)    

# 31. How to ignore all numpy warnings (not recommended)? (★☆☆)
import warnings
warnings.filterwarnings('ignore')   

# 32. Is the following expressions true? (★☆☆)
np.sqrt(-1) == np.emath.sqrt(-1)

# 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
today = np.datetime64('today')
yesterday = today - np.timedelta64(1, 'D')
tomorrow = today + np.timedelta64(1, 'D')   

# 34. How to get all the dates corresponding to the month of July 2016? (★★☆)
july_2016 = np.arange('2016-07', '2016-08', dtype='datetime64[D]')  

# 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
A = np.random.random((5, 5))
B = np.random.random((5, 5))
A += B
A *= -A / 2

# 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)
Z = np.random.random(10) * 10
integer_part1 = Z.astype(int)
integer_part2 = np.floor(Z).astype(int)
integer_part3 = np.trunc(Z).astype(int)
integer_part4 = np.array(Z, dtype=int)

# 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
Z = np.zeros((5, 5), dtype=int)
Z += np.arange(5)

# 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
def generator():
    for i in range(10):
        yield i
Z = np.fromiter(generator(), dtype=int)

# 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
Z = np.linspace(0, 1, 12, endpoint=False)[1:]
print(Z)

# 40. Create a random vector of size 10 and sort it (★★☆)
Z = np.random.random(10)
Z.sort()

# 41. How to sum a small array faster than np.sum? (★★☆)
Z = np.random.random(10)
total_sum = np.add.reduce(Z)
print(total_sum)

# 42. Consider two random array A and B, check if they are equal (★★☆)
A = np.random.random((5, 5))
B = np.random.random((5, 5))
are_equal = np.array_equal(A, B)

# 43. Make an array immutable (read-only) (★★☆)
Z = np.array([1, 2, 3, 4, 5])
Z.flags.writeable = False

# 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
Z = np.random.random((10, 2))
x = Z[:, 0]
y = Z[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
polar_coordinates = np.column_stack((r, theta))
print(polar_coordinates)

# 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
Z = np.random.random(10)
Z[Z.argmax()] = 0
print(Z)
# 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)
x = np.linspace(0, 1, 5)
y = np.linspace(0, 1, 5)
structured_array = np.array([(xi, yi) for xi in x for yi in y], dtype=[('x', float), ('y', float)])
print(structured_array)

# 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)
X = np.random.random(5)
Y = np.random.random(5)
C = 1 / (X[:, np.newaxis] - Y)  
print(C)

# 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)
for dtype in [np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64, np.float16, np.float32, np.float64]:
    info = np.iinfo(dtype) if np.issubdtype(dtype, np.integer) else np.finfo(dtype)
    print(f"{dtype}: min={info.min}, max={info.max}")

# 49. How to print all the values of an array? (★★☆)
Z = np.random.random((5, 5))
np.set_printoptions(threshold=np.inf)
print(Z)

# 50. How to find the closest value (to a given scalar) in a vector? (★★☆)
Z = np.random.random(10)
scalar = 0.5    
closest_value = Z[np.argmin(np.abs(Z - scalar))]
print(closest_value)

# 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
dtype = np.dtype([('position', [('x', float), ('y', float)]), ('color', [('r', int), ('g', int), ('b', int)])])
structured_array = np.array([((1.0, 2.0), (255, 0, 0)), ((3.0, 4.0), (0, 255, 0))], dtype=dtype)
print(structured_array)

# 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)
Z = np.random.random((100, 2))
distances = np.sqrt(np.sum((Z[:, np.newaxis] - Z) **2, axis=-1))
print(distances)

# 53. How to convert a float (32 bits) array into an integer (32 bits) in place?
Z = np.random.random(10).astype(np.float32)
Z = Z.astype(np.int32, copy=False)

# 54. How to read the following file? (★★☆)
'''1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11
'''
'''Z = np.genfromtxt('data.csv', delimiter=',', filling_values=np.nan)
print(Z)'''

# 55. What is the equivalent of enumerate for numpy arrays? (★★☆)
for i, value in enumerate(Z):
    print(f"Index: {i}, Value: {value}")
    
# 56. Generate a generic 2D Gaussian-like array (★★☆)
def gaussian_2d(size, sigma):
    x = np.linspace(-size // 2 + 1, size // 2, size)
    y = np.linspace(-size // 2 + 1, size // 2, size)
    x, y = np.meshgrid(x, y)
    d = np.sqrt(x**2 + y**2)
    g = np.exp(-(d**2 / (2.0 * sigma**2)))
    return g
gaussian_array = gaussian_2d(5, 1)
print(gaussian_array) 

# 57. How to randomly place p elements in a 2D array? (★★☆)
def place_random_elements(array, p):
    indices = np.random.choice(array.size, p, replace=False)
    np.put(array, indices, 1)
    return array
array = np.zeros((5, 5), dtype=int)
result = place_random_elements(array, 5)
print(result)

# 58. Subtract the mean of each row of a matrix (★★☆)
Z = np.random.random((5, 5))
row_means = Z.mean(axis=1, keepdims=True)
Z_centered = Z - row_means
print(Z_centered)

# 59. How to sort an array by the nth column? (★★☆)
Z = np.random.random((5, 5))
n = 2
sorted_Z = Z[Z[:, n].argsort()]
print(sorted_Z)

# 60. How to tell if a given 2D array has null columns? (★★☆)
Z = np.random.random((5, 5))
null_columns = np.all(Z == 0, axis=0)
print(null_columns)

# 61. Find the nearest value from a given value in an array (★★☆)
Z = np.random.random(10)
scalar = 0.5
closest_value = Z[np.argmin(np.abs(Z - scalar))]
print(closest_value)

# 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)
A = np.random.random((1, 3))
B = np.random.random((3, 1))
result = np.add.outer(A, B)
print(result)

# 63. Create an array class that has a name attribute (★★☆)
class NamedArray(np.ndarray):
    def __new__(cls, input_array, name):
        obj = np.asarray(input_array).view(cls)
        obj.name = name
        return obj
named_array = NamedArray([1, 2, 3], name="MyArray")
print(named_array)

# 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)
Z = np.zeros(10, dtype=int)
indices = np.array([0, 1, 2, 2, 3])
np.add.at(Z, indices, 1)
print(Z)    

# 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)
X = np.array([1, 2, 3, 4, 5])
F = np.zeros(10, dtype=int) 
I = np.array([0, 1, 2, 2, 3])
np.add.at(F, I, X)  
print(F)

# 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★☆)
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
unique_colors = np.unique(image.reshape(-1, 3), axis=0)     
num_unique_colors = unique_colors.shape[0]
print(num_unique_colors)    

# 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)
Z = np.random.random((2, 2, 2, 2))
result = Z.sum(axis=(-1, -2))   
print(result)

# 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★)
D = np.random.random(10)
S = np.random.randint(0, 3, 10)
means = np.zeros(S.max() + 1)
counts = np.zeros(S.max() + 1)  
np.add.at(means, S, D)
np.add.at(counts, S, 1)     
means /= counts
print(means)    

# 69. How to get the diagonal of a dot product? (★★★)
A = np.random.random((5, 5))
B = np.random.random((5, 5))    
diagonal = np.einsum('ij,ji->i', A, B)
print(diagonal)

# 70. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)
Z = np.array([1, 2, 3, 4, 5])
new_vector = np.zeros(len(Z) * 4 - 3, dtype=int)    
new_vector[::4] = Z
print(new_vector)

# 71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)
A = np.random.random((5, 5, 3))
B = np.random.random((5, 5))        
result = A * B[:, :, np.newaxis]
print(result)

# 72. How to swap two rows of an array? (★★★)
Z = np.random.random((5, 5))
Z[[0, 1]] = Z[[1, 0]]   
print(Z)

# 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the  triangles (★★★)
triangles = np.array([[[0, 0], [1, 0], [0, 1]],
                      [[1, 0], [1, 1], [0, 1]],
                        [[0, 0], [1, 0], [1, 1]],
                        [[0, 0], [0, 1], [1, 1]],
                        [[1, 0], [1, 1], [0, 0]],
                        [[0, 1], [1, 1], [0, 0]],
                        [[0, 0], [1, 1], [0, 1]],
                        [[1, 0], [0, 1], [1, 1]],
                        [[0, 0], [1, 0], [0, 1]],
                        [[1, 0], [1, 1], [0, 1]]])
edges = set()
for triangle in triangles:
    for i in range(3):
        edge = tuple(sorted((tuple(triangle[i]), tuple(triangle[(i + 1) % 3]))))
        edges.add(edge)
unique_edges = np.array(list(edges))
print(unique_edges)

# 74. Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)
C = np.array([0, 2, 3, 0, 1])
A = np.repeat(np.arange(len(C)), C) 
print(A)

# 75. How to compute averages using a sliding window over an array? (★★★)
def sliding_window_average(arr, window_size):   
    cumsum = np.cumsum(arr, dtype=float)
    cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
    return cumsum[window_size - 1:] / window_size
Z = np.random.random(10)
window_size = 3 
averages = sliding_window_average(Z, window_size)
print(averages)

# 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z[0],Z[1],Z[2]) and each subsequent row is  shifted by 1 (last row should be (Z[-3],Z[-2],Z[-1]) (★★★)
Z = np.random.random(10)
n = 3   
result = np.lib.stride_tricks.sliding_window_view(Z, window_shape=n)
print(result)   

# 77. How to negate a boolean, or to change the sign of a float inplace? (★★★)
Z = np.array([True, False, True])
Z = np.logical_not(Z, out=Z)        
Z = np.array([1.0, -2.0, 3.0])
Z = np.negative(Z, out=Z)

# 78. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i (P0[i],P1[i])? (★★★)
def distance_point_to_line(p, P0, P1):
    line_vec = P1 - P0
    p_vec = p - P0
    line_len = np.linalg.norm(line_vec, axis=1)
    line_unitvec = line_vec / line_len[:, np.newaxis]
    proj_length = np.sum(p_vec * line_unitvec, axis=1)
    proj_point = P0 + proj_length[:, np.newaxis] * line_unitvec
    distance = np.linalg.norm(proj_point - p, axis=1)
    return distance
p = np.array([1.0, 2.0])
P0 = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
P1 = np.array([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
distances = distance_point_to_line(p, P0, P1)   
print(distances)

# 79. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P[j]) to each line i (P0[i],P1[i])? (★★★)
def distance_points_to_lines(P, P0, P1):    
    line_vec = P1 - P0
    p_vec = P[:, np.newaxis, :] - P0
    line_len = np.linalg.norm(line_vec, axis=1)
    line_unitvec = line_vec / line_len[:, np.newaxis]
    proj_length = np.sum(p_vec * line_unitvec, axis=2)
    proj_point = P0 + proj_length[:, :, np.newaxis] * line_unitvec
    distance = np.linalg.norm(proj_point - P[:, np.newaxis, :], axis=2)
    return distance 
P = np.array([[1.0, 2.0], [2.0, 3.0]])
P0 = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
P1 = np.array([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
distances = distance_points_to_lines(P, P0, P1) 
print(distances)

# 80. Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a `fill` value when necessary) (★★★)
def extract_subpart(arr, center, shape, fill_value=0):  
    subpart = np.full(shape, fill_value, dtype=arr.dtype)
    arr_shape = arr.shape
    arr_slices = []
    subpart_slices = [] 
    for i in range(len(shape)):
        start = max(center[i] - shape[i] // 2, 0)
        end = min(center[i] + shape[i] // 2 + 1, arr_shape[i])
        subpart_start = max(shape[i] // 2 - center[i], 0)
        subpart_end = subpart_start + (end - start)
        arr_slices.append(slice(start, end))
        subpart_slices.append(slice(subpart_start, subpart_end))
    subpart[tuple(subpart_slices)] = arr[tuple(arr_slices)]
    return subpart
arr = np.random.random((5, 5))
center = (2, 2) 
shape = (3, 3)
subpart = extract_subpart(arr, center, shape)   
print(subpart)  

# 81. Consider an array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], how to generate an array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]? (★★★)
Z = np.arange(1, 15)
R = np.lib.stride_tricks.sliding_window_view(Z, window_shape=4) 
print(R)

# 82. Compute a matrix rank (★★★)
def matrix_rank(A, tol=1e-10):  
    u, s, vh = np.linalg.svd(A)
    rank = np.sum(s > tol)
    return rank
A = np.random.random((5, 5))
rank = matrix_rank(A)   
print(rank) 

# 83. How to find the most frequent value in an array?
Z = np.random.randint(0, 10, 100)
values, counts = np.unique(Z, return_counts=True)   
most_frequent_value = values[np.argmax(counts)]
print(most_frequent_value)

# 84. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★)
Z = np.random.random((10, 10))
blocks = np.lib.stride_tricks.sliding_window_view(Z, window_shape=(3, 3))
print(blocks)

# 85. Create a 2D array subclass such that Z[i,j] == Z[j,i] (★★★)
class SymmetricArray(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj

    def __setitem__(self, index, value):
        i, j = index
        super().__setitem__((i, j), value)
        super().__setitem__((j, i), value)
Z = SymmetricArray(np.zeros((5, 5)))
Z[1, 2] = 5 
print(Z)

# 86. Consider a set of p matrices with shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of of the p matrix products at once? (result has shape (n,1)) (★★★)
p = 3
n = 4   
matrices = np.random.random((p, n, n))
vectors = np.random.random((p, n, 1))   
result = np.einsum('pij,pjk->pik', matrices, vectors).sum(axis=0)
print(result)

# 87. Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★)
Z = np.random.random((16, 16))  
block_sum = Z.reshape(4, 4, 4, 4).sum(axis=(1, 3))
print(block_sum)

# 88. How to implement the Game of Life using numpy arrays? (★★★)
def game_of_life_step(Z):       
    neighbors = sum(np.roll(np.roll(Z, i, 0), j, 1) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i != 0 or j != 0))
    return (neighbors == 3) | (Z & (neighbors == 2))
Z = np.random.randint(0, 2, (5, 5), dtype=bool)
print("Initial state:\n", Z)    
Z = game_of_life_step(Z)
print("Next state:\n", Z)       

# 89. How to get the n largest values of an array (★★★)
Z = np.random.random(10)
n = 3
largest_values = np.partition(Z, -n)[-n:]
print(largest_values)

# 90. Given an arbitrary number of vectors, build the cartesian product (every combinations of every item) (★★★)
def cartesian_product(*arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = (len(a) for a in arrays)
    dtype = arrays[0].dtype
    result = np.empty(shape, dtype=dtype)
    for i, a in enumerate(arrays):
        result[..., i] = np.repeat(np.expand_dims(a, axis=tuple(range(i))), repeats=shape[i], axis=i)
    return result.reshape(-1, len(arrays))
A = np.array([1, 2])
B = np.array([3, 4])    
cartesian = cartesian_product(A, B)
print(cartesian)

# 91. How to create a record array from a regular array? (★★★)
Z = np.array([(1, 2.0), (3, 4.0)], dtype=[('x', int), ('y', float)])
record_array = Z.view(np.recarray)
print(record_array)

# 92. Consider a large vector Z, compute Z to the power of 3 using 3 different methods (★★★)
Z = np.random.random(1000000)
# Method 1: Using the power operator
Z_cubed_1 = Z ** 3
print(Z_cubed_1)

# Method 2: Using np.power
Z_cubed_2 = np.power(Z, 3)
print(Z_cubed_2)

# Method 3: Using np.multiply
Z_cubed_3 = np.multiply(np.multiply(Z, Z), Z)   
print(Z_cubed_3)


# 93. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B? (★★★)
A = np.random.randint(0, 10, (8, 3))
B = np.random.randint(0, 10, (2, 2))
mask = np.array([np.isin(row, B).all() for row in A])
matching_rows = A[mask] 
print(matching_rows)

# 94. Considering a 10x3 matrix, extract rows with unequal values (e.g. [2,2,3]) (★★★)
Z = np.random.randint(0, 5, (10, 3))
unequal_rows = Z[~np.all(Z[:, 0, None] == Z, axis=1)]
print(unequal_rows)  

# 95. Convert a vector of ints into a matrix binary representation (★★★)
def int_to_binary_matrix(vector, num_bits):
    binary_matrix = np.zeros((len(vector), num_bits), dtype=int)
    for i, num in enumerate(vector):
        binary_matrix[i] = np.array(list(np.binary_repr(num, width=num_bits)), dtype=int)
    return binary_matrix
vector = np.array([1, 2, 3, 4])
num_bits = 4
binary_matrix = int_to_binary_matrix(vector, num_bits)
print(binary_matrix)    

# 96. Given a two dimensional array, how to extract unique rows? (★★★)
Z = np.random.randint(0, 5, (10, 3))
unique_rows = np.unique(Z, axis=0)
print(unique_rows)

# 97. Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)
A = np.random.random(3)
B = np.random.random(3) 
inner_product = np.einsum('i,i->', A, B)
outer_product = np.einsum('i,j->ij', A, B)
sum_product = np.einsum('i->', A)
mul_product = np.einsum('i,i->i', A, B)
print("Inner product:", inner_product)
print("Outer product:", outer_product)
print("Sum product:", sum_product)
print("Mul product:", mul_product)

# 98. Considering a path described by two vectors (X,Y), how to sample it using equidistant samples (★★★)?
def sample_path(X, Y, num_samples):
    distances = np.sqrt(np.diff(X)**2 + np.diff(Y)**2)
    cumulative_distances = np.cumsum(distances)
    total_distance = cumulative_distances[-1]
    sample_distances = np.linspace(0, total_distance, num_samples)
    sampled_X = np.interp(sample_distances, cumulative_distances, X[1:])
    sampled_Y = np.interp(sample_distances, cumulative_distances, Y[1:])
    return sampled_X, sampled_Y
X = np.random.random(10)
Y = np.random.random(10)
sampled_X, sampled_Y = sample_path(X, Y, num_samples=5)
print("Sampled X:", sampled_X)
print("Sampled Y:", sampled_Y)

# 99. Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees, i.e., the rows which only contain integers and which sum to n. (★★★)
def select_multinomial_rows(X, n):
    mask = (X.sum(axis=1) == n) & np.all(X.astype(int) == X, axis=1)
    return X[mask]
X = np.array([[1, 2, 3], [0, 0, 5], [2, 2, 1], [3, 3, 3]])
n = 6
selected_rows = select_multinomial_rows(X, n)
print(selected_rows)

# 100. Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (i.e., resample the elements of an array with replacement N times, compute the mean of each sample, and then compute percentiles over the means). (★★★)
def bootstrap_confidence_interval(X, N=1000, confidence=95):    
    means = np.array([np.mean(np.random.choice(X, size=len(X), replace=True)) for _ in range(N)])
    lower_percentile = (100 - confidence) / 2
    upper_percentile = 100 - lower_percentile
    confidence_interval = np.percentile(means, [lower_percentile, upper_percentile])
    return confidence_interval
X = np.random.random(100)
confidence_interval = bootstrap_confidence_interval(X)  
print("'95%' confidence interval for the mean:", confidence_interval) 