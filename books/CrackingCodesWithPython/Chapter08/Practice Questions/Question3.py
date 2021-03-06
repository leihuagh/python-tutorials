# Draw the complete truth tables for the and, or, and not operators


def notTruthTable():
    print(" _________________________\n",
          "|not A    | Evaluates to:|\n",
          "|_________|______________|\n",
          "|not False| True         |\n",
          "|not True | False        |\n",
          "|_________|______________|\n")
    return None


def andTruthTable():
    print(" _______________________________\n",
          "|A and B        | Evaluates to:|\n",
          "|_______________|______________|\n",
          "|False and False| False        |\n",
          "|False and True | False        |\n",
          "|True and False | False        |\n",
          "|True and True  | True         |\n",
          "|_______________|______________|\n")
    return None


def orTruthTable():
    print(" ______________________________\n",
          "|A or B        | Evaluates to:|\n",
          "|______________|______________|\n",
          "|False or False| False        |\n",
          "|False or True | True         |\n",
          "|True or False | True         |\n",
          "|True or True  | True         |\n",
          "|______________|______________|\n")
    return None


notTruthTable()
andTruthTable()
orTruthTable()
