def main():
    numone = 999
    numtwo = 999
    highscore = 0
    for x in range(numone):
        for y in range(numtwo):
            strxy = str(x * y)
            if len(strxy) == 6:
                firstpart = strxy[0:3]
                lastpart = strxy[3:6]
                reverse = lastpart[::-1]

                if firstpart == reverse:
                    if int(strxy) > highscore:
                        highscore = int(strxy)
    print(highscore)
if __name__ == '__main__':
    main()
