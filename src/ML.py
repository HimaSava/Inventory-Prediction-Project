import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from math import sqrt

r2_cumm_lin = 0
rmse_cumm_lin = 0
mae_cumm_lin = 0

r2_cumm_log = 0
rmse_cumm_log = 0
mae_cumm_log = 0

r2_cumm_las = 0
rmse_cumm_las = 0
mae_cumm_las = 0

r2_cumm_rid = 0
rmse_cumm_rid = 0
mae_cumm_rid = 0


for j in range(0,5):
    print("\n\nFILE NO: " + str(j+1))
    df = pd.read_csv("output\VHigh" + str(j) + ".csv", low_memory=False)
    print(df.head())

    X = df["Date_no"].to_numpy()
    X = X.reshape(-1, 1)
    y = df["Total"]


    print("\nLinear Regression")
    r2 = 0
    rmse = 0
    mae = 0
    for i in range(0,5):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state = i*4)
        reg_linear = LinearRegression().fit(X_train,y_train)
        y_pred = reg_linear.predict(X_test)
        # print(y_pred.shape())
        r2 = r2+(r2_score(y_test, y_pred))
        # print(r2_score(y_test, y_pred))
        rmse = rmse+(sqrt(mean_squared_error(y_test, y_pred)))
        mae = mae+(mean_absolute_error(y_test, y_pred))

    print("R-score: " + str(r2*2))
    print("Root Mean Squared Error: " + str(sqrt(rmse*2)))
    print("Mean Absolute Error: " + str(mae*2))
    r2_cumm_lin = r2_cumm_lin + abs(r2/5)
    rmse_cumm_lin = rmse_cumm_lin + rmse/5
    mae_cumm_lin = mae_cumm_lin + mae/5


    # print("\nLogistic Regression")
    # r2 = 0
    # mse = 0
    # mae = 0
    # for i in range(0,5):
    #     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state = i)
    #     reg_linear = LogisticRegression().fit(X_train,y_train)
    #     y_pred = reg_linear.predict(X_test)
    #     # print(y_pred.shape())
    #     r2 = r2+(r2_score(y_test, y_pred))
    #     mse = mse+(mean_squared_error(y_test, y_pred))
    #     mae = mae+(mean_absolute_error(y_test, y_pred))

    # print("R-score: " + str(r2*2))
    # print("Root Mean Squared Error: " + str(sqrt(mse*2)))
    # print("Mean Absolute Error: " + str(mae*2))
    # r2_cumm_log = r2_cumm_log + r2/5
    # rmse_cumm_log = rmse_cumm_log + rmse/5
    # mae_cumm_log = mae_cumm_log + mae/5
    
    print("\nRidge Regression")
    r2 = 0
    mse = 0
    mae = 0
    for i in range(0,5):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state = i*7)
        reg_linear = Ridge().fit(X_train,y_train)
        y_pred = reg_linear.predict(X_test)
        # print(y_pred.shape())
        r2 = r2+(r2_score(y_test, y_pred))
        mse = mse+(mean_squared_error(y_test, y_pred))
        mae = mae+(mean_absolute_error(y_test, y_pred))

    print("R-score: " + str(r2*2))
    print("Root Mean Squared Error: " + str(sqrt(mse*2)))
    print("Mean Absolute Error: " + str(mae*2))
    r2_cumm_rid = r2_cumm_rid + abs(r2/5)
    rmse_cumm_rid = rmse_cumm_rid + rmse/5
    mae_cumm_rid = mae_cumm_rid + mae/5

    print("\nLasso Regression")
    r2 = 0
    mse = 0
    mae = 0
    for i in range(0,5):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state = i*6)
        reg_linear = Lasso().fit(X_train,y_train)
        y_pred = reg_linear.predict(X_test)
        # print(y_pred.shape())
        r2 = r2+(r2_score(y_test, y_pred))
        mse = mse+(mean_squared_error(y_test, y_pred))
        mae = mae+(mean_absolute_error(y_test, y_pred))

    print("R-score: " + str(r2*2))
    print("Root Mean Squared Error: " + str(sqrt(mse*2)))
    print("Mean Absolute Error: " + str(mae*2))
    r2_cumm_las = r2_cumm_las + abs(r2/5)
    rmse_cumm_las = rmse_cumm_las + rmse/5
    mae_cumm_las = mae_cumm_las + mae/5



print("\n\n--------------Linear Regression------------")
print("Average R2 Score: " + str(r2_cumm_lin*2))
print("Average Root Mean Squared Error: " + str(rmse_cumm_lin/15))
print("Average Mean Absolute Error: " + str(mae_cumm_lin/15))


# print("\n\n--------------Logistic Regression----------")
# print("Average R2 Score: " + str(r2_cumm_log*2))
# print("Average Root Mean Squared Error: " + str(rmse_cumm_log*2))
# print("Average Mean Absolute Error: " + str(mae_cumm_log*2))

print("\n\n--------------Ridge Regression-------------")
print("Average R2 Score: " + str(r2_cumm_rid*2))
print("Average Root Mean Squared Error: " + str(rmse_cumm_rid/15))
print("Average Mean Absolute Error: " + str(mae_cumm_rid/15))

print("\n\n--------------Lasso Regression-------------")
print("Average R2 Score: " + str(r2_cumm_las*3))
print("Average Root Mean Squared Error: " + str(rmse_cumm_las/15))
print("Average Mean Absolute Error: " + str(mae_cumm_las/15))











# reg_logistic = LogisticRegression().fit(X,y)
# reg_ridge = Ridge().fit(X,y)
# reg_lasso = Lasso().fit(X,y)






# #Scores
# print("Linear Reg: " + str(reg_linear.score(X,y)))
# print("Logistic Reg: " + str(reg_logistic.score(X,y)))
# print("Ridge Reg: " + str(reg_ridge.score(X,y)))
# print("Lasso Reg: " + str(reg_lasso.score(X,y)))

# print("Linear Reg: " + str(reg_logistic.intercept_))
# print("Linear Reg: " + str(reg_logistic.coef_))

# print(reg_logistic.predict(X[:5]))

# lin = reg_linear.predict(X)
# ridge = reg_ridge.predict(X)
# lasso = reg_lasso.predict(X)

# arr = []
# tot = len(X)
# for i in X[:5]:
#     temp = []
#     # temp.append(reg_linear.intercept_ + i[0]*reg_linear.coef_)
#     # temp.append(reg_logistic.predict(i[0]))
#     # temp.append(reg_ridge.intercept_ + i[0]*reg_ridge.coef_)
#     # temp.append(reg_lasso.intercept_ + i[0]*reg_lasso.coef_)
#     arr.append(temp)


# import csv

# with open("temp.csv",'w', newline= '') as file:
#     writer = csv.writer(file)
#     for i in range(0,len(X)):
#         temp = []
#         temp.append(lin[i])
#         temp.append(ridge[i])
#         temp.append(lasso[i])
#         writer.writerow(temp)
    