int main() {
    char username[50];
    char password[50];
    int success = 0;
    
    if (username[0] == 'u' && password[0] == 'p') {
        success = 1;
    } else {
        success = 0;
    }

    return success;
}
