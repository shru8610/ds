# E-commerce System: Linear and Binary Search for Customer Account IDs

# Function to perform Linear Search
def linear_search(customer_ids, target_id):
    for i in range(len(customer_ids)):
        if customer_ids[i] == target_id:
            return i  # Return the index where ID is found
    return -1  # Not found


# Function to perform Binary Search (list must be sorted)
def binary_search(customer_ids, target_id):
    low = 0
    high = len(customer_ids) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if customer_ids[mid] == target_id:
            return mid
        elif customer_ids[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Main Program
if __name__ == "__main__":
    # Taking input from user
    n = int(input("Enter the number of customer account IDs: "))
    
    customer_ids = []
    print("Enter the customer account IDs:")
    for i in range(n):
        cid = int(input(f"ID {i+1}: "))
        customer_ids.append(cid)
    
    target = int(input("\nEnter the Customer Account ID to search: "))
    
    # Linear Search
    linear_result = linear_search(customer_ids, target)
    if linear_result != -1:
        print(f"\nLinear Search: Account ID {target} found at position {linear_result + 1}")
    else:
        print(f"\nLinear Search: Account ID {target} not found.")
    
    # Sort the list for Binary Search
    sorted_ids = sorted(customer_ids)
    
    # Binary Search
    binary_result = binary_search(sorted_ids, target)
    if binary_result != -1:
        print(f"Binary Search: Account ID {target} found in sorted list at position {binary_result + 1}")
    else:
        print(f"Binary Search: Account ID {target} not found in sorted list.")