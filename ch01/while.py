count = 0
while count < 10:
    count += 1
    if count % 2:
        continue

    print(f'count {count}')

    if count > 8:
        break
