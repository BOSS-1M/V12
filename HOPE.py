
# ملف تشغيل للوحدة المشفرة HOPE.cpython-312.so
import HOPE

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(HOPE, 'main'):
    HOPE.main()
else:
    print("تم استيراد HOPE بنجاح، ولكن لا توجد دالة main للتشغيل.")
