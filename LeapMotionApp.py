import Leap, sys, thread, time, win32api, win32con, keyboardOutput
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from keyboardOutput import *

class LeapMotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Motion Sensor Connected"

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        print "Motion Sensor Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        frame = controller.frame()

        '''    print "frame ID: " + str(frame.id) \
              + " Timestamp: " + str(frame.timestamp) \
              + " Number of Hands " + str(len(frame.hands)) \
              + " Number of Fingers " + str(len(frame.fingers)) \
              + " Number of Tools " + str(len(frame.tools)) \
              + " Number of Gestures " + str(len(frame.gestures()))    '''
        previousNormal = 100

        leftHandInFrame = False
        rightHandInFrame = False

        for hand in frame.hands:
            if hand.is_left:
                leftHand = hand
                leftHandInFrame = True
            if hand.is_right:
                rightHand = hand
                rightHandInFrame = True




        #win32api.SetCursorPos((int(hand.palm_position[0]), int(hand.palm_position[1])

        #print handType + " Hand ID: " + str(hand.id) + " Palm Position: " + str(hand.palm_position)
        #print "Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) + " Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)
        if (leftHandInFrame):
            normalLeft = leftHand.palm_normal
            velocityLeft = leftHand.palm_velocity
            pinchLeft = leftHand.pinch_strength

            # left hand controlling play and pause of left deck
            if (leftHand.grab_strength == 1):
                SendInput(Keyboard(KEY_P, KEYEVENTF_EXTENDEDKEY))
                #print "play"
            elif (int(round(normalLeft[1])) == 1):
                #print "Normal"
                SendInput(Keyboard(VK_SPACE, KEYEVENTF_EXTENDEDKEY))

            SendInput(Keyboard(VK_SPACE, KEYEVENTF_KEYUP))
            SendInput(Keyboard(KEY_P, KEYEVENTF_KEYUP))

            # left hand controlling the volume on the left deck
            if ((pinchLeft == 1) and (int(round(velocityLeft[1])) > 80)):
                SendInput(Keyboard(KEY_Q))
            elif ((pinchLeft == 1) and (int(round(velocityLeft[1])) < -80)):
                SendInput(Keyboard(KEY_A))

        clockwiseness = "no circle"
            # left hand controlling pitch with circle gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = "clockwise"
                    SendInput(Keyboard(KEY_F, KEYEVENTF_EXTENDEDKEY))
                else:
                    clockwiseness = "counter-clockwise"
                    SendInput(Keyboard(KEY_D, KEYEVENTF_EXTENDEDKEY))

                swept_angle = 0


                if circle.state != Leap.Gesture.STATE_START:
                    previous = CircleGesture(controller.frame(1).gesture(circle.id))



        if (rightHandInFrame):
            normalRight = rightHand.palm_normal
            velocityRight = rightHand.palm_velocity
            pinchRight = rightHand.pinch_strength


            # right hand controlling play and pause of right deck

            if (rightHand.grab_strength == 1):
                SendInput(Keyboard(KEY_G, KEYEVENTF_EXTENDEDKEY))
                #print "play"
            elif (int(round(normalRight[1])) == 1):
                #print "Normal"
                SendInput(Keyboard(KEY_T, KEYEVENTF_EXTENDEDKEY))
                # scratch
            elif ((int(round(normalRight[1])) == -1) and int(round(velocityRight[2])) > 80):
                SendInput(Keyboard(KEY_J))
            elif ((int(round(normalRight[1])) == -1) and int(round(velocityRight[2])) < -80):
                SendInput(Keyboard(KEY_U))


            SendInput(Keyboard(KEY_G, KEYEVENTF_KEYUP))
            SendInput(Keyboard(KEY_T, KEYEVENTF_KEYUP))

            # right hand controlling the cross fade with a pinch as long as it is near the Leap device
            if ((pinchRight == 1) and (int(round(velocityRight[0])) > 80)):
                SendInput(Keyboard(VK_PRIOR))
            elif ((pinchRight == 1) and (int(round(velocityRight[0])) < -80)):
                SendInput(Keyboard(VK_NEXT))

            # right hand controlling the volume on the right deck

            elif ((pinchRight == 1) and (int(round(velocityRight[1])) > 80)):
                SendInput(Keyboard(KEY_W))
            elif ((pinchRight == 1) and (int(round(velocityRight[1])) < -80)):
                SendInput(Keyboard(KEY_S))




            '''
            print "Normal: " + str(int(round(normalRight[0]))) + " " + str(int(round(normalRight[1]))) + " " + str(int(round(normalRight[2]))) \
                + " Velocity: " + str(int(round(velocityRight[0]))) + " " + str(int(round(velocityRight[1]))) + " " + str(int(round(velocityRight[2])))
            '''
        SendInput(Keyboard(KEY_U, KEYEVENTF_KEYUP))
        SendInput(Keyboard(KEY_J, KEYEVENTF_KEYUP))

        SendInput(Keyboard(KEY_D, KEYEVENTF_KEYUP))
        SendInput(Keyboard(KEY_F, KEYEVENTF_KEYUP))

        SendInput(Keyboard(VK_NEXT,  KEYEVENTF_KEYUP))
        SendInput(Keyboard(VK_PRIOR, KEYEVENTF_KEYUP))






    '''    direction = hand.direction


        if (int(round(normal[1])) == -1):
            #SendInput(Keyboard(KEY_P, KEYEVENTF_EXTENDEDKEY))
            print "Pause"
            #SendInput(Keyboard(KEY_P, KEYEVENTF_KEYUP))
        elif (int(round(normal[1])) == 1):
            #SendInput(Keyboard(KEY_P, KEYEVENTF_EXTENDEDKEY))
            #SendInput(Keyboard(KEY_P, KEYEVENTF_KEYUP))
            print "Play"    '''


def main():
    listener = LeapMotionListener()
    controller = Leap.Controller()

    controller.add_listener(listener)

    print "Press Enter to Quit"

    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
