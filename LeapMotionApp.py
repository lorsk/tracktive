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


#        normal = hand.palm_normal
#        previousNormal = int(round(normal[1]))

        #win32api.SetCursorPos((int(hand.palm_position[0]), int(hand.palm_position[1])

        #print handType + " Hand ID: " + str(hand.id) + " Palm Position: " + str(hand.palm_position)
        #print "Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) + " Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)
        if (rightHandInFrame):
            if (rightHand.grab_strength == 1):
                SendInput(Keyboard(VK_LEFT, KEYEVENTF_EXTENDEDKEY))
                print "Pitch"
            else:
                print "Normal"
                SendInput(Keyboard(VK_LEFT, KEYEVENTF_KEYUP))

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
