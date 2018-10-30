#include <unistd.h>
#include <iostream>
#include <string>

const char PASSWORD[] = "Secret_Password_123";
char FLAG[] = "W]RXp.XcRjphjIIBhDiWHpYRe0";

void caesarShift(char* str, int length, int shift) {
    static const char rangeMin = '!', rangeMax = '~';
    static const int range = (rangeMax - rangeMin + 1);

    if (shift < 0) shift = (shift % range) + range;
    
    for (; length > 0; length--, str++)
        if (rangeMin <= *str && rangeMax >= *str)
             *str = rangeMin + (shift + *str - rangeMin)  %
                     (rangeMax - rangeMin + 1);
                     
}


int main()
{
    std::cout << "Please Enter The Password: ";
    std::string userInput;
    std::cin >> userInput;
    
    for (int i = 0; i < 10; i++) {
        std::cout << ".";
        sleep(0.5f);
    }
    std::cout << std::endl;
    
    if (userInput == std::string(PASSWORD)) {
        caesarShift(FLAG, sizeof(FLAG), -17);
        std::cout << "The Flag Is: " << FLAG << std::endl;
    } else {
        std::cout << "Wrong password" << std::endl;
    }
}
