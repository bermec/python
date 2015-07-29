def pay_calc(str):
    ''' convert hours worked into pay'''
    str2 = '22'
    for x in range(0, len(str)  + 1):
        if str[x:x+1] == str2:
            return  True



if __name__ == '__main__':


    ans = pay_calc('255227')
    print(ans)
