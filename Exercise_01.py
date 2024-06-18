def f1_score_classification(tp, fp, fn):
    #Kiểm tra cac so tp, fp và fn có phải là số nguyên và lớn hơn 0...
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fp, int):
        if not isinstance(tp, int):
            print('tp phải là số nguyên int')
        if not isinstance(fp, int):
            print('fp phải là số nguyên int')
        if not isinstance(fn, int):
            print('fn phải là số nguyên int')
        return
    # Kiểm tra các số có lớn hơn 0 không...
    if tp<=0 or fp<=0 or fn<=0:
        print('tp, fp, fn phải lớn hơn 0')  
        return     
    # Tính giá trị các yêu cầu
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*((precision*recall)/(precision+recall))
    print(f'precision: {round(precision, 2)}')
    print(f'recall: {round(recall, 2)}')
    print(f'f1_score: {round(f1_score,2)}')

f1_score_classification(tp=9, fp=3,fn=4)


