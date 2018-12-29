var Blynk = require("blynk-library");

var sense = require("node-sense-hat");

var AUTH = '21f9b3bfc78f4fb2beb46bee5d840d09';

//assigning varible to blynk object to include the auth key
var blynk = new Blynk.Blynk(AUTH);

//Assigning varible as I will be using virtual pin v1
var v1 = new blynk.VirtualPin(1);

//Assigning colour variable which will be used to iluminate sensehat led's
var green = [0, 255, 0];

//function to clear led's on sensehat
sense.Leds.clear();

// v1 write call back function
// Once the button is in an on state
// the sense hat will illuminate green
v1.on('write', function(param) {
  console.log('V1:', param[0]);
  //If equal to one, which is the onstate, clear the sense hat to green
  //Else clear the sense hat
  if (param[0]==1){
        sense.Leds.clear(green)
    }else{
        sense.Leds.clear();
    }
});
