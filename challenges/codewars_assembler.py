"""

https://www.codewars.com/kata/58e24788e24ddee28e000053

"""
def instructionParser(i: list, registers: dict, ip: int) -> dict:
    """
    The function returns 0 when commands executed successfully and 1 if there was an error
    """
    try:
        # print(f"Instruction rcvd {i[0]} {i[1]} {i[2]}, ip={ip}")
        arg1 = i[2]
    except IndexError:
        # print(f"Instruction rcvd {i[0]} {i[1]}, ip={ip}")
        pass
    finally:
        instruction = i[0]
        register = i[1]

    if instruction == 'mov':
        try:
            registers[register] = int(arg1)
        except ValueError:  # if arg1 is not a number, then it should be another register
            registers[register] = registers[arg1]
        finally:
            ip += 1
    elif instruction == 'inc':
        registers[register] += 1
        ip += 1
    elif instruction == 'dec':
        registers[register] -= 1
        ip += 1
    elif instruction == 'jnz':
        try:
            if registers[register] != 0:
                ip = ip + int(arg1)
                # print(f"ip moved to {ip} by {int(arg1)}")
            else:
                ip += 1
        except KeyError:  # jnz 0...
            ip = ip + int(arg1)
    else:
        print(f"instruction {instruction} is not understood, exiting")
        exit(1)

    # print(f"current state of registers {registers}")
    return registers, ip


def simple_assembler(program):
    # Storing the commands in a list where each element is a list itself
    commandlist = []

    for command in program:
        commandlist.append(command.split())

    # Executing commands one by one

    # 'initializing' registers at first use
    registers = dict()

    # instruction pointer
    ip = 0

    try:
        while commandlist[ip]:
            registers, ip = instructionParser(commandlist[ip], registers, ip)
    except IndexError:
        return registers
