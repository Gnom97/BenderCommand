#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>

#include <MeMCore.h>

MeDCMotor motor_9(9);
MeDCMotor motor_10(10);		

void move(int direction, int speed)
{
      int leftSpeed = 0;
      int rightSpeed = 0;
      if(direction == 1){
        	leftSpeed = speed;
        	rightSpeed = speed;
      }else if(direction == 2){
        	leftSpeed = -speed;
        	rightSpeed = -speed;
      }else if(direction == 3){
        	leftSpeed = -speed;
        	rightSpeed = speed;
      }else if(direction == 4){
        	leftSpeed = speed;
        	rightSpeed = -speed;
      }
      motor_9.run((9)==M1?-(leftSpeed):(leftSpeed));
      motor_10.run((10)==M1?-(rightSpeed):(rightSpeed));
}
				
double angle_rad = PI/180.0;
double angle_deg = 180.0/PI;
void manualMode(double speed);
void automaticDrive(double speed);
MeUltrasonicSensor ultrasonic_3(3);
MeLineFollower linefollower_2(2);
void inputParse();
double mode;
double ledLight;
MeSerial se;
MeRGBLed rgbled_7(7, 7==7?2:4);
double speed;


void manualMode(double speed)
{
}

void automaticDrive(double speed)
{
    if(((ultrasonic_3.distanceCm()) > (4)) && (((true&&(1?(linefollower_2.readSensors()&2):!(linefollower_2.readSensors()&2)))) && ((true&&(1?(linefollower_2.readSensors()&1):!(linefollower_2.readSensors()&1)))))){
        move(1,speed);
    }else{
        move(2,(speed) / (2));
        _delay(1);
        move(4,speed);
        _delay(0.6);
        move(1,0);
    }
    
}

void inputParse()
{
    if(se.equalString(se.readDataLine(),"stop")){
        mode = 0;
        move(1,0);
        _delay(0.5);
        if(((mode)==(0))){
            Serial.println(0);
        }else{
            Serial.println(1);
        }
    }
    
    if(se.equalString(se.readDataLine(),"auto")){
        move(1,0);
        mode = 1;
        _delay(0.5);
        if(((mode)==(1))){
            Serial.println(0);
        }else{
            Serial.println(1);
        }
    }
    
    if(se.equalString(se.readDataLine(),"man")){
        move(1,0);
        mode = 2;
        _delay(0.5);
        if(((mode)==(2))){
            Serial.println(0);
        }else{
            Serial.println(1);
        }
    }
    
    if(((mode)==(2))){
        if(se.equalString(se.readDataLine(),"0")){
            move(1,0);
        }
        if(se.equalString(se.readDataLine(),"w")){
            rgbled_7.setColor(0,0,0,ledLight);
            rgbled_7.show();
            move(1,100);
        }
        if(se.equalString(se.readDataLine(),"s")){
            rgbled_7.setColor(0,0,0,ledLight);
            rgbled_7.show();
            move(2,100);
        }
        if(se.equalString(se.readDataLine(),"a")){
            rgbled_7.setColor(0,0,0,ledLight);
            rgbled_7.show();
            move(3,75);
        }
        if(se.equalString(se.readDataLine(),"d")){
            rgbled_7.setColor(0,0,0,ledLight);
            rgbled_7.show();
            move(4,75);
        }
    }
    
}


void setup(){
    Serial.begin(115200);
    ledLight = 50;
    mode = 0;
    speed = 100;
    rgbled_7.setColor(0,ledLight,ledLight,ledLight);
    rgbled_7.show();
    _delay(1);
    
}

void loop(){
    
    if(se.dataLineAvailable()){
        inputParse();
    }
    if(((mode)==(0))){
        rgbled_7.setColor(0,ledLight,0,0);
        rgbled_7.show();
    }
    if(((mode)==(1))){
        rgbled_7.setColor(0,0,ledLight,0);
        rgbled_7.show();
        automaticDrive(speed);
    }
    if(((mode)==(2))){
        rgbled_7.setColor(0,0,0,ledLight);
        rgbled_7.show();
        manualMode(speed);
    }
    
    _loop();
}

void _delay(float seconds){
    long endTime = millis() + seconds * 1000;
    while(millis() < endTime)_loop();
}

void _loop(){
    
}

