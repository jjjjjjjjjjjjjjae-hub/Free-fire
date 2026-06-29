import os
def patch_all():
    res_dir = "decompiled/res"
    for root, dirs, files in os.walk(res_dir):
        for file in files:
            if "$" in file:
                os.rename(os.path.join(root, file), os.path.join(root, file.replace("$", "s_")))
    # Manifest-ке сервис қосу
    manifest = "decompiled/AndroidManifest.xml"
    if os.path.exists(manifest):
        with open(manifest, 'r', encoding='utf-8') as f:
            data = f.read()
        if 'ModMenuService' not in data:
            data = data.replace('</application>', '    <service android:name="com.mod.almasoffikal.ModMenuService" android:exported="false"/>\n    </application>')
        with open(manifest, 'w', encoding='utf-8') as f:
            f.write(data)
if __name__ == "__main__":
    patch_all()
    print("PATCHER: Success")
