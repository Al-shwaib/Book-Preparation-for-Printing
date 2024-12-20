from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os

def save_page_as_image(page_index, input_pdf_path, dpi=300, rotate=False):
    """تحويل صفحة PDF إلى صورة"""
    try:
        images = convert_from_path(input_pdf_path, first_page=page_index + 1, last_page=page_index + 1, dpi=dpi)
        img = images[0]
        if rotate:
            img = img.rotate(180, expand=True)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        img.save(temp_file.name, "JPEG", quality=100)
        return temp_file.name
    except Exception as e:
        print(f"خطأ في تحويل الصفحة {page_index + 1} إلى صورة: {str(e)}")
        raise

def cm_to_points(cm):
    """تحويل من سنتيمتر إلى نقاط"""
    return cm * 72 / 2.54

def rearrange_book_pages(input_pdf_path, output_pdf_path, dpi=300, page_width=48, page_height=33.5):
    """
    إعادة ترتيب صفحات المجلة للطباعة
    :param input_pdf_path: مسار ملف PDF المدخل
    :param output_pdf_path: مسار ملف PDF المخرج
    :param dpi: دقة الصور (نقطة في البوصة)
    :param page_width: عرض الصفحة بالسنتيمتر
    :param page_height: ارتفاع الصفحة بالسنتيمتر
    """
    try:
        print(f"معالجة ملف المجلة: {input_pdf_path}")
        
        # فتح ملف PDF
        reader = PdfReader(input_pdf_path)
        num_pages = len(reader.pages)
        print(f"عدد الصفحات: {num_pages}")
        
        if num_pages == 0:
            raise Exception("الملف فارغ")
            
        # تحويل المقاسات إلى نقاط
        page_width_points = cm_to_points(page_width)
        page_height_points = cm_to_points(page_height)
        
        # حساب أبعاد الصفحات الفرعية
        half_width = page_width_points / 2
        half_height = page_height_points / 2
        
        # إنشاء ملف PDF جديد
        c = canvas.Canvas(output_pdf_path, pagesize=(page_width_points, page_height_points))
        temp_files = []
        
        # معالجة الصفحات
        left_page = 0
        right_page = num_pages - 1
        
        while left_page < right_page:
            print(f"معالجة الصفحات: {left_page+1}, {left_page+2}, {right_page}, {right_page-1}")
            
            # تحويل الصفحات إلى صور
            img1 = save_page_as_image(left_page, input_pdf_path, dpi=dpi)
            img2 = save_page_as_image(left_page + 1, input_pdf_path, dpi=dpi, rotate=True)
            img3 = save_page_as_image(right_page - 1, input_pdf_path, dpi=dpi, rotate=True)
            img4 = save_page_as_image(right_page, input_pdf_path, dpi=dpi)
            
            # رسم الصور على الصفحة
            c.drawImage(img1, 0, 0, half_width, half_height)  # أسفل يسار
            c.drawImage(img2, 0, half_height, half_width, half_height)  # أعلى يسار
            c.drawImage(img3, half_width, half_height, half_width, half_height)  # أعلى يمين
            c.drawImage(img4, half_width, 0, half_width, half_height)  # أسفل يمين
            
            # تخزين الملفات المؤقتة للحذف لاحقاً
            temp_files.extend([img1, img2, img3, img4])
            
            # الانتقال إلى الصفحة التالية
            c.showPage()
            left_page += 2
            right_page -= 2
        
        # حفظ الملف
        print(f"حفظ الملف في: {output_pdf_path}")
        c.save()
        
        # حذف الملفات المؤقتة
        for temp_file in temp_files:
            os.remove(temp_file)
        
        print("تمت معالجة المجلة بنجاح")
        
    except Exception as e:
        print(f"حدث خطأ أثناء معالجة المجلة: {str(e)}")
        # حذف الملفات المؤقتة في حالة حدوث خطأ
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        raise