import os

def patch_all():
    res_dir = "decompiled/res"
    
    # 1. Файл аттарын өзгерту (rename)
    for root, dirs, files in os.walk(res_dir):
        for file in files:
            if file.startswith("$"):
                old_path = os.path.join(root, file)
                new_name = file.replace("$", "s_")
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)

    # 2. Барлық XML файлдарды сканерлеп, ішіндегі $ сілтемелерін ауыстыру
    for root, dirs, files in os.walk(res_dir):
        for file in files:
            if file.endswith(".xml"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Тек файл аттары емес, кодтағы сілтемелерді де s_-ке ауыстыру
                new_content = content.replace("$", "s_")
                
                if content != new_content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

def add_mod_menu():
    manifest = "decompiled/AndroidManifest.xml"
    if os.path.exists(manifest):
        with open(manifest, 'r', encoding='utf-8') as f:
            data = f.read()
        if 'ModMenuService' not in data:
            data = data.replace('</application>', '    <service android:name="com.mod.almasoffikal.ModMenuService" android:exported="false"/>\n    </application>')
        with open(manifest, 'w', encoding='utf-8') as f:
            f.write(data)

    smali_dir = "decompiled/smali/com/mod/almasoffikal"
    os.makedirs(smali_dir, exist_ok=True)
    with open(os.path.join(smali_dir, "ModMenuService.smali"), 'w', encoding='utf-8') as f:
        f.write(".class public Lcom/mod/almasoffikal/ModMenuService;\n.super Landroid/app/Service;\n\n.method public onCreate()V\n    .locals 0\n    invoke-super {p0}, Landroid/app/Service;->onCreate()V\n    return-void\n.end method\n\n.method public onBind(Landroid/content/Intent;)Landroid/os/IBinder;\n    .locals 1\n    const/4 v0, 0x0\n    return-object v0\n.end method")

if __name__ == "__main__":
    patch_all()
    add_mod_menu()
    print("PATCHER: Success - Everything renamed to s_")
