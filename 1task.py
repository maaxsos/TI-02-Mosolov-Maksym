correct = "0123456789 +-*/";
res = "res="
ind = 0
while ind=0:
    exp = input(" Enter expression: ")
    res = res + exp
    if False in [c in correct for c in exp]:
        print("Incorrect input!!");
        continue;
    exec(res)
    print(" Result: ", res)
