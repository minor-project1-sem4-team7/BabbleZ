# # Temporary Program to check programs and their working
# # Security
# import Security
#
# cls = Security
#
# # print('Private Key : ', cls.get_private_key())
#
# pvmsg = 'Hello This is a secret message'
# enc_msg = cls.personal_encrypt(pvmsg)
# dec_msg = cls.personal_decrypt(enc_msg)
#
#
# if pvmsg == dec_msg:
#     print('[+] Independent RSA Encryption successful')
# else:
#     print('[*] private enc msg :', enc_msg)
#     print('[*] private dec msg :', dec_msg)
#     print('[-] Failed RSA Encryption')
#
#
# apmsg = 'This is my app password $uperst0ng'
# app_enc = cls.app_encrypt(apmsg)
# app_dec = cls.app_decrypt(app_enc)
#
#
# if app_dec == apmsg:
#     print('[+] Independent APP Encryption successful')
# else:
#     print('[*] App Enc msg :', app_enc)
#     print('[*] App Dec msg :', app_dec)
#     print('[-] Failed App Encryption')
#
# # combined Encryption
#
# my_msg = text = 'Hello This is my Private secret Message - hey Devil You There ? \n' \
#                 'We are going to Attack on Cyber castle or Hero Emilia at Night of Dark Monday\n' \
#                 'Be ready ! You are our main protagonist in this attack.\n' \
#                 'Message For Dark Lord Arnav 😈'
#
#
# def zebrish(text):
#     drop = list()
#     secure = Security
#
#     encrypted_msg = secure.personal_encrypt(text)
#     drop.append(encrypted_msg)
#
#     metadata = 'This Is app Meta Data , Encrypted by App Encryption'
#
#     secure_meta = secure.app_encrypt(metadata)
#     drop.append(secure_meta)                            # Send over network
#
#     received_metadata = secure.app_decrypt(drop[1])
#     original_msg = secure.personal_decrypt(drop[0])
#
#     if text == original_msg and metadata == received_metadata :
#         print('[+] Combined Test Successfully Passed')
#         # print('Received Private message',original_msg)
#         # print('Received App message',received_metadata)
#     else:
#         print('[-] Something went wrong')
#         print('[*] Plain Message : ', text)
#         print('[*] Private encrypted Message : ', encrypted_msg)
#         print('[*] App Message : ', metadata)
#         print('[*] App encrypted Message : ', secure_meta)
#         print('[*] App decrypted Message : ', received_metadata)
#         print('[*] Private decrypted Message : ', original_msg)
#         print('[-] Test Failed')
#
# zebrish(my_msg)

