#Random string of number generator with max digits option
    def num_variable(digitos):
        """This function returns a random number in format string with length as parameter."""
        import random
        n = ""
        for i in range(digitos):
            n = n + str(random.randint(1,9))
        return n


