def massToJoules (massInteger: int) -> str:
    joules = massInteger * 300000000**2
    return ("E: " + str(joules))