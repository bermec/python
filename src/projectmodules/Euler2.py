def main():
    first = 0
    second = 1
    result = 0
    total = 0

    print("Project Euler (oiler!) second question.")
    while result < 4000000:
         result = first + second

         # Next two lines check for even terms

         if (result % 2) == 0 :
             total = total + result
         #---------------------------------------------------

         first = second
         second = result

    print("total of even terms = ",total)

if __name__ == '__main__':
    main()
