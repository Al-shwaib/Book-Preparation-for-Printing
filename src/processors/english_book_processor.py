import fitz
import os

def create_blank_page(size=(595.27, 841.89)):  # A4 بالنقاط
    """إنشاء صفحة فارغة بحجم معين."""
    doc = fitz.open()
    doc.new_page(width=size[0], height=size[1])
    temp_file = "blank_page.pdf"
    doc.save(temp_file)
    doc.close()
    return temp_file

def rearrange_book_pages(input_pdf_path, output_pdf_path):
    input_pdf = fitz.open(input_pdf_path)
    num_pages = len(input_pdf)

    # تحقق من العدد الفردي وأضف صفحة فارغة إذا لزم الأمر
    if num_pages % 2 != 0:
        blank_page_path = create_blank_page()
        blank_pdf = fitz.open(blank_page_path)
        input_pdf.insert_pdf(blank_pdf)  # إضافة الصفحة الفارغة في آخر الملف
        blank_pdf.close()
        os.remove(blank_page_path)
        num_pages += 1  # تأكد من تحديث عدد الصفحات بعد إضافة الصفحة الفارغة

    # إعداد ملف الإخراج بحجم A3 أفقي
    output_pdf = fitz.open()
    a3_width, a3_height = 1190.55, 841.89  # A3 بالنقاط (أفقي)

    left_page = 0
    right_page = num_pages - 1

    while left_page < right_page:
        # إنشاء صفحة A3 فارغة
        new_page = output_pdf.new_page(width=a3_width, height=a3_height)

        # وضع الصفحة الفردية على اليسار
        if (left_page + 1) % 2 == 0:  # تحقق أن الصفحة زوجية
            if left_page < input_pdf.page_count:  # تأكد من وجود الصفحة
                left_rect = fitz.Rect(0, 0, a3_width / 2, a3_height)
                page = input_pdf.load_page(left_page)
                if page.get_text("text"):  # تحقق من وجود محتوى نصي في الصفحة
                    if page.rect.width > page.rect.height:
                        new_page.show_pdf_page(left_rect, input_pdf, left_page , rotate=90 )
                    else:
                         new_page.show_pdf_page(left_rect, input_pdf, left_page )
            if right_page < input_pdf.page_count:  # تأكد من وجود الصفحة
                right_rect = fitz.Rect(a3_width / 2, 0, a3_width, a3_height)
                page = input_pdf.load_page(right_page)
                if page.get_text("text"):  # تحقق من وجود محتوى نصي في الصفحة
                    if page.rect.width > page.rect.height:
                        new_page.show_pdf_page(right_rect, input_pdf, right_page, rotate=90)
                    else:
                        new_page.show_pdf_page(right_rect, input_pdf, right_page)
        else:  # وضع الصفحة الفردية على اليمين
            if right_page < input_pdf.page_count:  # تأكد من وجود الصفحة
                left_rect = fitz.Rect(0, 0, a3_width / 2, a3_height)
                page = input_pdf.load_page(right_page)
                if page.get_text("text"):  # تحقق من وجود محتوى نصي في الصفحة
                    if page.rect.width > page.rect.height:
                        new_page.show_pdf_page(left_rect, input_pdf, right_page, rotate=90)
                    else:
                        new_page.show_pdf_page(left_rect, input_pdf, right_page)

            if left_page < input_pdf.page_count:  # تأكد من وجود الصفحة
                right_rect = fitz.Rect(a3_width / 2, 0, a3_width, a3_height)
                page = input_pdf.load_page(left_page)
                if page.get_text("text"):  # تحقق من وجود محتوى نصي في الصفحة
                    if page.rect.width > page.rect.height:
                        new_page.show_pdf_page(right_rect, input_pdf, left_page, rotate=90)
                    else:
                        new_page.show_pdf_page(right_rect, input_pdf, left_page)

        left_page += 1
        right_page -= 1

    # حفظ الملف
    output_pdf.save(output_pdf_path)
    output_pdf.close()
    input_pdf.close()

def rearrange_book_pages_en(input_pdf_path, output_pdf_path):
    """
    إعادة ترتيب صفحات الكتاب الإنجليزي
    :param input_pdf_path: مسار ملف PDF المدخل
    :param output_pdf_path: مسار ملف PDF المخرج
    """
    try:
        print(f"معالجة الكتاب الإنجليزي: {input_pdf_path}")
        
        # فتح ملف PDF
        input_pdf = fitz.open(input_pdf_path)
        output_pdf = fitz.open()
        
        # الحصول على عدد الصفحات
        total_pages = input_pdf.page_count
        print(f"عدد الصفحات: {total_pages}")
        
        if total_pages == 0:
            raise Exception("الملف فارغ")
            
        # معالجة الصفحات للكتب الإنجليزية
        # نقوم بإضافة الصفحات بالترتيب المعتاد من اليسار إلى اليمين
        for page_num in range(total_pages):
            page = input_pdf[page_num]
            output_pdf.insert_pdf(input_pdf, from_page=page_num, to_page=page_num)
            print(f"إضافة صفحة {page_num + 1}")
        
        # حفظ الملف
        print(f"حفظ الملف في: {output_pdf_path}")
        output_pdf.save(output_pdf_path)
        
        # إغلاق الملفات
        input_pdf.close()
        output_pdf.close()
        
        print("تمت معالجة الكتاب الإنجليزي بنجاح")
        
    except Exception as e:
        print(f"حدث خطأ أثناء معالجة الكتاب الإنجليزي: {str(e)}")
        raise
