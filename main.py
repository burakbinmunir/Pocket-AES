import binascii

# hexadecimal to binary text conversion
def hex_to_binary(hex_text):
    binary_text = bin(int(hex_text, 16))[2:] # [2:] to remove the 0b prefix
    binary_text = binary_text.zfill(8)  # pad with 0s to make it 8 bits long
    return binary_text

# hexadecimal to ASCII text conversion
def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '') # remove spaces, tabs, newlines, 0x
    ascii_str = binascii.unhexlify(hex_str) # convert to ASCII
 
    return ascii_str

# deep copy of matrix
def deep_copy_2x2 (matrix):
    new_matrix = [[0 for _ in range(2)] for _ in range(2)]
    
    for _ in range (0,2):
        for __ in range (0,2):
            new_matrix[_][__] = matrix[_][__]
    
    return new_matrix

# Finite field multiplication
def multiply_in_finite_field(a, b):
    m = 0
    polynomial = 0b10011  # Irreducible polynomial x^4 + x + 1

    a = int(a, 2)
    b = int(b, 2)

    while b > 0:
        if b & 1: # Check if the first bit is set in b
            m ^= a

        a <<= 1  # Left shift a by 1 (equivalent to multiplying by x in GF(2^4))

        if a & 0b10000:  # Check if the fourth bit is set in a
            a ^= polynomial  # XOR with the irreducible polynomial if fourth bit is set

        b >>= 1  # Right shift b by 1 (equivalent to dividing by x in GF(2^4))

    return format(m, '04b')  # Format the result as a 4-bit binary string

# finite field multiplication of matrix with constant matrix
def mix_columns (matrix):
    
    # binary equivalent of constant matrix
    # matrix
    # [ 1 , 4 ]
    # [ 4 , 1 ]

    constant_matrix = [
        ['0b001', '0b100'],
        ['0b100', '0b001']
    ]
    
    result_matrix = [[0 for _ in range(2)] for _ in range(2)]
    
    for _ in range(2):
        for __ in range(2):
            temp1 = multiply_in_finite_field(constant_matrix[_][0], matrix[0][__])
            temp2 = multiply_in_finite_field(constant_matrix[_][1], matrix[1][__])
            result_matrix[_][__] = int(temp1, 2) ^ int(temp2, 2)          
        
    # converting to 4-bit binary matrix
    binary_matrix = [['{:04b}'.format(num) for num in row] for row in result_matrix]
    
    return binary_matrix
    
# finite feild multiplication of matrix with inverse constant matrix
def inverse_mix_columns (matrix):
    
    # binary equivalent of constant matrix
    # matrix
    # [ 9 , 2 ]
    # [ 2 , 9 ]

    constant_matrix = [
        ['0b1001' , '0b010'],
        ['0b010' , '0b1001']
    ]
    
    result_matrix = [[0 for _ in range(2)] for _ in range(2)]
    
    for _ in range(2):
        for __ in range(2):
            temp1 = multiply_in_finite_field(constant_matrix[_][0], matrix[0][__])
            temp2 = multiply_in_finite_field(constant_matrix[_][1], matrix[1][__])
            result_matrix[_][__] = int(temp1, 2) ^ int(temp2, 2)          
    
    # converting to 4-bit binary matrix
    binary_matrix = [['{:04b}'.format(num) for num in row] for row in result_matrix]
    
    return binary_matrix

# hexadecimal to 4-bit binary conversion    
def hex_to_4bit_binary(hex_value):
    binary_value = bin(int(hex_value, 16))[2:] # [2:] to remove the 0b prefix
    return binary_value.zfill(4) # pad with 0s to make it 4 bits long

# hexadecimal to binary array conversion
def hex_to_binary_array ( hex_text ):
    binary = [0 for _ in range(4)]

    for _ in range (0 , 4):
        binary[_] = hex_to_4bit_binary(hex_text[_])
    
    return binary

