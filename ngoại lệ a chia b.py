try:
    a=int(input('nhập a: '))
    b=int(input('nhập b: '))
    kq=a/b
except Exception as ex:
    print('lỗi '+str(ex))
else:
    print('kq của a/b là:, a/b')