from robot_control_class import RobotControl
rc = RobotControl()

allLaser = rc.get_laser_full()

print(allLaser[0])
print(allLaser[360])
print(allLaser[719])