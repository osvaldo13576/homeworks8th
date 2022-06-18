#include "virtuabotixRTC.h"
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include "DHT.h"
#define DHTPIN 7
#define DHTTYPE DHT11
#include <SPI.h>
#include <SD.h>
File myFile;
LiquidCrystal_I2C lcd(0x27, 16, 2);  // I2C address 0x3F, 16 column and 2 rows
virtuabotixRTC myRTC(2, 3, 4); //The order here is DAT,CLK,RST. You can change this depending on the wiring
DHT dht(DHTPIN, DHTTYPE);

int light = 1;
int light_a;
int open_sd = 0;
int sd_c  = 0;
int sd_a;
char timeChar [8]; //number of digits for the format
uint8_t prevSeconds = 0; //

void setup()
{
  myRTC.setDS1302Time(00, 00, 00, 1, 1, 1, 2000);//
  pinMode(9, INPUT); 
  pinMode(8, INPUT); 
  dht.begin();     // initialize the sensor
  lcd.init();      // initialize the lcd
  lcd.backlight(); // open the backlight 
  ////////////////////////////////////
  Serial.begin(9600);
  while (!Serial) {
                  ; // wait for serial port to connect. Needed for native USB port only
                  }
if (!SD.begin(10)) {
    lcd.setCursor(0, 0);
    lcd.print("Error No SD");
    delay(500);
    lcd.clear();
    }else
    {
    lcd.setCursor(0, 0);
    lcd.print("SD CONNECTED");
    delay(500);
    lcd.clear();
      }
}

void loop()
{
  light_a = digitalRead(8);
  sd_a    = digitalRead(9);
  lcd.clear();
    float tempC = dht.readTemperature(); // read temperature
  //lcd.clear();
 myRTC.updateTime();
 lcd.setCursor(0, 1);
 lcd.print(myRTC.hours);
 lcd.print(":");
 lcd.print(myRTC.minutes);
 lcd.print(":");
 lcd.print(myRTC.seconds);
 lcd.setCursor(12, 1);
 lcd.print("IDLE");
  if (isnan(tempC)) {
    lcd.setCursor(0, 0);
    lcd.print("Temp: ");
    lcd.print(tempC);
  } else {
    lcd.setCursor(0, 0);  // start to print at the first row
    lcd.print("Temp: ");
    lcd.print(tempC);     // print the temperature
    lcd.print((char)223); // print ° character
    lcd.print("C");
  }
  if(light_a == 1){ 
    if(light == 1){
    lcd.noBacklight();light = 0;
                      }else{
    lcd.backlight();light = 1;                    
                        }
    }

    if(SD.begin(10) == 1){
      lcd.setCursor(14, 0);
      lcd.print("OK");
      }else{lcd.setCursor(14, 0);
      lcd.print("NO");}


if(sd_a == 1){
  if(open_sd == 0){open_sd = 1;}else{
      open_sd = 0;
      sd_c = 0;
      lcd.setCursor(9, 1);
      lcd.print(" SAVED!");
      myFile.close();        
      delay(1000);       
    }
  }
    
    if(open_sd == 1 && SD.begin(10) == 1){
     if(sd_c == 0){sd_c = 1;
      myFile = SD.open("temp.txt", FILE_WRITE);
         if (myFile) {
         myFile.println("'time', 'Temp'");
         myFile.print("'");
         myFile.print(myRTC.hours);
         myFile.print(":");
         myFile.print(myRTC.minutes);
         myFile.print(":");
         myFile.print(myRTC.seconds);
         myFile.print("', ");
         myFile.println(tempC);
         lcd.setCursor(9, 1);
         lcd.print("WRITING");
                 }
          
      }else{
        if (myFile) {
         myFile.print("'");
         myFile.print(myRTC.hours);
         myFile.print(":");
         myFile.print(myRTC.minutes);
         myFile.print(":");
         myFile.print(myRTC.seconds);
         myFile.print("', ");
         myFile.println(tempC);
         lcd.setCursor(9, 1);
         lcd.print("WRITING");
        }
        }
                      }
          
                        

  delay(2000); // wait a few seconds between measurements
}
