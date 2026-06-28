import os
import shutil

def fix_resources():
    res_dir = "decompiled/res"
    if not os.path.exists(res_dir): return
    
    # 1. $ белгісі бар файлдарды өзгерту
    for root, dirs, files in os.walk(res_dir):
        for file in files:
            if file.startswith("$"):
                old_path = os.path.join(root, file)
                new_name = file.replace("$", "s_")
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                
                # public.xml ішіндегі сілтемені түзеу
                old_key = file.replace('.xml', '')
                new_key = new_name.replace('.xml', '')
                path = "decompiled/res/values/public.xml"
                if os.path.exists(path):
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = content.replace(f"drawable/{old_key}", f"drawable/{new_key}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)

def add_mod_menu():
    # Manifest-ті патчтау
    manifest = "decompiled/AndroidManifest.xml"
    if os.path.exists(manifest):
        with open(manifest, 'r', encoding='utf-8') as f:
            data = f.read()
        if 'ModMenuService' not in data:
            data = data.replace('</application>', '    <service android:name="com.mod.almasoffikal.ModMenuService" android:exported="false"/>\n    </application>')
        with open(manifest, 'w', encoding='utf-8') as f:
            f.write(data)

    # Smali файл жасау
    smali_dir = "decompiled/smali/com/mod/almasoffikal"
    os.makedirs(smali_dir, exist_ok=True)
    with open(os.path.join(smali_dir, "ModMenuService.smali"), 'w', encoding='utf-8') as f:
        f.write(".class public Lcom/mod/almasoffikal/ModMenuService;\n.super Landroid/app/Service;\n\n.method public onCreate()V\n    .locals 0\n    invoke-super {p0}, Landroid/app/Service;->onCreate()V\n    return-void\n.end method\n\n.method public onBind(Landroid/content/Intent;)Landroid/os/IBinder;\n    .locals 1\n    const/4 v0, 0x0\n    return-object v0\n.end method")

if __name__ == "__main__":
    fix_resources()
    add_mod_menu()
    print("PATCHER: Success")
