import os

def patch_all():
    res_dir = "decompiled/res"
    # 1. $ белгісін s_-ке ауыстыру
    for root, dirs, files in os.walk(res_dir):
        for file in files:
            if "$" in file:
                os.rename(os.path.join(root, file), os.path.join(root, file.replace("$", "s_")))

    # 2. Барлық XML-дегі сілтемелерді жөндеу
    for root, dirs, files in os.walk(res_dir):
        for file in files:
            if file.endswith(".xml"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_content = content.replace("$", "s_")
                if content != new_content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

    # 3. Манифестке сервис қосу
    manifest = "decompiled/AndroidManifest.xml"
    with open(manifest, 'r', encoding='utf-8') as f:
        data = f.read()
    
    # SYSTEM_ALERT_WINDOW рұқсаты
    if 'SYSTEM_ALERT_WINDOW' not in data:
        data = data.replace('<uses-permission', '<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>\n    <uses-permission', 1)
    # Service қосу
    if 'ModMenuService' not in data:
        data = data.replace('</application>', '    <service android:name="com.mod.almasoffikal.ModMenuService" android:exported="false"/>\n    </application>')
    
    with open(manifest, 'w', encoding='utf-8') as f:
        f.write(data)

if __name__ == "__main__":
    patch_all()
    print("PATCHER: Success")
