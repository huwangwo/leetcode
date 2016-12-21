# Read from the file file.txt and output the tenth line to stdout.
awk 'NR==10 {print}' file.txt


#Solution One:
head -n 10 file.txt | tail -n +10

#Solution Two:
awk 'NR==10' file.txt

#Solution Three:
sed -n 10p file.txt