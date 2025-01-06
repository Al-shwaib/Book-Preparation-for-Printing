# المساهمة في مشروع تجهيز الكتب للطباعة
# Contributing to Book Preparation Project

نحن سعداء جداً باهتمامك في المساهمة في مشروع تجهيز الكتب للطباعة! هذا الدليل سيساعدك في عملية المساهمة.

We're really glad you're interested in contributing to the Book Preparation Project! This guide will help you through the contribution process.

## كيفية المساهمة (How to Contribute)

### 1. إعداد بيئة التطوير (Setting up the Development Environment)
1. قم بتثبيت Python 3.x
2. قم بعمل Fork للمشروع
3. قم بنسخ المشروع محلياً:
```bash
git clone https://github.com/Al-shwaib/book-preparation.git
cd book-preparation
```
4. قم بإضافة المستودع الأصلي كـ remote:
```bash
git remote add upstream https://github.com/ORIGINAL-OWNER/book-preparation.git
```
5. قم بتثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

### 2. إنشاء فرع جديد (Creating a Branch)
```bash
git checkout -b feature/YourFeatureName
```

### 3. معايير الكود (Code Standards)
- اتبع معايير PEP 8 لكود Python
- اكتب تعليقات توثيقية باللغتين العربية والإنجليزية
- استخدم أسماء وصفية للمتغيرات والدوال
- قم بتوثيق الدوال والكلاسات باستخدام docstrings

### 4. الاختبارات (Testing)
- تأكد من إضافة اختبارات لأي ميزة جديدة
- تأكد من نجاح جميع الاختبارات قبل تقديم Pull Request
- قم بتشغيل الاختبارات باستخدام:
```bash
python -m pytest tests/
```

### 5. تقديم التغييرات (Submitting Changes)
1. قم بعمل Commit للتغييرات:
```bash
git add .
git commit -m "وصف مختصر للتغييرات"
```
2. قم بدفع التغييرات:
```bash
git push origin feature/YourFeatureName
```
3. قم بإنشاء Pull Request على GitHub

### 6. مراجعة الكود (Code Review)
- سيتم مراجعة الكود من قبل المشرفين
- قد يُطلب منك إجراء تغييرات إضافية
- كن مستعداً للمناقشة والتعديل

## أنواع المساهمات (Types of Contributions)
- 🐛 إصلاح الأخطاء (Bug fixes)
- ✨ إضافة ميزات جديدة (New features)
- 📝 تحسين التوثيق (Documentation improvements)
- 🎨 تحسين واجهة المستخدم (UI improvements)
- ⚡ تحسين الأداء (Performance improvements)
- 🧪 إضافة اختبارات (Adding tests)

## إرشادات إضافية (Additional Guidelines)

### التزام Git (Git Commit Messages)
- استخدم صيغة المضارع: "يضيف ميزة" وليس "أضاف ميزة"
- اجعل الرسالة موجزة وواضحة
- استخدم Emoji للإشارة إلى نوع التغيير

### الإبلاغ عن الأخطاء (Bug Reports)
عند الإبلاغ عن خطأ، يرجى تضمين:
- وصف مفصل للمشكلة
- خطوات إعادة إنتاج الخطأ
- السلوك المتوقع والفعلي
- لقطات شاشة إن أمكن

### طلب ميزات (Feature Requests)
عند طلب ميزة جديدة، يرجى تضمين:
- وصف مفصل للميزة
- سبب الحاجة إليها
- أي تصميمات أو أفكار مقترحة

## الترخيص (License)
بالمساهمة في هذا المشروع، فإنك توافق على أن مساهماتك ستكون مرخصة تحت نفس [رخصة MIT](LICENSE).
