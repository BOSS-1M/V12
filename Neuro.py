
# ملف تشغيل للوحدة المشفرة Neuro.cpython-312.so
import Neuro

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(Neuro, 'main'):
    Neuro.main()
else:
    print("تم استيراد Neuro بنجاح، ولكن لا توجد دالة main للتشغيل.")
