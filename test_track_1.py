import vrep
import sys

vrep.simxFinish(-1) #just in case

clientID = vrep.simxStart('127.0.0.1', 20000, True, True, 5000, 5)

if clientID != -1:
    print "Connected to remote API server"
else:
    print "Connection not successful"
    sys.exit("Could not connect")

errorCode, left_motor_handle = \
           vrep.simxGetObjectHandle(clientID, \
                'Pioneer_p3dx_leftMotor', vrep.simx_opmode_oneshot_wait)
errorCode, right_motor_handle = \
           vrep.simxGetObjectHandle(clientID, \
                'Pioneer_p3dx_rightMotor', vrep.simx_opmode_oneshot_wait)

errorCode = vrep.simxSetJointTargetVelocity(\
    clientID, left_motor_handle, 0.5, vrep.simx_opmode_streaming)
errorCode = vrep.simxSetJointTargetVelocity(\
    clientID, right_motor_handle, 0.5, vrep.simx_opmode_streaming)
