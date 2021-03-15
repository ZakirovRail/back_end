# enc_str = 'Кодирование'
# enc_str_bytes = enc_str.encode('utf-8')
# print(enc_str_bytes)  # b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'

# =====================================================================================================================

# dec_str_bytes = b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'
# dec_str = dec_str_bytes.decode('utf-8')
# print(dec_str)  # Кодирование

# =====================================================================================================================
# my_str = 'Привет'
# print(my_str.encode('ascii'))
# =====================================================================================================================
my_str = 'Привет'
print(my_str)  # Привет
tmp = my_str.encode('utf-8')
print(tmp)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
err_tmp = tmp.decode('ascii')
print(err_tmp)  # UnicodeDecodeError: 'ascii' codec can't decode byte 0xd0 in position 0: ordinal not in range(128)
# =====================================================================================================================

 