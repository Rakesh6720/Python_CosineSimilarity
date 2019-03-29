import math 
import cmath
# The resulting similarity ranges from −1 meaning exactly opposite, 
# to 1 meaning exactly the same, with 0 indicating orthogonality or 
# decorrelation, while in-between values indicate intermediate similarity 
# or dissimilarity.


samantha = [.6, .8, -1, 1, .8, 1]
carrie = [.8, .6, 0, .7, -.3, .3]
charlotte = [-.3, -.6, .8, .5, 1, -.4]
miranda = [.9, .4, 1, -.2, .3, .8]
gita = [.5, 1, -.5, .5, 1, .5]

user = gita

def capture_user_input():
    print('Please answer the following 6 questions by entering an integer or decimal number on your keypad and pressing enter')
    print('On a scale from -1 to 1 where -1 is Oblivious and 1 is Self-Aware, how would you rate yourself? (Including up to 1 decimal place)')
    answer1 = input()
    print('On a scale from -1 to 1 where -1 is Serious and 1 is a Joke Fest, how would you rate yourself? (Including up to 1 decimal place)')
    answer2 = input()
    print('On a scale from -1 to 1 where -1 is Care-Free and 1 is Neurotic, how would you rate yourself? (Including up to 1 decimal place)')
    print('On a scale from -1 to 1 where -1 is Insecure and 1 is Confident, how would you rank yourself? (Including up to 1 decimal place) ')
    answer4 = input()
    print('On a scale from -1 to 1 where -1 is Blue Collar and 1 is Of Means, how would you rank yourself? (Including up to 1 decimal place)')
    answer5 = input()
    print('On a scale of -1 to 1 where -1 is Entitled and 1 is Ambitious, how would you rate yourself? (Including up to 1 decimal place)')
def add_and_square(vector_n):
    numbers2 = []
    for i in range(len(vector_n)):
        square = vector_n[i] * vector_n[i]
        numbers2.append(square)
    return numbers2

def vector_magnitude_maker(vector_n):
    vector_n_magnitude = add_and_square(vector_n)
    cosine_similarity_denominator = math.fsum(vector_n_magnitude)
    sum_square = cmath.sqrt(cosine_similarity_denominator)
    # print(sum_square)
    return sum_square

def find_dot_product(vector_a, vector_b):
    numbers = []
    
    for i in range(len(vector_a)):
        total = vector_a[i] * vector_b[i]
        numbers.append(total)

    sum = math.fsum(numbers)
    #print(sum)
    return sum

def make_numerator(vector_a, vector_b):
    numerator = find_dot_product(vector_a, vector_b)
    return numerator

def make_denominator(vector_a, vector_b):
    sum_square_vector_a = vector_magnitude_maker(vector_a)
    sum_square_vector_b = vector_magnitude_maker(vector_b)
    denominator = sum_square_vector_a * sum_square_vector_b
    return denominator

def calculate_cosine_similarity(vector_a, vector_b):
    numerator = make_numerator(vector_a, vector_b)
    denominator = make_denominator(vector_a, vector_b)
    cosine_similarity_final = numerator / denominator
    return cosine_similarity_final

#numerator = find_dot_product(gita, samantha)

#sum_square_gita = vector_magnitude_maker(gita)
#sum_square_samantha = vector_magnitude_maker(samantha)

# denominator = sum_square_gita * sum_square_samantha

#print(make_denominator(gita, samantha))

#denominator = make_denominator(gita, samantha)
#cosine_similarity_final = numerator / denominator

#print(cosine_similarity_final)

cosine_values = []

cosine1 = calculate_cosine_similarity(user, samantha)
cosine_values.append(cosine1)
cosine_values.append('samantha')

cosine2 = calculate_cosine_similarity(user, carrie)
cosine_values.append(cosine2)
cosine_values.append('carrie')

cosine3 = calculate_cosine_similarity(user, charlotte)
cosine_values.append(cosine3)
cosine_values.append('charlotte')

cosine4 = calculate_cosine_similarity(user, miranda)
cosine_values.append(cosine4)
cosine_values.append('miranda')

for i in range(len(cosine_values)):

    if i < 1:
        top_value = cosine_values[i]
        top_value_index = i
        #print(i)
    else:
        if i % 2 == 0:
            current_value = cosine_values[i]
            current_index = i
            if top_value.real < current_value.real: #you have to access the real part of the number cause the imaginary parts can't sort or compare
                top_value.real = current_value.real
                top_value_index = current_index


print(top_value_index)
print(cosine_values[top_value_index + 1])
print(cosine_values[top_value_index].real)



