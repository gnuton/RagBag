def solution(A):
    # The idea:
    # The profit is maximized when the profit: PriceStock[dayQ] - PriceStock[DayP]
    # is calculated used the higher PriceStock[dayQ]
    # the lower PriceStock[DayP] so that Q>P
    if not len(A):
        return 0

    min_price=A[0]
    max_profit=0
    for a in A[1:]:
        min_price = min(min_price, a)
        profit = a - min_price
        max_profit = max(max_profit, profit)
    return max_profit