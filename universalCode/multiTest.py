def multiTest(testNum):
    from LRClassify import LRClassify
    acc = 0.0
    for i in range(testNum):
        print('%d th test'  %(i+1))
        acc += LRClassify()
    acc = float(acc/10)
    print("The test acc is %f" %acc)