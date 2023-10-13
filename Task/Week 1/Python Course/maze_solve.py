# Import the robot_control_class.py module
from robot_control_class import RobotControl
# Create an instance of the RobotControl class
rc = RobotControl()

depan = rc.get_laser(360)
kiri = rc.get_laser(0)
kanan = rc.get_laser(714)

def navigate_maze():
    def obstacle_in_front():
        depan = rc.get_laser(360)
        return  depan < threshold
    
    def obstacle_in_kiri():
        kiri = rc.get_laser(0)
        return kiri < threshold
    
    def obstacle_in_kanan():
        kanan = rc.get_laser(714)
        return kanan < threshold

    
    threshold = 1 

  
    while not obstacle_in_front():
        rc.move_straight()


    rc.stop_robot()
    
    if obstacle_in_kiri():
        
        rc.rotate(250)

    elif obstacle_in_kanan():
       
        rc.rotate(80)
   
while (depan < 10 and kiri < 10 and kanan < 10):
    navigate_maze()


rc.stop_robot()
