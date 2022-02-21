import ps_operator

from ps_operator import *


class InvalidOperatorErrorYouDumbIdiot(Exception):
    pass


class MathFactory:

    def retrieve_operator(self, op_code):
        op_code = op_code.lower()
        if op_code == 'a':
            return Addition()
        elif op_code == 's':
            return Subtraction()
        elif op_code == 'd':
            return Division()
        elif op_code == 'm':
            return Multiplication()
        else:
            raise InvalidOperatorErrorYouDumbIdiot('That wasnt an operator... Wtf is your problem? Are you dumb? How did you even manage to install and run the greatest package manager in history if you cant even use a godamn mathmatical operator... I mean, seriously. This code is elegant. Sleek. Clean. And you fuck up using the math factory opertor??? I literally cannot stand you. You are a fucking insult to the global community of programmers. If you are getting this error, I want you to go revoke your access to every fucking repo you have ever touched. The world will seriously be better off.')
