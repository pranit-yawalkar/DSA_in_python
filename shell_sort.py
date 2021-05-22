def shell_sort(elements):
    size = len(elements)
    gap = size//2

    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j>=gap and elements[j-gap]>anchor:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        gap //= 2

if __name__ == "__main__":
    elements = [45, 34, 17, 23, 14, 67, 11, 9, 12]
    shell_sort(elements)
    print(elements)