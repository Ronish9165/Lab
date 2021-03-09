#you live in 4 miles from the university. The bus drivers at 25 mph but spends 2 minutes each of the 10 stops on the way.
#How long will bus journey take? Alternatively, you could run to university, you jog first mile at 7 mph; then run the
#next two at 15 mph; before jogging the last at 7 mph again. Will this be quicker or slower than the bus.

distance_from_university=4
bus_speed=25
time_taken=((distance_from_university/bus_speed)*60)
#2 minutes in each stop

time_spend=20
total_time=time_taken = time_spend
print(f'Total time taken by bus is {total_time}')

jog_1= ((1/7)*60)
jog_2= ((2/15)*60)
jog_3= ((1/7)*60)

total_jog_time= jog_1 + jog_2 + jog_3
print(f'Total time taken by jogging is {total_jog_time}')

if (total_time > total_jog_time):
    print("Taking bus is slower than jogging")
else:
    print('Taking bus is quicker than jogging')