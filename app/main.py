import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    commands = {
        'echo':'',
        'exit':'',
        'type':''
    }
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()   
        command = input()
        
        if command.split(' ')[0]=='exit':
            sys. exit(0) 
        elif command.split(' ')[0]=='echo':
            sys.stdout.write(' '.join(command.split(' ')[1:])+'\n')
        elif command.split(' ')[0]=='type':
            if(command.split(' ')[1] in commands.keys()):
                print(command.split(' ')[1]+' is a shell builtin')
            else:
                print(command.split(' ')[1]+' not found')
        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
