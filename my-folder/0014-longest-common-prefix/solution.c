char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";

    int min_str_len = strlen(strs[0]);

    // Find the shortest string
    for (int i = 1; i < strsSize; i++) {
        if (strlen(strs[i]) < min_str_len) {
            min_str_len = strlen(strs[i]);
        }
    }

    char* prefix = malloc(min_str_len + 1);
    int k = 0;

    for (int j = 0; j < min_str_len; j++) {
        for (int i = 1; i < strsSize; i++) {
            if (strs[i][j] != strs[0][j]) {
                prefix[k] = '\0';
                return prefix;
            }
        }

        prefix[k++] = strs[0][j];
    }

    prefix[k] = '\0';

    return prefix;
}
