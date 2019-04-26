for i in range(0, int(input())):
    s1 = input()
    s2 = input()
    if len(s1) != len(s2):
        print("Strand #" + str(i + 1) + ": frameshift")
    else:
        errors = []
        for j in range(0, len(s1)):
            if(s1[j] == "a" and s2[j] != "t"):
                errors.append(j)
            if(s1[j] == "t" and s2[j] != "a"):
                errors.append(j)
            if(s1[j] == "c" and s2[j] != "g"):
                errors.append(j)
            if(s1[j] == "g" and s2[j] != "c"):
                errors.append(j)
        if len(errors) == 0:
            print("Strand #" + str(i + 1) + ": no errors")
        else:
            numbers = ""
            for e in range(len(errors) - 1):
                numbers = numbers + str(errors[e]) + ", "
            numbers = numbers + str(errors[len(errors)-1])
            print("Strand #" + str(i + 1) + ": errors at " + numbers)
