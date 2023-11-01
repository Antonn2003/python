deposed_sum = float(input())
deposit_range_in_months = int(input())
annual_lihva_percent = float(input())

godishna_lihva = deposed_sum * (annual_lihva_percent/100)
mesechna_lihva = godishna_lihva / 12

total_sum = deposed_sum + deposit_range_in_months * mesechna_lihva
print(total_sum)