content = open("day19.txt", encoding="utf8").read()
contentList = content.split('\n\n')

parts = {}
wf = {}

for line in contentList[0].split('\n'):
    wfName, flow = line.split('{')
    wf[wfName] = list(flow.strip('}').split(','))

for i, line in enumerate(contentList[1].split('\n')):
    atts = line.strip('{}').split(',')
    parts[i] = (int(atts[0].split('=')[1]),int(atts[1].split('=')[1]),int(atts[2].split('=')[1]),int(atts[3].split('=')[1]))

open_list = [('in', {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000)}, ['in'])]
success_intervals_list = []

while len(open_list) > 0:
    current_wf, intervals, visited = open_list.pop()
    for rule in wf[current_wf][:-1]:
        success_intervals = {}
        fail_intervals = {}

        splitedOnewf = rule.split(':')
        condition, destination = splitedOnewf[0], splitedOnewf[1]
        att = condition[0]

        for key in intervals:
            if key != att:
                success_intervals[key] = intervals[key]
                fail_intervals[key] = intervals[key]

        comparible = condition[1]
        value = int(condition[2:])
        interval = intervals[att]

        if comparible == '>':
            value += 1

        if interval[0] < value:
            small_interval = (interval[0], value-1)
        if interval[1] >= value:
            big_interval = (value, interval[1])

        if comparible == '<':
            success_intervals[att] = small_interval
            fail_intervals[att] = big_interval
        else:
            success_intervals[att] = big_interval
            fail_intervals[att] = small_interval

        if destination == 'A':
            success_intervals_list.append(success_intervals)
        elif destination != 'R' and destination not in visited:
            visited_copy = visited.copy()
            visited_copy.append(destination)
            new_dest = (destination, success_intervals, visited_copy)
            open_list.append(new_dest)

        intervals = fail_intervals

    if wf[current_wf][-1] == 'A':
        success_intervals_list.append(intervals)
    elif wf[current_wf][-1] != 'R' and wf[current_wf][-1] not in visited:
        visited_copy = visited.copy()
        visited_copy.append(wf[current_wf][-1])
        new_dest = (wf[current_wf][-1], intervals, visited_copy)
        open_list.append(new_dest)

allSuccess = 0

for success in success_intervals_list:
    successValue = 1
    for start, end in success.values():
        successValue *= end-start+1
    allSuccess += successValue

print(allSuccess)