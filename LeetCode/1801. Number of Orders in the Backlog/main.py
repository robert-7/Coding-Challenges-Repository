import bisect
import math

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        if len(orders) == 1:
            return orders[0][1]

        buy_backlog, sell_backlog = [], []
        for i in range(len(orders)):
            original_order = orders[i]
            order_type = original_order[2]

            if order_type == 0:
                remaining_order = process_buy_order(sell_backlog, original_order)
                if remaining_order[1] != 0:
                    buy_backlog = add_to_backlog(buy_backlog, remaining_order)

            if order_type == 1:
                remaining_order = process_sell_order(buy_backlog, original_order)
                if remaining_order[1] != 0:
                    sell_backlog = add_to_backlog(sell_backlog, remaining_order)
        
            print(f"{i}. {original_order} -> {remaining_order}\nbuy_backlog:  {buy_backlog}\nsell_backlog: {sell_backlog}\n")

        # return the number we want
        buy_backlog_length = sum(backlog_item[1] for backlog_item in buy_backlog)
        sell_backlog_length = sum(backlog_item[1] for backlog_item in sell_backlog)
        backlog_length = buy_backlog_length + sell_backlog_length
        return int(backlog_length % (math.pow(10, 9) + 7))

def process_buy_order(sell_backlog, order):
    buy_price = order[0]
    buy_amount = order[1]
    # this is a quick and dirty solution
    # check if there are any sell orders in the backlog less than the buy order amount
    i = 0
    while (i <= len(sell_backlog)-1) and (buy_amount != 0):
        if sell_backlog[i][0] <= buy_price:
            if buy_amount >= sell_backlog[i][1]:
                amount_bought = sell_backlog[i][1]
                buy_amount -= sell_backlog[i][1]
                sell_backlog.pop(i)
            else:
                amount_bought = buy_amount
                buy_amount = 0
                sell_backlog[i][1] -= amount_bought
                i += 1
        else:
            i += 1

    return [buy_price, buy_amount]


def process_sell_order(buy_backlog, order):
    sell_price = order[0]
    sell_amount = order[1]
    # this is a quick and dirty solution
    # check if there are any buy orders in the backlog greater than the sell order amount
    i = len(buy_backlog)-1
    while (i >= 0) and (sell_amount != 0):
        if buy_backlog[i][0] >= sell_price:
            if sell_amount >= buy_backlog[i][1]:
                amount_sold = buy_backlog[i][1]
                sell_amount -= buy_backlog[i][1]
                buy_backlog.pop(i)
                i -= 1
            else:
                amount_sold = sell_amount
                sell_amount = 0
                buy_backlog[i][1] -= amount_sold
                i -= 1
        else:
            i -= 1

    return [sell_price, sell_amount]


def add_to_backlog(backlog, order):
    bisect.insort(backlog, order, key=lambda x: x[0])
    return backlog
