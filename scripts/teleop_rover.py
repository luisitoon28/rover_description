import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# Configuración de teclas
msg = """
Controla tu Rover!
---------------------------
Moverse:
    w
a   s   d

q/z : aumentar/disminuir velocidad lineal un 10%
e/c : aumentar/disminuir velocidad angular un 10%

CTRL-C para salir
"""

class TeleopRover(Node):
    def __init__(self):
        super().__init__('teleop_rover')
        # Publicamos en /cmd_vel como pide la práctica
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.linear_vel = 0.5
        self.angular_vel = 1.0

    def publish_vel(self, x, th):
        twist = Twist()
        twist.linear.x = x * self.linear_vel
        twist.angular.z = th * self.angular_vel
        self.publisher_.publish(twist)

def get_key(settings):
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0.1)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, settings)
    return key

def main():
    settings = termios.tcgetattr(sys.stdin)
    rclpy.init()
    node = TeleopRover()
    print(msg)

    try:
        while True:
            key = get_key(settings)
            x, th = 0.0, 0.0
            
            if key == 'w': x = 1.0
            elif key == 's': x = -1.0
            elif key == 'a': th = 1.0
            elif key == 'd': th = -1.0
            elif key == '\x03': break # CTRL-C
            
            node.publish_vel(x, th)
            
    except Exception as e:
        print(e)
    finally:
        node.publish_vel(0.0, 0.0)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, settings)
        rclpy.shutdown()

if __name__ == '__main__':
    main()