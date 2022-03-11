out_arr = []
def flatten(arr):
    
    for a in arr:
        if type(a) == list:
            flatten(a)
        else:
            out_arr.append(a)
    
    return out_arr

out = flatten([[1],[2],3,[4,5]])
#print(out)

def capitalizeFirst(arr):
    
    output = []
    if len(arr) == 1:
        return output.append(arr[0].title())
    
    capitalizeFirst(arr[1:])
    
    output.append(arr[0].title())
    return   output

print(capitalizeFirst(['car','taco','bus']))

