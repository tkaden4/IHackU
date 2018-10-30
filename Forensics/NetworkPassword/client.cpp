#include <netdb.h>          /* gethostbyname, struct hostent */
#include <arpa/inet.h>      /* inet_ntoa, inet_addr */
#include <cstring>          /* bzero */
#include <unistd.h>         /* read, write, close */
#include <sys/time.h>       /* struct timeval, gettimeofday */
#include <iostream>
#include <string>

extern int errno;

const int ON = 1;
const int ERROR_SEND = 1;
const int ERROR_CONNECT = 1;
const int ERROR_SOCK_CREATE = 2;
const int BUFFER_LEN = 100;
char FLAG[] = "Y_TZr0ZeTlr]FKDEkr[Tg2";

/**
 * @param 1     Server name as null terminated string.
 * @param 2     Port as 16 bit integer.
 * @param 3     Output buffer where data is writen to.
 */
int pullFromClient(const char* server_name, uint16_t server_port, char* buffer, int bufferLen) {
    // Check if address exists and convert it to Internet host address in network byte order
    struct hostent* host = gethostbyname( server_name );
    
    // Puts the socket family, ip address, and port together.
    sockaddr_in sendSockAddr;
    bzero( (char*)&sendSockAddr, sizeof( sendSockAddr ) );
    sendSockAddr.sin_family = AF_INET; // Address Family Internet
    sendSockAddr.sin_addr.s_addr =
        inet_addr( inet_ntoa( *(struct in_addr*)*host->h_addr_list ) );
    sendSockAddr.sin_port = htons( server_port );
    
    // Create a TCP socket and open a connection.
    int clientSd = -1;

    if ( ( clientSd = socket( AF_INET, SOCK_STREAM, 0 ) ) < 0 ) {
        std::cout << "Error Creating Socket: "  << errno << std::endl;
        exit( ERROR_SOCK_CREATE );
    }
    
    if ( connect( clientSd, (sockaddr*)&sendSockAddr, sizeof( sendSockAddr ) ) != 0 ) {
        std::cout << "Error Connecting to Server: " << errno << std::endl;
        exit( ERROR_CONNECT );
    }
    
    // Ger server acknowledgment
    int bytesRead = -1;
    if ( ( bytesRead = read( clientSd, buffer, bufferLen ) ) <= 0 ) {
        std::cout << "Error Reading: " << errno << std::endl;
        exit( ERROR_CONNECT );
    }
    
    close( clientSd );
    
    return bytesRead;
}

void caesarShift(char* str, int length, int shift) {
    static const char rangeMin = '!', rangeMax = '~';
    static const int range = (rangeMax - rangeMin + 1);

    if (shift < 0) shift = (shift % range) + range;
    
    for (; length > 0; length--, str++)
        if (rangeMin <= *str && rangeMax >= *str)
             *str = rangeMin + (shift + *str - rangeMin)  %
                     (rangeMax - rangeMin + 1);
                     
}

int main(int argc, char* argv[]) {
    // The two supplied cmd arguments.
    uint16_t remotePort = (uint16_t) 13412;
    char remoteAddress[] = "127.0.0.1"; //"107.170.192.50";
    char buffer[BUFFER_LEN];
    
    std::cout << "Please Enter The Password: ";
    std::string userInput;
    std::cin >> userInput;
    
    for (int i = 0; i < 10; i++) {
        std::cout << ".";
        sleep(0.5f);
    }
    std::cout << std::endl;
    
    int readLen = pullFromClient(remoteAddress, remotePort, buffer, BUFFER_LEN);
    buffer[readLen] = 0;
    
    if (userInput == std::string(buffer)) {
        caesarShift(FLAG, sizeof(FLAG), -19);
        std::cout << "The Flag Is: " << FLAG << std::endl;
    } else {
        std::cout << "Wrong password" << std::endl;
    }
}
