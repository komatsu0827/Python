class Student: #クラス定義
    def __init__(self,name): #コンストラクタでnameを定義
        self.name = name
    
    def calculateAvg(self,data): #メソッド,平均を計算
        sum = 0

        for num in data:
            sum += num

        avg = sum/len(data) #len(data)でdataの数を算出
        return avg

    def judge(self,avg): #メソッド,60以上なら合格60以下なら不合格

        if(avg>=60):
            result="passed"

        else:
            result="failed"
        return result

a001 = Student("sato") #オブジェクト化、インスタンス化
data = [70,65,50,10,30] #点数データを作る
avg = a001.calculateAvg(data) #avgに平均算出の結果を代入
result = a001.judge(avg) #resultに合否判定を代入

print(avg)
print(a001.name+" "+result)
    