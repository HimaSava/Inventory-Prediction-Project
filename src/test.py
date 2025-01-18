import pandas as pd
from datetime import datetime  

# Read the csv file
df = pd.read_csv("cardex with values.csv", low_memory=False)
df["Trxn 12"] = df["Trxn 12"].fillna("NAN")
df["Trxn Date"] = df["Trxn Date"].fillna("NAN")

# def divider(lengths):
#     total = 0
#     vlow = 0
#     low = 0
#     medium = 0
#     high = 0
#     vhigh = 0
#     for i in lengths:
#         if i<=5:
#             vlow = vlow+1
#         elif i<=100:
#             low = low + 1
#         elif i<=500:
#             medium = medium + 1
#         elif i<=1000:
#             high = high + 1
#         else:
#             vhigh = vhigh + 1
#         total = total + i

#     print("Very Low: " + str(vlow))
#     print("Low: " + str(low))
#     print("Medium: " + str(medium))
#     print("High: " + str(high))
#     print("Very High: " + str(vhigh))
#     print("Total:" + str(total))

# count = -1
# number_count = 0
# flag = 0
# tot_flag =0
# temp_len = []
# lens = []
# last_date = 0
# id = []
# lengths = []
# tot = []
# dead_inventory = 0
# zero_inventory = 0
# item_info_id = 0
# item_info_name = 0
# item_info_final_qty = 0
# item_info_final_prize = 0

# # This loop iterates through the whole file line by line
# for k in range(0, len(df)-1):
#     i = df["Trxn Date"][k]
#     # Sets flag to 1 if the start of a new item is identified
#     if i.isnumeric():
#         item_info_id = i
#         item_info_name = df["Type"][k]
#         flag = 1
#         temp_len.append(i)
#         number_count = number_count+1
#         id.append(i)
    
#     # Saves the total  
#     if tot_flag == 1:
#         tot.append(float(df["Trxn 12"][k]))
#         if float(df["Trxn 12"][k]) == 0:
#             zero_inventory = zero_inventory + 1
#         tot_flag = 0

#     if i == "NAN" and flag == 1:
#         temp_len.append(count)
#         lengths.append(count)
#         lens.append(temp_len)
#         temp_len = []
#         count = -1
#         flag = 0
#         tot_flag = 1
#         if last_date <=2022:
#             dead_inventory = dead_inventory + 1
        
    
#     if flag == 1:
#         count = count + 1
#         last_date = int(i.split('-')[-1])

# if flag == 1:
#     temp_len.append(count)
#     lengths.append(count)


# # print(lens)
# print(number_count)
# print("No. of transaction:")
# divider(lengths)
# print("\n\nNo. of Stock:")
# divider(tot)
# print("Dead Inventory: " + str(dead_inventory))
# print("Zero Inventory: " + str(zero_inventory))

# print(tot[:5])
print(df.head())


# GLobal flags
start_item_flag = 0
end_item_flag = 0

#Global lists
item_info_list = []
item_trans_list = []
item_list = []
all_item_list = []

#Global vars
transaction_count = 0

for k in range(0, len(df)-1):
    # Sets flag to 1 if the start of a new item is identified
    
    
    if end_item_flag == 1:
        # Add final qty
        item_info_list.append(float(df["Trxn 12"][k]))
        item_info_list.append(float(df["Final Qty"][k]))
        item_info_list.append(transaction_count)
        
        item_list.append(item_info_list)
        item_list.append(item_trans_list)
        all_item_list.append(item_list)
        item_info_list = []
        item_trans_list = []
        item_list = []

        end_item_flag = 0

    if df["Trxn Date"][k] == "NAN" and start_item_flag == 1:
        
        start_item_flag = 0
        end_item_flag = 1

    if start_item_flag == 1:
        temp_list = []
        temp_list.append(df["Trxn Date"][k])
        if df["Qty"][k] !='0':
            temp_list.append(0)
            temp_list.append(df["Qty"][k])
            temp_list.append(df["Value"][k])
        else:
            temp_list.append(1)
            temp_list.append(df["Qty.1"][k])
            temp_list.append(df["Value.1"][k])
        temp_list.append(df["Qty.2"][k])
        item_trans_list.append(temp_list)
        transaction_count = transaction_count + 1

    if df["Trxn Date"][k].isnumeric():
        start_item_flag = 1
        # Save the id and name is the list
        item_info_list.append(df["Trxn Date"][k])
        item_info_list.append(df["Type"][k])
        #Reset transaction count
        transaction_count = 0

# Split the data based on number of transactions
trans_vlow_list = [0]
trans_low_list = [0]
trans_medium_list = [0]
trans_high_list = [0]
trans_vhigh_list = [0]
trans_vlow = 0
trans_low = 0
trans_medium = 0
trans_high = 0
trans_vhigh = 0


for i in all_item_list:
    if i[0][4] <= 5:
        trans_vlow = trans_vlow+1
        trans_vlow_list.append(i)
    elif i[0][4] <=100:
        trans_low = trans_low + 1
        trans_low_list.append(i)
    elif i[0][4] <=500:
        trans_medium = trans_medium + 1
        trans_medium_list.append(i)
    elif i[0][4] <=1000:
        trans_high = trans_high + 1
        trans_high_list.append(i)
    else:
        trans_vhigh = trans_vhigh + 1
        trans_vhigh_list.append(i)
