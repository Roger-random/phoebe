#!/usr/bin/env python
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg

def send_neato_base():
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "base_link"
    t.child_frame_id = "neato_laser"
    t.transform.translation.x = -0.045 # Center of laser is roughly 4.5cm behind wheel center
    t.transform.translation.y = 0.0
    t.transform.translation.z = 0.08 # Laser is 8cm above ground level
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, 3.14) # Laser's 'forward' points back.
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('phoebe_baseneato')
    r_time = rospy.Rate(10)
    while not rospy.is_shutdown():
        send_neato_base()
        r_time.sleep()
