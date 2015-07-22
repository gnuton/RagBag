def solution(S):
    print S
    # write your code in Python 2.7
    stack=0
    for i in S:
        if i == "(":
            stack+=1
        elif i == ")":
            if stack <= 0:
                return 0
            else:
                stack-=1
    
    return 0 if stack > 0 else 1

# score https://codility.com/demo/results/demo9SNE78-8BW/
