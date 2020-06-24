from extract import idecode
from instructions import AbstractInstruction
from memory import Memory
from operands import AbstractOperand
from process import Process


# import Memory and Process here
class Machine:
    def __init__(self, program1, program2):
        self.memory = Memory(4096)
        self.memory.load(program1, 0)
        self.memory.load(program2, 2048)
        if len(program1) * 32 > 2048 or len(program2) * 32 > 2048:
            raise ValueError
        self.process_queue = [[Process()], [Process()]]
        self.player1 = self.process_queue[0]  # process queue of program1
        self.player2 = self.process_queue[1]  # process queue of program2
        self.state = None

    def status(self):
        return self.state

    def step(self):
        # for player_queue in self.process_queue:
        #     if len(player_queue) > 0:
        #         working_pro = player_queue.pop()
        #         instr = self.memory.__getitem__()
        #         # todo: decode instr, execute, update the status

        # for process queue 1

        # there are only 2 programs => 2 process queues
        def run_in_p_queue(queue_idx):
            p1_idx = 0
            for i in self.process_queue[queue_idx]:
                # get instruction from memory
                raw_instr = self.memory.__getitem__(p1_idx)
                # decode instruction
                opcode, (mode_a, operand_a), (mode_b, operand_b) = idecode(raw_instr)

                oper_a = AbstractOperand.create(opmode=mode_a, opvalue=operand_a)
                oper_b = AbstractOperand.create(opmode=mode_b, opvalue=operand_b)
                instr = AbstractInstruction.create(opcode=opcode, operandA=oper_a, operandB=oper_b)
                instr.exec()
                p1_idx += 1

        run_in_p_queue(0)
        run_in_p_queue(1)

    def run(self):
        while self.state is None:
            self.step()
