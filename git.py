# #1-misol
# def soz_uzun_texts(fayl_path):
#     try:
#         with open(fayl_path, 'r', encoding='utf-8') as f:
#             text = f.read()
#         sozlar = text.split()
        
        
#         soz_len = len(sozlar)
        
#         return soz_len
#     except FileNotFoundError:
#         return "Fayl topilmadi."
#     except Exception as e:
#         return f"Xatolik yuz berdi: {e}"


# fayl_path = 'shokirov.txt'  
# soz_count = soz_uzun_texts(fayl_path)
# print(f" so'zlar soni: {soz_count}")


# #2-misol
# def soz_uzun_texts(fayl_path):
#     try:
#         with open(fayl_path, 'r', encoding='utf-8') as f:
#             text = f.read()
#         sozlar = text.split()
        
#         if sozlar:
#             longest_word = max(sozlar, key=len)
#         else:
#             longest_word = ""

#         return longest_word
#     except FileNotFoundError:
#         return "Fayl topilmadi."
#     except Exception as e:
#         return f"Xatolik yuz berdi: {e}"

# fayl_path = 'shokirov.txt'  
# soz_count = soz_uzun_texts(fayl_path)
# print(f"katta so'z: {soz_count}")


#3-misol:
# def raqam (sonlar:list):
#     for i in range(len(sonlar)-1) :
#         if sonlar[i]<sonlar[i+1]:
#          ...
#         else :
#            return f" shu sondan boshlab o'zgarish:{(sonlar[i+1])}"



# sonlar = [1,2,3,4,5,6,7,4,9,10]

# print(raqam(sonlar))


#4-miso
# malumot=['salom','alik',  'axliddin@gmail.com',20,'asliddin@gmail.com',"shokirov@gmail.com",'malumot']
# def saralsh(malumot:list):
#     maluts=[]
#     for i in range(len(malumot)):
#        sham=malumot[i]
#        if isinstance(malumot[i], str):
#          if  sham[-10:]=='@gmail.com':
#             maluts.append(malumot[i])
#     return maluts        
# print(saralsh(malumot))