trans_vlow_list[0] = trans_vlow
trans_low_list[0] = trans_low
trans_medium_list[0] = trans_medium
trans_high_list[0] = trans_high
trans_vhigh_list[0] = trans_vhigh

# Split the data based on number of transactions
qty_vlow_list = [0]
qty_low_list = [0]
qty_medium_list = [0]
qty_high_list = [0]
qty_vhigh_list = [0]
qty_vlow = 0
qty_low = 0
qty_medium = 0
qty_high = 0
qty_vhigh = 0


for i in all_item_list:
    if i[0][2] <= 5:
        qty_vlow = qty_vlow+1
        qty_vlow_list.append(i)
    elif i[0][2] <=100:
        qty_low = qty_low + 1
        qty_low_list.append(i)
    elif i[0][2] <=500:
        qty_medium = qty_medium + 1
        qty_medium_list.append(i)
    elif i[0][2] <=1000:
        qty_high = qty_high + 1
        qty_high_list.append(i)
    else:
        qty_vhigh = qty_vhigh + 1
        qty_vhigh_list.append(i)
qty_vlow_list[0] = qty_vlow
qty_low_list[0] = qty_low
qty_medium_list[0] = qty_medium
qty_high_list[0] = qty_high
qty_vhigh_list[0] = qty_vhigh


# Dead Inventory

# import csv

# dead_inventory_list = []
# dead_inventory_count = 0
# for i in all_item_list:
#     temp_list = []
#     if len(i[1]) == 0:
#         temp_list.append(i[0][0])
#         temp_list.append(i[0][1])
#         temp_list.append(i[0][2])
#         temp_list.append(i[0][4])
#         temp_list.append("NAN")
#         dead_inventory_list.append(temp_list)
#         dead_inventory_count = dead_inventory_count + 1
#     else:
#         last_date_year = int(i[1][-1][0].split('-')[-1])
#         if last_date_year <=2021:
#             temp_list.append(i[0][0])
#             temp_list.append(i[0][1])
#             temp_list.append(i[0][2])
#             temp_list.append(i[0][4])
#             temp_list.append(i[1][-1][0])
#             dead_inventory_list.append(temp_list)
#             dead_inventory_count = dead_inventory_count + 1
    
# with open("Dead Inventory Report.csv", 'w', newline='') as file:

#     write = csv.writer(file)
#     entry = ['Dead Inventory Report', "Total Dead Inventory:", dead_inventory_count]
#     title = ['Item ID', 'Name', 'Quantity', 'Price', 'Last Transaction Date']
    
#     write.writerow(entry)
#     write.writerow("")
#     write.writerow(title)
#     write.writerows(dead_inventory_list)


# zero_inventory_list = []
# zero_inventory_count = 0
# for i in dead_inventory_list:
#     if i[2] == 0:
#         temp = []
#         temp.append(i[0])
#         temp.append(i[1])
#         temp.append(i[4])
#         zero_inventory_list.append(temp)
#         zero_inventory_count = zero_inventory_count + 1

# with open("Zero Inventory Report.csv", 'w', newline='') as file:

#     write = csv.writer(file)
#     entry = ['Zero Inventory Report', "Total Zero Inventory:", zero_inventory_count]
#     title = ['Item ID', 'Name','Last Transaction Date']
    
#     write.writerow(entry)
#     write.writerow("")
#     write.writerow(title)
#     write.writerows(zero_inventory_list[:])



date_str = '02/28/2023 02:30 PM'
date_format = ' %d-%b-%Y'



# # Save Trans High results to csv file
# with open("High.csv", 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(trans_high_list[1][0])
#     for i in trans_high_list[1][1]:
#         i[0] = datetime.strptime(i[0], date_format).toordinal()
#         writer.writerow(i)


import csv
# Save Trans VHigh results to csv file
with open("VHigh.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date","Type","Qty","Price","Total","Date_no"])
    for i in trans_vhigh_list[1][1]:
        i.append(datetime.strptime(i[0], date_format).toordinal())
        writer.writerow(i)

for j in range(0,5):
    with open("output\VHigh" + str(j) + "-ARIMA.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(["Date","Type","Qty","Price","Total","Date_no"])
        for i in trans_vhigh_list[j+1][1]:
            # i.append(datetime.strptime(i[0], date_format).toordinal())
            k = []
            k.append(i[0])
            k.append(i[4])
            writer.writerow(k)  

for j in range(0,5):
    with open("output\VHigh" + str(j) + ".csv", 'w', newline='') as file:        
        writer = csv.writer(file)
        writer.writerow(["Total","Date_no"])
        for i in trans_vhigh_list[j+1][1]:
            k = []
            k.append(i[4])
            k.append(datetime.strptime(i[0], date_format).toordinal())
            writer.writerow(k)

  


with open("LIst.csv",'w', newline='') as file:
    writer = csv.writer(file)
    for i in trans_vhigh_list[1:]:
        writer.writerow(i[0])


sum = 0
for i in all_item_list:
    sum = sum + i[0][4]

print("Total Transaction: " + str(sum))



# print(all_item_list[-1])
# print(int(all_item_list[0][1][-1][0].split('-')[-1]))
# print(trans_high_list[1:5][0])

