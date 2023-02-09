
cache_area = dict()
def apply_cache(index):
    if index in cache_area:
        return cache_area[index]
    
    if index == 0 or index == 1:
        stored_result = index
        cache_area[index] = stored_result
        return stored_result
    else:
        stored_result = apply_cache(index-2) + apply_cache(index-1)
        cache_area[index] = stored_result
        return stored_result
apply_cache(8)
print(cache_area)