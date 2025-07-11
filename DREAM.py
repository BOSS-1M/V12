
# ملف تشغيل للوحدة المشفرة DREAM.cpython-312.so
import DREAM

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(DREAM, 'main'):
    DREAM.main()
else:
    print("تم استيراد DREAM بنجاح، ولكن لا توجد دالة main للتشغيل.")
