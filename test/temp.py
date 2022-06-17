sensor_file_name = '/sys/bus/w1/devices/28-03219779d03f/w1_slave'
while True:
        sensor_file = open(sensor_file_name)
        line = sensor_file.readlines()[-1]
        uitkomst = line[line.rfind("t"):]
        geheel = int(uitkomst[2:])
        temperatuur = geheel/1000
        print(f"T={temperatuur}")