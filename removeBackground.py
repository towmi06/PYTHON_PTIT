import os
from rembg import remove
from PIL import Image

# Đường dẫn ảnh đầu vào
input_path = r"D:\downloaddd\UploadFromMobile\IMG_2199.jpeg"

# Đường dẫn ảnh đầu ra
output_path = r"D:\downloaddd\UploadFromMobile\output.png"

# Kiểm tra xem tệp đầu vào có tồn tại không
if not os.path.exists(input_path):
    print(f"File not found: {input_path}")
else:
    try:
        # Mở tệp đầu vào
        input = Image.open(input_path)
        
        # Xóa nền
        output = remove(input)
        
        # Lưu ảnh đã xử lý
        output.save(output_path)
        print(f"Image processed and saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
