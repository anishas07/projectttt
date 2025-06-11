def subsets(input, size):
    total = 2 ** size
    
    for outer in range(total):
        for inner in range(size):
            if (outer & (1 << inner)) > 0:
                print(input[inner], end="")
        print("")

input = input("Enter a string: ")
subsets(input, len(input))
