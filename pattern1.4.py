customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
arrival_time, time_required = zip(*customers)
waiting_time=[]
previous_time=[]
for i in range(len(customers)):
    
    ans = input("Iroh starts immediately(Y/N): ")
    if ans == 'Y':
        time = time_required[i]
        print(time)
        waiting_time.append(time)
        previous_time.append(arrival_time[i]+time_required[i])
    elif ans=='N':
        if arrival_time[i]==arrival_time[i-1]:
           time=time_required[i-1]+time_required[i]
           print(time)
           waiting_time.append(time)
           previous_time.append(previous_time[i-1]+time_required[i])

        elif arrival_time[i]<previous_time[i-1]:
            time_extra=previous_time[i-1]-arrival_time[i]
            time=time_extra+time_required[i]
            print(time)
            waiting_time.append(time)
            previous_time.append(previous_time[i-1]+time_required[i])
    else:
        print("enter Y or N")
print(waiting_time)
total=0
for i in waiting_time:
    total +=i
print(f"average waiting tme :{total/len(waiting_time)}")