#
# if __name__ == '__main__':
#     recPK = b'\x10\xf6\xf92\x17=\x00\x01\x94\xfd\xf8=c\xb15i\xac8lI\xb2=\x8e\xbe\xff\xfb2\xb8i7\x96\xb2=\xf0\t\x9d\x95zl\xc9B>s_\xd6/\xe3Sa\xee\xd1\xe1\x040\xd0\x056\xb0\xb17\xf9\xe3\xd7\x1cZC\x04\xcc|\xd8\xca\x9e;j\x82\x8e7\x16*Yo\x9c \x8e\x8bC[I\xea\x18\xc2Z\x81\xff\xac\x07\xb9g\xa4\x9f\xf0j\xf6Il4\xf8yebFuEdD\x9b-\x0c\x9d\xb9\x91\r\x91\xd4\xecF\x8c\xa1\xe3F\x86\xef\xbex\xb8\x94f\x98\xd6\x93\x99T\xd0\x85\x83\x8b\xf84\xfb\xe2\t\xa1\xde\x08\xf1\xee\xe7`\x93\xc9FRr;\xe9%\xe3G\x1a7\xb0\x1f7n\x95\x89/N\x0eaQ&\xeeGK\x16Z\xd7\xc6)\xc23\xad\x9f:\x99\xc9`\xbd\\\x15>,\xb1;qb\xb4E\x0cYC\xe6\x02\x07\xa7\xc8\x92\xef\xeb\xb2\x18\xe6\x19o\xdb\xc2\xec\xc3\x90.\x03\xffcEx\xac\\\x1e\xb1\xd2\xab\x9awr\xec\xff:\xb9\xdb\xd2\x0e\x04\xd5\x93\x02'
#     senPK = b'\x10\xf6\xf92\x17=\x00\x01\x94\xfd\xf8=c\xb15i\xac8lI\xb2=\x8e\xbe\xff\xfb2\xb8i7\x96\xb2=\xf0\t\x9d\x95zl\xc9B>s_\xd6/\xe3Sa\xee\xd1\xe1\x040\xd0\x056\xb0\xb17\xf9\xe3\xd7\x1cZC\x04\xcc|\xd8\xca\x9e;j\x82\x8e7\x16*Yo\x9c \x8e\x8bC[I\xea\x18\xc2Z\x81\xff\xac\x07\xb9g\xa4\x9f\xf0j\xf6Il4\xf8yebFuEdD\x9b-\x0c\x9d\xb9\x91\r\x91\xd4\xecF\x8c\xa1\xe3F\x86\xef\xbex\xb8\x94f\x98\xd6\x93\x99T\xd0\x85\x83\x8b\xf84\xfb\xe2\t\xa1\xde\x08\xf1\xee\xe7`\x93\xc9FRr;\xe9%\xe3G\x1a7\xb0\x1f7n\x95\x89/N\x0eaQ&\xeeGK\x16Z\xd7\xc6)\xc23\xad\x9f:\x99\xc9`\xbd\\\x15>,\xb1;qb\xb4E\x0cYC\xe6\x02\x07\xa7\xc8\x92\xef\xeb\xb2\x18\xe6\x19o\xdb\xc2\xec\xc3\x90.\x03\xffcEx\xac\\\x1e\xb1\xd2\xab\x9awr\xec\xff:\xb9\xdb\xd2\x0e\x04\xd5\x93\x02'
#
#     recMeta = [b'gAAAAABgaIv60qAtsPF0uySqTBvVTrhgcvl1D4esvIze8eL-N_3j7p9NGfGdDn30OFckhEZaZmDd6ZohXiZIt2QQsj7UcxxMUQ==', b'gAAAAABgaIv6CZOVrXwD3f7UOkPUboPznSq-ZfYHqQOfsL0aI_uhYPwgEthBJONdOTqnD61kkemNO_gAkYWsbevd83JNFqQpDw==', b'gAAAAABgaIv6Iw28Gl5FFp1DNtjEcnTHCL_3HZJ2ynU_suo3OQVDgK36VF5Aq_sOYY0D1guYJudIowerdh8nqwt-v8jl1QZshHU3KiZWA_oFpxw2zJLXW5s=']
#     senMeta = [b'gAAAAABgaIv60qAtsPF0uySqTBvVTrhgcvl1D4esvIze8eL-N_3j7p9NGfGdDn30OFckhEZaZmDd6ZohXiZIt2QQsj7UcxxMUQ==', b'gAAAAABgaIv6CZOVrXwD3f7UOkPUboPznSq-ZfYHqQOfsL0aI_uhYPwgEthBJONdOTqnD61kkemNO_gAkYWsbevd83JNFqQpDw==', b'gAAAAABgaIv6Iw28Gl5FFp1DNtjEcnTHCL_3HZJ2ynU_suo3OQVDgK36VF5Aq_sOYY0D1guYJudIowerdh8nqwt-v8jl1QZshHU3KiZWA_oFpxw2zJLXW5s=']
#
#     if recPK == senPK:
#         print(True)
import rsa

if __name__ == '__main__':
    pub_key, priv = rsa.newkeys(4096)

    print(pub_key)
    print()
    print()
    print()
    print()
    print(priv)