# binary array to 2x2 matrix conversion
def binary_array_to_matrix ( binary ): # 1D binary array
    matrix = [[0 for _ in range(2)] for _ in range(2)]
    
    # conversion according to the format of P matrix
    # [ P0 , P2 ]
    # [ P1 , P3 ]
    
    matrix[0][0] = binary[0] # p0
    matrix[0][1] = binary[2] # p2
    matrix[1][0] = binary[1] # p1
    matrix[1][1] = binary[3] # p3
    
    return matrix

# hexadeciaml matrix to hex text conversion
def hex_matrix_to_hex ( matrix ):
    new = ''

    # conversion again is on the base of P-matrix
    # text will be P0P1P2P3
    
    new += hex(matrix[0][0])[2:] # [2:] to remove the 0x prefix
    new += hex(matrix[1][0])[2:] 
    new += hex(matrix[0][1])[2:] 
    new += hex(matrix[1][1])[2:]
    
    return new

# returns the subnible of the given binary
def find_sub_nibble ( binary ):
    
    # substitution table
    s_box = [
        ['0000', '1010'],
        ['0001', '0000'],
        ['0010', '1001'],
        ['0011', '1110'],
        ['0100', '0110'],
        ['0101', '0011'],
        ['0110', '1111'],
        ['0111', '0101'],
        ['1000', '0001'],
        ['1001', '1101'],
        ['1010', '1100'],
        ['1011', '0111'],
        ['1100', '1011'],
        ['1101', '0100'],
        ['1110', '0010'],
        ['1111', '1000']
    ] 

    for __ in range (0, len(s_box)):
        if binary == s_box[__][0]:
            return s_box[__][1]

# returns the reverse subnible of the given binary
def find_reverse_sub_nibble ( binary ):
    
    # reverse substitution table
    reverse_s_box = [
        ['1010', '0000'],
        ['0000', '0001'],
        ['1001', '0010'],
        ['1110', '0011'],
        ['0110', '0100'],
        ['0011', '0101'],
        ['1111', '0110'],
        ['0101', '0111'],
        ['0001', '1000'],
        ['1101', '1001'],
        ['1100', '1010'],
        ['0111', '1011'],
        ['1011', '1100'],
        ['0100', '1101'],
        ['0010', '1110'],
        ['1000', '1111']
    ]
    
    for _ in range (0 , len ( reverse_s_box ) ):
        if binary == reverse_s_box[_][0]:
            return reverse_s_box[_][1]        

# returns the subnible of the given matrix from s-box
def subnibles ( matrix ):
    for _ in range (0, 2):
            for __ in range (0, 2):
                matrix[_][__] = find_sub_nibble ( matrix[_][__] )
                
    return matrix
    
# returns the reverse subnible of the given matrix from reverse s-box
def reverse_subnibles_matrix ( matrix ) :
    for _ in range (0, 2):
        for __ in range (0, 2):
            matrix[_][__] = find_reverse_sub_nibble ( matrix[_][__] )
            
    return matrix

# shift row
def shift_row ( matrix ):
    matrix[0][0] , matrix[0][1] = matrix[0][1] , matrix[0][0] # swapping p0 and p2
    
    return matrix

# 2 round keys generation from master key matrix
def generate_round_keys(master_key_matrix): 
    
    orginal_master_key = deep_copy_2x2 (master_key_matrix)   
    
    key1 = [['' for _ in range(2)] for _ in range(2)]
    key2 = [['' for _ in range(2)] for _ in range(2)]
    
    round_count_01 = '1110' 
    round_count_01 = int(round_count_01, 2) # converting to integer
    round_count_02 = '1010'
    round_count_02 = int(round_count_02, 2)
    
    # Convert the binary strings to integers    
    for _ in range (0,2):
        for __ in range(0,2):
            master_key_matrix[_][__] = int(master_key_matrix[_][__], 2)
    
    # finding subnible of p1
    sub_nibble_result = int( find_sub_nibble(orginal_master_key[1][1]), 2)
    
    # keys are generated according to algotithm given in PDF
    
    key1[0][0] = bin(master_key_matrix[0][0] ^ sub_nibble_result ^ round_count_01)[2:].zfill(4) # w4
    key1[0][0] = int (key1[0][0], 2)
    
    key1[1][0] = master_key_matrix[1][0] ^ key1[0][0]   # w5
    
    key1[0][1] = master_key_matrix[0][1] ^ key1[1][0]   # w6
    
    key1[1][1] = master_key_matrix[1][1] ^ key1[0][1]   # w7
    
    # converting to binary strings
    s = str(bin(key1[1][1])[2:])
    
    # padding with 0s to make it 4 bits long
    if len(s) < 4:
        if len(s) == 3:
            s = '0' + s
        elif len(s) == 2:
            s = '00' + s
        elif len(s) == 1:
            s = '000' + s
        elif len(s) == 0:
            s = '0000'
  
    key2[0][0] = key1[0][0] ^ int(find_sub_nibble(s),2) ^ round_count_02   # w8
    
    key2[1][0] = key1[1][0] ^ key2[0][0]   # w9
    
    key2[0][1] = key1[0][1] ^ key2[1][0]   # w10
    
    key2[1][1] = key1[1][1] ^ key2[0][1]   # w11
    
    return key1 , key2

