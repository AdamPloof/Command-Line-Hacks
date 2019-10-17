import sys

def get_uniq_lines(object_to_read):
    all_lines = []
    for line in object_to_read:
        all_lines.append(line)
    output_string = set(all_lines)            
    
    return("".join(output_string))

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        print(get_uniq_lines(f)) 
else:
    input_object = sys.stdin.readlines()
    print(get_uniq_lines(input_object))