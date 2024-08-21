## Yesterday - 2024-08-20

* collections module
* Purpose of collections
* Available types & uses
* Exercies

## Today - 2024-08-21

* Regex introduction
* Regex pattern and sequences
* Regex in Python (re module)
* Exercises


### Regular Expressions (Regex)

---

#### **Basic Syntax**

| Pattern  | Description                                      | Example            | Matches                          |
|----------|--------------------------------------------------|--------------------|----------------------------------|
| `.`      | Any single character except newline              | `c.t`              | cat, cot, cut                    |
| `\d`     | Any digit (0-9)                                  | `\d\d`             | 12, 99                           |
| `\D`     | Any non-digit                                    | `\D\D\D`           | abc, XYZ                         |
| `\w`     | Any word character (alphanumeric + underscore)   | `\w\w\w`           | cat, 123, _a1                    |
| `\W`     | Any non-word character                           | `\W\W\W`           | #$%, ^&*                         |
| `\s`     | Any whitespace character                         | `\s\s`             | (space)(tab), (tab)(tab)         |
| `\S`     | Any non-whitespace character                     | `\S\S\S`           | abc, a1!, XYZ                    |

---

#### **Anchors**

| Pattern  | Description                                      | Example            | Matches                          |
|----------|--------------------------------------------------|--------------------|----------------------------------|
| `^`      | Start of a string                                | `^Hello`           | Hello world, Hello there         |
| `$`      | End of a string                                  | `world$`           | Hello world, Goodbye world       |
| `\b`     | Word boundary                                    | `\bcat\b`          | cat (as a whole word)            |
| `\B`     | Non-word boundary                                | `\Bcat\B`          | category, scat                   |

---

#### **Character Classes**

| Pattern  | Description                                      | Example            | Matches                          |
|----------|--------------------------------------------------|--------------------|----------------------------------|
| `[abc]`  | Any one of the characters a, b, or c             | `[aeiou]`          | a, e, i, o, u                    |
| `[^abc]` | Any character except a, b, or c                  | `[^0-9]`           | Any non-digit                    |
| `[a-z]`  | Any character in the range a-z                   | `[A-Z]`            | A, B, ... Z                      |
| `[0-9]`  | Any digit from 0 to 9                            | `[0-5]`            | 0, 1, 2, 3, 4, 5                 |

---

#### **Quantifiers**

| Pattern    | Description                                          | Example           | Matches                                      |
|------------|------------------------------------------------------|-------------------|----------------------------------------------|
| `*`        | 0 or more of the preceding element                   | `ca*t`            | ct, cat, caat, caaat                         |
| `+`        | 1 or more of the preceding element                   | `ca+t`            | cat, caat, caaat                             |
| `?`        | 0 or 1 of the preceding element                      | `ca?t`            | ct, cat                                      |
| `{n}`      | Exactly `n` occurrences                              | `a{3}`            | aaa                                          |
| `{n,}`     | `n` or more occurrences                              | `a{2,}`           | aa, aaa, aaaa                                |
| `{n,m}`    | Between `n` and `m` occurrences                      | `a{2,4}`          | aa, aaa, aaaa                                |

---

#### **Groups and Capturing**

| Pattern  | Description                                      | Example            | Matches                          |
|----------|--------------------------------------------------|--------------------|----------------------------------|
| `(abc)`  | Capturing group for abc                          | `(abc)\1`          | abcabc                          |
| `(?:abc)`| Non-capturing group for abc                      | `(?:abc)+`         | abc, abcabc                      |
| `(?<name>abc)`| Named capturing group for abc              | `(?<year>\d{4})`   | 2023 (stored as "year")          |

---

#### **Alternation and Conditional**

| Pattern  | Description                                      | Example            | Matches                          |
|----------|--------------------------------------------------|--------------------|----------------------------------|
| `a\|b`   | Matches either a or b                            | `cat\|dog`         | cat, dog                         |
| `(?=abc)`| Positive lookahead for abc                       | `(?=dog)doghouse`  | dog in doghouse                  |
| `(?!abc)`| Negative lookahead for abc                       | `(?!dog)house`     | house, not doghouse              |
| `(?<=abc)`| Positive lookbehind for abc                     | `(?<=\$)\d+`       | 100 (in $100)                    |
| `(?<!abc)`| Negative lookbehind for abc                     | `(?<!\$)\d+`       | 123 (but not $123)               |

---

#### **Escaping Special Characters**

- Special characters (e.g., `.`, `\`, `+`, `*`, etc.) can be escaped with a backslash (`\`).
  - Example: To match a literal dot `.` use `\.`

---

#### **Flags**

- `i` : Case-insensitive matching (e.g., `/cat/i` matches "Cat" or "cat").
- `g` : Global search (matches all occurrences, not just the first).
- `m` : Multiline matching (anchors `^` and `$` match start/end of lines).

---
