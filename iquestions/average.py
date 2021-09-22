"""
write a program to find the average of numbers in a list in Python?
"""

def average_program():
    total_elements = int(input('total elements to be inserted: '))
    elem = []
    
    for _ in range(0, total_elements):
        elem.append(int(input('Enter Element: ')))
    
    avg = sum(elem)/total_elements
    print("Average of the elements:", avg)

    return avg

if __name__ == '__main__':
    result =average_program()
    
    