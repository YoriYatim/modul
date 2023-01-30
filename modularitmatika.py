import aritmatika1

def main(aritmatika1):
    a = int(input('masukan nilai a : '))
    b = int(input('masukan nilai b : '))

    print('a\t: &d' %a)
    print('b\t: &d' %b)

    print('a+b\t: &d' % aritmatika1.tambah(a, b))
    print('a-b\t: &d' % aritmatika1.kurang(a, b))
    print('a/b\t: &d' % aritmatika1.bagi(a, b))
    print('a*b\t: &d' % aritmatika1.kali(a, b))

if __name__=="__main__":
    main()