import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms


def set_color(result):
    list_of_colors = []

    for r in result:
        if r < 0:
            list_of_colors.append('darkorange')
        else:
            list_of_colors.append('darkgreen')
    return list_of_colors

def count_money_result(result):
    live_money = []
    temp_val = 0

    for idx, val in enumerate(result):
        temp_val += val

        live_money.append(temp_val)

    return live_money

def plot_money_chart(live_time, sell_action_result, money_invested_in_stock):

    fig, ax = plt.subplots()
    ax.scatter(live_time, sell_action_result, c=set_color(sell_action_result), s=money_invested_in_stock, alpha=0.3, cmap='viridis')
    ax.plot(live_time, count_money_result(sell_action_result))
    ax.set(xticklabels=[])
    # plt.axhline(y=0.5, color='r', linestyle='-')
    ax.set_ylabel('Money (PLN)')
    ax.set_title('Money Chart')
    ax.set_xlabel('Time')
    plt.show()



#read data
df_actions = pd.read_csv(r"C:\Users\jerzy\Downloads\from_2021-01-01_to_2021-02-14_MTYxMzI1NzUyNTY3OQ.csv")

#count all payments
df_payments = df_actions[df_actions['Notes'].notna()].reset_index(drop=True)
total_payments = df_payments.iloc[:,-5].sum()

#drop payments action

df_trading_actions = df_actions[df_actions['Action'] != 'Deposit']

#investment in time
idx = df_actions['Result (PLN)'].dropna().index
sell_action_result = df_actions['Result (PLN)'].dropna()
live_time = df_actions['Time'][df_actions['Result (PLN)'].notna()]
money_invested_in_stock = df_actions['Total (PLN)'].dropna()[idx]


plot_money_chart(live_time, sell_action_result, money_invested_in_stock)



