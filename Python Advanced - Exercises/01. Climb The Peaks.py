d_meals, d_energy = [int(x) for x in input().split(", ")], [int(x) for x in input().split(", ")]
c_peaks, m_peaks = [], [{"Vihren": 80}, {"Kutelo": 90}, {"Banski Suhodol": 100}, {"Polezhan": 60}, {"Kamenitza": 70}]
while d_meals and d_energy and m_peaks:
    boost_sum = d_meals.pop() + d_energy.pop(0)
    peak_name, difficult_level = list(m_peaks[0].items())[0]
    if boost_sum >= difficult_level:
        del m_peaks[0]
        c_peaks.append(peak_name)
if not m_peaks:
    result_conquered = "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"
else:
    result_conquered = "Alex failed! He has to organize his journey better next time -> @PIRINWINS"
print(result_conquered)
if c_peaks:
    print("Conquered peaks:")
    print(*c_peaks, sep="\n")