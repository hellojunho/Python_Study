### 전달값 & 반환값 ###
# 계좌 생성 함수
def open_accout():
    print("새로운 계좌가 생성되었습니다.")

# 입금 함수
def deposit(balance, money):    
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money
    
# 출금 함수    
def withdraw(balance, money):   
    if (balance >= money):
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance

# 밤에 출금 시, 수수료
def withdraw_night(balance, money):
    commission = 100    # 수수료 100원
    return commission, balance - money - commission     # 튜플 형식으로 두 개의 값을 리턴

balance = 0     # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원 이며, 잔액은 {1} 원 입니다.".format(commission, balance))