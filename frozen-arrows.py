'''
        Read Gyro and Accelerometer by Interfacing Raspberry Pi with MPU6050 using Python
	http://www.electronicwings.com
'''
import smbus			#import SMBus module of I2C
from time import sleep
import pyautogui as py#import
from math import atan2
py.FAILSAFE =False

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47
#low-pass filter for gyro
# lx=0
# ly=0
# lz=0

#we will be rotating in x-z plane
M_PI = 3.14159265359
dt=.01
pitch=90
yaw = 0


def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

counter = 0
pitch_prev = 0
yaw_prev = 0
cu=0
cd=0
cr=0
cl=0

while True:
	
	#Read Accelerometer raw value
	acc_x = read_raw_data(ACCEL_XOUT_H)
	acc_y = read_raw_data(ACCEL_YOUT_H)
	acc_z = read_raw_data(ACCEL_ZOUT_H)
	
	#Read Gyroscope raw value
	gyro_x = read_raw_data(GYRO_XOUT_H)
	gyro_y = read_raw_data(GYRO_YOUT_H)
	gyro_z = read_raw_data(GYRO_ZOUT_H)
	
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Ax = acc_x/16384.0
	Ay = acc_y/16384.0
	Az = acc_z/16384.0
	
	Gx = gyro_x/131.0
	Gy = gyro_y/131.0
	Gz = gyro_z/131.0
	
	# lx = 0.9*lx + 0.1*Gx
	# Gx = Gx - lx
	# ly = 0.9*ly + 0.1*Gy
	# Gy = Gy - ly
	# lz = 0.9*lz + 0.1*Gz
	# Gz = Gz - lz
	# if (Gx > 5):
	# 	py.press('up')
	# elif (Gx < -5):
	# 	py.press('down')
	# if (Gz > 5):
	# 	py.press('left')
	# elif (Gz <-5):
	# 	py.press('right')

	pitch += Gx*dt
	yaw += Gz*dt
	forceMag = abs(Ax) + abs(Ay) + abs(Az)
	if (forceMag > 0.5 and forceMag < 2):#may be 0.25 and 1
		pitchAcc = atan2(Ay,Az)*180/M_PI
		yawAcc = atan2(Ax,Ay)*180/M_PI
		pitch = pitch*0.98 + pitchAcc*0.02
		yaw = yaw*0.98 + yawAcc*0.02

	if (pitch_prev - pitch) > 5 or pitch < 70 and cd==0:
		py.press('down',10)
		print("down")
		cd=1
	elif (pitch - pitch_prev) > 5 and cu==0:
		py.press('up')
		cu=1
		print("up")
	else:
            py.keyUp('up')
            cu=0
            cd=0
	if yaw - yaw_prev > 3 or yaw > 15 and cr==0:
		py.press('right',25)
		cr=1
		print("right")
	elif yaw_prev - yaw >3 or yaw < -10 and cl==0:
		py.press('left',25)
		cl=1
		print("left")
	else:
            cl=0
            cr=0
#            #py.keyUp('left')
#            #py.keyUp('right')
#	print (pitch, yaw)
	counter +=1
	if counter == 20:
            pitch_prev = pitch
            yaw_prev = yaw
            counter = 0
	#print (pitch, yaw, "Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
	sleep(dt)


