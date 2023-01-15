class UnlimitedRegisterMachine:

        @staticmethod
        def execute(input, instructions):

                instructions = instructions.split('\n')
                registers = defaultdict(lambda: 0)
                registers.update(input)
                i = -1

                while True:
                        i += 1

                        instruction = instructions[i].split(' ')
                        arguments = [int(x) for x in instruction[1:]]
                        operation = instruction[0]

                        if operation == 'z':
                                registers[arguments[0]] = 0

                        elif operation == 's':
                                registers[arguments[0]] += 1

                        elif operation == 'm':
                                registers[arguments[1]] = registers[arguments[0]]

                        elif operation == 'j':
                                if registers[arguments[0]] == registers[arguments[1]]:
                                        i = arguments[2] - 1

                        elif operation == 'x':
                                break

                        else:
                                raise SyntaxError(f'Unknown operation {operation}.')

                return i, registers
