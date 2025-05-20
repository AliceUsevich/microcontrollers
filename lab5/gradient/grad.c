#include "grad.h"
#include "ili9341.h"


void create_gradient(uint8_t* buffer) 
{
    uint8_t color = 50;
    
    // uint8_t d = (SCREEN_WIDTH * SCREEN_HEIGHT - 1)/320;
    for (int y = 0; y < SCREEN_HEIGHT; y += (SCREEN_HEIGHT / 6)) 
    {
        for (int i = y * SCREEN_WIDTH * 2; i < (SCREEN_WIDTH * y * 2) + (SCREEN_HEIGHT / 6 * SCREEN_WIDTH * 2); i+=SCREEN_WIDTH * 2)
        {
            for (int j = 0; j < SCREEN_WIDTH* 2; j+=2)
            {
                buffer[i+j] = color;
                buffer[i+j+1] = color;
            }
        }
        color += 1;
    }
}