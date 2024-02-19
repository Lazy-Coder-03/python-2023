import sys

def count_vowels(line):
    c=0
    for i in line:
        if i in "aeiouAEIOU":
            c+=1
    return c

#count number of lines in a file
def num_words(line):
    words=line.split()
    return len(words)
    

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <inputfile> <outputfile>")
        sys.exit(1)

    inputfile_name = sys.argv[1]
    outputfile_name = sys.argv[2]

    try:
        numlines=0
        total_words=0
        with open(inputfile_name, 'r') as inputfile, open(outputfile_name, 'w') as outputfile:
            for line in inputfile:
                numlines+=1
                total_words+=num_words(line)
                vowel_count = count_vowels(line)
                outputfile.write(f"{line.strip()} vowel count: {vowel_count}\n")
            print("Changes made to outputfile successfully")
            print("Number of lines in input file:",numlines)
            print("Number of words in input file:",total_words)

            
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
