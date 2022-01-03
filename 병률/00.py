A,B,C = input().split()

바보 = '''(A+B)%C
((A%C) + (B%C))%C
(A*B)%C
((A%C) * (B%C))%C'''

바보=바보.replace('A',A)
바보=바보.replace('B',B)
바보=바보.replace('C',C)

for re in 바보.split('\n'):
    print(eval(re))