# one-one matrix XOR
def matrix_XOR ( matrix1 , matrix2 ):
    result_matrix = [[0 for _ in range(2)] for _ in range(2)]
    
    for _ in range (0,2):
        for __ in range(0,2):
            matrix1[_][__] = int(matrix1[_][__], 2)
            
    for _ in range (0,2):
        for __ in range(0,2):
            matrix2[_][__] = int(matrix2[_][__], 2)
            
    for _ in range (0, 2):
        for __ in range (0, 2):
            result_matrix[_][__] = matrix1[_][__] ^ matrix2[_][__]
    
    # converting to 4-bit binary matrix
    binary_matrix = [['{:04b}'.format(num) for num in row] for row in result_matrix]
    
    return binary_matrix
    
# hex matrix to hex text conversion according to P-matrix
def hex_matrix_hex_text ( hex_matrix ):
    hex_text = ''
    
    hex_text += hex_matrix[0][0]
    hex_text += hex_matrix[1][0]
    hex_text += hex_matrix[0][1]
    hex_text += hex_matrix[1][1]
    
    return hex_text

# binary matrix to hex matrix conversion
def binary_matrix_to_hex_matrix ( matrix ):
    output1 = deep_copy_2x2 (matrix)

    for _ in range (0, 2):
        for __ in range (0,2):
            output1[_][__] = int(output1[_][__],2)


    for _ in range (0, 2):
        for __ in range (0,2):
            output1[_][__] = hex(output1[_][__])[2:]
    
    return output1


def deliverable_1 ( hex_text , master_key ):
    
    # binary array conversion from hexadeciaml text
    binary_array = hex_to_binary_array ( hex_text = hex_text )
    
    # binary array to 2x2 matrix conversion
    matrix = binary_array_to_matrix ( binary = binary_array )
    
    # creating copies of matrix for each output
    matrix1 = deep_copy_2x2 (matrix)
    matrix2 = deep_copy_2x2 (matrix)
    matrix3 = deep_copy_2x2 (matrix)
    
    matrix1 = subnibles ( matrix1 )
    
    # Subinbles
    output1 = binary_matrix_to_hex_matrix ( matrix1 )
    output1 = hex_matrix_hex_text ( output1 )
    
    print ( "Sub nibles: ", output1 )
    
    # applying shift row
    matrix2 = shift_row ( matrix2 )

    output2 = binary_matrix_to_hex_matrix ( matrix2 )
    output2 = hex_matrix_hex_text ( output2 )

    print ( "Shift Row: ", output2 )
    
    matrix3 = mix_columns( matrix3 )

    output3 = binary_matrix_to_hex_matrix ( matrix3 )
    output3 = hex_matrix_hex_text ( output3 )

    print ( "Mix columns: ", output3  )   
    
    # Round keys generation
    master_key_binary_array = hex_to_binary_array ( hex_text = master_key )
    master_key_matrix = binary_array_to_matrix ( binary = master_key_binary_array )
    
    key1 , key2 = generate_round_keys (master_key_matrix)
    
    # converting to equivalent hex text
    key1 = hex_matrix_to_hex ( key1 )
    key2 = hex_matrix_to_hex ( key2 )
    
    print ("Key-01: ", key1, " ", "Key-02: ", key2) 


