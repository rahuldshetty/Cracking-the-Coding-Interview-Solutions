from typing import List, Any
from copy import deepcopy

class TestCaseReport:
    def __init__(self, input, expected, out, status):
        self.input = input
        self.expected = expected
        self.status = status
        self.out = out
    
    def print(self):
        print(f"| ---------------------- |")
        print(f"Input:    {self.input}\n")
        print(f"Expected: {self.expected}")
        print(f"Output:   {self.out}")
        
    
class TestSuiteReport:
    def __init__(self, reports, valid_count):
        self.reports = reports
        self.valid_count = valid_count
    
    def print(self):
        total = len(self.reports)
        valid = self.valid_count

        print(f"---------- TEST REPORT ----------")
        print(f"---------------------------------")
        print(f"| Total {total}  Success: {valid} Failed: {total - valid}  |")
        
        if total - valid != 0:
            for tc_report in self.reports:
                if tc_report and not tc_report.status:
                    tc_report.print()

        print(f"---------------------------------")

class TestSuite:
    def __init__(self):
        self.input = []
        self.output = []
    
    def add_test(self, input, output):
        self.input.append(deepcopy(input))
        self.output.append(output)
        return self

    def run(self, fn):
        res_set = [None] * len(self.input)
        valid = 0
        for i, input in enumerate(self.input):
            out = fn(input)
            status = (str(out) == str(self.output[i]))
            res_set[i] = (TestCaseReport(input, self.output[i], out, status))
            valid += int(status)
            if not status:
                break

        report = TestSuiteReport(res_set, valid) 

        report.print()


if __name__ == "__main__":
    ts = TestSuite(
        ["1", "1", "2"],
        ["1", "1", "2"]
    )

    ts.run(lambda x:x)


    ts = TestSuite(
        ["1", "0", "0"],
        ["1", "1", "2"]
    )

    ts.run(lambda x:x)
    
