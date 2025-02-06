The program is checking password hashes extracted from 
websites using SQL injection for example and then comparing
against known the most common password list in the file
passwordlist.txt. There are implemented md5 and sha1 atm.


for the testing purposes pick any pass from passwordlist
and then go online to hash it in one of the formats and 
run it, so the script will find the right password after
decrypting it