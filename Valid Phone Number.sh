# Read from the file file.txt and output all valid phone numbers to stdout.

cat file.txt | grep -Eo '^(\([0-9]{3}\) ){1}[0-9]{3}-[0-9]{4}$|^([0-9]{3}-){2}[0-9]{4}$'
# -E用拓展正则 -o是only matching
# ^代表开始 $代表结束 [0-9]匹配0-9的数字  {3}匹配三个  \用于转义


