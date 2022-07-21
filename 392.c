bool isSubsequence(char * s, char * t){
    // using two pointers to check for substrings
    char * t_pointer = t;
    
    // iterating through the string using the pointer
    for (char * s_pointer = s ; *s != '\0' ; ) {
        
        if (*(s_pointer + 1) == '\0' 
        && *s_pointer == *t_pointer) {
            return true;
        }
        
        if (*t_pointer == '\0') {
            // if we reached the end of t_pointer, they aren't substrings
            return false;
        }
        
        // if the chars match, iterate both pointers
        if (*s_pointer == *t_pointer) {
            s_pointer++;
            t_pointer++;
        } else { // only iterate one pointer
            t_pointer++;
        }       
    }
    
    return true;
    
}