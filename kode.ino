

#include "pins_arduino.h" 

// MIDI
int note = 0x1E;
int velocity =127;  
int noteOn   = 144; 
int noteOff = 128;  
//deepest note
int note_start = 35;

int DEBUG=0; 

int sensitivity[18]={7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7};

int pinIsActive[18]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}; 



uint8_t readCapacitivePin(int pinToMeasure) {

  volatile uint8_t* port;
  volatile uint8_t* ddr;
  volatile uint8_t* pin;
 
  byte bitmask;
  port = portOutputRegister(digitalPinToPort(pinToMeasure));
  ddr = portModeRegister(digitalPinToPort(pinToMeasure));
  bitmask = digitalPinToBitMask(pinToMeasure);
  pin = portInputRegister(digitalPinToPort(pinToMeasure));
  
  *port &= ~(bitmask);
  *ddr  |= bitmask;
  delay(1);
  uint8_t SREG_old = SREG; 
  
  noInterrupts();

  *ddr &= ~(bitmask);
  *port |= bitmask;

  uint8_t cycles = 50;
           if (*pin & bitmask) { cycles =  0;}
  else if (*pin & bitmask) { cycles =  1;}
  else if (*pin & bitmask) { cycles =  2;}
  else if (*pin & bitmask) { cycles =  3;}
  else if (*pin & bitmask) { cycles =  4;}
  else if (*pin & bitmask) { cycles =  5;}
  else if (*pin & bitmask) { cycles =  6;}
  else if (*pin & bitmask) { cycles =  7;}
  else if (*pin & bitmask) { cycles =  8;}
  else if (*pin & bitmask) { cycles =  9;}
  else if (*pin & bitmask) { cycles = 10;}
  else if (*pin & bitmask) { cycles = 11;}
  else if (*pin & bitmask) { cycles = 12;}
  else if (*pin & bitmask) { cycles = 13;}
  else if (*pin & bitmask) { cycles = 14;}
  else if (*pin & bitmask) { cycles = 15;}
  else if (*pin & bitmask) { cycles = 16;}
  else if (*pin & bitmask) { cycles = 17;}
  else if (*pin & bitmask) { cycles = 18;}
  else if (*pin & bitmask) { cycles = 19;}
  else if (*pin & bitmask) { cycles = 20;}
  else if (*pin & bitmask) { cycles = 21;}
  else if (*pin & bitmask) { cycles = 22;}
  else if (*pin & bitmask) { cycles = 23;}
  else if (*pin & bitmask) { cycles = 24;}
  else if (*pin & bitmask) { cycles = 25;}
  else if (*pin & bitmask) { cycles = 26;}
  else if (*pin & bitmask) { cycles = 27;}
  else if (*pin & bitmask) { cycles = 28;}
  else if (*pin & bitmask) { cycles = 29;}
  else if (*pin & bitmask) { cycles = 30;}
  else if (*pin & bitmask) { cycles = 31;}
  else if (*pin & bitmask) { cycles = 32;}
  else if (*pin & bitmask) { cycles = 33;}
  else if (*pin & bitmask) { cycles = 34;}
  else if (*pin & bitmask) { cycles = 35;}
  else if (*pin & bitmask) { cycles = 36;}
  else if (*pin & bitmask) { cycles = 37;}
  else if (*pin & bitmask) { cycles = 38;}
  else if (*pin & bitmask) { cycles = 39;}
  else if (*pin & bitmask) { cycles = 40;}
  else if (*pin & bitmask) { cycles = 41;}
  else if (*pin & bitmask) { cycles = 42;}
  else if (*pin & bitmask) { cycles = 43;}
  else if (*pin & bitmask) { cycles = 44;}
  else if (*pin & bitmask) { cycles = 45;}
  else if (*pin & bitmask) { cycles = 46;}
  else if (*pin & bitmask) { cycles = 47;}
  else if (*pin & bitmask) { cycles = 48;}
  else if (*pin & bitmask) { cycles = 49;}
  
  SREG = SREG_old;
  
  *port &= ~(bitmask);
  *ddr  |= bitmask;

  return cycles;
}

void setup() {

 
  Serial.begin(115200);
}


void midiMessage(int cmd, int note, int velocity) {
  Serial.write(cmd);
  Serial.write(note);
  Serial.write(velocity);
}

void loop() {

  for(int i =0;i<=17;i++){
    uint8_t value= readCapacitivePin(i+2); 
    value = map(value, 0, 50, 0, 127);
    if(DEBUG){
        Serial.print(value);
        Serial.print('\t');
    }
      if(value  > sensitivity[i] and pinIsActive[i]==0){
         midiMessage(noteOn, i+(note_start), 127);
         pinIsActive[i]= 1;
         
    }
    else if(value <=sensitivity[i] and pinIsActive[i]==1){
       midiMessage(noteOff, i+(note_start), 127);
       pinIsActive[i]= 0;
      
    }
  }
  if(DEBUG){
    Serial.println();
   
  }
}

