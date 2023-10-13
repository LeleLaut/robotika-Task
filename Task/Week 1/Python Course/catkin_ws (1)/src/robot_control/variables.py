from robot_control_class import RobotControl
rc = RobotControl()

laser1 = rc.get_laser(360)
print ("The distance laser 1 measured is: ", laser1, " m.")
laser2 = rc.get_laser(270)
print ("The distance laser 2 measured is: ", laser2, " m.")
laser2 = rc.get_laser(90)
print ("The distance laser 2 measured is: ", laser2, " m.")

