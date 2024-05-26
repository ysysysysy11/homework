def count_character(s,  char):

    count = 0
    for c in s:
        if c == char:
            count += 1
    return count



s = "yang shi"
char = "y"
count = count_character(s, char)
print(f"字符 '{char}' 在字符串中出现了 {count} 次。")