# # fit an ARIMA model and plot residual errors
# from datetime import datetime
# from pandas import read_csv
# from pandas import DataFrame
# from statsmodels.tsa.arima.model import ARIMA
# from matplotlib import pyplot
# # load dataset
# def parser(x):
# 	return datetime.strptime(x, ' %d-%b-%Y')
# series = read_csv('VHigh2.csv', header=0, index_col=0, parse_dates=True, date_parser=parser)
# series.index = series.index.to_period('M')
# # fit model
# model = ARIMA(series, order=(5,1,0))
# model_fit = model.fit()
# # summary of fit model
# print(model_fit.summary())
# # line plot of residuals
# residuals = DataFrame(model_fit.resid)
# residuals.plot()
# pyplot.show()
# # density plot of residuals
# residuals.plot(kind='kde')
# pyplot.show()
# # summary stats of residuals
# print(residuals.describe())


# evaluate an ARIMA model using a walk-forward validation
from pandas import read_csv
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
# load dataset
def parser(x):
	return datetime.strptime(x, ' %d-%b-%Y')


# series = read_csv("output\VHigh" + str(1) + "-ARIMA.csv", header=0, index_col=0, parse_dates=True, date_parser=parser)
# series.index = series.index.to_period('M')
# # split into train and test sets
# X = series.values
# size = int(len(X) * 0.66)
# train, test = X[0:size], X[size:len(X)]
# history = [x for x in train]
# predictions = list()
# # walk-forward validation
# for t in range(len(test)):
# 	model = ARIMA(history, order=(5,1,0))
# 	model_fit = model.fit()
# 	output = model_fit.forecast()
# 	yhat = output[0]
# 	predictions.append(yhat)
# 	obs = test[t]
# 	history.append(obs)
# 	print('predicted=%f, expected=%f' % (yhat, obs))
# # evaluate forecasts
# rmse = sqrt(mean_squared_error(test, predictions))
# mae = mean_absolute_error(test,predictions)
# r2 = r2_score(test,predictions)
# print('Test RMSE: %.3f' % rmse)
# print('Test MAE: %.3f' % mae)
# print('Test R-Squared: %.3f' % r2)
# # plot forecasts against actual outcomes
# pyplot.plot(test, color='blue')
# # pyplot.plot(test)
# pyplot.plot(predictions, color='red')
# pyplot.show()


# from pandas import read_csv
# from matplotlib import pyplot
# from statsmodels.tsa.arima.model import ARIMA
# from datetime import datetime
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# from math import sqrt
# from tqdm.auto import tqdm
# import warnings

# # load dataset
# def parser(x):
# 	return datetime.strptime(x, ' %d-%b-%Y')
# warnings.simplefilter(action='ignore', category=FutureWarning)

# r2_cumm = 0
# rmse_cumm = 0
# mae_cumm = 0

# for i in (range(0,5)):
# 	print("\n\nFile No: " + str(i+1))
# 	series = read_csv("output\VHigh" + str(i) + "-ARIMA.csv", header=0, index_col=0, parse_dates=True, date_parser=parser)
# 	# series = read_csv('VHigh2.csv', header=0, index_col=0, parse_dates=True, date_parser=parser)
# 	series.index = series.index.to_period('M')
# 	# split into train and test sets
# 	X = series.values
# 	size = int(len(X) * 0.66)
# 	train, test = X[0:size], X[size:len(X)]
# 	history = [x for x in train]
# 	predictions = list()
# 	# walk-forward validation
# 	for t in tqdm(range(len(test))):
# 		model = ARIMA(history, order=(5,1,0))
# 		model_fit = model.fit()
# 		output = model_fit.forecast()
# 		yhat = output[0]
# 		predictions.append(yhat)
# 		obs = test[t]
# 		history.append(obs)
# 		# print('predicted=%f, expected=%f' % (yhat, obs))
# 	# evaluate forecasts
# 	rmse = sqrt(mean_squared_error(test, predictions))
# 	mae = mean_absolute_error(test,predictions)
# 	r2 = r2_score(test,predictions)
# 	print('\nTest RMSE: %.3f' % rmse)
# 	print('Test MAE: %.3f' % mae)
# 	print('Test R-Squared: %.3f' % r2)
# 	r2_cumm = r2_cumm + r2
# 	mae_cumm = mae_cumm + mae
# 	rmse_cumm = rmse_cumm + rmse

# print("\n\n---------------Average Values--------------")
# print("Average R2 Score: " + str(r2_cumm/5))
# print("Average Root Mean Squared Error: " + str(rmse_cumm/5))
# print("Average Mean Absolute Error: " + str(mae_cumm/5))
	

# series = read_csv("output\VHigh" + str(0) + "-ARIMA.csv", header=0, index_col=0, parse_dates=True, date_parser=parser)
# series.index = series.index.to_period('M')
# # split into train and test sets
# X = series.values
# size = int(len(X) * 0.66)
# train, test = X[0:size], X[size:len(X)]
# history = [x for x in train]
# predictions = list()
# # walk-forward validation
# for t in range(len(test)):
# 	model = ARIMA(history, order=(1,1,5))
# 	model_fit = model.fit()
# 	output = model_fit.forecast()
# 	yhat = output[0]
# 	predictions.append(yhat)
# 	obs = test[t]
# 	history.append(obs+1)
# 	print('predicted=%f, expected=%f' % (yhat, obs))
# # evaluate forecasts
# rmse = sqrt(mean_squared_error(test, predictions))
# mae = mean_absolute_error(test,predictions)
# r2 = r2_score(test,predictions)
# print('Test RMSE: %.3f' % rmse)
# print('Test MAE: %.3f' % mae)
# print('Test R-Squared: %.3f' % r2)
# # plot forecasts against actual outcomes
# pyplot.plot(test[0:len(test)-200], color='blue')
# # pyplot.plot(test)
# pyplot.plot(predictions, color='red')
# pyplot.show()

series = read_csv("output\VHigh" + str(0) + "-ARIMA.csv", header=0, index_col=0, parse_dates=True, date_parser=parser)
series.index = series.index.to_period('M')
# split into train and test sets
X = series.values
# size = int(len(X) * 0.66)
# train, test = X[0:size], X[size:len(X)]
# history = [x for x in train]
# predictions = list()
# # walk-forward validation
# for t in range(len(test)):
# 	model = ARIMA(history, order=(1,1,5))
# 	model_fit = model.fit()
# 	output = model_fit.forecast()
# 	yhat = output[0]
# 	predictions.append(yhat)
# 	obs = test[t]
# 	history.append(obs+1)
# 	print('predicted=%f, expected=%f' % (yhat, obs))
# # evaluate forecasts
# rmse = sqrt(mean_squared_error(test, predictions))
# mae = mean_absolute_error(test,predictions)
# r2 = r2_score(test,predictions)
# print('Test RMSE: %.3f' % rmse)
# print('Test MAE: %.3f' % mae)
# print('Test R-Squared: %.3f' % r2)
# plot forecasts against actual outcomes

plt.plot(X[0:len(X)], color='red',label = "Validation Data Set")

plt.plot(X[0:int(len(X)*0.7)], color='blue',label = "Training Data Set")

# pyplot.plot(test)
# pyplot.plot(predictions, color='red')
plt.ylabel("Stock Quantity")
plt.xlabel("Time")
plt.legend(loc = 1)
plt.show()
