# Function to perform Selection Sort
def selection_sort(salaries):
    n = len(salaries)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries


# Function to perform Bubble Sort
def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
    return salaries


# Main program
if __name__ == "__main__":
    # Take user input
    n = int(input("Enter the number of employees: "))
    salaries = []

    print("Enter employee salaries:")
    for i in range(n):
        sal = float(input(f"Salary {i + 1}: "))
        salaries.append(sal)

    # Selection Sort
    sel_sorted = selection_sort(salaries.copy())
    print("\nSalaries sorted using Selection Sort (ascending):")
    print(sel_sorted)

    # Bubble Sort
    bub_sorted = bubble_sort(salaries.copy())
    print("\nSalaries sorted using Bubble Sort (ascending):")
    print(bub_sorted)

    # Display Top 5 Highest Salaries
    top_five = sorted(salaries, reverse=True)[:5]
    print("\nTop 5 Highest Salaries:")
    for i, salary in enumerate(top_five, start=1):
        print(f"{i}. ₹{salary:.2f}")
