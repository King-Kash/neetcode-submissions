class Solution {
public:
    bool isAnagram(string s, string t) {
        int slen = s.length();
        int tlen = t.length();
        if(slen != tlen){
            return false;
        }
        int sumS = 0;
        int sumT = 0;
        for(int i = 0; i < slen; i++){
            sumS += s[i];
            sumT += t[i];
        }
        if(sumS != sumT){
            return false;
        }
        return true;
    }
};

//add up the asci value of the characters and it should come out as the same