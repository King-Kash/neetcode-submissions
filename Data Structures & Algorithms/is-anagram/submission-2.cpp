class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        hash<string> hash_fn;
        int shash = hash_fn(s);
        int thash = hash_fn(t);

        if (shash != thash){
            return false;
        }
        return true;
    }
};

//add up the asci value of the characters and it should come out as the same