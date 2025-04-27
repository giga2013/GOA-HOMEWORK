def sum_array(arr):
     # Validate the input
    if arr is None or len(arr) <= 1:
        return 0
    
    min_val = min(arr)
    max_val = max(arr)
    
    arr.remove(min_val)
    arr.remove(max_val)
    
    return sum(arr)