from flask import Flask, render_template, request, send_file, flash, url_for, jsonify
import os
from werkzeug.utils import secure_filename
import traceback
import importlib.util
import sys
import time

# إضافة مسار المشروع إلى مسارات Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/output'

# Create directories if they don't exist
for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# قاموس لتخزين حالة التقدم لكل ملف
processing_status = {}

@app.route('/progress/<filename>')
def get_progress(filename):
    progress = processing_status.get(filename, 0)
    return jsonify({'progress': progress})

def update_progress(filename, progress):
    processing_status[filename] = progress

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_processor(module_name):
    """تحميل وحدة المعالجة الديناميكية"""
    try:
        # التحقق من وجود الملف
        module_path = os.path.join(os.path.dirname(__file__), "src", "processors", f"{module_name}.py")
        if not os.path.exists(module_path):
            raise Exception(f"ملف المعالجة غير موجود: {module_name}.py")

        # تحميل الوحدة ديناميكياً
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        # التحقق من وجود الدالة المطلوبة
        if not hasattr(module, 'rearrange_book_pages'):
            raise Exception(f"الدالة rearrange_book_pages غير موجودة في {module_name}.py")
        
        return module.rearrange_book_pages
    except Exception as e:
        print(f"خطأ في تحميل الوحدة {module_name}: {str(e)}")
        raise

def get_processor_module(file_type, sub_type):
    """تحديد ملف المعالجة المناسب بناءً على نوع الملف والخيارات"""
    if file_type == 'document':
        if sub_type == 'arabic':
            return 'arabic_book_processor'
        elif sub_type == 'english':
            return 'english_book_processor'
    elif file_type == 'magazine':
        if sub_type == 'printAndFlip':
            return 'Sort_magazine'
        elif sub_type == 'twoOperations':
            raise Exception("خيار 'عمليتين' غير متوفر حالياً")
    elif file_type == 'other':
        return 'ex_ar'  # استخدام المعالج الافتراضي
    
    raise Exception("نوع ملف غير معروف")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_path = None  
        try:
            if 'file' not in request.files:
                return {
                    'status': 'error',
                    'message': 'لم يتم اختيار ملف'
                }
            
            file = request.files['file']
            if file.filename == '':
                return {
                    'status': 'error',
                    'message': 'لم يتم اختيار ملف'
                }

            if file and allowed_file(file.filename):
                # الحصول على نوع الملف والخيارات
                file_type = request.form.get('fileType', 'document')
                sub_type = request.form.get('documentLanguage' if file_type == 'document' else 'magazineType', 'arabic')
                
                # تحديد وتحميل وحدة المعالجة المناسبة
                processor_module = get_processor_module(file_type, sub_type)
                process_function = load_processor(processor_module)
                
                filename = secure_filename(file.filename)
                input_path = os.path.join(UPLOAD_FOLDER, filename)
                output_filename = 'processed_' + filename
                output_path = os.path.join(OUTPUT_FOLDER, output_filename)
                
                # تأكد من وجود المجلدات
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                os.makedirs(OUTPUT_FOLDER, exist_ok=True)
                
                # حفظ الملف المرفوع
                file.save(input_path)
                
                print(f"معالجة الملف باستخدام: {processor_module}")
                print(f"نوع الملف: {file_type}")
                print(f"النوع الفرعي: {sub_type}")
                
                # تحديث التقدم للملف
                update_progress(filename, 10)  # بدء المعالجة
                
                # محاكاة خطوات المعالجة
                update_progress(filename, 30)  # قراءة الملف
                time.sleep(0.5)
                
                update_progress(filename, 60)  # معالجة الصفحات
                process_function(input_path, output_path)
                
                update_progress(filename, 90)  # حفظ الملف
                time.sleep(0.5)
                
                if not os.path.exists(output_path):
                    raise Exception("لم يتم إنشاء ملف المخرجات")
                
                update_progress(filename, 100)  # اكتمال المعالجة
                
                return {
                    'status': 'success',
                    'message': 'تمت معالجة الملف بنجاح',
                    'filename': output_filename,
                    'download_url': url_for('download_file', filename=output_filename)
                }
            else:
                return {
                    'status': 'error',
                    'message': 'يُسمح فقط بملفات PDF'
                }
        except Exception as e:
            print("حدث خطأ:")
            print(traceback.format_exc())
            return {
                'status': 'error',
                'message': str(e)
            }
        finally:
            # تنظيف ملف المدخلات
            if input_path and os.path.exists(input_path):
                os.remove(input_path)
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(OUTPUT_FOLDER, filename)
        if not os.path.exists(file_path):
            return "الملف غير موجود", 404
            
        if os.path.getsize(file_path) == 0:
            return "الملف فارغ", 404
            
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        print("خطأ في التحميل:")
        print(traceback.format_exc())
        return "حدث خطأ أثناء تحميل الملف", 500

if __name__ == '__main__':
    app.run(debug=True)
