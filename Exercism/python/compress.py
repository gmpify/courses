def compress2(input):
    previous_letter = input[0]
    current_count = 0
    
    j = 0 #writer index
    
    for i in range(len(input)):
        current_letter = input[i]
        
        if previous_letter != current_letter:
            
            if current_count == 1:
                input[j] = previous_letter
                j += 1
            elif current_count >= 10:
                str_count = str(current_count)
                for k in range(len(str_count)):
                    input[j] = str_count[k]
                    j += 1
                input[j] = previous_letter
                j += 1
            else:
                input[j] = current_count
                input[j + 1] = previous_letter
                j += 2
            
            previous_letter = current_letter
            current_count = 1

        else:
            current_count += 1
    
    if current_count != 1:
        input[j] = current_count
        input[j + 1] = previous_letter
        j += 2
    else:
        input[j] = previous_letter
        j += 1

    return input[0:j]

print(example2)
print(compress2(example2))
