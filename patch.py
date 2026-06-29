import os
import re

def clean_public_xml():
    public_xml = "decompiled/res/values/public.xml"
    if not os.path.exists(public_xml): 
        print("[!] public.xml табылмады.")
        return

    print("[*] public.xml ішіндегі қате сілтемелерді тазарту...")
    
    # Қате беретін drawable аттары
    problematic_resources = [
        "avd_hide_password", "avd_show_password", 
        "m3_avd_hide_password", "m3_avd_show_password",
        "mtrl_checkbox_button"
    ]

    with open(public_xml, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(public_xml, 'w', encoding='utf-8') as f:
        for line in lines:
            should_skip = False
            for prob in problematic_resources:
                if prob in line:
                    should_skip = True
                    break
            if not should_skip:
                f.write(line)
    print("[+] public.xml тазартылды.")

def patch_resources_and_manifest():
    # 1. $ белгісін өзгерту
    res_dir = "decompiled/res"
    for root, dirs, files in os.walk(res_dir):
        for file in files:
            if "$" in file:
                os.rename(os.path.join(root, file), os.path.join(root, file.replace("$", "s_")))
    
    # 2. Manifest патчтау
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
    patch_resources_and_manifest()
    print("PATCHER: Success")
