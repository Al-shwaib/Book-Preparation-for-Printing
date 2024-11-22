# معالج تحضير الكتب للطباعة | Book Preparation for Printing

<div dir="rtl">

[العربية](#العربية) | [English](#english)

# العربية

## نظرة عامة
هذا المشروع مخصص لتحضير الكتب والمجلات للطباعة على مطابع الأوفست. يقوم البرنامج بإعادة ترتيب صفحات PDF بطريقة تناسب الطباعة التجارية على ورق A3، مما يسمح بطباعة صفحتين من حجم A4 على كل وجه من الورقة.

![Project Interface](screenshot/img.png)

## المميزات الرئيسية
- دعم الكتب العربية (من اليمين إلى اليسار)
- دعم الكتب الإنجليزية (من اليسار إلى اليمين)
- دعم المجلات والمطبوعات المختلفة
- تحويل تلقائي من A4 إلى A3 للطباعة المزدوجة
- معالجة الصفحات الأفقية والعمودية بشكل تلقائي
- إضافة صفحات فارغة تلقائياً عند الحاجة
- واجهة ويب سهلة الاستخدام

## مميزات خاصة للطباعة التجارية
- ترتيب الصفحات بطريقة تناسب الطي والتجميع في المطبعة
- دعم الطباعة على وجهي الورقة (الطباعة المزدوجة)
- تحسين استغلال مساحة الورق لتقليل التكلفة
- تدوير تلقائي للصفحات الأفقية لضمان جودة الطباعة

## متطلبات النظام
- Python 3.7 أو أحدث
- متصفح ويب حديث
- مساحة تخزين كافية لمعالجة ملفات PDF

## التثبيت
1. قم بتنزيل المشروع أو نسخه:
```bash
git clone https://github.com/Al-shwaib/Book-Preparation-for-Printing.git
cd Book-Preparation-for-Printing
```

2. قم بتثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

## كيفية الاستخدام
1. قم بتشغيل البرنامج:
```bash
python app.py
```

2. افتح المتصفح وانتقل إلى:
```
http://localhost:5000
```

3. اختر نوع المستند:
   - كتاب عربي (من اليمين لليسار)
   - كتاب إنجليزي (من اليسار لليمين)
   - مجلة

4. ارفع ملف PDF المراد معالجته

5. انتظر حتى تكتمل المعالجة وقم بتحميل الملف الناتج

## إرشادات للمطابع
- الملف الناتج يكون بحجم A3 أفقي
- كل ورقة تحتوي على صفحتين من حجم A4
- ترتيب الصفحات يناسب الطباعة المزدوجة والتجميع
- يمكن طباعة الملف مباشرة على آلات الأوفست

## المساهمة في المشروع
نرحب بمساهماتكم! يرجى قراءة [دليل المساهمة](docs/CONTRIBUTING.md) للمزيد من المعلومات.

## الترخيص
هذا المشروع مرخص تحت [رخصة MIT](LICENSE).

## الدعم
إذا واجهتك أي مشكلة أو لديك اقتراح، يرجى فتح issue في صفحة المشروع على GitHub.

</div>

---

# English

[Arabic](#العربية) | [English](#english)

## Overview
This project is designed for preparing books and magazines for offset printing. The program rearranges PDF pages to suit commercial printing on A3 paper, allowing two A4 pages to be printed on each side of the sheet.

## Key Features
- Support for Arabic books (right-to-left)
- Support for English books (left-to-right)
- Magazine and various publication support
- Automatic A4 to A3 conversion for duplex printing
- Automatic handling of landscape and portrait pages
- Automatic blank page insertion when needed
- User-friendly web interface

## Special Features for Commercial Printing
- Page arrangement suitable for folding and binding in print shops
- Support for duplex printing (double-sided)
- Paper space optimization to reduce costs
- Automatic rotation of landscape pages for print quality

## System Requirements
- Python 3.7 or newer
- Modern web browser
- Sufficient storage space for PDF processing

## Installation
1. Download or clone the project:
```bash
git clone https://github.com/Al-shwaib/Book-Preparation-for-Printing.git
cd Book-Preparation-for-Printing
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## How to Use
1. Run the program:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Choose document type:
   - Arabic book (right-to-left)
   - English book (left-to-right)
   - Magazine

4. Upload the PDF file to be processed

5. Wait for processing to complete and download the resulting file

## Print Shop Guidelines
- Output file is in A3 landscape format
- Each sheet contains two A4 pages
- Page arrangement suits duplex printing and binding
- Files can be printed directly on offset machines

## Contributing
Contributions are welcome! Please read the [contribution guide](docs/CONTRIBUTING.md) for more information.

## License
This project is licensed under the [MIT License](LICENSE).

## Support
If you encounter any issues or have suggestions, please open an issue on the GitHub project page.
