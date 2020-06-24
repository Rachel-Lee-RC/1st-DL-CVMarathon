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
    # 可使用content-based and collaborative filtering models