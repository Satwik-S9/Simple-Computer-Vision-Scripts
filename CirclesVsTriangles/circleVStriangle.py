import time

# global variables
INPUT_PATH = 'input.txt'
OUTPUT_PATH = 'output.txt'

# clearing the contents of the file if any
open(OUTPUT_PATH, 'w').close()


def circles_vs_triangles(image):
    increasing = False

    # identify the starting row
    for idx, row in enumerate(image):
        has_object = False
        row_sum = sum(row)
        if row_sum > 0:
            has_object = True
            if (idx < len(image) - 1) and row_sum < sum(image[idx+1]):
                increasing = True

            start_idx = idx
            break
    
    if not has_object:
        return "No Object Found!"
    
    # checking for edge cases
    if (start_idx == len(image)-1):
        return "Circle"

    elif (start_idx < len(image)-1) and (sum(image[start_idx+1]) == 0):
        return "Circle"

    is_circle = False
    for idx, row in enumerate(image[start_idx+1:]):
        # if we have iterated over the image
        if sum(row) == 0:
            break
        
        # sum of previous row
        idxi = start_idx + idx
        temp_sum = sum(image[idxi])

        if increasing and sum(row) < temp_sum:
            is_circle = True
            break

        elif (not increasing) and sum(row) > temp_sum:
            is_circle = True
            break


    
    if is_circle:
        return "Circle"

    return "Triangle"


if __name__ == '__main__':
    with open(INPUT_PATH, 'r') as f:
        T = int(f.readline())

        for _ in range(T):
            num_rows, num_cols = (int(i) for i in f.readline().split(" "))
        
            img = []
            for _ in range(num_rows):
                row = [int(i) for i in f.readline().split(" ")]
                img.append(row)

            assert len(img[0]) == num_cols
            start = time.process_time()
            ans = circles_vs_triangles(img)
            end = time.process_time()
        
            with open(OUTPUT_PATH, 'a') as fo:
                fo.write(f"The object is a {ans} and time taken for detection: {(end-start)*1e6: .2f} ms\n")   
        
    