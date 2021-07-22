class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        # 0xff => 11 11 11 11 => 1 byte
      # & with 1111 1111 will make the new bits 8 bit long with only rightmost 8 bits
        print(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]

        char = [(x >> (i * 8) & 0xff) for i in range(4)]
        print(char)
        print(bytes)
        bytes.reverse()
        print(bytes)
        bytes_str = ''.join(bytes)
        print(bytes_str)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output

strs = ["hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohello", "world"]
codec = Codec()
print(codec.decode(codec.encode(strs)))
# print(codec.len_to_str(strs[0]))