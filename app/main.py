import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()   
        command = input()
        if command.split(' ')[0]=='exit':
            sys. exit(0) 
        elif command.split(' ')[0]=='echo':
            sys.stdout.write(' '.join(command.split(' ')[1:])+'\n')
        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
