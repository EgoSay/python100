# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/5/6 21:45
# @IDE     : PyCharm


class Student:
    name = ""
    age = 0
    score = [None] * 4

    def input(self):
        self.name = input("Input name, please: ")
        self.age = int(input("Input age, please: "))
        for i in range(len(self.score)):
            self.score[i] = int(input("Input %d score, please: " % (i + 1)))

    def output(self):
        print('Output name: %s' % self.name)
        print('Output age: %d' % self.age)
        for i in range(len(self.score)):
            print('Output %d score: %d' % ((i + 1), self.score[i]))


if __name__ == "__main__":
    N = 5
    studentArray = [Student()] * N
    for i in range(len(studentArray)):
        studentArray[i].input()

    for i in range(len(studentArray)):
        studentArray[i].output()