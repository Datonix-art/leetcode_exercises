bool isPalindrome(int x) {
    if(x < 0) return false;
    
    int length = 0;
    int cp_x = x;

    do {
        cp_x /= 10;
        length++;
    } while(cp_x!=0);

    int remainders[length];

    cp_x = x;
 
    for(int i = 0; i < length; i++) {
        remainders[i] = cp_x % 10;
        cp_x /= 10;
    }

    for(int i = 0; i < length; i++) {
        if(remainders[i] != remainders[length - i - 1]) {
            return false;
        }
    }

    return true;
}
