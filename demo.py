try:
    lst=[10,11,12,13,14,15,16,17,18,19]
    even=[i for i in lst if i%2==0]
    odd=[i for i in lst if i%2==1]
    mx=[i*i*i for i in lst ]

    print(even)
    print(odd)
    print(mx)
except:
    print('Error message')