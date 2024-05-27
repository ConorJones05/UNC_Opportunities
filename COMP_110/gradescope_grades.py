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
                elif self.raw_input[j + index] == 'S' or self.raw_input[j + index] == 'U' or self.raw_input[j + index] == 'N':
                    tf = False
                    slash_indexes.append(j + index)
                else:
                    index += 1 
        points_gotten = []
        points_out_of = []
        for i in slash_indexes:
            if self.raw_input[i + 1] == ' ' and self.raw_input[i - 1] == ' ':
                points_gotten.append(self.raw_input[i-6:i])
                points_out_of.append(self.raw_input[i+1:i+7:])
            else:
                points_gotten.append(None)
                points_out_of.append(None)
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
    
    def make_dataframe(self):
        assignment_names = self.assignment_names()
        assignment_types = self.assignment_types()
        points_gotten, points_out_of = self.points_earned_and_out_of()
        scores = self.calculate_percentage()

        data = {'assignment_names': assignment_names, 'assignment_types': assignment_types, 'points_gotten': points_gotten, 'points_out_of': points_out_of, 'scores': scores}

        return pd.DataFrame(data)


x = Gradescope_Grades("EX06 - Dictionary Unit Tests 96.0 / 100.0 Mar 06 at 5:00PMMar 21 at 11:59PM Late Due Date: Mar 28 at 11:59PM")
print(x.make_dataframe())