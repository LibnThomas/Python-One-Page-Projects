a = input("Enter a Word For Guessing :")

key_li = []
lenth = len(a)
for i in range(lenth):
    key_li.append("_")

ans_key = ""
c = ""
error_c = 0
ans = list(a)
print("\n----------GAME ON----------\n")
print(" ", lenth, " letter Word")
while (c != a):
    print("\n", c, "\n")
    ans_key = input("Enter The Guess :")

    if (ans_key in ans):
        count = -1
        c = ""

        for i in ans:
            count += 1

            if (i == ans_key):
                key_li[count] = ans_key
            c = c + key_li[count]

    else:
        error_c += 1
        print("\nNo Match Found !!\nError Count :", error_c)
        if (error_c == 4):
            print("\n______________________________\n\n  Warning Last Chance!!!\n______________________________")
        if (error_c == 5):
            print(
                "\n______________________________\n\n  Sorry You FAILED!!!\n  Better Luck Next Time:)\n\n------Game Over------\n\n______________________________")
            exit()
print("\n______________________________\n\n  Congratulation YOU WIN!\n______________________________")
