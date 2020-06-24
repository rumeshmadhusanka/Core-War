import sys
from machine import Machine


# should import sys and Machine
def main():
    # print(sys.argv)
    def get_file_contents(arg_pos):
        with open(sys.argv[arg_pos], 'rb') as stream:
            contents = stream.read()
            if len(contents) % 4 != 0:
                raise ValueError
            contents = [
                int.from_bytes(contents[i:i + 4], 'little')
                for i in range(0, len(contents), 4)
            ]
            print(contents)
            return contents

    ma1_contents = get_file_contents(1)
    ma2_contents = get_file_contents(2)

    machine = Machine(ma1_contents, ma2_contents)
    machine.run()


if __name__ == '__main__':
    main()
