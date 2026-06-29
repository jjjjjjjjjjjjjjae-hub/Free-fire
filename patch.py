import os
import re

def clean_public_xml():
    res_path = "decompiled/res"
    public_xml = "decompiled/res/values/public.xml"

    # 1. Барлық бар drawable файлдардың тізімін жинау
    valid_drawables = set()
    for root, dirs, files in os.walk(res_path):
        if "drawable" in root:
            for file in files:
                valid_drawables.add(os.path.splitext(file)[0])

    # 2. public.xml-ді оқып, жоқ ресурстарды өшіру
    if os.path.exists(public_xml):
        with open(public_xml, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open(public_xml, 'w', encoding='utf-8') as f:
            for line in lines:
                match = re.search(r'name="drawable/([^"]+)"', line)
                if match:
                    drawable_name = match.group(1)
                    # Егер бұл сурет папкада жоқ болса, оны public.xml-ге жазбаймыз
                    if drawable_name not in valid_drawables:
                        continue 
                f.write(line)
    print("[+] public.xml тазартылды.")

def patch_manifest():
    manifest = "decompiled/AndroidManifest.xml"
    if os.path.exists(manifest):
        with open(manifest, 'r', encoding='utf-8') as f:
            data = f.read()
        if 'SYSTEM_ALERT_WINDOW' not in data:
            data = data.replace('<uses-permission', '<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>\n    <uses-permission', 1)
        if 'ModMenuService' not in data:
            data = data.replace('</application>', '    <service android:name="com.mod.almasoffikal.ModMenuService" android:exported="false"/>\n    </application>')
        with open(manifest, 'w', encoding='utf-8') as f:
            f.write(data)

if __name__ == "__main__":
    clean_public_xml()
    patch_manifest()
    print("PATCHER: Success")
