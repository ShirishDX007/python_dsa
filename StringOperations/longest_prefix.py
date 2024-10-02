def longest_common_prefix(strs):
    # Your code here
    if not str:
        return ""
    strs.sort()

    first_strs = strs[0]
    last_strs = strs[-1]
    i = 0
    while i < len(first_strs) and i < len(last_strs) and first_strs[i] == last_strs[i]:
        i +=1
    return first_strs[:i]
    

# Test the function
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"