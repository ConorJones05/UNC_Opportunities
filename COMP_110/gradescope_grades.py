import pandas as pd

class Gradescope_Grades:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input
        self.ls_indexes: list[int] = []
        self.qz_indexes: list[int] = []
        self.cq_indexes: list[int] = []
        self.ex_indexes: list[int] = []
        self.rd_indexes: list[int] = []

    def find_indexes(self) -> None:
        for i in range(len(self.raw_input)):
            if self.raw_input[i] == 'L' and self.raw_input[i+1] == 'S':
                self.ls_indexes.append(i)
            elif self.raw_input[i] == 'Q' and self.raw_input[i+1] == 'Z':
                self.qz_indexes.append(i)
            elif self.raw_input[i] == 'C' and self.raw_input[i+1] == 'Q':
                self.cq_indexes.append(i)
            elif self.raw_input[i] == 'E' and self.raw_input[i+1] == 'X':
                self.ex_indexes.append(i)
            elif self.raw_input[i] == 'R' and self.raw_input[i+1] == 'D':
                self.rd_indexes.append(i)

    def assignment_names(self) -> list:
        self.find_indexes()
        unique_indexes = list(set(self.ls_indexes + self.qz_indexes + self.cq_indexes + self.ex_indexes + self.rd_indexes))
        assignment_names = [self.raw_input[i:i+5].strip() for i in unique_indexes]
        print(assignment_names)
        return assignment_names

    def assignment_types(self) -> list:
        assignment_names = self.assignment_names()
        types = []
        for name in assignment_names:
            if 'LS' in name:
                types.append("Assignment")
            elif 'QZ' in name:
                types.append("Quiz")
            elif 'CQ' in name:
                types.append('Challenge Question')
            elif 'EX' in name:
                types.append('Extra??????')
            elif 'RD' in name:
                types.append('Reading')
        print(types)
        return types

    def points_earned_and_out_of(self) -> tuple:
        unique_indexes = list(set(self.ls_indexes + self.qz_indexes + self.cq_indexes + self.ex_indexes + self.rd_indexes))
        slash_indexes = []
        for j in unique_indexes:
            tf = True
            index = 0
            while tf:
                if self.raw_input[j + index] == '/':
                    tf = False
                    slash_indexes.append(j + index)
                    print(slash_indexes)
                elif self.raw_input[j + index] == 'S' or self.raw_input[j + index] == "U" or self.raw_input[j + index] == "N":
                    # Returning None if the status is "Submitted", "Not Submitted", or "Ungraded"
                    slash_indexes.append(None)
                    tf = False
                else:
                    index += 1 
        points_gotten = []
        points_out_of = []
        for i in slash_indexes:
            if i is None:
                points_gotten.append(None)
                points_out_of.append(None)
            elif self.raw_input[i + 1] == ' ' and self.raw_input[i - 1] == ' ':
                points_gotten.append(self.raw_input[i-6:i])
                points_out_of.append(self.raw_input[i+1:i+7:])
        for i in range(len(points_gotten)):
            if points_gotten[i] is not None:
                points_gotten[i] = float(''.join(char for char in points_gotten[i] if not char.isalpha() and char != ' '))
        for i in range(len(points_out_of)):
            if points_out_of[i] is not None:
                points_out_of[i] = float(''.join(char for char in points_out_of[i] if not char.isalpha() and char != ' '))
        return points_gotten, points_out_of




    def calculate_percentage(self) -> list[float]:
        points_gotten, points_out_of = self.points_earned_and_out_of()
        scores = []
        for i in range(len(points_gotten)):
            if type(points_gotten[i]) == float:
                scores.append((points_gotten[i] / points_out_of[i]) * 100)
            else:
                scores.append(None)
        print(scores)
        return scores

    def __str__(self) -> str:
        assignment_names = self.assignment_names()
        assignment_types = self.assignment_types()
        points_gotten, points_out_of = self.points_earned_and_out_of()
        scores = self.calculate_percentage()
        
        result = "Number of assignments: {}\n".format(assignment_names)
        result += "Assignment Type: {}\n".format(assignment_types)
        result += "Points Earned: {}\n".format(points_gotten)
        result += "Out of: {}\n".format(points_out_of)
        result += "Percentage: {}\n".format(scores)
    
        return result





x = Gradescope_Grades("LS27 - Operator Overloading 2.0 / 2.0 Apr 15 at 12:00AMApr 16 at 11:59PM Late Due Date: Apr 22 at 11:59PM CQ08 - Practice with OOP 100.0 / 100.0 Apr 12 at 12:00AMApr 12 at 11:59PM Late Due Date: Apr 18 at 11:59PM")
print(x)