class Intcode():

    def __init__(self, program):
        self.program = program
        
    def run_program(self):
        i = 0
        
        while self.program[i] != 99:
            
            if self.program[i] == 1:
                self.program[self.program[i+3]] = self.program[self.program[i+1]] + self.program[self.program[i+2]]
                
            elif self.program[i] == 2:
                self.program[self.program[i+3]] = self.program[self.program[i+1]] * self.program[self.program[i+2]]
                
            i += 4
            
