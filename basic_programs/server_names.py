import os.path

def ask_servernames(filename):
   with open(filename, 'w+') as server_name_file:
       servername = None
       while servername != 'Q':
           servername = input("Please provide a servername: [enter Q to quit] ")
           if servername == 'Q':
               break
           else:
               server_name_file.write(servername + "\n")


def print_names_from_file(filename):
   with open(filename, 'r') as server_name_file:
       for line in server_name_file:
           print('#', line.rstrip())

def main():
    try:
        input_filename = input("Please type the file name where your data is to be sent: ")
        filename = os.path.join("C:/Users/Routzer/Documents/net_python/projects/globalknowledge-python-training/data", input_filename)
        ask_servernames(filename)
        print_names_from_file(filename)
    except Exception as e:
        print("Something went wrong...")
        print(e)

if __name__ == "__main__":
    main()