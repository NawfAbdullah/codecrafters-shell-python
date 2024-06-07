import sys
import os


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

        PATH = os.environ.get("PATH")
        
        if command.split(' ')[0]=='exit':
            sys. exit(0) 
        elif command.split(' ')[0]=='echo':
            sys.stdout.write(' '.join(command.split(' ')[1:])+'\n')
        elif command.split(' ')[0]=='type':

            cmd = command.split(" ")[1]
            print(cmd)
            cmd_path = None
            paths = PATH.split(":")
            for path in paths:
                if os.path.isfile(f"{path}/{cmd}"):
                    cmd_path = f"{path}/{cmd}"
            
            if cmd in commands.keys():
                sys.stdout.write(f"{cmd} is a shell builtin\n")
            elif cmd_path:
                sys.stdout.write(f"{cmd} is {cmd_path}\n")
            else:
                sys.stdout.write(f"{cmd} not found\n")

        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
