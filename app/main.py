import sys
import os
import subprocess

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    
    def echo(_):
        sys.stdout.write(' '.join(command.split(' ')[1:])+'\n')



    def handle_type(cmd):
        cmd = command.split(" ")[1]
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

    def change_dir(cmd):
        try:
            os.chdir(' '.join(cmd.split(' ')[1:]))
        except FileNotFoundError:
            sys.stdout.write(f"{' '.join(cmd.split(' ')[1:])} no such file or directory exists")

    commands = {
        'echo':echo,
        'exit':lambda  _:sys.exit(0) ,
        'type':handle_type,
        'pwd':lambda _:sys.stdout.write(os.getcwd()+"\n"),
        'cd':change_dir
    }


    def locate_executable(command):
        path = os.environ.get("PATH", "")
        for directory in path.split(":"):
            file_path = os.path.join(directory, command)
            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                return file_path

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()   
        command = input()

        PATH = os.environ.get("PATH")
        
        if command.split(' ')[0] in commands.keys():
            commands[command.split(' ')[0]](command)
      
        else:
            main_cmd,*args = command.split(' ')
            executable = locate_executable(main_cmd)
            if executable:
                subprocess.run([executable, *args])
            else:
                print(f"{command}: command not found")




if __name__ == "__main__":
    main()
