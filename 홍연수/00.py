# while_break.py
# 함수 기능 + while문 + 20에서 break문 작동

def main():
  i = 0
  while i < 100:
    print(i, end = ' ')
    i += 1
    if i == 20 :
      break

main()
