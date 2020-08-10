def process_line(line, d):
    if line[0] == 'ordered':
        order_id,user_id,ordered_at,x,y = line[1:]
        if order_id not in d:
            d[order_id] = {}
        d[order_id]['user_id'] = user_id
        d[order_id]['ordered_at'] = int(ordered_at)
        d[order_id]['x'] = int(x)
        d[order_id]['y'] = int(y)
    else:
        event,order_id,smth_at = line
        if order_id not in d:
            d[order_id] = {}
        if event == 'arrived':
            d[order_id]['arrived_at'] = int(smth_at)
        elif event == 'started':
            d[order_id]['started_at'] = int(smth_at)
        elif event == 'finished':
            d[order_id]['finished_at'] = int(smth_at)


def calculate_points(k, user_id, ordered_at, arrived_at, started_at, finished_at, x, y):
    if 60 * k < started_at - arrived_at:
        return user_id, 0
    return user_id, max(0, finished_at - (ordered_at + x * 60 + k * 60 + y * 60))


def solveE(d, k, n):
    user_points = {}
    
    for _,order in d.items():
        if ('ordered_at' not in order
            or 'arrived_at' not in order
            or 'started_at' not in order
            or 'finished_at' not in order):  # ignore
            continue
        user_id, points = calculate_points(k, **order)
        if user_id in user_points:
            user_points[user_id] += points
        else:
            user_points[user_id] = points
    
    users = sorted(
        ((user_id, points) for user_id, points in user_points.items() if points > 0),
        key=lambda x: (-x[1], x[0])
    )
    result = [user_id for user_id,_ in users[:n]]
    if result:
        return result
    else:
        return '-'


T = int(input().strip())
for _ in range(T):
    e, n, k = map(int, input().strip().split())
    d = {}
    for _ in range(e):
        process_line(input().strip().split(), d)
    
    print(*solveE(d, k, n))
