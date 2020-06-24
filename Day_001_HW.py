import numpy as np
import matplotlib.pyplot as plt
def mean_absolute_error(y, yp):
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae

# 定義 mean_squared_error 這個函數, 計算並傳回 MSE
def mean_squared_error(y, yp):
    mse=MSE=sum((y-yp)**2)/ len(y)
    return mse

w = 3
b = 0.5
x_lin = np.linspace(0, 100, 101)
y = (x_lin + np.random.randn(101) * 5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()
# 與範例相同, 不另外解說
y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()
# 執行 Function, 確認有沒有正常執行
MSE = mean_squared_error(y, y_hat)
MAE = mean_absolute_error(y, y_hat)
print("The Mean squared error is %.3f" % (MSE))
print("The Mean absolute error is %.3f" % (MAE))
#作業二請上 Kaggle, 在 Competitions 或 Dataset 中找一組競賽或資料並寫下：

# 1. 你選的這組資料為何重要
#   我選 Netflix Movies and TV Shows這組資料,這組資料可以作為對於各地人文喜好的研究,是了解各城市很有用的資料,
#   可做在地經營各種事業的參考

# 2. 資料從何而來 (tips: 譬如提供者是誰、以什麼方式蒐集)
#    提供者是 Flixable, Updated every month.

# 3. 蒐集而來的資料型態為何
#   資料為結構化的文字, .csv檔

# 4. 這組資料想解決的問題如何評估
#   可使用content-based and collaborative filtering models

# 作業3：申論題目可直接將答案回覆在HW檔案裡面，Jupyter notebook可直接編輯文字。

# 想像你經營一個自由載客車隊，你希望能透過數據分析以提升業績，請你思考並描述你如何規劃整體的分析/解決方案：
# 1. 核心問題為何 (tips：如何定義 「提升業績 & 你的假設」)
#   取得車隊中每個成員的業績狀況, 並做排名, 設定最後 5%成員需提升其業績 10%

# 2. 資料從何而來 (tips：哪些資料可能會對你想問的問題產生影響 & 資料如何蒐集)
#   資料需要由每位成員每一次載客即時提供, 因此須由叫車服務系統紀錄並自動將資料寫入資料庫, 
#   資料庫將記載每位成員的基本資訊, 包括性別, 年齡, 車款, 車齡, 所在地, 載客時間, 語言種類, 客戶滿意度調查, 客源

# 3. 蒐集而來的資料型態為何
#   寫入資料庫的文字, 數字

# 4. 你要回答的問題，其如何評估 (tips：你的假設如何驗證)
#   寫一程式定時分析出資料結果業績排名, 並依記載的資料分析出其共通性, 依據共通性結果檢討給予解決方案及註記, 
#   於下次定期資料結果出爐觀察該成員業績提升狀況