# Decryption of cipher text in hexedecimal
def deliverable_2 ( hex_text , master_key ):

    # binary array conversion from hexadeciaml text
    binary_array = hex_to_binary_array ( hex_text = hex_text )
    
    # binary array to 2x2 matrix conversion
    matrix = binary_array_to_matrix ( binary = binary_array )

    # Creating master key matrix
    master_key_binary_array = hex_to_binary_array ( hex_text = master_key )
    master_key_matrix = binary_array_to_matrix ( binary = master_key_binary_array )

    # applying shift row
    matrix = shift_row ( matrix )

    output1 = binary_matrix_to_hex_matrix ( matrix )
    output1 = hex_matrix_hex_text ( output1 )

    print ( "Shift Row: ", output1 )
    
    # Round keys generation
    key1 , key2 = generate_round_keys ( master_key_matrix )

    key1 = hex_matrix_to_hex ( key1 )
    key2 = hex_matrix_to_hex ( key2 )

    # converting to binary array
    key1_matrix = binary_array_to_matrix ( hex_to_binary_array ( key1 ) )
    key2_matrix = binary_array_to_matrix ( hex_to_binary_array ( key2 ) )

    # applying XOR operation on AdD round Key-02
    matrix = matrix_XOR (  matrix , key2_matrix)

    output2 = binary_matrix_to_hex_matrix ( matrix )
    output2 = hex_matrix_hex_text ( output2 )

    print ("Add Round Key-02: ", output2)

    # applying reverse subnibles
    matrix = reverse_subnibles_matrix ( matrix )

    output3 = binary_matrix_to_hex_matrix ( matrix )
    output3 = hex_matrix_hex_text ( output3)

    print ("Reverse Sub Nibbles: ", output3)

    matrix = shift_row ( matrix )

    output4 = binary_matrix_to_hex_matrix ( matrix )
    output4 = hex_matrix_hex_text ( output4)

    print ("Shift Row: ", output4)

    # Inverse Mix Columns for decryption 
    matrix = inverse_mix_columns ( matrix )

    output5 = binary_matrix_to_hex_matrix ( matrix )
    output5 = hex_matrix_hex_text ( output5)

    print ("Inverse Mix Columns: ", output5)

    # applying XOR operation on AdD round Key-01
    matrix = matrix_XOR ( key1_matrix , matrix )

    output6 = binary_matrix_to_hex_matrix ( matrix )
    output6 = hex_matrix_hex_text ( output6)

    print ("Add Round Key-01: ", output6)
    
    # applying reverse subnibles
    matrix = reverse_subnibles_matrix ( matrix )

    output7 = binary_matrix_to_hex_matrix ( matrix )
    output7 = hex_matrix_hex_text ( output7)

    print ("Reverse Sub Nibbles: ", output7) 
    
    return output7   
    

def deliverable_3 ( filename ):
    file = open(filename, 'r')
    lines = file.readlines()
    
    
    pairs = []

    # converting to pairs of 4 hex values
    for line in lines:
        pairs.extend([line[i:i+4] for i in range(0, len(line), 4) if line[i] != '\n'])
    
    # decrypting each pair
    decrypted_text = []
    for _ in range (0, len(pairs)):
        decrypted_text.append(deliverable_2 ( pairs[_] , '2a09' ))  

    # converting to ascii text
    ascii_text = ''
    for _ in range (0, len(decrypted_text)):
        ascii_text += hex_to_ascii(decrypted_text[_]).decode()
    
    # removing the padding
    ascii_text.rfind('\x00')
    
    file = open ( 'plain.txt', 'w')
    file.write(ascii_text)
    

deliverable_1 ( hex_text = '903b' , master_key = '02cc')  
decrypted_text = deliverable_2 ( hex_text = 'f3d7' , master_key = '40ee' )
deliverable_3 ( 'input.txt' )