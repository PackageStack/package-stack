

enum Operators {
    Addition,
    Division,
    Subtraction,
    Multiplication
}


public class MathFactory {

    public Operator RetrieveMathOperatorFromFactory(Operators theOperatorIWantToGet)
    {
        if(theOperatorIWantToGet == Operators.Addition)
        {
            return new Addition();
        }

        else if(theOperatorIWantToGet == Operators.Subtraction)
        {
            return new Subtraction();
        }

        else if(theOperatorIWantToGet == Operators.Multiplication)
        {
            return new Multiplication();

        }

        else if(theOperatorIWantToGet == Operators.Division)
        {
            return new Division();
        }

        return new Addition();
    }
}