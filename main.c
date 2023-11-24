#include <stdio.h>
#include <string.h>
#include <pico/stdlib.h>

const uint red_led1 = 27;
const uint red_led2 = 26;
const uint yellow_led1 = 18;
const uint yellow_led2 = 19;
const uint buzzer = 22;
const uint infrared_sensorForward = 16;
const uint infrared_sensorBackward = 28;
// motors sensors
const uint forward_input1 = 3;
const uint forward_input2 = 4;
const uint forward_input3 = 5;
const uint forward_input4 = 6;
const uint forward_enableA = 2;
const uint forward_enableB = 7;

const uint backward_input1 = 9;
const uint backward_input2 = 10;
const uint backward_input3 = 11;
const uint backward_input4 = 12;
const uint backward_enableA = 13;
const uint backward_enableB = 14;

void turnOffYellow();
void turnOffRed();

int main()
{

  // Initialize LED pin
  gpio_init(red_led1);
  gpio_set_dir(red_led1, GPIO_OUT);

  gpio_init(red_led2);
  gpio_set_dir(red_led2, GPIO_OUT);

  gpio_init(yellow_led1);
  gpio_set_dir(yellow_led1, GPIO_OUT);

  gpio_init(yellow_led2);
  gpio_set_dir(yellow_led2, GPIO_OUT);

  gpio_init(buzzer);
  gpio_set_dir(buzzer, GPIO_OUT);

  gpio_init(infrared_sensorForward);
  gpio_set_dir(infrared_sensorForward, GPIO_IN);

  gpio_init(infrared_sensorBackward);
  gpio_set_dir(infrared_sensorBackward, GPIO_IN);

  // motors sensors
  gpio_init(forward_input1);
  gpio_set_dir(forward_input1, GPIO_OUT);

  gpio_init(forward_input2);
  gpio_set_dir(forward_input2, GPIO_OUT);

  gpio_init(forward_input3);
  gpio_set_dir(forward_input3, GPIO_OUT);

  gpio_init(forward_input4);
  gpio_set_dir(forward_input4, GPIO_OUT);

  gpio_init(forward_enableA);
  gpio_set_dir(forward_enableA, GPIO_OUT);

  gpio_init(forward_enableB);
  gpio_set_dir(forward_enableB, GPIO_OUT);

  gpio_init(backward_input1);
  gpio_set_dir(backward_input1, GPIO_OUT);

  gpio_init(backward_input2);
  gpio_set_dir(backward_input2, GPIO_OUT);

  gpio_init(backward_input3);
  gpio_set_dir(backward_input3, GPIO_OUT);

  gpio_init(backward_input4);
  gpio_set_dir(backward_input4, GPIO_OUT);

  gpio_init(backward_enableA);
  gpio_set_dir(backward_enableA, GPIO_OUT);

  gpio_init(backward_enableB);
  gpio_set_dir(backward_enableB, GPIO_OUT);
  // Initialize chosen serial port
  stdio_init_all();

  char currentResponse[] = "000";
  char previousResponse[] = "111";
  // Loop forever
  while (true)
  {
    bool valueForward = gpio_get(infrared_sensorForward);

    bool valueBackward = gpio_get(infrared_sensorBackward);

    // Network response part

    //

    // STOP
    if (strcmp(currentResponse, "000") == 0)
    {

      if (valueBackward && strcmp(previousResponse, "010") == 0)
      {
        gpio_put(buzzer, false);
        strcpy(currentResponse, previousResponse);
      }

      if (valueForward && strcmp(previousResponse, "010") != 0 && strcmp(previousResponse, "000") != 0)
      {
        gpio_put(buzzer, false);
        strcpy(currentResponse, previousResponse);
      }

      gpio_put(red_led1, true);
      gpio_put(red_led2, true);

      turnOffYellow();

      gpio_put(forward_enableA, false);
      gpio_put(forward_enableB, false);
      gpio_put(forward_input1, false);
      gpio_put(forward_input2, false);
      gpio_put(forward_input3, false);
      gpio_put(forward_input4, false);

      gpio_put(backward_enableA, false);
      gpio_put(backward_enableB, false);
      gpio_put(backward_input1, false);
      gpio_put(backward_input2, false);
      gpio_put(backward_input3, false);
      gpio_put(backward_input4, false);
    }

    // moveForward
    if (strcmp(currentResponse, "001") == 0)
    {
      if (!valueForward)
      {
        gpio_put(buzzer, true);
        strcpy(previousResponse, currentResponse);
        strcpy(currentResponse, "000");
      }

      turnOffYellow();
      turnOffRed();

      gpio_put(forward_enableA, true);
      gpio_put(forward_enableB, true);
      gpio_put(forward_input1, true);
      gpio_put(forward_input2, false);
      gpio_put(forward_input3, false);
      gpio_put(forward_input4, true);

      gpio_put(backward_enableA, true);
      gpio_put(backward_enableB, true);
      gpio_put(backward_input1, true);
      gpio_put(backward_input2, false);
      gpio_put(backward_input3, false);
      gpio_put(backward_input4, true);
    }

    // MOVE BACKWARDS
    if (strcmp(currentResponse, "010") == 0)
    {
      if (!valueBackward)
      {
        gpio_put(buzzer, true);
        strcpy(previousResponse, currentResponse);
        strcpy(currentResponse, "000");
      }

      turnOffYellow();
      turnOffRed();

      gpio_put(forward_enableA, true);
      gpio_put(forward_enableB, true);
      gpio_put(forward_input1, false);
      gpio_put(forward_input2, true);
      gpio_put(forward_input3, true);
      gpio_put(forward_input4, false);

      gpio_put(backward_enableA, true);
      gpio_put(backward_enableB, true);
      gpio_put(backward_input1, false);
      gpio_put(backward_input2, true);
      gpio_put(backward_input3, true);
      gpio_put(backward_input4, false);
    }

    // Right
    if (strcmp(currentResponse, "011") == 0)
    {
      if (!valueForward)
      {
        gpio_put(buzzer, true);
        strcpy(previousResponse, currentResponse);
        strcpy(currentResponse, "000");
      }

      turnOffRed();

      gpio_put(yellow_led1, true);

      gpio_put(forward_enableA, true);
      gpio_put(forward_enableB, false);
      gpio_put(forward_input1, true);
      gpio_put(forward_input2, false);
      gpio_put(forward_input3, false);
      gpio_put(forward_input4, false);

      gpio_put(backward_enableA, false);
      gpio_put(backward_enableB, true);
      gpio_put(backward_input1, false);
      gpio_put(backward_input2, false);
      gpio_put(backward_input3, false);
      gpio_put(backward_input4, true);
    }

    // Left
    if (strcmp(currentResponse, "100") == 0)
    {
      if (!valueForward)
      {
        gpio_put(buzzer, true);
        strcpy(previousResponse, currentResponse);
        strcpy(currentResponse, "000");
      }

      turnOffRed();

      gpio_put(yellow_led2, true);

      gpio_put(forward_enableA, false);
      gpio_put(forward_enableB, true);
      gpio_put(forward_input1, false);
      gpio_put(forward_input2, false);
      gpio_put(forward_input3, false);
      gpio_put(forward_input4, true);

      gpio_put(backward_enableA, true);
      gpio_put(backward_enableB, false);
      gpio_put(backward_input1, true);
      gpio_put(backward_input2, false);
      gpio_put(backward_input3, false);
      gpio_put(backward_input4, false);
    }

    printf("Current response: %s\n", currentResponse);
  }
}

void turnOffYellow()
{
  gpio_put(yellow_led1, false);
  gpio_put(yellow_led2, false);
}

void turnOffRed()
{
  gpio_put(red_led1, false);
  gpio_put(red_led2, false);
}