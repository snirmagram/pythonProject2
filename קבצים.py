#להביא קובץ מהמחשב
#file = open("c:/snir.txt")
#print(file.read())
#file.close()


#כמה בייטים (כל אות זה בייט) אנחנו רוצים מהקובץ
#file = open("c:/snir.txt")
#print(file.read(2))
#file.close()


#ה print השני ממשיך אחרי איפה שהוא נעצר
#file = open("c:/snir.txt")
#print(file.read(2))
#print(file.read())
#file.close()


#ה seek מתחיל לכתוב לפי המספר שרשום לו
#file = open("c:/snir.txt")
#print(file.read(2))
#file.seek(6)
#print(file.read())
#file.close()


#ה seek השני לוקח אותו לסוף
#file = open("c:/snir.txt")
#file.seek(0,2)
#length_of_file = file.tell()
#print("length_of_file:",length_of_file)
#file.seek(0)
#for i in range(0,length_of_file,3):
#    print(file.read(3))
#file.close()


#מדפיס לנו לפי שורות
#file = open("c:/snir.txt")
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#file.close()


#מדפיס רשימה של כל השורות
#file = open("c:/snir.txt")
#lines = file.read().splitlines()
#file.close()
#print(lines)


#פותח את המסמך לכתיבה (מוחק את כל מה שהיה שם לפני
#file = open("c:/snir1.txt" , "w")
#file.close()


#איך לכתוב בקובץ
#file = open("c:/snir1.txt" , "w")
#file.write("test write to file")
#file.close()


#איך להדפיס עוד שורות (לא לשכוח להוסיף n\ כדי שזה ירד שורה)
#file = open("c:/snir1.txt" , "w")
#file.write("test write to file\n")
#file.write("more writing to file\n")
#file.write("more\n")
#file.close()


#עוד צורה להדפיס (יותר מהירה)
#f = open("c:/snir1.txt" , "w")
#print("WOW PRINT TO FILE?!?!?", file=f)
#print("WOW PRINT TO FILE?!?!?", file=f)
#print("WOW PRINT TO FILE?!?!?", file=f)
#f.close()


#כדי להוסיף שורות ולא למחוק ולעשות מההתחלה
f = open("c:/snir1.txt" , "a")
print("tets append print to file", file=f)
f.close()
