#include <iostream>
#include <cstdlib>
#include <string>

const int NUM_OF_BUFFERS = 2;
const int BUFFER_LEN = 40;

char buffer[NUM_OF_BUFFERS][BUFFER_LEN + 1] = 
    {"", "jf843947hfjf48f9p3jw894f34wb34pufd"};

void advancedCaesarShift(char* str, int length, int shift);
const char* loadFlag();

int main(int argc, char* argv[]) {
    // Randomly change buffer value
    advancedCaesarShift(buffer[1], BUFFER_LEN, rand());
    
    // Write user input to buffer
    std::cout << "Please enter the password: ";
    std::cin >> buffer[0];
    
    // Null terminate strings
    buffer[0][BUFFER_LEN] = 0;
    buffer[1][BUFFER_LEN] = 0;
    
    // Check if the password matches the users input
    if (memcmp(buffer[0], buffer[1], BUFFER_LEN) == 0) {
        std::cout << "Flag: " << loadFlag() << std::endl;
    } else {
        std::cout << "Wrong password." << std::endl;
    }
}

const char* loadFlag() {
    if (memcmp(buffer[0], buffer[1], BUFFER_LEN) == 0) {
        static char FLAG[] = "ek`f~<fq`x~ubWXetQR~g`s>";
        advancedCaesarShift(FLAG, sizeof(FLAG), -31);
        return FLAG;
    }
    
    static const char ERROR_BAD_VALUES[] = "Wrong password";
    return ERROR_BAD_VALUES;
}

void advancedCaesarShift(char* str, int length, int shift) {
    static const char rangeMin = '!', rangeMax = '~';
    static const int range = (rangeMax - rangeMin + 1);

    if (shift < 0) shift = (shift % range) + range;
    
    for (; length > 0; length--, str++)
        if (rangeMin <= *str && rangeMax >= *str)
             *str = rangeMin + (shift + *str - rangeMin)  %
                     (rangeMax - rangeMin + 1);
                     
}