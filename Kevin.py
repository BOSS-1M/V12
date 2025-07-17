
# ملف تشغيل للوحدة المشفرة Kevin.cpython-312.so
import Kevin

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(Kevin, 'main'):
    Kevin.main()
else:
    print("تم استيراد Kevin بنجاح، ولكن لا توجد دالة main للتشغيل.")
