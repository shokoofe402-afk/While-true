while True:
    try:
        num = int(input("یک عدد وارد کنید:"))       
    except ValueError: 
        print("لطفا فقط یک‌ عدد وارد کنید")         
        continue  
    if num > 0 : 
        print("عدد مثبت است")     
    elif num < 0 : 
        print("عدد منفی است") 
    else : 
        print("عدد صفر است")   
        
    choice = input("(y/n)میخواهید ادامه دهید؟")
    if choice.lower() !='y' : 
        print("خداحافظ")