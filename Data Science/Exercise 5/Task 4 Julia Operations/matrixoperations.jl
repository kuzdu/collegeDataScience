println("addition of two matrices")
matrix1 = [1 2 3; 4 5 6]
matrix2 = [1 2 3; 4 5 6]
sum = matrix1 + matrix1

println("multiplication of two matrices with *")
mult_matrix1 = [1 2 3; 4 5 6]
mult_matrix2 = [1 2; 3 4; 5 6]
mult = mult_matrix1 * mult_matrix2

println("multiplication of two matrices with .*")
same_dimensions_matrix1 = [1 2 3; 4 5 6]
same_dimensions_matrix2 = [5 5 5; 5 5 5]
same_dimensions_matrix_result = same_dimensions_matrix1 .* same_dimensions_matrix2


println("division with /")
div_a = [9 9; 9 9; 9 9]
div_b = [3 3; 3 3; 3 3]
div_result =  div_a / div_b

println("div_result_2 and div_result_3 are equal - have to change matrices")
div_a = [4 6; 6 10]
div_b = [2 2; 2 2]
div_result_3 = inv(div_a) * div_b
div_result_2 =  div_a \ div_b

println("some math operations")
matrix_with_useful_numbers = rand(1:10,3,3)
matrix_with_useful_numbers+1
matrix_with_useful_numbers-1
matrix_with_useful_numbers*2
matrix_with_useful_numbers/2

println("multiple matrix with vector")
matrix_for_vector = rand(1:10,3,4)
vector = [7, 8, 9, 10]
result = matrix_for_vector * vector
