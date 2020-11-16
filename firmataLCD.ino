#include <LiquidCrystal_I2C.h>
#include <Firmata.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
int lastLine = 1;

void stringDataCallback(char *stringData){
  char *temp;
  lcd.clear();
  if(strlen(stringData) > 16){
    temp = new char[16];
    strcpy(temp, stringData);
    lcd.print(temp);
    delete[] temp;
    temp = new char[strlen(stringData) - 16];
    strcpy (temp, stringData + 16);
    lcd.setCursor(0, 1);
    lcd.print(temp);
  }
  else lcd.print(stringData);
  
}

void setup() {
  lcd.begin();
  lcd.print("Uploaded.");
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
  Firmata.attach( STRING_DATA, stringDataCallback);
  Firmata.begin();  
}

void loop() {
  while ( Firmata.available() ) {
    Firmata.processInput();
  }
}
