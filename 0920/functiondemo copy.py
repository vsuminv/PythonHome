def calc_sum(start,end):
    sum = 0
    for i in range(start,end):
        sum += i
    return sum

start = 50
end = 70
result = calc_sum(start,end)
print('%d부터 %d까지의 합은 %d입니다.'%(start,end, result))
    
