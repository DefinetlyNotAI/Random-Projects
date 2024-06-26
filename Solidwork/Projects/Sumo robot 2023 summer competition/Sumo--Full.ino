/*
   STEPS:
    Front IR = 10
    Right IR = 15
    Left IR = 20

    Right ML2 = 25
    Left ML2 = 30
    Back ML2 = 35
    Right & Left ML2 = 40
*/

#include <Ramp.h>

#define frontIR_step 10
#define rightIR_step 15
#define leftIR_step 20

#define rightML2_step 25
#define leftML2_step 30
#define backML2_step 35
#define rightLeftML2_step 40

ramp LM_R;  // Left motor R_PWM
ramp LM_L;  // Left motor L_PWM
ramp RM_R;  // Right motor R_PWM
ramp RM_L;  // Right motor L_PWM

// ========== 5 second delay ==========
int b_pin = 13;
bool delayed;

// ====================== WIP ======================
struct sensor {
  int mode; // 0 = digital; 1 = analog
  int pin;
  int reading;

  void initSensor() {
    if (mode == 0) {
      pinMode(pin, INPUT);
    }
  }

  void readSensor() {
    if (mode == 0) reading = digitalRead(pin);
    else reading = analogRead(pin);
  }
};

// ========== IR ==========
int IR_RIGHT = 2;
int IR_LEFT = 3;
int IR_FRONT = 4;
bool ir_right;
bool ir_left;
bool ir_front;

// ========== ML2 ==========
int ml2_right_p = 7;
int ml2_left_p = 8;
int ml2_back_p = 9;
bool ml2_right;
bool ml2_left;
bool ml2_back;

// ========== BTS ==========
int EN = 12;
int R_PWM = 11;
int L_PWM = 10;

int R_PWM2 = 5;
int L_PWM2 = 6;

unsigned long currentMillis;
unsigned long prevMillis;
int stepFlag;

void setup() {
  // Sensors
  pinMode(b_pin, INPUT_PULLUP);
  pinMode(ml2_right_p, INPUT);
  pinMode(ml2_left_p, INPUT);
  pinMode(ml2_back_p, INPUT);
  pinMode(IR_RIGHT, INPUT);
  pinMode(IR_LEFT, INPUT);
  pinMode(IR_FRONT, INPUT);

  // BTS
  pinMode(EN, OUTPUT);
  digitalWrite(EN, LOW);

  Serial.begin(9600);

  delay(1000);
  stepFlag = 1;
  digitalWrite(EN, HIGH);
  //LM_R.go(255, 5000);
  Serial.println("End of setup");
}

void loop() {
  Loop();
} // End of main loop

int mapSpeed(int _s) {
  byte s = map(_s, 0, 100, 0, 255);
  return s;
}

void Loop() {
  while (true) {
    currentMillis = millis();

    ml2_right = digitalRead(ml2_right_p);
    ml2_left = digitalRead(ml2_left_p);
    ml2_back = digitalRead(ml2_back_p);
    ir_right = digitalRead(IR_RIGHT);
    ir_left = digitalRead(IR_LEFT);
    ir_front = digitalRead(IR_FRONT);

    if (ir_front && stepFlag != frontIR_step) stepFlag = frontIR_step;
    else if (ir_right && stepFlag != rightIR_step) stepFlag = rightIR_step;
    else if (ir_left && stepFlag != leftIR_step) stepFlag = leftIR_step;

    if (ml2_right && ml2_left && stepFlag != rightLeftML2_step) stepFlag = rightLeftML2_step;
    else if (ml2_right && stepFlag != rightML2_step) stepFlag = rightML2_step;
    else if (ml2_left && stepFlag != leftML2_step) stepFlag = leftML2_step;
    else if (ml2_back && stepFlag != backML2_step) stepFlag = backML2_step;

    if (stepFlag == 1) {
      Serial.println("STEP 1");
      LM_R.go(mapSpeed(50), 1000);

      prevMillis = currentMillis;
      stepFlag = 2;
    }
    if (stepFlag == 2) {
      Forward(LM_R.update());

      prevMillis = currentMillis;
    }

    if (stepFlag == 10) { // Front IR
      Serial.println("STEP 10");
      LM_R.go(mapSpeed(100), 1000);

      prevMillis = currentMillis;
      stepFlag = 11;
    }
    if (stepFlag == 11) {
      Serial.println("STEP 11");
      Forward(LM_R.update());

      prevMillis = currentMillis;
    }

    if (stepFlag == 15) { // Right IR
      Serial.println("STEP 15");
      Right(50);

      prevMillis = currentMillis;
    }
    if (stepFlag == 20) { // Left IR
      Serial.println("STEP 20");
      Left(50);

      prevMillis = currentMillis;
    }

    if (stepFlag == 25) { // Right ML2
      Serial.println("STEP 25");
      Right(mapSpeed(25));

      prevMillis = currentMillis;
    }
    if (stepFlag == 30) { // Left ML2
      Serial.println("STEP 30");
      Left(mapSpeed(25));

      prevMillis = currentMillis;
    }
    if (stepFlag == 35) { // Back ML2
      Serial.println("STEP 30");

      prevMillis = currentMillis;
    }
    if (stepFlag == 40) {
      Serial.println("STEP 40");
      Backward(mapSpeed(50));

      prevMillis = currentMillis;
      stepFlag = 41;
    }
    if (stepFlag == 41 && currentMillis - prevMillis == 1000) {
      Serial.println("STEP 41");
      Right(mapSpeed(75));

      prevMillis = currentMillis;
    }

    if (stepFlag != 2) stepFlag = 1;
  }
}

void Forward(byte s) {
  analogWrite(R_PWM, s);
  analogWrite(L_PWM, 0);
  analogWrite(R_PWM2, s);
  analogWrite(L_PWM2, 0);
}

void Backward(byte s) {
  analogWrite(R_PWM, 0);
  analogWrite(L_PWM, s);
  analogWrite(R_PWM2, 0);
  analogWrite(L_PWM2, s);
}

void Right(byte s) {
  analogWrite(R_PWM, s);
  analogWrite(L_PWM, 0);
  analogWrite(R_PWM2, 0);
  analogWrite(L_PWM2, s);
}

void Left(byte s) {
  analogWrite(R_PWM, 0);
  analogWrite(L_PWM, s);
  analogWrite(R_PWM2, s);
  analogWrite(L_PWM2, 0);
}


// ====================== WIP ======================
bool wait(unsigned long duration) {
  duration += millis();

  if (millis <= duration) {
    return true;
  }
  else wait(duration - millis());
}
