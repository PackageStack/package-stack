from abc import ABC, abstractmethod


class PSOperator(ABC):
    @abstractmethod
    def compute(mcs, a, b):
        pass


class Multiplication(PSOperator):

    def compute(mcs, a, b):
        return a * b


class Division(PSOperator):

    def compute(mcs, a, b):
        return a / b


class Addition(PSOperator):

    def compute(mcs, a, b):
        return a + b


class Subtraction(PSOperator):

    def compute(mcs, a, b):
        return a - b



