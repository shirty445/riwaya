import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ('Search بحث', '<span class="lang-texten">Search</span><span class="lang-textar" style="display:none">بحث</span>'),
    ('Sources المصادر', '<span class="lang-texten">Sources</span><span class="lang-textar" style="display:none">المصادر</span>'),
    ('Sanad Pattern قالب إسناد', '<span class="lang-texten">Sanad Pattern</span><span class="lang-textar" style="display:none">قالب إسناد</span>'),
    ('Hadith Query عبارة البحث', '<span class="lang-texten">Hadith Query</span><span class="lang-textar" style="display:none">عبارة البحث</span>'),
    ('Submit بحث', '<span class="lang-texten">Submit</span><span class="lang-textar" style="display:none">بحث</span>'),
    ('Draw رسم', '<span class="lang-texten">Draw</span><span class="lang-textar" style="display:none">رسم</span>'),
    ('Settings إعدادات', '<span class="lang-texten">Settings</span><span class="lang-textar" style="display:none">إعدادات</span>'),
    ('Custom Data البيانات', '<span class="lang-texten">Custom Data</span><span class="lang-textar" style="display:none">البيانات</span>'),
    ('Links Coloring تغيير العرض', '<span class="lang-texten">Links Coloring</span><span class="lang-textar" style="display:none">تغيير العرض</span>'),
    ('Group by Matn — تمييز المتون بالألوان', '<span class="lang-texten">Group by Matn</span><span class="lang-textar" style="display:none">تمييز المتون بالألوان</span>'),
    ('Group by Sanad — تمييز الأسانيد بالألوان', '<span class="lang-texten">Group by Sanad</span><span class="lang-textar" style="display:none">تمييز الأسانيد بالألوان</span>'),
    ('Multiple Matn Alignment — مقارنة المتون بالألوان', '<span class="lang-texten">Multiple Matn Alignment</span><span class="lang-textar" style="display:none">مقارنة المتون بالألوان</span>'),
    ('Connectivity Assessment — تمييز الاتصال بالألوان', '<span class="lang-texten">Connectivity Assessment</span><span class="lang-textar" style="display:none">تمييز الاتصال بالألوان</span>'),
    ('Friendly Colors (20)\\n            <small>ألوان سهلة</small>', '<span class="lang-texten">Friendly Colors (20)</span>\\n            <span class="lang-textar" style="display:none">ألوان سهلة</span>'),
    ('Clear Route\\n            <small>إعادة الترتيب</small>', '<span class="lang-texten">Clear Route</span>\\n            <span class="lang-textar" style="display:none">إعادة الترتيب</span>'),
    ('Light Theme\\n            <small>خلفية بيضاء</small>', '<span class="lang-texten">Light Theme</span>\\n            <span class="lang-textar" style="display:none">خلفية بيضاء</span>'),
    ('Log Scale\\n            <small>مقياس لوغاريتمي</small>', '<span class="lang-texten">Log Scale</span>\\n            <span class="lang-textar" style="display:none">مقياس لوغاريتمي</span>'),
    ('Save Chart حفظ التشجير', '<span class="lang-texten">Save Chart</span><span class="lang-textar" style="display:none">حفظ التشجير</span>'),
    ('Narrator Grades الجرح والتعديل', '<span class="lang-texten">Narrator Grades</span><span class="lang-textar" style="display:none">الجرح والتعديل</span>'),
    ('Connectivity الاتصال', '<span class="lang-texten">Connectivity</span><span class="lang-textar" style="display:none">الاتصال</span>'),
    ('Mermaid Code — كود الرسم البياني', '<span class="lang-texten">Mermaid Code</span><span class="lang-textar" style="display:none">كود الرسم البياني</span>'),
]

for src, dst in replacements:
    html = html.replace(src, dst)
    html = html.replace(src.replace('\\n', '\n'), dst.replace('\\n', '\n'))
    
# Replace the select options as well. Since bootstrap-select is used, data-content is a good idea. Or simply we will rely on JS for select fields, or add a span to the option which bootstrap-select may carry over.
options = [
    ('Bukhari البخاري', 'Bukhari', 'البخاري'),
    ('Muslim مسلم', 'Muslim', 'مسلم'),
    ('Malik مالك', 'Malik', 'مالك'),
    ("Nasa'i النسائي", "Nasa'i", "النسائي"),
    ("Abu Daw'ud أبو داود", "Abu Daw'ud", "أبو داود"),
    ('Termithi الترمذي', 'Termithi', 'الترمذي'),
    ('Daremi الدارمي', 'Daremi', 'الدارمي'),
    ('Ibn Majah ابن ماجه', 'Ibn Majah', 'ابن ماجه'),
    ('Ahmad أحمد', 'Ahmad', 'أحمد')
]
for src, en, ar in options:
    html = html.replace(f">{src}<", f" data-en=\"{en}\" data-ar=\"{ar}\">{en}<")
    
# for select options in sankey view
s_options = [
    ('<option selected>Group by Matn — تمييز المتون بالألوان</option>', '<option data-en="Group by Matn" data-ar="تمييز المتون بالألوان" selected>Group by Matn</option>'),
    ('<option>Group by Sanad — تمييز الأسانيد بالألوان</option>', '<option data-en="Group by Sanad" data-ar="تمييز الأسانيد بالألوان">Group by Sanad</option>'),
    ('<option>Multiple Matn Alignment — مقارنة المتون بالألوان</option>', '<option data-en="Multiple Matn Alignment" data-ar="مقارنة المتون بالألوان">Multiple Matn Alignment</option>'),
    ('<option>Connectivity Assessment — تمييز الاتصال بالألوان</option>', '<option data-en="Connectivity Assessment" data-ar="تمييز الاتصال بالألوان">Connectivity Assessment</option>')
]
for src, dst in s_options:
    html = html.replace(src, dst)

with open('index2.html', 'w', encoding='utf-8') as f:
    f.write(html)
