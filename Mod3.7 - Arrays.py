# This program is meant to simulate a heart rate tracker that
# takes a patient's heart rate multiple times a day

total = 0
time_slots = ['Morning', 'Midday', 'Afternoon', 'Evening']
for time in time_slots:
    rate = int(input(f'Enter your heart rate (in BPM) in the {time} '))
    heart_rates = []
    heart_rates.append([time, rate])
    total = total + rate
average = total / 4
print(f'Average heart rate today: {average:.2f}')
