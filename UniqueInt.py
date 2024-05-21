class UniqueInt:
    """Class which contains all the methods used in processing input file and output file."""
    @staticmethod
    def ltrim(s):
        """Remove leading spaces and tabs from the string."""
        i = 0
        while s[i] == ' ' or s[i] == '\t':
            i += 1
        return s[i:]

    @staticmethod
    def custom_append(lst, item):
        """Append an item to the list."""
        lst += [item]
        return lst

    @staticmethod
    def rtrim(s):
        """Remove trailing spaces, newlines, and tabs from the string."""
        i = 1
        while i <= len(s) and (s[-i] == ' ' or s[-i] == '\n' or s[-i] == '\t'):
            i += 1
        return s[:(len(s) + 1) - i]

    @staticmethod
    def trim(s):
        """Remove both leading and trailing spaces, newlines, and tabs from the string."""
        return UniqueInt.rtrim(UniqueInt.ltrim(s))

    @staticmethod
    def reverse_string(s):
        """Reverse the given string."""
        output = ''
        for i in range(1,  len(s) + 1):
            output += s[-i]
        return output

    @staticmethod
    def str_to_int(s):
        """Convert a string to an integer. Returns False if the string is not a valid integer or exceeds 1023."""
        output = 0
        for i in s:
            if i == ' ':
                return False
            if i == '-':
                continue
            if ord(i) < ord('0') or ord(i) > ord('9') + 1:
                return False
            output = (output * 10) + (ord(i) - ord('0'))
            if output > 1023:
                return False
        if s[0] == '-':
            output *= -1
        return output

    @staticmethod
    def int_to_str(i):
        """Convert an integer to a string."""
        output = ''
        negative = 0
        if i < 0:
            negative = 1
            i *= -1
        if i == 0:
            return '0'
        while i > 0:
            output += chr((i % 10) + ord('0'))
            i //= 10
        output = UniqueInt.reverse_string(output)
        return ('-' * negative) + output

    @staticmethod
    def custom_sort(array):
        """Sort the array using a custom quicksort implementation."""
        if len(array) <= 1:
            return array
        pivot = array[-1]
        left = []
        right = []
        for i in array[:-1]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return UniqueInt.custom_sort(left) + [pivot] + UniqueInt.custom_sort(right)

    # AllNumbers = {}
    # allstrings = []
    # for i in range(-1203, 1204):
    #         num = int_to_str(i)
    #         AllNumbers[num] = i
    #         allstrings.append(num)

    @staticmethod
    def processFile(input_file, output_file):
        """
        Read numbers from the input file, process and remove duplicates,
        then write the sorted unique numbers to the output file.
        """
        if not output_file:
            output_file = input_file + '_results.txt'
        unique_ints = []
        bool_contains = [False for i in range(-1023, 1024)]
        with open(input_file, 'r') as f:
            for i in f:
                i = UniqueInt.trim(i)
                if len(i) == 0:
                    continue
                num = UniqueInt.str_to_int(i)
                if num is False:
                    continue
                if bool_contains[num] == False:
                    UniqueInt.custom_append(unique_ints, num)
                    bool_contains[num] = True

        with open(output_file, 'w') as f:
            for index, i in enumerate(UniqueInt.custom_sort(unique_ints)):
                f.write(UniqueInt.int_to_str(i) + '\n')


if __name__ == "__main__":
    input_file = input("Enter the path of the input file: ")
    output_file = input("Enter the path of the output file: ")
    obj = UniqueInt()
    obj.processFile(input_file, output_file)
